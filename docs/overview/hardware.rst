############
ATS Hardware
############

The ATS hardware closely matches the production equipment at the summit.
It combines real-time TMA, axes, and auxiliary controllers with a Speedgoat axis simulation target, encoder and safety interfaces, and an ESXi host for its supporting virtual machines.

Architecture
############

The TMA PXI, AXES PXI, and AUX PXI divide the real-time control workload by subsystem.
The Speedgoat target provides the high-rate main-axis simulation that the AXES controller requires.
The EIB supplies tape-encoder information, while the Pilz system provides the independent safety interface.
The supporting compute environment runs user interfaces, simulators, operations services, and automated tests outside the real-time controllers.

Network and safety boundaries
#############################

The ATS has separate control, simulator, and management-network responsibilities.
EtherCAT device order, safety wiring, switch configuration, and device addresses are controlled configuration items and must be verified against the approved installation record before a change is deployed.
The historic vendor design is useful for understanding those boundaries, but it is not a substitute for current Rubin configuration or safety procedures.

.. list-table:: Hardware

   * - Name
     - Model
     - Description
     - Host Name
     - Operating System
   * - ATS TMA PXI
     - NI PXI-8880
     - Provides real time control over the various TMA subsystems.
     - ats-tma-pxi.ls.lsst.org
     - NI RT Linux 24
   * - ATS AXES PXI
     - NI PXI-8881
     - Provides real time control over the TMA AXES subsystem.
     - ats-axes-pxi.ls.lsst.org
     - NI RT Linux 24
   * - ATS AUX PXI
     - Beckhoff industrial slide in PC
     - Provides auxiliary subsystems to reduce load on TMA PXI
     - ats-aux-pxi.ls.lsst.org
     - NI RT Linux 24
   * - Speedgoat
     - Speedgoat Performance Target Machine
     - Provides AXES simulation model to PXI.
     - 
     - MATLAB R2025b
   * - EIB Tape Encoder
     - Heidenhain EIB 8791
     - Provides encoder data to the AXES PXI
     - 
     - 
   * - PILZ Safety System
     -
     - Provides safety signal to system.
     - 
     -
   * - ESXI VM host
     - 
     - Provides hypervisor based Virtual Machines
     -
     - VMWare ESXI
