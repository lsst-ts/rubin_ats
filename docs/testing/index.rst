###########
ATS Testing
###########

The ATS supports both manual and automated verification of TMA software changes against simulated hardware.
Automated testing is the preferred regression path before a change is introduced to production equipment.
Manual checks remain necessary for controlled commissioning and for confirming behavior that cannot be reproduced in the simulator.

Test organization
#################

Test procedures are organized by TMA subsystem and cover normal operation, movement, stops, subsystem-specific behavior, event handling, alarm handling, and invalid operation sequences.
Robot Framework runs the automated test suite from the supporting Linux environment.
Test results should be retained with the change record and reviewed for failures, logs, and unexpected alarms.

Historical status
#################

The Tekniker test plan was written before the TMA was shipped to Chile and is historical background only.
Use the current Rubin test procedures and automated-test repositories when selecting or updating test cases.

