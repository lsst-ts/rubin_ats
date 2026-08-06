############
ATS Software
############

The ATS software ecosystem is primarily implemented in LabVIEW and C++, with Python-based services such as the Top End Chiller simulator.
It includes TMA control and HMI applications, real-time simulation models, subsystem simulators, communications tools, safety software, and Robot Framework automated tests.

Architecture
############

The software is organized around the controller interfaces rather than as one monolithic simulator.
Main-axis behavior is simulated on the Speedgoat because it needs real-time execution, while the secondary-axis and subsystem simulations run on supporting hosts.
The simulator layer represents power supplies, thermal systems, limits, encoders, oil systems, deployable extensions, and other TMA interfaces.

Communications tools provide controlled access to network shared variables and fieldbus-facing values for the simulators and operators.
Some historic tools, including Force EtherCAT and the original network-shared-variable simulator, are deprecated and must not be selected for new deployments.
The Pilz safety implementation remains a separate safety concern from the normal simulator and controller software.

Testing and operations software uses the same interfaces as the simulated system where practical.
Robot Framework exercises automated scenarios, while the operator interfaces and management services support setup and supervised operation.

Component overviews
###################

Browse the ATS components by operational role and dependency.

.. toctree::
   :maxdepth: 1
   :titlesonly:

   components/index

Repository inventory
####################

The following repositories are the operational ATS inventory identified in the Tekniker design and deployment documentation.
Status describes the component's ATS role, not its current GitHub availability.

.. list-table:: Controller and operations software
   :header-rows: 1

   * - Component
     - Repository
     - Purpose
     - Status
   * - :doc:`PXI controller <components/pxi-controller>`
     - ``ts_tma_labview_pxi-controller``
     - Builds and configures the TMA, AXES, and AUX real-time controllers.
     - Active
   * - :doc:`Human-machine interfaces <components/hmi>`
     - ``ts_tma_labview_hmi-computers``
     - Provides the maintained EUI used with the ATS; the handheld HMI is deprecated.
     - Supporting
   * - :doc:`Mount Operation Manager <components/operation-manager>`
     - ``ts_tma_operation-manager_mt-mount-operation-manager``
     - Coordinates mount operations services used with the EUI.
     - Supporting

.. list-table:: Simulator software
   :header-rows: 1

   * - Component
     - Repository
     - Purpose
     - Status
   * - :doc:`Main axes <components/main-axes>`
     - ``ts_tma_hil_main-axes_lsst-hil``
     - Runs the Speedgoat main-axis, drive, and encoder models.
     - Active
   * - :doc:`Secondary axes <components/secondary-axes>`
     - ``ts_tma_hil_secondary-axis_secondaryaxissil``
     - Runs one configured auxiliary-axis simulator per Bosch axis.
     - Active
   * - :doc:`Limits <components/limits>`
     - ``ts_tma_hil_simulate-limits``
     - Simulates limit switches from position and controller variables.
     - Active
   * - :doc:`Motor thermal model <components/motor-thermal>`
     - ``ts_tma_hil_motor-thermal-model_motor-thermal-model-simulator``
     - Simulates phase-drive and cabinet thermal behavior.
     - Active
   * - :doc:`Cabinet temperature controllers <components/cabinet-temperature>`
     - ``ts_tma_hil_cabinet-temperature-controller_cabinets``
     - Provides Modbus cabinet-temperature controllers to the AUX PXI.
     - Active
   * - :doc:`Oil Supply System <components/oil-supply-system>`
     - ``ts_tma_hil_oil-supply-system_oil-supply-system-simulator``
     - Provides the OSS Modbus interface and simulated faults.
     - Active
   * - :doc:`Phase power supply <components/phase-power-supply>`
     - ``ts_tma_hil_phase-power-supply_phase-power-supply-simulator``
     - Simulates phase-power-supply states and faults.
     - Active
   * - :doc:`Bosch power supply <components/bosch-power-supply>`
     - ``ts_tma_hil_bosch-power-supply_bosch-power-supply-simulator``
     - Simulates Bosch power-supply status inputs.
     - Active
   * - :doc:`Deployable-platform extensions <components/deployable-extensions>`
     - ``ts_tma_hil_deployable-platform-extensions-simulator``
     - Simulates extension-lock inputs for the safety system.
     - Active
   * - :doc:`Top End Chiller <components/top-end-chiller>`
     - ``ts_tma_hil_simulator_top-end-chiller``
     - Provides the Python-based chiller Modbus service for the AUX PXI.
     - Active
   * - :doc:`Safety system <components/safety-system>`
     - ``ts_tma_hil_test-dual-modbus``
     - Implements the Pilz-based simulated interlock system.
     - Active

.. list-table:: Simulator tools
   :header-rows: 1

   * - Component
     - Repository
     - Purpose
     - Status
   * - :doc:`ReadVariables <components/read-variables>`
     - ``ts_tma_hil_read-variables``
     - Bridges TMA PXI, AXES PXI, and local network-shared variables.
     - Active
   * - :doc:`WriteTekNSVVariables <components/write-teknsv-variables>`
     - ``ts_tma_hil_write-TekNSV-variables``
     - Sets simulation-facing TekNSV values such as brake and extension states.
     - Active
   * - :doc:`Speedgoat Manager <components/speedgoat-manager>`
     - ``ts_tma_hil_main-axes_lsst-hil`` (``src/speedgoatManager.mlapp``); ``ts_tma_hil_speedgoat-speedgoat-manager-python-interface``
     - Manages the MATLAB R2025b Speedgoat model lifecycle and injected faults.
     - Active
   * - :doc:`Windows orchestration scripts <components/windows-orchestration>`
     - ``ts_tma_hil_simulators-start-stop-scripts``
     - Starts and stops the Windows simulator suite.
     - Supporting

.. list-table:: Testing and recovery
   :header-rows: 1

   * - Component
     - Repository
     - Purpose
     - Status
   * - :doc:`Automated tests <components/automated-tests>`
     - ``ts_tma_test_automatic-test-code``
     - Contains the Robot Framework ATS test suite.
     - Active
   * - :doc:`Test procedures <components/test-procedures>`
     - ``ts_tma_test_testing-procedures``
     - Contains subsystem-oriented manual test procedures.
     - Supporting

Deprecated or historical components
###################################

.. list-table:: Components excluded from new ATS deployments
   :header-rows: 1

   * - Component
     - Repository
     - Reason
   * - Force EtherCAT
     - ``ts_tma_hil_force-ethercat-vars``
     - Deprecated because the ATS uses network-shared variables instead.
   * - Network Shared Variables simulator
     - ``ts_tma_hil_network-shared-variables-simulation``
     - Explicitly marked as no longer in use in the Tekniker software design.
   * - Legacy Speedgoat Manager
     - ``ts_tma_hil_speedgoat-speedgoat-manager``; ``ts_tma_hil_speedgoat-speedgoat-manager-binaries``
     - Deprecated with MATLAB R2025b; use ``speedgoatManager.mlapp`` in the main-axes repository.
   * - ATS database backups
     - ``ts_tma_ats_database-backup``
     - Historical repository that does not provision the current ATS database.
