
#### Part 1 - Data cleaning:
- Remove / fill rows which have null values in essential columns
- Drop unnecessary columns
- Drop duplicates
- Format datetime columns
- Format numeric columns
- Validate event types

#### Part 2 - Data Analysis:
- **Session bounce rate:**
	- determine percentage of users who view a page and take no further action
		- aka ((total_sessions - sessions_which_take_action) / total_sessions) * 100

- **Average page view time:**
	- For each page view id, sum time spent on page (initial view + pings), and average across all page views
	- Account for outliers

- **Average scroll depth percentage:**
	- Remove row which are not ping
	- group by page_view_id and calculate percentage as pp_yoffset_max / page_height
	- average across all page views

- **Percent of users who start on snowplowanalytics.com and navigate to discourse.snowplowanalytics.com:**
	- get number of users who's first page view is snowplowanalytics.com
	- get number of users who at any time visit discourse.snowplowanalytics.com
	- join based on user cookie to see who did both
	- get number of unique users
	- calculate percentage as number of unique users who hit both sites / users who started on snowplowanalytics.com

#### Part 3 - Further Analysis

*Imagine you intend to use this dataset for repeated analysis in the future, describe what transformations you would perform on the dataset to derive a set of views that contain analytics ready data. You do not need to write code defining your view(s).*

##### Use case: Product and Customer Journey

**Data Transformations:**
- Device and Browser Analysis
	- Understand mobile vs desktop users
		- User_device_type
- User Timestamps
	- Determine when certain users are more likely to be active / engage with content and how long they do so
		- eg: page_spent_most_time_on
- Location Analysis
	- Identify user groups from different geographic locations and analyze their product journey
- Page Version for A/B testing
	- Helps identify effectiveness of small tweaks in UI and content
		- session_page_version
- Identify user heat maps
	- Help understand which areas of the site are most traveled, by whom, and in what stage of their path through the site
		- eg: avg_mouse_position or mouse_timestamps
- Funnel Analytics
	- Check user sessions who took some kind of page action along with where they started and where they ended up to determine where users may be dropping off
		- eg: user_start page, user_last_visited

#### Future Improvements

- Identify performance bottlenecks
	- Messy joins
	- Datetime conversion
	- Lead/Lag
	- etc
- URL validation
- Handle outliers
- Move script into hosted platform/environment
	- Could easily translate this script into a simple AWS Glue job to run after data ingestion
	- Create dashboards

