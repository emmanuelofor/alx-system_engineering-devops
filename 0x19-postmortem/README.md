Postmortem: Server Outage on 3rd June 2023
Issue Summary
•	Duration: The outage started on 3rd June 2023 at 10:00 am GMT + 1 and lasted for 37 minutes.
•	Impact: All clients encountered an HTTP 500 error. This disruption affected 100% of our user base, rendering them unable to access our services.
•	Root Cause: Upgrades were deployed directly to production servers without prior testing in a controlled environment, leading to software version incompatibilities.
Timeline (GMT + 1)
•	9:45 AM: Server upgrades started without prior testing on test environments.
•	10:00 AM: All production servers experienced an outage.
•	10:00 AM: Monitoring tools detected the outage and alerted the on-call team.
•	10:10 AM: On-call team acknowledged the alert and began assessing the situation.
•	10:15 AM: Decision made to roll back servers to their previous state.
•	10:20 AM: Rollback completed successfully.
•	10:20 AM: Restart of servers initiated.
•	10:22 AM: Traffic fully restored. All users could access the services again.
Root Cause and Resolution 
The issue commenced after a server upgrade began at 9:45 am GMT + 1. Unfortunately, this upgrade hadn't been tested in a staging environment. It required authentication from a third-party software, which wasn't compatible with the software version on our servers. The immediate resolution was rolling back to the server's previous state and then updating the software to a compatible version.
Corrective and Preventative Measures
1.	Broad Improvements:
•	Always deploy changes first to test environments.
•	Refine alert mechanisms to predict potential crashes or failures.
2.	Specific Tasks:
•	Enforce a strict protocol where all changes must be validated in test environments before moving to production.
•	Upgrade all servers to ensure compatibility with the latest third-party software integrations.
•	Adjust monitoring tool thresholds to alert engineers even with minor performance degradations, giving them a head start before a full-blown outage.
•	Conduct regular training sessions for the engineering team to reinforce best practices in deployment and emergency response.
In conclusion, this outage, while unfortunate, has provided us with valuable insights. We are committed to implementing the corrective measures outlined above to ensure that such disruptions do not recur in the future. We deeply regret the inconvenience caused and thank our clients for their patience.
