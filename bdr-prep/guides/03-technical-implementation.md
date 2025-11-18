# Technical Implementation Guide

This guide covers everything you need to know to implement PostHog without engineering help. As a Founding BDR, technical self-sufficiency is non-negotiable.

## Why Technical Skills Matter

PostHog explicitly states:

> "Technical aptitude - their team members are the primary person responsible for the customer relationship, and that includes solving technical problems."

You need to be able to:
- Implement PostHog in common frameworks
- Troubleshoot basic issues
- Answer technical questions on calls
- Demo the product convincingly
- Understand what engineers are talking about

---

## Getting Started

### 1. Create Your PostHog Account

Sign up at [app.posthog.com/signup](https://app.posthog.com/signup)

**Free tier includes:**
- 1 million events/month
- 5,000 session recordings
- 1 million feature flag requests
- 100,000 exceptions
- 1,500 survey responses

### 2. Get Your Project API Key

After signup:
1. Go to Project Settings
2. Find your API Key and Project ID
3. You'll need these for every implementation

---

## Core Concepts

### Events

Everything in PostHog is an event. Events have:
- **Name**: What happened (e.g., "button_clicked")
- **Properties**: Details about what happened
- **Distinct ID**: Who did it
- **Timestamp**: When it happened

### Autocapture vs Custom Events

**Autocapture** (automatic):
- Page views
- Page leaves
- Clicks on `<a>`, `<button>`, `<input>`, etc.
- Form submissions
- Input changes

**Custom Events** (you define):
- Business-specific actions
- Backend events
- Anything autocapture doesn't catch

### Best Practice: Event Naming

Use `[object] [verb]` format:
- `project created`
- `user signed up`
- `invite sent`
- `feature flag evaluated`

---

## JavaScript Web Implementation

This is the most common implementation and what you'll use most often.

### Basic Installation

**Option 1: Script Tag**

```html
<script>
    !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures getActiveMatchingSurveys getSurveys onSessionId".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    posthog.init('<YOUR_API_KEY>',{api_host:'https://us.i.posthog.com'})
</script>
```

**Option 2: npm Package**

```bash
npm install posthog-js
# or
yarn add posthog-js
```

```javascript
import posthog from 'posthog-js'

posthog.init('<YOUR_API_KEY>', {
    api_host: 'https://us.i.posthog.com',
    person_profiles: 'identified_only' // Recommended
})
```

### Capturing Custom Events

```javascript
// Basic event
posthog.capture('button_clicked')

// Event with properties
posthog.capture('purchase_completed', {
    product_id: '12345',
    price: 99.99,
    currency: 'USD'
})
```

### Identifying Users

```javascript
// When user logs in
posthog.identify('user_123', {
    email: 'user@example.com',
    name: 'John Doe',
    plan: 'pro'
})

// Reset on logout
posthog.reset()
```

### Feature Flags

```javascript
// Check if flag is enabled
if (posthog.isFeatureEnabled('new_dashboard')) {
    // Show new dashboard
} else {
    // Show old dashboard
}

// Get flag payload
const payload = posthog.getFeatureFlagPayload('new_dashboard')

// Wait for flags to load
posthog.onFeatureFlags(function() {
    if (posthog.isFeatureEnabled('new_dashboard')) {
        // Now safe to use
    }
})
```

### Configuration Options

```javascript
posthog.init('<YOUR_API_KEY>', {
    api_host: 'https://us.i.posthog.com',

    // Recommended settings
    person_profiles: 'identified_only', // Reduces costs
    capture_pageview: true,            // Auto pageviews
    capture_pageleave: true,           // Track exits

    // Session replay
    disable_session_recording: false,  // Enable replay

    // Privacy
    respect_dnt: false,                // Respect Do Not Track

    // Performance
    loaded: function(posthog) {
        // Called when PostHog is ready
    }
})
```

---

## React Implementation

### Installation

```bash
npm install posthog-js
# or
yarn add posthog-js
```

### Provider Setup

```jsx
// app/providers.js
'use client'

import posthog from 'posthog-js'
import { PostHogProvider } from 'posthog-js/react'

if (typeof window !== 'undefined') {
  posthog.init('<YOUR_API_KEY>', {
    api_host: 'https://us.i.posthog.com',
    person_profiles: 'identified_only',
  })
}

export function PHProvider({ children }) {
  return <PostHogProvider client={posthog}>{children}</PostHogProvider>
}
```

### Using the Hook

```jsx
import { usePostHog } from 'posthog-js/react'

function MyComponent() {
  const posthog = usePostHog()

  const handleClick = () => {
    posthog.capture('button_clicked', {
      button_name: 'signup'
    })
  }

  return <button onClick={handleClick}>Sign Up</button>
}
```

### Feature Flags in React

```jsx
import { useFeatureFlagEnabled, useFeatureFlagPayload } from 'posthog-js/react'

function Dashboard() {
  const isNewDashboard = useFeatureFlagEnabled('new_dashboard')
  const payload = useFeatureFlagPayload('new_dashboard')

  if (isNewDashboard) {
    return <NewDashboard config={payload} />
  }

  return <OldDashboard />
}
```

---

## Next.js Implementation

### App Router Setup

```jsx
// app/providers.js
'use client'

import posthog from 'posthog-js'
import { PostHogProvider } from 'posthog-js/react'

if (typeof window !== 'undefined') {
  posthog.init(process.env.NEXT_PUBLIC_POSTHOG_KEY, {
    api_host: process.env.NEXT_PUBLIC_POSTHOG_HOST,
    person_profiles: 'identified_only',
    capture_pageview: false // We'll capture manually
  })
}

export function PHProvider({ children }) {
  return <PostHogProvider client={posthog}>{children}</PostHogProvider>
}
```

```jsx
// app/layout.js
import { PHProvider } from './providers'

export default function RootLayout({ children }) {
  return (
    <html>
      <PHProvider>
        <body>{children}</body>
      </PHProvider>
    </html>
  )
}
```

### Page View Tracking

```jsx
// app/PostHogPageView.js
'use client'

import { usePathname, useSearchParams } from 'next/navigation'
import { useEffect } from 'react'
import { usePostHog } from 'posthog-js/react'

export default function PostHogPageView() {
  const pathname = usePathname()
  const searchParams = useSearchParams()
  const posthog = usePostHog()

  useEffect(() => {
    if (pathname && posthog) {
      let url = window.origin + pathname
      if (searchParams.toString()) {
        url = url + `?${searchParams.toString()}`
      }
      posthog.capture('$pageview', { '$current_url': url })
    }
  }, [pathname, searchParams, posthog])

  return null
}
```

---

## Python (Server-Side) Implementation

Use this for backend event tracking.

### Installation

```bash
pip install posthog
```

### Basic Usage

```python
from posthog import Posthog

posthog = Posthog(
    project_api_key='<YOUR_API_KEY>',
    host='https://us.i.posthog.com'
)

# Capture event
posthog.capture(
    distinct_id='user_123',
    event='purchase_completed',
    properties={
        'product_id': '12345',
        'price': 99.99
    }
)

# Identify user
posthog.identify(
    distinct_id='user_123',
    properties={
        'email': 'user@example.com',
        'plan': 'pro'
    }
)

# Feature flag check
if posthog.feature_enabled('new_feature', 'user_123'):
    # New feature logic
    pass
```

### Important Note

Server-side libraries **don't support**:
- Autocapture
- Session recording

These are client-side only features.

---

## Node.js Implementation

### Installation

```bash
npm install posthog-node
# or
yarn add posthog-node
```

### Basic Usage

```javascript
const { PostHog } = require('posthog-node')

const client = new PostHog(
    '<YOUR_API_KEY>',
    { host: 'https://us.i.posthog.com' }
)

// Capture event
client.capture({
    distinctId: 'user_123',
    event: 'purchase_completed',
    properties: {
        product_id: '12345',
        price: 99.99
    }
})

// Feature flag
const isEnabled = await client.isFeatureEnabled('new_feature', 'user_123')

// Shutdown on exit
await client.shutdown()
```

---

## Session Replay

### How It Works

Session replay records user interactions to replay later. It captures:
- DOM changes
- Mouse movements
- Clicks
- Scrolls
- Console logs
- Network requests

### Enabling Session Replay

```javascript
posthog.init('<YOUR_API_KEY>', {
    api_host: 'https://us.i.posthog.com',
    disable_session_recording: false, // Enabled by default

    // Recording options
    session_recording: {
        maskAllInputs: true,         // Privacy
        maskTextSelector: '.private' // Custom masking
    }
})
```

### Privacy Controls

```javascript
// Mask all inputs (recommended for PII)
session_recording: {
    maskAllInputs: true
}

// Mask specific elements
// Add class="ph-no-capture" to elements
<div class="ph-no-capture">Sensitive content</div>
```

### Useful for Sales

Session replay is powerful for:
- Understanding user pain points
- Debugging issues customers report
- Showing prospects the value
- Connecting analytics to real behavior

---

## Feature Flags and Experiments

### Creating a Feature Flag

1. Go to Feature Flags in PostHog
2. Click "New feature flag"
3. Set key (e.g., `new_checkout`)
4. Configure rollout (percentage, user properties, etc.)
5. Save

### Using in Code

```javascript
// Simple check
if (posthog.isFeatureEnabled('new_checkout')) {
    showNewCheckout()
}

// With payload (for configuration)
const config = posthog.getFeatureFlagPayload('new_checkout')
```

### Running an Experiment

1. Create experiment in PostHog
2. Define variants (control, test)
3. Set goal metric (conversion, retention, etc.)
4. Implement variants in code
5. Let it run to statistical significance

```javascript
// Experiment code
const variant = posthog.getFeatureFlag('checkout_experiment')

if (variant === 'control') {
    showControlCheckout()
} else if (variant === 'test') {
    showNewCheckout()
}
```

---

## Common Issues and Debugging

### Events Not Appearing

1. **Check API key**: Is it correct for this project?
2. **Check API host**: Using `us.i.posthog.com` or `eu.i.posthog.com`?
3. **Check console**: Any errors in browser console?
4. **Check network tab**: Are requests to PostHog succeeding?

### Feature Flags Not Working

1. **Wait for load**: Use `onFeatureFlags` callback
2. **Check distinct ID**: Must match between client and server
3. **Check conditions**: Are flag conditions met?

### Session Replay Not Recording

1. **Check settings**: `disable_session_recording` should be `false`
2. **Check quota**: Free tier is 5,000 recordings/month
3. **Check browser**: Some browsers/extensions block it

### Debug Mode

```javascript
posthog.init('<YOUR_API_KEY>', {
    api_host: 'https://us.i.posthog.com',
    debug: true // Logs everything to console
})
```

---

## SDK Comparison

| Feature | Web | React | Node | Python |
|---------|-----|-------|------|--------|
| Autocapture | Yes | Yes | No | No |
| Session Replay | Yes | Yes | No | No |
| Feature Flags | Yes | Yes | Yes | Yes |
| Identify | Yes | Yes | Yes | Yes |
| Custom Events | Yes | Yes | Yes | Yes |
| Async | No | No | Yes | Yes |

---

## Best Practices

### 1. Use identified_only for Person Profiles

```javascript
person_profiles: 'identified_only'
```

This reduces costs significantly (anonymous events are 4x cheaper).

### 2. Capture Business-Relevant Events

Don't just rely on autocapture. Capture what matters:
- Sign ups
- Purchases
- Feature usage
- Key conversions

### 3. Use Properties Thoughtfully

```javascript
// Good - specific and useful
posthog.capture('purchase_completed', {
    product_id: '12345',
    price: 99.99,
    currency: 'USD',
    payment_method: 'card'
})

// Bad - too generic
posthog.capture('click')
```

### 4. Test in Development

Always test your implementation before going live. Use debug mode.

### 5. Respect Privacy

- Use masking for sensitive data
- Consider GDPR/CCPA requirements
- Give users opt-out options

---

## Demo Environment Setup

Create a demo project you can use in sales calls:

### 1. Create a Simple Web App

Use something like:
- Static HTML page
- Simple React app
- Next.js starter

### 2. Implement PostHog Fully

- Autocapture enabled
- Custom events for key actions
- User identification
- Feature flags with variants
- Session recording

### 3. Generate Sample Data

- Create multiple user journeys
- Trigger various events
- Test feature flag variants

### 4. Build Demo Dashboards

- Trends for key metrics
- Funnels for conversion
- Retention charts
- Session playlists

### 5. Practice the Demo

Know how to:
- Show insights creation
- Navigate from chart to session
- Explain feature flags
- Show experiment results

---

## Resources

### Official Documentation
- [JavaScript Web](https://posthog.com/docs/libraries/js)
- [React](https://posthog.com/docs/libraries/react)
- [Next.js](https://posthog.com/docs/libraries/next-js)
- [Python](https://posthog.com/docs/libraries/python)
- [Node.js](https://posthog.com/docs/libraries/node)

### Tutorials
- [Event Tracking Guide](https://posthog.com/tutorials/event-tracking-guide)
- [Feature Flags Tutorial](https://posthog.com/tutorials/feature-flags)
- [All Tutorials](https://posthog.com/tutorials)

### GitHub
- [posthog-js](https://github.com/PostHog/posthog-js)
- [posthog-python](https://github.com/PostHog/posthog-python)
- [posthog-node](https://github.com/PostHog/posthog-node)
