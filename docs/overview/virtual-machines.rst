####################
ATS Virtual Machines
####################

The ATS virtual machines provide dedicated environments for development, runtime applications, simulators, operations tools, and automated test execution.
They are hosted on the Base Data Center infastructure and support both day-to-day development and system operation.

Roles and boundaries
####################

The virtualized environment separates Windows-based build and LabVIEW runtime work from Linux-based simulator, operations, and test workloads.
This separation prevents simulator or test activity from changing the real-time PXI controller environment.
Historic vendor documentation describes an earlier Windows and Linux layout, but current host assignments, operating systems, and access controls are maintained by Rubin operations.

.. list-table:: Virtual Machines

   * - Hostname
     - OS
     - Purpose
   * - ats-tma-dev.ls.lsst.org
     - Windows 10
     - Builds executables
   * - ats-windows.ls.lsst.org
     - Windows 10
     - Runs LabVIEW executables.
   * - 
     - Linux
     - Runs bosch simulator
   * - 
     - Linux
     - Runs EUI and operations manager
   * - 
     - Linux
     - Robotframework execution

