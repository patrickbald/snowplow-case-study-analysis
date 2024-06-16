#!/usr/bin/python3

import pandas as pd
import uuid

# INGESTION / CLEANING

def clean_data(df):

    necessary_cols = [
        'event_id', 
        'page_view_id', 
        'session_id', 
        'user_cookie', 
        'event_name', 
        'page_urlhostname', 
        'page_url', 
        'referral_url', 
        'dvce_created_tstamp', 
        'pp_xoffset_min', 
        'pp_xoffset_max', 
        'pp_yoffset_min', 
        'pp_yoffset_max', 
        'page_height', 
        'link_click_target_url'
    ]
    
    drop_cols = [
        'page_title',
        'geo_country',
        'geo_region',
        'geo_city',
        'geo_timezone',
        'page_width',
        'useragent_family',
        'os_family',
        'device_family',
        'os_timezone'
    ]
    
    df = df.drop(columns=drop_cols)

    # Drop Duplicates
    df.drop_duplicates(inplace=True)

    # Strip session ids
    df['session_id'] = df['session_id'].str.strip()

    # Remove rows with null values in essential columns
    non_null_cols = ['event_id', 'page_view_id', 'session_id', 'page_url', 'page_urlhostname', 'dvce_created_tstamp']
    df.dropna(subset=non_null_cols, inplace=True)

    # Format Datetime columns
    df['dvce_created_tstamp'] = pd.to_datetime(df['dvce_created_tstamp'], errors='coerce')
    df = df.dropna(subset=['dvce_created_tstamp'])

    # Validate event types
    df = df[df['event_name'].isin(['page_view', 'page_ping', 'link_click'])]

    return df

def ingest_data(csv_path):
    df = pd.read_csv(csv_path)
    return df

def write_file(df, path):
    df.to_csv(path, index=False)

# ANALYSIS

def calc_bounce_rate(df):
    '''
        % of visitors that leave the webpage without taking an action.
        - sessions which contain only a page_view event

        Assumptions:
        - page_views of two different pages in same session would have to connected by some user action
        - page pings do not count as user action

        Ex:

        |   session_id  |   event_name  | 
        ---------------------------------
        |   1           |   page_view   |
        ---------------------------------
        |   1           |   page_ping   | 

        Is a bounce.

        Ex:

        |   session_id  |   event_name  |   page_url            |
        ---------------------------------------------------------
        |   1           |   page_view   |   snowplow.io
        ---------------------------------------------------------
        |   1           |   page_view   |   discourse.snowplow.io

        Needs a linking 'link_click' event to be valid.

        Ex: 

        |   session_id  |   event_name  | 
        ---------------------------------
        |   1           |   link_click  |
        ---------------------------------
        |   1           |   page_ping   |

        Is not a bounce. 

    '''
    df = df.sort_values(by=['session_id', 'dvce_created_tstamp'])
    
    session_groups = df.groupby('session_id')

    # Filter for groups which contain only page_view / page_ping, and at least one page_view
    single_page_view_sessions = session_groups.filter(
        lambda x: all(e in ['page_view', 'page_ping'] for e in x['event_name']) and any(x['event_name'] == 'page_view')
    )
    # Count unique sessions 
    bounce_count = single_page_view_sessions['session_id'].nunique()

    total_sessions = df['session_id'].nunique()

    bounce_rate = (bounce_count / total_sessions) * 100

    print('Session Bounce rate: ', bounce_rate)

    return

def calc_avg_time_per_page_view(df):
    '''
        Get sum of timestamp diff of each page_view_id group.
        - group by page_view_id, timestamp
        - get diff of earliest timestamp and most recent timestamp of page_view_id group
        - sum up diff of timestamps
        - get average of page_view_time sum

        Assumptions:
        - link_click page view ids do not account for engaged time on page

        Improvements:
        - Ensure removal of timestamp outliers
    '''
    df = df.sort_values(by=['page_view_id', 'dvce_created_tstamp'])

    df = df[df['event_name'].isin(['page_view', 'page_ping'])]

    df['page_view_time_diff'] = df.groupby(['page_view_id'])['dvce_created_tstamp'].diff().shift(-1)
    df = df.dropna(subset=['page_view_time_diff'])

    page_view_total = df.groupby(['page_view_id'])['page_view_time_diff'].sum()
    average_time = page_view_total.median()

    print('Average time spent on each page view: ', average_time)

    return

def calc_avg_scroll_depth(df):
    '''
        Calculate scroll depth max for each page view
            - use page_view_id 
            - use pp_yoffset_ma
            - use page_height

        Compute mean scroll depth across all page views
    '''
    # Remove rows which are not ping as they do not contain the max scroll depth of the page_view_id
    ping_index = df[df['event_name'] != 'page_ping'].index
    df = df.drop(ping_index)

    df['scroll_percentage'] = (df['pp_yoffset_max'] / df['page_height']) * 100

    scroll_percentage_max = df.groupby('page_view_id')['scroll_percentage'].max()

    avg_scroll_depth_percentage = scroll_percentage_max.mean()

    print('Average scroll depth percentage per page view: ', avg_scroll_depth_percentage)

    return

def calc_discourse_percentage(df):
    '''
        - Identify users who first navigate to snowplowanalytics.com
        - Idenitfy users who navigate to discourse.showplowanalytics.com
        - join users based on user cookie to determine who started at snowplowanalytics, and also visited discourse.snowplowanalytics.com
    '''
    # Filter out page_pings and link_clicks 
    filter_index = df[df['event_name'] != 'page_view'].index
    df = df.drop(filter_index)

    df = df.sort_values(by=['user_cookie', 'dvce_created_tstamp'])

    # Identify users who first visit snowplowanalytics.com
    snowplow_first_visitors = df.drop_duplicates(subset=['user_cookie'], keep='first')
    snowplow_index = snowplow_first_visitors[snowplow_first_visitors['page_urlhostname'] != 'snowplowanalytics.com'].index
    snowplow_first_visitors = snowplow_first_visitors.drop(snowplow_index)
    snowplow_first_visitors_count = snowplow_first_visitors['user_cookie'].nunique()

    # Identify users who visit discourse.snowplowanalytics.com at any point 
    discourse_index = df[df['page_urlhostname'] != 'discourse.snowplowanalytics.com'].index
    discourse_visitors = df.drop(discourse_index)

    # Join dfs on user id
    users_who_end_up_at_discourse = pd.merge(snowplow_first_visitors, discourse_visitors, on='user_cookie', suffixes=('_1', '_2'))

    # Get unique users who start on snowplow and end up on discourse
    users_who_end_up_at_discourse_count = users_who_end_up_at_discourse['user_cookie'].nunique()

    if snowplow_first_visitors_count != 0:
        user_journey_percentage = (users_who_end_up_at_discourse_count / snowplow_first_visitors_count) * 100
        print('Percentage of users who start on snowplowanalytics.com and end up at discourse.snowplowanalytics.com: ', user_journey_percentage)
    else:
        print('No users start at snowplowanalytics.com and end up at discourse.snowplowanalytics.com')

    return

def main():
    # File Names
    cleaned_data_name = 'cleaned-dataset-' + str(uuid.uuid4()) + '.csv'
    # File Paths
    raw_dataset_path = '../snowplow-dataset.csv'
    cleaned_data_path = '../cleaned-datasets/' + cleaned_data_name

    print('Ingesting dataset...')
    snowplow_df = ingest_data(raw_dataset_path)
    print('Dataset Ingested.\n')

    print('Cleaning dataset...')
    snowplow_df_cleaned = clean_data(snowplow_df)
    print('Cleaning complete.\n')

    print('Performing analyses on dataset... \n')
    calc_bounce_rate(snowplow_df_cleaned)
    calc_avg_time_per_page_view(snowplow_df_cleaned)
    calc_avg_scroll_depth(snowplow_df_cleaned)
    calc_discourse_percentage(snowplow_df_cleaned)
    print('\nDone performing analysis on datset.')

    return

if __name__ == '__main__':
    main()