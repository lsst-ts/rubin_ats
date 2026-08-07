#############################
Safety and Encoder Deployment
#############################

PILZ
****
1. Clone `ts_tma_hil_test-dual-modbus <https://github.com/lsst-ts/ts_tma_hil_test-dual-modbus>`_ to an approved working location.
#. Copy or rename the working project to ``TestDualModbus`` and grant the PAS4000 user permission to modify it.
#. Open PAS4000, authenticate with the approved credentials, open the project, and activate it.
#. Create a backup before making changes.
#. Configure the approved IP address, port, and allowed peer connections.
#. Build and deploy the project to the Pilz.

EIB
***

Configure the approved EIB IP address and port in the EIB application.
The ATS TMA PXI overwrites the EIB UDP destination during operation.
Validate encoder data after deployment before enabling automated motion tests.
