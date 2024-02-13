# Postmortem: Database Connection Failure on Feb 10, 2024

## Issue Summary

On Feb 10, 2024, from 10:15 AM to 10:45 AM WAT, our web application experienced a database connection failure that resulted in a 503 Service Unavailable error for all users. The issue affected 100% of the users who tried to access the application during that time. The root cause was a misconfigured firewall rule that blocked the traffic between the web server and the database server.

## Timeline

-   10:15 AM: A monitoring alert notified the DevOps team that the web server was returning a 503 error code.
-   10:17 AM: The DevOps team checked the web server logs and found that the application was unable to connect to the database server.
-   10:20 AM: The DevOps team pinged the database server from the web server and confirmed that there was no network connectivity between them.
-   10:22 AM: The DevOps team checked the firewall rules on both servers and found that a new rule had been added on the database server that denied all incoming traffic from the web server's IP address.
-   10:25 AM: The DevOps team contacted the Security team to ask about the firewall rule and learned that it was part of a security update that was applied earlier that morning.
-   10:28 AM: The Security team explained that the firewall rule was intended to block unauthorized access to the database server, but they had mistakenly applied it to the wrong server group.
-   10:30 AM: The Security team removed the firewall rule from the database server and verified that the network connectivity was restored.
-   10:32 AM: The DevOps team restarted the web server and confirmed that the application was working normally.
-   10:35 AM: The DevOps team updated the monitoring dashboard and notified the stakeholders that the issue was resolved.
-   10:45 AM: The DevOps team and the Security team conducted a post-incident review and identified the corrective and preventative measures.

## Root Cause and Resolution

The root cause of the issue was a human error by the Security team, who applied a firewall rule that blocked the traffic between the web server and the database server. The resolution was to remove the firewall rule and restore the network connectivity.

## Corrective and Preventative Measures

To prevent this issue from happening again, we recommend the following actions:

-   Implement a change management process that requires approval and testing before applying any firewall rules to production servers.
-   Improve the communication and coordination between the DevOps team and the Security team to ensure that they are aware of each other's activities and potential impacts.
-   Add more granular and specific firewall rules that only allow the necessary traffic between the web server and the database server, and deny all other traffic by default.
-   Increase the frequency and coverage of the monitoring alerts and checks to detect any anomalies or failures in the web stack.
-   Conduct regular training and reviews for the Security team to ensure that they follow the best practices and standards for firewall configuration and management.
