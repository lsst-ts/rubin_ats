from documenteer.conf.guide import *  # noqa: F401,F403

# These ATS repositories require authenticated GitHub access and return 404 to
# Sphinx's unauthenticated link checker.
linkcheck_ignore = [
    r"^https://github\.com/lsst-ts/ts_tma_hil_test-dual-modbus$",
    r"^https://github\.com/lsst-ts/ts_tma_hil_simulators-start-stop-scripts/blob/master/ATS_StartSimulatorsAndTools\.cmd$",
    r"^https://github\.com/lsst-ts/ts_tma_labview_pxi-controller/blob/develop/ESIFiles/MainAxes/AxesPXI/Configuration/MainAxisConfig_forATS\.ini$",
]
