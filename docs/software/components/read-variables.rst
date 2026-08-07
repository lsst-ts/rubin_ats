#############
ReadVariables
#############

Status
######

Active.

Purpose
#######

ReadVariables bridges simulator applications with network shared variables hosted by the TMA PXI, AXES PXI, and the local host.

Interfaces and dependencies
###########################

The ATS runs separate configured instances for those three variable hosts.
It is a dependency of several simulator components, including limits, thermal, power, and cabinet-temperature simulation.

Repository
##########

``ts_tma_hil_read-variables``

