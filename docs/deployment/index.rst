##############
ATS Deployment
##############

This section provides the coordinated runbook for deploying the Rubin ATS.
Use the approved configuration records for exact addresses, ports, credentials, and release versions.

Deployment sequence
###################

Plan a deployment as a coordinated system change rather than as independent controller updates.
Confirm approved firmware, controller configuration, network endpoints, simulator versions, and safety configuration before changing a target.
Deploy supporting services before controller applications, then validate the safety and encoder interfaces before functional testing.

.. toctree::
   :maxdepth: 1
   :titlesonly:

   simulators-and-tools
   pxi
   safety-and-encoder

Common post-deployment validation
#################################

1. Confirm the deployed versions and application logs for every changed component.
#. Verify each controller and service reaches only approved ATS endpoints.
#. Perform safe component health checks and retain the relevant automated smoke-test result with the deployment record.

