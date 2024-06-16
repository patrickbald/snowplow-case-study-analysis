#!/usr/bin/python3 

import sys
import pandas as pd

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
    session_groups = df.groupby('session_id')

    # Filter for groups which contain only page_view and page_ping, and at least one page_view
    single_page_view_sessions = session_groups.filter(
        lambda x: all(e in ['page_view', 'page_ping'] for e in x['event_name']) and any(x['event_name'] == 'page_view')
    )
    # Count unique sessions 
    bounce_count = single_page_view_sessions['session_id'].nunique()

    total_sessions = df['session_id'].nunique()

    bounce_rate = (bounce_count / total_sessions) * 100

    print('Bounce rate: ', bounce_rate)

    return

def calc_avg_time_per_page_view(df):
    '''
        Get sum of timestamp diff of each page_view_id group.

        - group by page_view_id, timestamp
        - get diff of earliest timestamp and most recent timestamp of page_view_id group
        - sum up diff of timestamps
        - get average of page_view_time sum
    '''
    # Ensure timestamp is ingested as datetime
    df['dvce_created_tstamp'] = pd.to_datetime(df['dvce_created_tstamp'], errors='coerce')
    df = df.dropna(subset=['dvce_created_tstamp'])

    df = df.sort_values(by=['page_view_id', 'dvce_created_tstamp'])

    df = df[df['event_name'].isin(['page_view', 'page_ping'])]

    df['page_view_time_diff'] = df.groupby(['page_view_id'])['dvce_created_tstamp'].diff().shift(-1)
    df = df.dropna(subset=['page_view_time_diff'])

    page_view_total = df.groupby(['page_view_id'])['page_view_time_diff'].sum()

    average_time = page_view_total.median()

    print('Average time spent on each page view: ', average_time)

    return

def calc_avg_scroll_depth(df):
    pass

def calc_discourse_percentage(df):
    pass

def ingest_data(csv_path):
    df = pd.read_csv(csv_path)
    return df

def main():
    # Get cleaned dataset filename
    input_filename = sys.argv[1]
    input_path = '../' + input_filename

    print('Ingesting dataset...')
    snowplow_df = ingest_data(input_path)
    # print(snowplow_df.to_string())
    print('Dataset Ingested.')

    print('Performing analysis on dataset...')
    calc_bounce_rate(snowplow_df)
    calc_avg_time_per_page_view(snowplow_df)
    calc_avg_scroll_depth(snowplow_df)
    calc_discourse_percentage(snowplow_df)
    print('Analysis complete.')

if __name__ == '__main__':
    main()