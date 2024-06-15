#!/usr/bin/python3

import pandas as pd
import uuid

def clean_data(df):

    # Remove null values from essential columns
    non_null_cols = ['event_id', 'page_view_id', 'session_id', 'page_url', 'page_urlhostname', 'dvce_created_tstamp', 'referral_url']
    df.dropna(subset=non_null_cols, inplace=True)

    # Fill Geo Cols
    df = df.fillna({'geo_country': 'Unknown', 'geo_region': 'Unknown', 'geo_city': 'Unknown', 'geo_timezone': 'Unknown'})

    # Drop Duplicates
    df.drop_duplicates(inplace=True)

    # Fix Datetime columns
    df['dvce_created_tstamp'] = pd.to_datetime(df['dvce_created_tstamp'], errors='coerce')

    # Strip session ids
    df['session_id'] = df['session_id'].str.strip()

    # Fix Urls


    return df

def ingest_data(csv_path):
    df = pd.read_csv(csv_path)
    return df

def write_file(df, path):
    df.to_csv(path, index=False)

def main():
    # File Names
    cleaned_data_name = 'cleaned-dataset-' + str(uuid.uuid4())

    # File Paths
    dataset_path = '../snowplow-dataset.csv'
    cleaned_data_path = '../cleaned-datasets/' + cleaned_data_name

    print('Cleaning dataset . . .')
    
    snowplow_df = ingest_data(dataset_path)

    snowplow_df_cleaned = clean_data(snowplow_df)

    write_file(snowplow_df_cleaned, cleaned_data_path)

    print('Cleaning complete.')

if __name__ == '__main__':
    main()