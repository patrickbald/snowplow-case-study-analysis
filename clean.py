#!/usr/bin/python3

import pandas as pd

def clean_data(df):

    # Remove null values
    df.dropna(inplace=True)

    # Drop Duplicates
    df.drop_duplicates(inplace=True)

    # Fix Datetime columns
    df['dvce_created_tstamp'] = pd.to_datetime(df['dvce_created_tstamp'], errors='coerce')

    # Fix Urls

    return df

def ingest_data(csv_path):
    df = pd.read_csv(csv_path)
    return df

def write_file(df, path):
    df.to_csv(path, index=False)

def main():

    # File Paths
    dataset_path = '../snowplow-dataset.csv'
    cleaned_data_path = '../snowplow_dataset_cleaned.csv'

    print('Cleaning dataset . . .')
    
    snowplow_df = ingest_data(dataset_path)

    snowplow_df_cleaned = clean_data(snowplow_df)

    write_file(snowplow_df_cleaned, cleaned_data_path)

    print('Cleaning complete.')

if __name__ == '__main__':
    main()