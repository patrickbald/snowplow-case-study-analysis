# Snowplow Case Study Data Analysis

This repo serves to provide event definitions, data cleansing, and data analysis for given use cases pertaining to features of Snowplow.io. 

The Event and Entity tracking schemas provide insight into what events and entities would be useful to include in a Tracking Plan. Using the tracking plan, users can identify which entities correlate to which events, event triggers, and tracking implementation status. 

The Data Analysis script serves to cleanse a set of example data gathered by Snowplow, and perform subsequent calculations on the cleansed data which could provide valuable insights. 

## Event and Entity Tracking
### Search Optimization

### Product / Customer Journey

## Data Analysis
### Clean

Before performing analysis on the data, we need to ensure our data is void of null values, mismatching data type, and has the appropriate columns. 

Cleaning steps:
- drop duplicates
- strip values which contain extra whitespace
- format datetime columns
- drop rows with null value in essential rows
- validate event types

### Analysis