########################
Human-machine Interfaces
########################

Status
######

Supporting.

Purpose
#######

The maintained EUI provides the operator-facing interface for monitoring and supervising the ATS.
The handheld HMI is deprecated, is no longer maintained, and must not be used for new ATS deployments.

Interfaces and dependencies
###########################

The EUI must target the ATS database, PXIs, and operation services rather than production services.
It is used for safe health checks such as validating encoder and controller state.

Repository
##########

``ts_tma_labview_hmi-computers``
