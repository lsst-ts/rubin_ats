#################
Speedgoat Manager
#################

Status
######

Active.

Purpose
#######

The MATLAB R2025b ``speedgoatManager.mlapp`` application controls the model running on the Speedgoat, including model lifecycle and injected drive or encoder faults.

Interfaces and dependencies
###########################

It is maintained with the :doc:`main-axes` model in ``ts_tma_hil_main-axes_lsst-hil`` and is used by automated tests through its Python interface.
The former standalone Speedgoat Manager source and binary releases are deprecated with MATLAB R2025b and must not be used for new deployments.

Current repositories
####################

``ts_tma_hil_main-axes_lsst-hil`` (``src/speedgoatManager.mlapp``)

``ts_tma_hil_speedgoat-speedgoat-manager-python-interface``

Deprecated repositories
#######################

``ts_tma_hil_speedgoat-speedgoat-manager``

``ts_tma_hil_speedgoat-speedgoat-manager-binaries``
