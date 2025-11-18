# My PostHog BDR Preparation Notes

Use this file to capture your learnings, insights, and preparation progress.

---

## Key Insights & Observations

### PostHog Philosophy
_What resonates with you about their approach?_




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


2) **Get on texting or slack terms**

When an ICP fit Engineer signsup, offer them to get on texting terms and offer help whenever possible. Give them tactical, and easy guides to follow based on any triggers you find. You can use Clay for this. Setup webhook from signup page, identify ICP, push specific non salesy messaging. 

Varun - "To build an authentic relationship with your buyer, get out of the formality of email and text them instead."

3)  Joine communities as a helper, not a seller.

Slack channels, Whatsapp groups.. join communuties where Product Engineers live. 

4) Create content that teaches, not sells.

5) 


---

## Study Progress

### Resources Completed
- [ ] PostHog Handbook - Sales Overview
- [ ] PostHog Handbook - How We Work
- [ ] PostHog Handbook - Culture
- [ ] PostHog Handbook - Values
- [ ] First Round Review - Clay GTM Article
- [ ] Varun Anand Podcast (First Round)
- [ ] Varun Anand Podcast (Notion First Block)
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

You know how when you run a store, you want to understand your customers? Like, which products do they look at? Where do they get confused and leave? What makes them actually buy something?

PostHog does that for websites and apps.

When someone builds an app - like a banking app or a shopping app - they need to understand how people actually use it. Are people getting stuck? Are they finding the features they need? Are they leaving before they sign up?

PostHog shows you exactly what's happening.

Think of it like security cameras for your app, but instead of watching for theft, you're watching to see where customers get confused or frustrated. You can literally replay what someone did - where they clicked, where they got stuck, where they gave up.

But here's what makes PostHog special:

First, most companies need to buy 4 or 5 different tools to do all this. One tool to see the numbers, another to watch recordings, another to test different versions of their website. PostHog does all of it in one place. That's simpler and cheaper.

Second, PostHog is built for the engineers who actually build these apps. Most of these tools are built for marketing people, so engineers hate using them. PostHog is built the way engineers think, so they actually enjoy using it.

Third, the code is open - anyone can see exactly how it works. That builds trust because there are no secrets about what it's doing with your data.

Why does this matter for businesses?

If you're losing 50% of people during signup, and you can see exactly why and fix it, that could double your customers. If you're testing whether a blue button or green button gets more clicks, you can make decisions based on real data instead of guessing.

Companies like Airbnb and Spotify use tools like this to make their products better. PostHog is the version built specifically for the technical teams who build the product.

The bottom line: PostHog helps companies understand how people use their apps so they can make them better. And they do it in a way that engineers actually like, which means it actually gets used.

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


## Random Ideas & Thoughts

_Capture anything that comes to mind_




