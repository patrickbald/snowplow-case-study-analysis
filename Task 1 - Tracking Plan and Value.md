
## Use cases

Acme have bought Snowplow as a data platform to enable the following use cases:
- **Marketing attribution** - understanding best how marketing traffic is driven to the site to allow for smarter future marketing spend
- **Product and customer journey analytics** - optimizing the product for customer experience and conversion
- **On site search optimization** - ensuring the search results are relevant to the customers
- **Reporting back to their partners to justify value** - ensuring the partners who use Acme’s service understand the value that the service is adding beyond sales
- **Content engagement** - understanding how the content acme.com creates contributes to sales and/or wider brand awareness

## Part 1: 

Pick either one or multiple of the use-cases listed above and propose any events and entities you would suggest Acme start tracking in order to meet the desired use-cases. You do not need to write JSON schemas for the event definitions, simply naming the event and giving some of the indicative properties that could comprise the event. You can present this back in any format you choose.

#### Product / Customer Journey

Goal: Describe the customer journey effectively in order to better align with their persona. 

**Entities:**
- User Entity
	- `user_id`
	- `email`
	- `username`
	- `password`
	- `purchase_history`
	- `location`
- Session Entity
	- `session_id`
	- `user_id`
	- `start_timestamp`
	- `end_timestamp`
	- `pages_viewed`
- Product Entity
	- `product_id`
	- `product_name`
	- `product_price`
	- `product_stock`
	- `product_tags`
- Cart Entity
	- `cart_items`
	- `user_id`
	- `session_id`
	- `start_checkout_timestamp`
	- `end_checkout_timestamp`
- Page Entity
	- `page_id`
	- `product_items`
	- `page_index`
	- `page_links`
	- `page_width`
	- `page_height`
- Content Entity

**Events:**
- Page View Event
	- `page_url`
	- `session_id`
	- `user_id`
	- `timestamp`
	- `in_link`
	- `page_width`
	- `page_height`
- Search Event
	- `search_query`
	- `search_filters`
	- `user_id`
	- `timestamp`
	- `session_id`
	- `results`
- Product Listing Page View/Ping
	- `session_id`
	- `page_items`
	- `page_index`
	- `user_id`
	- `page_width`
	- `page_height`
	- `referral_page`
- Product View
	- `product_id`
	- `product_name`
	- `product_tags`
	- `product_price`
	- `user_id`
	- `session_id`
	- `timestamp`
- Add to Cart Event
	- `product_id`
	- `product_name`
	- `quantity`
	- `timestamp`
	- `user_id`
	- `session_id`
	- `product_price`
- Add to Wishlist Event
	- `product_id`
	- `user_id`
	- `timestamp`
	- `session_id`
- Checkout Initiated Event
	- `timestamp`
	- `user_id`
	- `cart_items`
	- `geo`
	- `session_id`
- Checkout Complete Event
	- `user_id`
	- `checkout_value`
	- `user_location`
	- `timestamp`
- Transaction Event
	- `transaction_id`
- Content View
	- `content_id`
	- `session_id`
	- `user_id`
	- `timestamp`


**Product Journey Insights**:
- Most frequent path taken by user groups
- Customer engagement / ad pop-up
- Email follow-ups
- Determine pain-points
- Determine next best action for each customer

#### Search Optimization 

Goal: Give customers better search results in order to increase clickthrough rates from search to purchase.

**Entities:**
- Search Entity
	- `search_id`
	- `search_term`
	- `timestamp`
	- `search_filters`
- User Entity
	- `user_id`
	- `name`
	- `age`
	- `email`
	- `past_searches`
- Result (Product) Entity
	- `product_id`
	- `product_name`
	- `product_tags`
	- `product_price`

**Events:**
- Search Started
	- `user_id`
	- `search_term`
	- `timestamp`
	- `session_id`
	- `filters_added`
- Search Results Returned
	- `user_id`
	- `timestamp`
	- `session_id`
	- `search_term`
	- `list of products`
- Search Result Viewed
	- `user_id`
	- `timestamp`
	- `search_term`
	- `search_id`
- Search Ended
	- `user_id`
	- `timestamp`
	- `search_terms`
	- `session_id`

![[Snowplow Case Study Tracking Plan.xlsx]]

**Search Optimization Insights:**
- Monitoring customer intent through search term and filters vs what they put in cart
- Analyzing click through rates for search results
- Personalization based on past search history or user metrics
- Search Term and Result relevance

## Part 2:

For a given use-case listed above, give a high level explanation of how you would suggest going about demonstrating value/outcomes through use of the data collected (including out of the box data). You do not need to write any example SQL, more how you would suggest aggregating this data to make progress towards the use-case.

#### Use Case: Product Journey Analytics

Goal: Utilize aggregated event data to identify value add of customer behavioral data through dashboards, personas, personalization, etc.

##### Data Aggregation:
- **Page Engagement:**
	- Sum up time spent per page of full journey
	- Map mouse location to identify most useful page areas or pain points
	- Track button clicks to determine UI effectiveness
- **Funnel Analysis:**
	- Track rates users are progressing through different site areas
		- cart -> checkout
		- search -> cart add
		- wishlist -> cart
		- etc
	- This helps determine where the site may have higher drop off rates
- **Checkout Progress / Recommendations**
	- Track progress through check out process
		- Time spent, options selected, payment types
	- Determine where users struggle or spend the most time
		- Identify how many users back out after viewing payment options / full total
		- Correlate time spent in cart to purchase percentage
	- Identify desired payment methods / shipping options
		- certain shipping options may be more desirable depending on location, day of week, etc
	- Give additional options to minimize cart drops
- **Ad Engagement**
	- Determine how many users landed at site through ad campaign
	- Track on site add clicks
	- Determine promotion code effectiveness

