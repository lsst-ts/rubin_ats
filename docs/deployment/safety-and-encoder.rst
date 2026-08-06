#############################
Safety and Encoder Deployment
#############################

PILZ
****
1. Clone the test dual modbus project via - `https://github.com/lsst-ts/ts_tma_hil_test-dual-modbus <https://github.com/lsst-ts/ts_tma_hil_test-dual-modbus>`_
#. Open the PAS4000 IDE.
#. Open the project via username and password (provided via 1password vault)
#. Create a backup file
#. Open the backup file
#. Build and deploy to the Pilz.

EIB
***

Confirm that the approved EIB configuration and UDP destination match the current AXES PXI configuration.
Validate encoder data after deployment before enabling automated motion tests.
