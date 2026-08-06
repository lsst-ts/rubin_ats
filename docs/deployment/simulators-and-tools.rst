Simulator and supporting tool deployment
########################################

The following procedures describe the ATS simulator and tool deployment pattern.
They are validation-gated: before building or replacing an application, confirm the approved repository revision, target host, network endpoint, port, configuration file, and credentials for the active ATS environment.
Do not reuse an address, port, or configuration file from a historic deployment without that validation.

Preflight
*********

1. Record the component version and obtain the approved source revision or released build artifact.
#. Confirm that the target Windows or Linux host is the approved ATS host.
#. Back up the deployed configuration and record the running application version.
#. Verify the controller-side configuration points to the intended simulator endpoint.
#. Stop the existing service in a controlled manner before replacing its files.

Startup order
*************

Use the `ATS_StartSimulatorsAndTools.cmd <https://github.com/lsst-ts/ts_tma_hil_simulators-start-stop-scripts/blob/master/ATS_StartSimulatorsAndTools.cmd>`_ script as the source of truth for the Windows startup order.
Start the network-shared-variable and TekNSV readers first, wait for them to become ready, then start the subsystem simulators.
Start the Speedgoat manager, Top End Chiller, and WriteTekNSVVariables only after their dependencies are available.

Windows LabVIEW executables
***************************

For the LabVIEW applications below, use an approved installer or executable release when one is available.
Otherwise, clone the approved revision, open the named LabVIEW project, build the named executable or installer from *Build Specifications*, and copy the complete build output to the target Windows host.
Do not deploy only the executable because the build directory can contain required supporting files.
After deployment, start the application and confirm that its controller-facing interface is available before proceeding to the next component.

Read/Write Network Shared Variables tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Build the ``ReadVariables.lvproj`` project and its ``Executable`` specification, then deploy the complete build output.
In the deployed ``data`` directory, set ``TCP_configuration_file`` in ``WriteReadVarConfig.xml`` to the local ``TCP_ServerConfig.xml`` path.
Configure and validate separate instances for the TMA PXI, AXES PXI, and local Windows-host variables before starting ``ReadWriteNSVs.exe``.

Bosch power supply simulator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Build the ``BoschPowerSupplySimulator.lvproj`` ``Executable`` specification and deploy its complete output.
Start ``BoschPowerSupplySimulator.exe`` and verify that the TMA PXI receives the expected simulated power-supply status.

Motor thermal model simulator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Build the ``motorThermalModelSimulator.lvproj`` ``Executable`` specification and deploy its complete output.
Start ``motorThermalModelSimulator.exe`` and verify the configured motor-temperature inputs and valve-control interface.

Phase power supply simulator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Build the ``PhasePowerSupplySimulator.lvproj`` ``Executable`` specification and deploy its complete output.
Start ``PhasePowerSupplySimulator.exe`` and verify the TMA PXI receives the expected analog power-supply status.

Limits simulator
^^^^^^^^^^^^^^^^

Build the ``SimulateLimits.lvproj`` ``SimulateLimits`` specification and deploy its complete output.
Before starting ``SimulateLimits.exe``, validate the limit-variable addresses in ``data/GeneralConfiguration.xml`` against the current ATS configuration.

Cabinet temperature controller simulator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Build the ``cabinetTemperatureControllerSimulator.lvproj`` ``Executable`` specification and deploy its complete output.
Start ``cabinetTemperatureControllerSimulator.exe`` only after confirming the AUX PXI Modbus mapping files reference the correct host and ports.
Verify each required cabinet controller can be reset and reports the expected simulated state.

Deployable-platform extension simulator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Build the ``DPextensionsSimulator.lvproj`` ``Executable`` specification and deploy its complete output.
Start ``extensionSimulatorForDP.exe`` and verify that the Pilz safety interface receives the expected extension states.

Oil supply system simulator
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Build the ``OilSupplySystemSimulator.lvproj`` ``Executable`` specification and deploy its complete output.
Start ``OilSupplySystemSimulator.exe`` after confirming its Modbus server address and port agree with the AUX PXI OSS configuration.

WriteTekNSVVariables tool
^^^^^^^^^^^^^^^^^^^^^^^^^

Build the ``Write TekNSV Variables.lvproj`` ``Executable`` specification and deploy its complete output.
Start ``WriteTekNsvVariables.exe`` only after reviewing its configuration because it can set simulator defaults and manually supplied values for deployable extensions, brake pressure, and other TekNSV variables.

Externally built simulators and services
****************************************

Build and deploy these components using the current instructions in their owning repositories.

Top End Chiller simulator
^^^^^^^^^^^^^^^^^^^^^^^^^

Build and package the Top End Chiller simulator using the current instructions in its owning repository.
Before starting it, confirm the deployed server address and port match the ATS AUX PXI TEC configuration.
Verify the AUX PXI can establish the expected Modbus connection after startup.

Secondary-axis SIL
^^^^^^^^^^^^^^^^^^

Build and install ``secondaryAxisSil`` using the current instructions in its owning repository on the approved Linux host.
Confirm that its Modbus server configuration targets the TMA PXI and validate status communication for each simulated secondary axis.

Speedgoat Manager and main-axis models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the MATLAB R2025b ``speedgoatManager.mlapp`` application in ``ts_tma_hil_main-axes_lsst-hil`` to manage the approved main-axis model.
Verify that the manager can connect to the Speedgoat before Robot Framework tests are enabled.
Do not deploy the deprecated standalone Speedgoat Manager source or binary releases.

Robot Framework
^^^^^^^^^^^^^^^

Install the ATS automated-test environment on the approved Linux host using the current instructions in the automated-test repository.
Confirm that its configuration targets the ATS database, controllers, and simulator endpoints rather than production services before running a smoke test.

Windows start and stop scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configure the Windows start/stop scripts with the deployed application paths.
Test controlled startup and shutdown of one non-safety simulator first, then verify that the full sequence follows the documented startup order.

Deprecated component
********************

Force EtherCAT is deprecated and is intentionally not part of the ATS deployment runbook.
Do not introduce it into a new or rebuilt ATS environment.

Post-deployment validation
**************************

1. Confirm every required simulator or tool is running from the approved location and version.
#. Verify its configured network connection from the corresponding PXI or client application.
#. Exercise one safe, component-specific health check and review the application log for connection or configuration errors.
#. Run the relevant automated smoke test before enabling broader functional testing.
