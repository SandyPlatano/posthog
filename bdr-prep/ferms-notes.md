# My PostHog BDR Preparation Notes

Loose mental notes:

Key principles (Value First, No Pressure, Radical Honesty)

Presentation idea for creative sales ideas = create a super simple PostHog game where the Hog is presenting the concepts, instead of a plain / boring slide deck. 

What's in the presentation?

What I heard was really important for this role:

- Not ruining brand image with sleezy sales tactcis while building piepline.
- 

Also instead of calling them prospects, you can call them potential customers is another idea I had as well. 

With such great brand reputation, PostHog's name doesn't have to overcome the skepticism barrier — people already know the brand, so outreach feels less cold.

But with such great brand indentity, comes great brand protection..

sleezy sales tactics are one of the quickest ways to ruin it. 

examples:

- Gatekeeping price
- Not doing demo's when thats what the customner wanted
- Promising features.

Coming opinionated about the right tooling and process for the job.
 So my opinions are that educating and creating resource and value before we even contact a customer is going to be a critical point here. A lot of sales is all about extracting and that's what feels sleazy sometimes is that you're contacting a total stranger and trying to extract. I think a better idea for outreach is trying to provide value without anything or without expecting anything in return. It's more like, hey, I thought this might be good for you and relevant. Here's what I made. If you have any questions for me to send them my way, just thought it would be helpful. It's more of that mindset that you want to approach. There might be a time where you're asking someone for time and that's okay if people want to meet. And of course, with a little bit of polite persistence, things people do forget to answer back or maybe their priorities shifted for just a moment and you need to reach out another time.

 The main goal is to reach out to potential customers and try to show them how awesome PostHog is. 

 

 So what does this look like in practice?

 For your first intiative of...

"Research and identify high-quality target accounts using firmographic, technographic, and behavioral signals. Do this in a way that doesn't scale, and then does."

Lets get the tools out of the way:



Sequencer --> Outreach or Instantly.. Lemlist for LI outreach
Data sourcing for personalizaiton --> Scripts on cursor or Clay
Indentify prospects --> Apollo, Clay, BuiltWith, Apify scraper, Rb2B, Ocean.io, Cursor
Inbox infracture --> Scaled Mail

Choosing a tool that is going to solve a certain problem is how I'd choose the tech stack. 


This is what the process typically looks like

Source data → qualification → research   → personalized outreach. 

Source data where potential customers live .. 


- Reverse demo's are a great way to put the customer in the drivers seat and let them feel what it would be like to drive your product.
- When an ICP fit Engineer signsup, offer them to get on texting terms and offer help whenever possible. Give them tactical, and guides to follow based on their specifci industry. You can use Clay for this. Setup webhook from signup page, identify ICP, push specific non salesy messaging through the program Outreach which is a sequencer. Allows people to feel like they can reach directly to someone to help them.

In terms of messaging tone: Unassumptive tones! Every one hates having a stranger contact them about their life and make the assumption they know these are facts within your outreach messaging. Terms like "Not sure" "Possibly" "Is this?" .. When you're reaching out to someone you're basing it on 3rd party data, you don't have access to their 1st party data so its always an educated guess. 

Creating campaigns

Tag based campaigns 


Cold → General cold outreach
Warm → Following up on signups
Consolidation → Tool consolidation

Example Campaigns:
B2B-SaaS - Cold - Q1-2025 → Tool consolidation messaging

I'd use the SPAM frame work to create messaging that is targeteed.

The SPAM Framework for PostHog
1. Segment
This is where you group prospects based on their existing analytics tool stack, which indicates a specific set of operational challenges.

Segment A: Multi-tool Analytics Users (e.g., Mixpanel + LaunchDarkly + FullStory)

Implied Pain: Managing multiple vendors for analytics, feature flags, and session replay. Data scattered across platforms, integration nightmares, and ballooning costs.
Segment B: Legacy Analytics Users (e.g., Google Analytics + Firebase + Optimizely)


2. Persona (Who You're Talking To)
Within each segment, you must tailor your message to the specific individual you're contacting, as their priorities differ.

Head of Product: Cares about user insights, understanding the "why" behind user behavior, speed to insight, and making data-driven product decisions.

VP of Engineering/CTO: Cares about technical implementation complexity, performance impact, data security, infrastructure costs, and developer productivity.

3. Angle (Your Argument or Hypothesis)
The angle is the specific pain point or opportunity you're highlighting. Before writing a single word of copy, you should test several high-level angles to see what resonates.

Angle A: Tool Consolidation ("Replace 3-5 tools with one platform.")

Angle B: Cost Optimization ("Cut your analytics spend by 60% without losing features.")

Angle C: Privacy & Data Ownership ("Your data stays on your infrastructure. Full GDPR compliance by default.")


4. Message (The Actual Words)
The message is the tactical execution of your chosen Segment, Persona, and Angle. This is where you test different ways of articulating a specific pain point.

Example: Targeting Head of Product (Persona) using Mixpanel + LaunchDarkly + FullStory (Segment)


Research and identify high-quality target accounts .. pain based segmenting by doing reesearch at scale with Clay and help expand your current ICP Scoring Model to include segmentation based on certain data points such as tech stack their using, recent funding, if they are hiring a Product Engineer -- these data points allow us to see who would potentially be a better fit for us based on pain they are experiencing that PostHog could potentailly solve. . 

This prodcut engineers hate from sales pepole which is what i'll try not to do:

- Overpromising or bullshitting
- Trying to "handle" objections, if they don't want to talk to me on the phone.. its ok, just ask if you can send them an email.

What I'll do instead:

- Honest conversations about tradeoffs
- Acknowledging when you're not a fit ..

This is my plan for outbound at PostHog, still needs and will always need polishing and revising as its a living document. The goal is to ship experiments without being a sleezy sales person and making it fun to interact with a salesperson thats not trying to slam the sale down their throats. 

Tools will change, messaging, tactics, but the core values of how those are produced will alwyas keep the best interest of the PC. 


-----



Use this file to capture your learnings, insights, and preparation progress.

One thing I found really interesting is that when you publicly announce everything you're doing publicly, it really puts this positiver pressue to product something better. No gatekeeping information, no doing shady stuff.. it provides accountability. 

The reason I say that is because while doing this execise publicly on LinkedIn, I noticed you have to be a lot more honest about the work you do. 

I appreciate this sensation a lot because it forces you to not skip corners when building something. 


---

TODO:
- Understand what autocapture does vs custom events
- Can explain feature flags and experiments to an engineer
- Know when to use server-side vs client-side SDKs
- Understand the data pipeline and how events flow

Case Study: Webshare
Proxy and web scraping services

Use Case: Consolidated analytics + experimentation platform
Result: 26% conversion improvement from "Buy Now" CTA experiment

Case Study: Juicebox
AI application

Use Case: User experience research
How: Watches session replays to identify confusion points
## Key Insights & Observations

**Why buy PostHog?**

By integrating PostHog into your app, you’ll be able to track and diagnose errors, roll out and test new features and gain a better understanding of your users. Getting all of these capabilities through one SDK means you reduce the overhead of maintaining your app and **can focus on shipping your product.** .. 


For Prodcut Engineers this means:

- Auto Error tracking: session replay + product analytics
- Target new features: Target a specific segment/cohort and see how they experience features.
- A/b test new features: see if the new experience is better than the old.
- Debug: see how users consume AI, you can monitor performance, costs, latency and see how diff models perform

**Main talking points:**
1) All products in one place.. don't have to pay for more tools, reduce data silos, and context switching.
2) They build the things people actually need, not what the sales teams asks for.
3) Usage based pricing -- clear pricing model.
4) Do sales differently!

[Handbook (Outbound sales) ]([url](https://posthog.com/handbook/growth/sales/outbound-sales))

- They need to get really good at outbound as inbound dries up.

**What is considered outbound?**

Person signed up, but not really using, usually just kicking the tires
Person had signed up or used PostHog previously, has moved on to a new job which is not using PostHog
Not signed up, but has heard of PostHog
Not signed up, never heard of PostHog

Examples of good outreach:

Hello [name], It looks like your Product Analytics usage has increased over the past month and I wanted to ensure that the increase was expected. 

Here are some tools you can use to ensure you are collecting the correct events and getting valuable insights from them. 

We have a whole host of tutorials and guides to help you get the most out of PostHog. If you have any questions, don't hesitate to ask.

PVP would be a really good example of how to do outreach. 

.. do a little digging on a good PVP for PostHog.

**Use cases**

Understanding user behavior → Product Analytics
Debugging conversion drops → Funnels + Session Replay
Safe feature releases → Feature Flags
Testing hypotheses → Experiments
Collecting feedback → Surveys
Privacy/compliance → Self-hosting

### PostHog Philosophy



Really like that they don't want you to execute your previous company's playbook. They're trying to do things differently from 90% of the industry. If you come in with traditional BDR tactics, you'll fail.







### [ICP Scoring Handbook immprovements]([url](https://posthog.com/handbook/growth/marketing/icp))

Currently using Clearbit for their scoring model, which is a score out of 24. Think there's room for improvement as this only contains mainly firmographic data like company type, country, revenue, etc. 

From an outbound perspective, having a pain based model included into this current model can help find companies that are actively experiencing problems PostHog solves. Other things such as technographics can be included. Based on first party data, PostHog might consistently win over other specific competitors which would be weigfhted differently on the scoring model. 

Using Clay, you can scale sourcing these unique data points that are relevant to PostHog and impact which company would be the absolute best fit based on many other data points beyond firmographic data.

One thing I found interesting is they score companies above 500 employees lower due to slower deals. 



### Technical Learnings
_Notes from implementing PostHog, SDK quirks, useful features discovered_




### Sales Approach Ideas
_Your own ideas for outbound, messaging, reverse demos_

1) Reverse Demo Idea

Varun (Clay) - "If you’re learning how to drive a car, you don’t sit in the passenger seat while the instructor lectures you. You take the wheel while the instructor safely guides you." ... “Let’s say you signed up for the waitlist. I would review the list in Clay every morning, and if you fit our ICP I would trigger an email that said, ‘Hey, book some time with me and come prepared for this conversation with a dataset you want enriched or a problem that you wanted solved in this 30-minute slot,’” says Anand. 

This appraoch of letting the Engineer drive the wheel and feel in control is going to be critical to a non-salesy approach. 

Why does the reverse demo work? (Varun)
- Customers gained the confidence to come back
- Folks joined the community Slack
<br>

<img width="1600" height="900" alt="Clay&#39;s Reverse Demo" src="https://github.com/user-attachments/assets/c4e35a8d-420b-4966-a6d8-4d5a5ef1d5ce" />

<br>

2) **Get on texting or slack terms**

When an ICP fit Engineer signsup, offer them to get on texting terms and offer help whenever possible. Give them tactical, and easy guides to follow based on any triggers you find. You can use Clay for this. Setup webhook from signup page, identify ICP, push specific non salesy messaging. 

Varun - "To build an authentic relationship with your buyer, get out of the formality of email and text them instead."

3)  Joine communities as a helper, not a seller.

Slack channels, Whatsapp groups.. join communuties where Product Engineers live. 

4) Create content that teaches, not sells.

5) From PostHog Sales Handbook - Warm outbound to product leads: We get hundreds of ICP signups to PostHog every week, and we want to make sure we're laser focused on ensuring they have the best possible experience with PostHog by proactively reaching out to them based on certain triggers. Some people call this 'warm outbound'.

- Setting up Clay to accomodate the massive amounts of signups is crucial here.
- Questions here for myself.. how can the sales team continue to enhacnce the experience after signing up? How can sales be a helpful guide after signing up?




---

## Study Progress

### Resources Completed
- [ ] PostHog Handbook - Sales Overview
- [ ] PostHog Handbook - How We Work
- [ ] PostHog Handbook - Culture
- [ ] PostHog Handbook - Values
- [ ] PostHog Documentation - Product Analytics
- [ ] PostHog Documentation - Feature Flags
- [ ] PostHog Documentation - Session Replay

### Implementation Practice
- [ ] Set up PostHog account
- [ ] Implemented in test project
- [ ] Created custom events
- [ ] Built a funnel
- [ ] Set up feature flag
- [ ] Ran an experiment
- [ ] Configured session replay
- [ ] Built demo environment

---

## Interview Preparation

### Questions I Want to Ask
1.
2.
3.

### Stories to Share
_Specific examples that demonstrate relevant skills_

**Technical problem I solved:**


**Time I was honest even when difficult:**


**Example of self-starting/autonomy:**


**How I've helped customers succeed:**


---

## Competitive Intelligence Notes

### Amplitude
_Key differentiators, common objections, when they win_




### Mixpanel
_Key differentiators, common objections, when they win_




### Heap
_Key differentiators, common objections, when they win_




### LaunchDarkly
_Key differentiators, common objections, when they win_




---

## ICP Practice

## Learning about Product Engineer's

PE's are software engineers that are full-stack but typically more frontend focused. They are customer obssessed, data-driven & autonomous (ship without gatekeepers).

They interact with customers to deeply understand problems.

Consiladating tools is one primary reason PostHog wins.. how does this help PE's?
- Reduce data silos.
- More tools = more expensive. 

Like most folks in SaaS, they are using 10+ tools.. GitHub, IDE, Slack --> more context switching means getting less done.

Engineers evluate tools by actually using the tool. "Technical evaluation matters more than sales pitch" <---- REALLY IMPORTANT. Get rid of the sales BS talk. 



### Company Analysis Examples
_Practice qualifying companies using PostHog's ICP criteria_

**Company 1:**
- Name:
- Employees:
- Funding:
- Revenue signals:
- Engineering-led?:
- ICP Score:
- Qualified? Why/why not:

**Company 2:**
- Name:
- Employees:
- Funding:
- Revenue signals:
- Engineering-led?:
- ICP Score:
- Qualified? Why/why not:

---

## Outbound Messaging Drafts

### Email Template 1: Tool Consolidation
**Subject:**

**Body:**




---

### Email Template 2: Specific Pain Point
**Subject:**

**Body:**




---

### LinkedIn Message Template
**Message:**




---

## Questions & Uncertainties

_Things to research further or ask in the interview_

1.
2.
3.

---

## Reflections

**What I learned:**


**What I practiced:**


**What's still unclear:**


---

## Pitches

Pitch 1: Simple Version (For my partner Morgan)

Have you ever walked into a busy store looking for one specific thing - maybe a birthday card or a phone charger - and you just couldn't find it? You walked around, got frustrated, and eventually just left without buying anything.

Now imagine you're the store owner. You have no idea that just happened. You don't know that 20 people today walked in wanting to buy something but left empty-handed because they couldn't find it. You can't fix a problem you don't know exists.

That's exactly what happens with apps and websites - but it's even worse.

When someone downloads your banking app or visits your online store, you can't see them getting confused. You can't see them tapping the wrong button five times. You can't see them give up right before signing up because the page was too slow or confusing.

PostHog lets you see all of that.

It's like having a way to watch a replay of every customer's experience in your store - where they went, what they looked at, where they got stuck, and why they left. Except it's for apps and websites.

Let me give you a real example:

Say you run an app and notice that half of people who start signing up never finish. That's a huge problem - but why is it happening? With PostHog, you can literally watch recordings of what those people did. Maybe they all got stuck on the same confusing screen. Maybe the "Next" button was hard to find. Once you see it, you can fix it - and suddenly twice as many people are signing up.

Here's what makes PostHog different:

One: Most companies need to buy 4 or 5 different tools for this. One to see the numbers, one to watch recordings, one to test different versions. PostHog does all of it in one place. Simpler and cheaper.

Two: It's built for the engineers who actually create these apps. Most tools like this are built for marketing people, so the engineers who need to use them hate them. PostHog is built the way engineers think, so they actually use it.

Three: It's open - anyone can look at the code and see exactly what it does. No secrets. That matters when you're trusting a tool with your customer data.

Why should businesses care?

Think about it this way: if 100 people visit your website and only 2 buy something, that's pretty normal. But if you could figure out why the other 98 left and fix even some of those problems, you could double or triple your sales without spending more on advertising.

PostHog shows you exactly where people are "walking out of your store" - and why - so you can actually do something about it.

The bottom line: You know that frustrating experience of not finding what you need in a store and just leaving? PostHog helps companies see when that's happening in their apps, so they can fix it. And they built it specifically for the technical people who can actually make those fixes.

NOTES: Clean up beginning and end of pitch to be more impactful. 
---

**Pitch 2: Technical Pitch **

PostHog is the all-in-one product analytics platform built for engineers.

The problem it solves:

Right now, most teams are running Amplitude or Mixpanel for analytics, LaunchDarkly for feature flags, Hotjar for session replay, and maybe Optimizely for experiments. That's four different tools, four different data sources, four different bills, and none of them talk to each other properly.

PostHog consolidates all of that into one platform with a unified data model.

What's included:

Product analytics with funnels, retention, and trends
Session replay with full DOM reconstruction
Feature flags with percentage rollouts and user targeting
A/B testing with statistical significance
Surveys for in-app feedback
And a data warehouse you can query with SQL
Why engineers prefer it:

Autocapture. Unlike Mixpanel or Amplitude, PostHog starts capturing events the moment you deploy. Pageviews, clicks, form submissions - all automatic. You can do retroactive analysis on data you didn't know you'd need. Custom events are still there when you need them.

Native integration. Because everything shares the same data layer, you can go from a conversion funnel to a session replay in one click. You can see exactly how your feature flag variants affect your metrics. The data is actually connected.

Open source. The core is MIT licensed. You can self-host if you need to, inspect the code, and there's no vendor lock-in. For teams with compliance requirements, that matters.

API-first. Everything you can do in the UI, you can do via API. Create insights programmatically, manage flags in your CI/CD, export data to your warehouse.

Implementation is straightforward:

JavaScript snippet or npm package. About 10 lines of code to get started:

posthog.init('your-key', { api_host: 'https://us.i.posthog.com' })
posthog.capture('event_name', { property: 'value' })
SDKs for React, Next.js, Python, Node, iOS, Android, and more.

Pricing:

Generous free tier - 1 million events, 5K session recordings, 1M flag requests per month. Usage-based after that. Transparent pricing on the website, no "talk to sales" to see what it costs. Even Enterprise is self-serve at $2k/month.

Who it's for:

Product engineers at Series B+ startups who want to move fast, ship safely with feature flags, and understand their users without stitching together five different tools.

Bottom line: It's the analytics platform engineers would build for themselves - because it was. And it actually replaces your whole stack, not just one piece of it.

---

Quicker pitch using secret shopper as core analogy (45s):

Think about how grocery stores transformed over the decades. They went from simply stocking shelves to obsessing over customer experience—using secret shoppers, receipt surveys, and store layout optimization to understand why customers leave without buying.

Now, every business has a digital storefront. But you can't send a secret shopper to your website. You can't watch someone abandon their cart and ask them why.

That's where PostHog comes in.

PostHog is like having a secret shopper for every single visitor to your site. You can see exactly where customers get stuck, what makes them hesitate, and why they don't complete that final purchase. Session recordings show you the "why" behind the data. Analytics tell you what's working and what isn't. And you can test improvements instantly with feature flags.

Grocery stores revolutionized retail by understanding their customers. PostHog lets you do the same thing—for your digital storefront.

---


## Random Ideas & Thoughts

Implemeenting PostHog

Really cool.. with LLM analytics you can tracks your app's server-side LLM usage (cost, performance, model usage). For instnace if you have a AI generate summary button, you can track the event of a button clicked.. and the LLM usuaage of that AI action, then use that data to make better decisions. 






