##############
PXI Deployment
##############

PXI deployment preflight
************************

Perform these checks before deploying any PXI application.

1. Confirm the approved NI Linux RT image, drivers, firmware, LabVIEW version, source revision, and target identity.
#. Back up the target application's current configuration and record the deployed version.
#. Verify that required shared libraries, time synchronization, cron jobs, configuration directories, and log directories are present with the approved ownership.
#. Review every controller, simulator, gateway, and UDP endpoint in the target configuration against the approved ATS record.
#. Stop the target application in a controlled manner before replacing the executable or configuration.

Do not reuse addresses, ports, credentials, or configuration files from a historical or production deployment without validation.

TMA PXI
*******

The TMA PXI runs the ATS control application for the TMA subsystems.

1. Clone the approved revision of the PXI-controller repository and initialize its required submodules.
#. Open ``ATS_Projects/ATS_LSST_MainControllerPXI.lvproj`` and set the LabVIEW conditional-disable symbol ``HIL`` to ``True``.
#. Open ``RT_MCS_Main.vi``, resolve any requested dependencies, then close the VI and save all required files.
#. Clear the LabVIEW build cache, reopen the project, and build the real-time executable from *Build Specifications*.
#. Deploy the built executable to the approved TMA PXI by the approved LabVIEW or secure-copy procedure.
#. Before rebooting, open ``ATS_Projects/ATS_TMA_PXI.lvproj``, connect it to the target, and deploy ``ATS_ECATSlave_NSV.lvlib``.
#. Disconnect the project and reboot the PXI, then confirm the application boot completed from its approved log or status interface.

The ATS TMA PXI uses the deployed network-shared-variable library for simulation mode.
Do not deploy the EtherCAT master configuration to this controller for the ATS.

Configure the approved ATS variants of the EIB, safety-Modbus, and Bosch SIL files before enabling the application.
The EIB configuration must direct encoder UDP traffic to the approved AXES PXI, safety mapping files must use the ATS mappings, and the Bosch SIL configuration must identify the approved secondary-axis simulator endpoint.
After boot, validate encoder data from the EUI and verify the controller can communicate with the required simulator services.

AXES PXI
********

The AXES PXI runs the main-axis control application and its EtherCAT interface.

1. Clone the approved revision of the PXI-controller repository and initialize its required submodules.
#. Open ``ATS_Projects/ATS_MainAxes.lvproj`` and set the conditional-disable symbol ``HIL`` to ``True``.
#. Open ``MAIN_AxesPXI.vi``, resolve dependencies, save required files, clear the LabVIEW build cache, and reopen the project.
#. Verify that the EtherCAT project matches the approved ATS hardware connection order.
#. Build and deploy the real-time target to the approved AXES PXI.
#. Deploy the EtherCAT master from the ATS AXES project; unlike the TMA PXI, the AXES PXI does not use the TMA NSV-library deployment.
#. Install or deploy the approved cRIO-9145 FPGA bitfile and copy the approved ATS main-axis configuration as ``/c/Configuration/MainAxisConfig.ini``.
#. Reboot the target and confirm that the Speedgoat is available before enabling the EtherCAT chain.

Use the EtherCAT *Online Master State* view to confirm that the two Speedgoat modules and the cRIO are Operational.
If a slave is unavailable, confirm the Speedgoat is running and verify the approved physical connection order before changing configuration.
Confirm cRIO FPGA health through its running LED, an increasing cycle counter, and its changing running-clock status.

AUX PXI
*******

The AUX PXI runs auxiliary subsystem control and connects to the cabinet-temperature, oil-supply, and Top End Chiller simulators.

1. Clone the approved revision of the PXI-controller repository and initialize its required submodules.
#. Open ``ATS_Projects/ATS_AuxSystemsController.lvproj`` and ``AuxSystemsMain.vi``, resolve dependencies, save files, clear the LabVIEW build cache, and reopen the project.
#. Build and deploy the real-time target to the approved AUX PXI.
#. Reboot the target and verify normal application startup and logging.

No separate ATS library deployment is required for the AUX PXI.
For CPU-temperature monitoring, validate that the AUX PXI service account can use its approved SSH credentials to reach the TMA and AXES PXIs, and confirm the configured temperature-sensor path exists on the target.

Copy the approved cabinet-temperature controller mappings into ``/c/Configuration``, remove the ``_forATS`` suffix only when creating the runtime mapping names, and verify their addresses and ports point to the approved cabinet-temperature simulator.
Set the Top End Chiller and Oil Supply System server configuration to the approved simulator endpoints, then validate each Modbus connection from the AUX PXI.
If the installed AUX hardware is a Beckhoff device, perform the approved device-to-PXI configuration before deploying the application.

PXI post-deployment validation
*******************************

1. Verify the deployed executable version, configuration ownership, and application logs on each PXI.
#. Confirm each controller reaches only the approved ATS simulator, gateway, and safety endpoints.
#. Perform one safe, component-specific health check for each PXI before enabling broader functional testing.
#. Run the relevant automated smoke test and retain its result with the deployment record.

