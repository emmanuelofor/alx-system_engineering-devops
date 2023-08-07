# Postmortem: Server Outage on 3rd June 2023 🚫🔥

## 📋 Issue Summary
- **Duration**: Started at **10:00 am GMT** on **3rd June 2023**, lasting **37 minutes**.
- **Impact**: Everyone met our not-so-friendly neighbor, Mr. HTTP 500 Error. Result? **100%** of our users were twiddling their thumbs, unable to access our services.
- **Root Cause**: Deployed upgrades to our live audience (a.k.a. production servers) without a dress rehearsal in the test environment. And, of course, software version dramas ensued.

## 🕰️ Timeline (GMT)
- **9:45 AM**: Began server upgrades without the safety net (testing).
- **10:00 AM**: Boom! Production servers go dark.
- **10:00 AM**: Our trusty monitoring tools sense disturbance in the force and scream alerts.
- **10:10 AM**: On-call team springs to action (hopefully not spilling coffee).
- **10:15 AM**: "Time to go back!" Decision to roll back servers is made.
- **10:20 AM**: We're back in time! Rollback success.
- **10:20 AM**: Servers flexing their muscles with a restart.
- **10:22 AM**: Green lights everywhere. Traffic is flowing, and all is right in the world.

## 🔍 Root Cause and Resolution
Commenced a server upgrade at **9:45 am GMT** without the usual testing protocol. The new, shiny upgrade wanted a special handshake (authentication) from third-party software. Alas! Our servers didn't know the secret handshake because of software version mismatch. Immediate fix? Time-travel (roll back) to when everyone was friends and then teach our servers the new handshake (update software).

## 🛠️ Corrective and Preventative Measures

### Broad Improvements:
- **First Impressions Matter**: Always introduce changes first in the test environment.
- **ESP for Servers**: Refine our alert system to catch even the faintest whispers of issues.

### Specific Tasks:
1. **Golden Rule**: Make it law to validate all changes in test environments first.
2. **Keeping Up With The Joneses**: Ensure all servers are compatible with the latest software trends.
3. **Sensitive Ears**: Tune our monitoring tools to be more sensitive, catching even minor hiccups.
4. **Server University**: Regular training for the engineering folks. Brush up on best practices and emergency maneuvers.

In conclusion, while this was a hiccup in our usually smooth journey, it's given us some learning homework. We promise to be better. Huge shout-out to our users for their patience and understanding. Here's to smoother surfing! 🌊🏄‍♂️
