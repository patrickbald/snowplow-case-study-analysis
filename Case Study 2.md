- *Understanding Your Customer: Developing an understanding of a customerʼs current-state landscape*

- *Churn Prevention: How to notice and reduce the probability of a customer ending their contract*

### Part 1 - Understanding your customer

An existing customer of Snowplow has requested some advice on how to structure their data function and team(s) around their Snowplow usage, with a focus on how this could help support their wider data initiatives. This existing customer is a long-standing customer of Snowplow, and one of the more strategic accounts in Snowplowʼs portfolio.

In an effort to support these conversations, you have been brought in to support the Snowplow Customer Success Manager, who owns the account relationship with this customer. You have been added to this account to support the conversations and to provide advice and consultancy on how to structure data functions based on current usage within an organization.

- What kind of questions would you pose to the customer, in order to gather the necessary information and requirements, to give the best advice on how to structure their data team? These questions could cover, but should not be limited to, for example - team size, skill sets, adjacent teams, growth, future plans etc.
    
- What different team set-ups, discussions, and data team structures would you propose to the customer. Please present a few different options, illustrating the benefits and potential challenges associated with the different proposed structures.
##### **Landscape Discovery Phase**

Given we are currently working with the existing customer we can somewhat streamline our discovery phase, however, the following touch points would be valuable in evaluating the current landscape:
	- **Current Use Cases and Limitations**
		- What are the main pain points and limitations of the current system?
		- Who are the primary stakeholders of the platform? (Teams, Users, Business Units)
		- What current use cases is the Snowplow platform servicing?
		- Are there any pricing concerns / targets to meet with the next phase of the platform?
	- **Future Plans and Growth Opportunities**
		- What are the primary goals for the next phase of the Snowplow platform?
		- What additional data capabilities will we need in order to meet our goals for the future?
		- Will the team need any additional resources in order to accomplish future goals? 
	- **Desired Insights and Areas for Optimizations**
		- What additional metrics and insights will we need to implement in order to meet additional use cases?
		- What tools are we using to implement the current Snowplow platform and will those tools need to change or expand?
	- **Team Size, Expertise, and Structure** 
		- Who are the primary developers and users of the Snowplow platform?
		- What skillsets does the team possess / areas for improvement?
		- Who are the adjacent teams which work closely or are impacted by the Snowplow platform?
		- How is the team structured currently and what pain points are you experiencing?

##### **Team Recommendations**

**Option 1: Core Snowplow Platform Team**

In this scenario, we could architect the data team to be centralized around the Snowplow platform, and keep all Acme data analysts and engineers under the same umbrella. This would keep the analysts close to the data engineers running the Snowplow pipeline.
- Benefits:
	- Ease of knowledge sharing and quick feedback loop between analysts and engineers
	- Alignment with Acme needs rather than individual team needs
	- Control over Snowplow data strategy
	- Easy support requests for Snowplow customer service
	- Less potential for duplicate work as analysts have insight into full scope of data project
- Cons:
	- Snowplow team may be more limited in servicing individual business units in parallel
	- Acme may feel less engaged with Snowplow services if business units are not actively engaged in the Snowplow system and data projects

**Option 2: Embedded Snowplow Analysts with Core Team** 

In this scenario we could decentralize the analysts who primarily use Acme's Snowplow platform to their respective teams, while keeping a core team of data engineers in order to maintain the Snowplow pipeline. This will enable the analysts to work closely with team initiatives
- Benefits:
	- Data analysts are aligned with the needs of their individual team needs rather than company wide
	- Much faster feedback loop between the team needs and the data analysts as they do not have to make a request to a separate team
	- Greater context around data intricacies relevant to team needs and can tailor solutions to their business unit
- Cons:
	- Potential for duplicate work if there is not a protocol for knowledge sharing between business units
	- May silo off team needs rather than aligning with Acme data goals
	- Can lead to inconsistencies in data protocols between teams 

##### **Process Recommendations**
- **Knowledge Sharing Protocols**
	- Establishing a regular cadence for knowledge sharing will help keep each team up to date on work being done, changes in processes, and new technology being used. 
- **Data Governance**
	- Establishing a data governance framework will ensure data quality, consistency, security, and management across each team regardless of team structure
- **Project Management Tools**
	- Implementing a project management tool will help reduce duplicative work and keep the company engaged with what the data teams are working on.


### Part 2 - Churn Prevention

Acme is a customer of Snowplow, and has been for over a year. Weʼve just heard Acme has been acquired by BigCo. BigCo has an internally-built behavioral data collection pipeline (sometimes called a ʻhomebrewʼ or ʻDIYʼ pipeline) which they believe is a functional alternative to Acme using Snowplow. They want to move Acme over to using the homebrew pipeline.

Your goal is to prevent Acme from churning as a Snowplow customer following the acquisition. Below is a series of details of the account, team players and recent communications, aimed to give you additional insight and detail to the current situation. Once this detail is reviewed, please answer the three questions referenced at the end of this section.

**Current Acme Use Cases on Snowplow:**
- Marketing Attribution - understanding how best traffic is driven to the site to allow for smarter future marketing spend
- Product and customer journey analytics - optimizing the product for customer experience and conversion
- On site search optimization - ensuring search results are relevant to customers
- Value Reporting - ensuring the partners on Acme's site understand the service Acme is providing through partnership

Snowplow vs Panopticon:

|                           | Snowplow (Acme)                                                                 | Panopticon (BigCo)                                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Business Use Case Support | Can be used for any use case necessary for business units within Acme           | Optimized around a few specific business units of BigCo                                                                 |
| Business Customization    | Generic technology used across industries, verticals, and team sizes            | Designed specifically for BigCo business vertical and may have business specific logic built into the pipeline directly |
| Robustness                | Vigorously tested through various teams, open sourcing, and volume of customers | Tested against specific scenarios of BigCo                                                                              |
| Vendor lock-in            | None - open source technology                                                   | None, but requires team of engineers in order to maintain the pipeline                                                  |

**Emails**:

**Email 1:**
> From: Clive
> To: You
> Subject: Fwd: Migrating to BigCo’s internal platform
> 
> hi - I have more information on the planned migration, see below. ==my worry is that==
> ==panoptiCON seems to have been hardcoded around bigco’s own specific business==
> 
> (tracking customers of their network of car dealerships). i am not sure how it will
> handle acme’s marketplace-shaped needs.
> 
> c
> 
> ---------- Forwarded message ---------
> From: Susan
> Subject: Migrating to BigCo’s internal platform
> To: Clive
> CC: Rahul
> 
> Hello Clive,
> I spoke to Rahul (CC’ed) and the Panopticon team and can now confirm:
> 
> - ==We will want to start the Snowplow migration process within 3 months from today==
> 
> -  We estimate it will take 3 months to complete
>     
> - We expect a full shutdown of Snowplow once Acme is running on Panopticon
>     
> KR, Susan

**Email 2:**
> From: Clive
> To: You
> Subject: I just found out...
>     
>     hi - i just found out that panoptiCON is actually only used by bigco’s data science
>     team - the marketing team there are still using adobe analytics. ==afaik use cases==
>     ==for panoptiCON seem to be marketing attribution and dealer/forecourt analytics.==
>     marketing there don’t love adobe but apparently they’ve never been shown how to use
>     panopticon data...
>     
>     c

**Email 3:**
> From: You
> To: Clive
>  Subject: Re: Quick questions
>     
>     Hi Clive,
>     Apologies for the delay in getting back to you; please see my answers inline...
>     
	- remind me when our next Snowplow renewal is?
>     12 weeks from now
>     
    - can we renew for 12 months instead of 24? does Snowplow do break clauses eg after
>     3 months?
>     Yes on the renewal for 12 months. No, we don’t offer break clauses.
>     
>     Thanks

Email 4:
> From: Susan
> To: You
> CC: Rahul, Clive
> Subject: Feedback on the Snowplow QBR
> 
> Hello,
> 
> I am grateful to you and Clive for allowing Rahul and me to sit in on this. You
> made some compelling arguments and it’s clear that Snowplow has driven a lot of
> value for Acme.
> 
> I share Rahul’s concern around persisting Acme’s vendor lock-in with Snowplow
> post-acquisition. ==I’m also excited about the potential for us to update Panopticon==
> ==to support Acme’s use cases in the very tailored way that Panopticon has supported==
> ==BigCo’s needs==.
> 
> KR, Susan

##### Questions to Address:

1. **What is your general read of the situation? Please provide a general description (no more than 2-3 paragraphs), then a brief summary (no more than 1 paragraph) on how each participant is thinking/acting.**

**General Sentiment**
Based on the provided emails, it appears to me that there are a few parties involved with differing sentiments regarding a full migration off Snowplow. Each party has reasonable grounds to lean in either direction, but more context would serve each group in making a fully informed decision around whether to continue using IceData for an extended period. 

The current Snowplow stakeholders (Clive and team) have been able to generate significant value through the IceData platform, and are concerned around the thought of migrating to a new platform within BigCo. Conversely, the team from BigCo is understandably pushing for the full migration onto Panopticon to bring the system in house.

The BigCo team led by Susan is excited about the potential to customize Panopticon to the Acme use case and is concerned about vendor lock-in with Snowplow, which displays some amount of missing context around both the Snowplow technology and the current customization of the system. Additionally, Susan and her team seem to be pushing for a migration timeline which could cause temporary disruptions, as the Snowplow renewal would need to occur well before the migration would be complete. 

In order to best determine a path forward, it would be critical to provide further context around the usage of Snowplow at Acme, highlighting its robustness, lack of lock-in clause, and use-case potential. Given this information, Susan and her team may have second thoughts around a full fledged migration. 

**Participant Sentiment**
- Clive
	Based on the emails between myself and Clive, it appears that Clive is hesitant to migrate off of the Snowplow platform. He has voiced concerns around Panopticon being tailored to a different set of use cases with BigCo and how it will be unable to handle Acme's use case. Additionally, I think Clive senses that his team will no longer be a priority at BigCo, given some of their own in house teams have yet to be trained on the Panopticon platform yet. 

- Susan
	As BigCo's Chief Data Officer, it follows that Susan would be pushing to migrate Acme's platform onto their own preexisting solution. While she understands the value that IceData has provided Acme thus far, she is excited about the possibility to customize Panopticon around Acme's use cases. 

- Rahul
	Per the set of emails, it appears that Rahul is mainly concerned with a Snowplow lock-in after the acquisition. He seems to be on board with Susan regarding a full switch to Panopticon and customizing it to fit the new Acme use cases. 

- Me
	As the solutions architect for Snowplow, our goal is to enable the success of our customers on the Snowplow and simultaneously prevent churn on our end. 

2. **Draft an email response to Susanʼs last email (Email 4). Make a persuasive case for Acme continuing to use IceData post-acquisition.**

Hi Susan, 

Thanks again for taking the time to join us in our QBR and sharing your concerns around remaining on the Snowplow platform. I appreciate the feedback and am happy to hear the value of Snowplow is compelling. I wanted to both address some of your concerns and highlight a few areas that I believe make a strong case for staying on the Snowplow platform for further period of time. 

Per your concerns around vendor lock-in with Snowplow, I will highlight the fact that Snowplow is built on open source technology, which does not necessarily tie BigCo to Snowplow as a service specifically. That being said, our expertise is certainly valuable in extracting the most value from our open source technology for Acme's use cases. In a collaborative effort, we can upscale the BigCo team to work efficiently alongside the Snowplow platform.

Regarding the customization of Panopticon around Acme's use cases, I believe it is noteworthy to acknowledge that while the technology is generic, IceData has been specifically tailored to support Acme's business use cases. While transitioning to Panopticon may allow for more alignment with the existing BigCo data team, it may be difficult to perform a seamless transition without significant level of effort involved in the customization of Panopticon. I'd also like to highlight that the Snowplow platform is built to scale alongside new use cases for Acme, and would adapt well to any new functionality BigCo would like to implement. 

We are very much open to working closely alongside Clive, Rahul, and BigCo to ensure Acme continues to generate its value within BigCo. I'd strongly recommend utilizing the Snowplow platform for an extended period of time through Acme's transition into BigCo so that we can best adapt the system to work in conjunction with Panopticon. 

Please let me know how we can discuss further in order to ensure the success of both platforms. 

Best,
Patrick

3. **Take yourself back to the moment you heard of the acquisition and the plan to swap out Snowplow for Panopticon. You drafted a short battle plan. What was that short battle plan?**

- **Understand the Situation:**
	- Contact Snowplow contract holder at Acme
	- Determine migration timeline
	- Gather knowledge around competitor / reasoning/ stakeholders
	- Determine team sentiment around IceData and panopticon
- **Provide Thoughtful Insight into IceData's value**
	- Identify potential areas to highlight regarding the Snowplow platform and corresponding downsides of panopticon
	- Provide insights into the migration and how it could effect the current use cases
	- Understand potential for pricing / contract duration changes
- **Maintain Feedback Loop and Advise in First Principles**
	- Advise in best interest for stakeholders and maintain high level of customer support and professionalism
