# Clay Video Script: Building a Qualification Funnel for PostHog
## Video Tutorial Outline & Talking Points

**Target Length**: 15-20 minutes
**Target Audience**: BDRs, SDRs, Sales Ops professionals
**Video Goal**: Show how to build a comprehensive lead scoring system using Clay and web enrichment

---

## Video Structure

### Intro (1 minute)
### Part 1: The Problem (2 minutes)
### Part 2: The Solution Overview (2 minutes)
### Part 3: Building Table 1 - Scoring Engine (6 minutes)
### Part 4: Building Table 2 - Contact Finding (3 minutes)
### Part 5: Building Table 3 - Personalization (3 minutes)
### Part 6: Results & Wrap-up (2 minutes)

---

## Detailed Script

### INTRO (1 minute)

**[Screen: Your face or logo]**

**YOU**:
"Hey everyone! Today I'm going to show you how to build a qualification funnel in Clay specifically for PostHog - but this framework works for any B2B SaaS product.

Most lead scoring systems just look at basic firmographics - company size, industry, job title. That's fine, but it misses SO much.

What if you could automatically score leads based on:
- Whether they just raised funding
- If they're actively hiring engineers
- What tools they're currently using
- Recent product launches or pain points they're experiencing

That's what we're building today. By the end of this video, you'll have a complete 60-point scoring system that automatically:
1. Enriches leads with web data
2. Scores them across 5 categories
3. Generates personalized messaging hooks
4. Syncs to your CRM

Let's dive in."

---

### PART 1: THE PROBLEM (2 minutes)

**[Screen: Show PostHog's current ICP scoring doc or your notes]**

**YOU**:
"So PostHog currently uses a 24-point scoring model powered by Clearbit. Here's what it looks at:

**[Show on screen]**:
- Engineering role: 6 points
- Leadership: 3 points
- Product role: 3 points
- Private company: 3 points
- Founded 2015-2022: 3 points
- 15-500 employees: 3 points
- Good geography: 3 points

This is solid! It tells you WHO fits the ICP. But here's what it doesn't tell you:

**[Show on screen]**:
❌ WHAT problems they're experiencing
❌ WHEN to reach out (timing signals)
❌ WHY PostHog matters to them specifically
❌ WHAT tools they're currently using

So you end up with leads that LOOK good on paper, but you have no idea how to personalize your message. You're still sending pretty generic outreach.

That's the gap we're filling today."

---

### PART 2: THE SOLUTION OVERVIEW (2 minutes)

**[Screen: Show the scoring framework document or a visual breakdown]**

**YOU**:
"Here's the framework we're building. It's a 60-point system across 5 categories:

**[Show on screen as you talk]**:

**Category 1: Core ICP Fit (24 points)**
- This is PostHog's existing scoring
- Company size, role, founding date, etc.

**Category 2: Financial & Growth Signals (12 points)**
- Recent funding rounds
- Revenue growth
- Top-tier investors
- Runway health

**Category 3: Pain Indicators (12 points)**
- Hiring product engineers
- Hiring data/analytics roles
- Recent product launches
- Growth indicators

**Category 4: Tech Stack & Competitors (8 points)**
- Using PostHog competitors (Mixpanel, Amplitude, etc.)
- Multiple point solutions
- Engineering blog presence

**Category 5: Behavioral & Timing (4 points)**
- Posting about data challenges
- Active in product communities
- Recent competitor reviews

Add it all up, and you get a lead score that tells you not just IF they're a good fit, but WHEN to reach out and WHAT to say.

Let me show you how to build this in Clay."

---

### PART 3: BUILDING TABLE 1 - SCORING ENGINE (6 minutes)

**[Screen: Clay interface, creating a new table]**

**YOU**:
"Alright, let's build this. I'm going to start with Table 1, which is our main scoring engine.

**Step 1: Input your leads**

**[Show importing]**:
I'm starting with a simple list of company domains. You can import this from:
- Your CRM
- A LinkedIn Sales Navigator export
- A manual list
- Anywhere really

**[Show column 1 with company domains]**

**Step 2: Core enrichment with Clearbit**

**[Click to add Clearbit enrichment]**:
First, I'm adding Clearbit Company API enrichment. This gets us all the firmographic data.

**[Show configuring]**:
- Input is the company domain
- I'm setting up a waterfall with People Data Labs as backup
- This gives us: employee count, founded date, industry, revenue, etc.

**[Show the data populating]**

Now I'm going to create formula columns to score each ICP criterion.

**[Add formula column 'Company Size Score']**:
This formula checks if they're between 15-500 employees. If yes, 3 points.

**[Show the formula]**:
```javascript
if (clearbit.employees >= 15 && clearbit.employees <= 500) {
  return 3;
} else {
  return 0;
}
```

**[Show it calculating]**

I'll do the same for:
- Founded date (2015-2022 = 3 points)
- Private company (3 points)
- Geography (US, UK, EU = 3 points)

**[Show these columns being added - can speed up the video here]**

**Step 3: Funding data with Crunchbase**

**[Add Crunchbase enrichment]**:
Next up, funding data. I'm adding Crunchbase enrichment to pull:
- Last funding date and amount
- Funding round (Series A, B, C, etc.)
- Investor names
- Total funding

**[Show data populating]**

Now the scoring formulas. This one checks if they raised funding in the last 12 months at Series B or later:

**[Show formula]**:
```javascript
const lastFundingDate = new Date(crunchbase.lastFundingDate);
const monthsSinceFunding = (Date.now() - lastFundingDate) / (1000 * 60 * 60 * 24 * 30);

if (monthsSinceFunding <= 12 && ["Series B", "Series C"].includes(crunchbase.lastFundingRound)) {
  return 5;
} else {
  return 0;
}
```

That's 5 points if they recently raised money - perfect timing to reach out!

**[Show another formula for top investors]**:
This one checks if they have a top-tier investor. If they're backed by Sequoia, a16z, YC, etc., that's 2 more points.

**Step 4: Job postings data**

**[Add LinkedIn Jobs scraper or HTTP API]**:
This is where it gets really interesting. I'm scraping their job postings to see what they're hiring for.

**[Show job data populating]**

Now I can score based on what roles they're hiring:

**[Show formula]**:
- 5 points if hiring 3+ product engineers
- 3 points if hiring data/analytics roles
- 2 points if hiring product managers

This tells us they're scaling and likely experiencing the exact pain points PostHog solves.

**Step 5: Tech stack with BuiltWith**

**[Add BuiltWith enrichment]**:
BuiltWith detects what technologies they're using on their website.

**[Show tech stack data]**

The magic here is detecting competitors:

**[Show formula]**:
If they're using Mixpanel, Amplitude, LaunchDarkly, FullStory, etc. - that's 5 points.

Why? Because they're ALREADY bought into this category. They're not cold on the problem - they're using a solution. That's a warm lead.

**Step 6: Calculate total score**

**[Add final formula column]**:
Now I'm adding one final column that adds up all the individual scores.

**[Show the formula summing everything]**

**[Show the scores calculating]**

Beautiful! Now I have leads scored from 0-60.

**Step 7: Add priority tiers**

**[Add formula column]**:
Last thing - I'm creating priority tiers:
- 45-60: Hot Lead (immediate outreach)
- 35-44: Warm Lead (personalized outreach)
- 25-34: Qualified Lead (semi-personalized)
- Below 25: Skip or nurture

**[Show the priority column populating]**

**Step 8: Filter**

**[Add filter]**:
And I'm filtering to only pass leads with 25+ points to the next table. No point wasting time on poor fits.

**[Show filtered results]**

That's Table 1! We now have scored, qualified companies. Next, let's find the actual people."

---

### PART 4: BUILDING TABLE 2 - CONTACT FINDING (3 minutes)

**[Screen: Create Table 2]**

**YOU**:
"Table 2 is simpler. We're taking qualified companies and finding decision-makers.

**Step 1: Import qualified companies**

**[Show importing from Table 1]**:
I'm importing all companies from Table 1 that scored 25 or higher.

**Step 2: Find people with Apollo**

**[Add Apollo enrichment]**:
Now I'm using Apollo's People Search to find contacts at each company.

**[Show configuring filters]**:
I'm filtering for:
- Job titles: Engineering, CTO, VP Engineering, Product Manager, CEO
- Seniority: Manager, Director, VP, C-Level
- Limit: 10 per company

**[Show contacts populating]**

**Step 3: Score by role**

**[Add formula column]**:
Different roles get different points:
- Engineering roles: 6 points (they're the primary buyers)
- Leadership: 3 points
- Product: 3 points

**[Show the formula]**

**Step 4: Verify emails**

**[Add email verification]**:
I'm running emails through a verification service to remove bounces.

**Step 5: Final score**

**[Add formula]**:
Final contact score = company score + role score

**[Show scores]**

So now I have individual contacts with scores. A product engineer at a recently-funded company hiring engineers might score 50+ points. That's someone I'm reaching out to TODAY.

**[Add filter for 30+]**:
I'm filtering for 30+ and passing high-priority contacts to Table 3 for deep personalization."

---

### PART 5: BUILDING TABLE 3 - PERSONALIZATION (3 minutes)

**[Screen: Create Table 3]**

**YOU**:
"Table 3 is where the magic happens. This is deep research on your hottest leads to generate truly personalized messages.

**Step 1: Import high-priority contacts**

**[Show importing contacts with 35+ score]**:
I'm only doing this for 35+ scored contacts. These are my hot and warm leads worth the extra effort.

**Step 2: LinkedIn activity**

**[Add LinkedIn post scraper]**:
I'm scraping their last 5 LinkedIn posts to see what they're talking about.

**[Show posts populating]**

If they've posted about data challenges, analytics, experiments - that's pure gold for personalization.

**Step 3: Company blog scraper**

**[Add blog scraper]**:
Same thing with their company blog. Looking for articles they wrote or product announcements.

**Step 4: AI-generated personalization**

**[Add Claude or GPT-4 enrichment]**:
Now here's the really cool part. I'm feeding ALL of this context into Claude (or GPT-4) to generate personalized messages.

**[Show the AI prompt]**:
The prompt includes:
- Their role and company
- Funding info
- Job postings
- Tech stack
- Recent posts
- Recent blog articles

And I'm asking Claude to write a 4-6 sentence email that:
1. Opens with a specific observation
2. Asks a thoughtful question about a real pain point
3. Mentions PostHog naturally
4. Includes social proof
5. Low-friction CTA

**[Show a generated message]**:
Look at this output. This isn't a template - it's genuinely personalized based on their specific signals.

**[Read an example]**:
'Hey Sarah, congrats on the Series B! Saw you're scaling the eng team to 80 engineers and hiring 5 more product engineers right now. As you scale, how are you handling the coordination tax between Mixpanel for analytics, LaunchDarkly for flags, and FullStory for session replay? We work with a lot of Sequoia companies who consolidated all of that into PostHog. Worth a quick chat?'

That's SO much better than 'I noticed your company...'

**Step 5: Generate subject lines**

**[Add another AI formula]**:
I'm also generating 3 subject line options for each message.

**[Show subject lines generating]**

**Step 6: Export to CRM**

**[Show HubSpot integration]**:
Finally, I'm syncing all of this to HubSpot:
- Companies with scores
- Contacts with roles
- Generated messages ready to send

Done!"

---

### PART 6: RESULTS & WRAP-UP (2 minutes)

**[Screen: Show the final results in a table or dashboard]**

**YOU**:
"Alright, let's look at what we've built.

**[Show Table 1 results]**:
We're taking raw company domains and outputting qualified, scored leads.

**[Show Table 2 results]**:
We're finding decision-makers and scoring them by role.

**[Show Table 3 results]**:
And we're generating truly personalized messages for our hottest leads.

**[Show examples side by side]**:
This is the difference:

**BEFORE**: 'Hi, I help companies like yours with analytics...'

**AFTER**: 'Congrats on the Series B - saw you're hiring 8 engineers. As you scale, how are you handling the coordination between Mixpanel, LaunchDarkly, and FullStory?'

One is generic. One shows you actually did research.

**The results**:

**[Show metrics if you have them, or estimated]**:
- Reply rates: 30-40% on hot leads vs. 5-10% on cold
- Meeting rate: 15-20% on hot leads vs. 2-3% on cold
- Time savings: 90% reduction in manual research

**Cost**:
- ~$3.50 per fully qualified lead with personalization
- Compare that to the value of a PostHog customer ($20k+/year minimum)
- The ROI is insane

**[Show final Clay table]**:
You can clone this entire workflow. I'll drop links in the description to:
- The full scoring framework document
- The Clay implementation guide
- Example prompts for AI personalization

Questions? Drop them in the comments. If you want to see more Clay workflows like this, let me know what products you're selling and I'll build it.

Thanks for watching!"

**[End screen with links]**

---

## B-Roll Suggestions

**Throughout the video, show**:
- Close-ups of formulas being written
- Data populating in real-time (speed up)
- Side-by-side comparisons of before/after messages
- Examples of signals being detected (funding news, job posts, etc.)
- The priority tiers updating

**Graphics to create**:
- The 60-point scoring breakdown (infographic)
- Before/after message comparison
- ROI calculator (cost per lead vs. customer value)
- Workflow diagram (3 tables → CRM)

---

## Alternative Intro Hooks (Choose One)

**Option 1 - Problem-focused**:
"You know what sucks about most lead scoring? It tells you WHO to reach out to, but not WHAT to say. Today I'm fixing that."

**Option 2 - Results-focused**:
"What if I told you I could take your reply rate from 5% to 35% by just adding better data to your outreach? That's what this Clay workflow does."

**Option 3 - Story-focused**:
"I was manually researching leads for hours, checking funding news, job posts, tech stacks. Then I realized - Clay can automate ALL of this. Here's how."

---

## Key Phrases to Emphasize

**Repeat these concepts**:
- "The score tells you WHO, the signals tell you WHAT to say"
- "Not just firmographics, but pain-ographics"
- "Truly personalized, not just mail-merged"
- "Work smarter, not harder"
- "Timing is everything - catch them right after funding or hiring"

---

## Common Questions to Address (in video or pinned comment)

**Q: How much do the Clay credits cost?**
A: ~$3.50 per lead for full enrichment. Worth it for $20k+ ACV customers.

**Q: Can I use this for other products besides PostHog?**
A: Absolutely! Just adjust the scoring weights and competitor list.

**Q: What if enrichment sources don't have data?**
A: Use waterfalls - try 3-4 sources for each data point.

**Q: Do I need all these integrations?**
A: Start with Clearbit + Crunchbase + Apollo. Add others as needed.

**Q: How do I avoid sounding creepy with all this data?**
A: Only reference PUBLIC information (funding news, job posts, blog articles). Never mention you "saw" something unless it's publicly posted.

---

## Thumbnail Ideas

**Option 1**: Split screen
- Left: "Generic Outreach" with low score
- Right: "Personalized Outreach" with high score

**Option 2**: Before/After
- Before: Sad face, 5% reply rate
- After: Happy face, 35% reply rate

**Option 3**: Visual of the scoring
- Company logo in center
- 5 categories radiating out with points

---

## Video Description Template

```
🔥 Build a PostHog qualification funnel in Clay that automatically:
✅ Scores leads 0-60 across 5 categories
✅ Enriches with funding, hiring, tech stack data
✅ Generates personalized messaging hooks
✅ Syncs to your CRM

📚 Resources:
→ Full scoring framework: [link]
→ Clay implementation guide: [link]
→ Message templates: [link]

⏱️ Timestamps:
0:00 - Intro
1:00 - The Problem with Basic Lead Scoring
3:00 - The 60-Point Framework
5:00 - Building Table 1: Scoring Engine
11:00 - Building Table 2: Contact Finding
14:00 - Building Table 3: Personalization
17:00 - Results & Wrap-up

💬 Questions? Comment below!

#Clay #LeadScoring #SalesAutomation #PostHog #BDR #SDR #B2BSales
```

---

## Post-Production Checklist

- [ ] Add zoom-ins on important formulas
- [ ] Speed up data population sections (3-4x)
- [ ] Add text overlays for key points
- [ ] Background music (subtle, not distracting)
- [ ] Color grade for consistency
- [ ] Add chapter markers on YouTube
- [ ] Pin a comment with the resources
- [ ] Respond to comments within first 24 hours

---

**Pro Tips for Recording**:

1. **Screen Resolution**: Record at 1920x1080
2. **Clay UI**: Zoom to 125% so viewers can see clearly
3. **Mouse Movement**: Slow and deliberate - give viewers time to follow
4. **Pace**: Speak clearly but energetically - you're excited to show this!
5. **Mistakes**: Don't worry about them - fix in post or leave them (shows authenticity)
6. **Practice**: Do a dry run to catch any technical issues

**Energy Level**: Match Casey Neistat or Ali Abdaal - high energy but genuine, not forced.

**Goal**: By the end, viewers should feel "I could build this myself right now." Make it actionable, not just informational.

Good luck! 🚀
