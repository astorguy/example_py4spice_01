import tomllib
from pathlib import Path

import py4spice as spi

CONFIG_FILENAME = Path("/workspaces/example_py4spice_01/circuits/config.toml")
PROJECT_SECTION = "SEC_1_04_04"


class Ky:
    """Keys for dictionaries.  Defined here at top level so they can be
    referenced instead of using strings for keys. (helps with autocomplete)
    """

    # Keys for decoding config file
    GLOBAL = "GLOBAL"
    NGSPICE_EXE_STR = "NGSPICE_EXE_STR"
    NETLISTS_DIR_STR = "NETLISTS_DIR_STR"
    RESULTS_DIR_STR = "RESULTS_DIR_STR"
    SIM_TRANSCRIPT_STR = "SIM_TRANSCRIPT_STR"
    PROJ_PATH_STR = "PROJ_PATH_STR"

    # Keys for the paths_dict
    NGSPICE_EXE = "ngspice_exe"
    PROJ_PATH = "proj_path"
    NETLISTS_PATH = "netlists_path"
    RESULTS_PATH = "results_path"
    SIM_TRANSCRIPT_FILENAME = "sim_transcript_filename"

    # # Keys for the netlists_dict
    BLANKLINE = "blankline"
    TITLE = "title"
    END_LINE = "end_line"
    LOAD1 = "load1"
    LOAD2 = "load2"
    LOAD3 = "load3"
    LOAD4 = "load4"
    LOAD5 = "load5"
    LOAD6 = "load6"
    LOAD7 = "load7"
    STIMULUS1 = "stimulus1"
    STIMULUS2 = "stimulus2"
    STIMULUS3 = "stimulus3"
    STIMULUS4 = "stimulus4"
    STIMULUS5 = "stimulus5"
    STIMULUS6 = "stimulus6"
    STIMULUS7 = "stimulus7"
    SUPPLIES = "supplies"
    MODELS = "models"
    DUT = "dut"
    RC = "rc"
    # RF = "rf"
    # CF = "cf"
    # RF_470K = "rf_470k"
    COUT = "cout"
    # CONTROL1 = "control1"
    # CONTROL2 = "control2"
    # CONTROL3 = "control3"
    # CONTROL4 = "control4"
    # CONTROL5 = "control5"
    # CONTROL6 = "control6"
    # CONTROL7 = "control7"
    # TOP1 = "top1"
    # TOP2 = "top2"
    # TOP3 = "top3"
    # TOP4 = "top4"
    # TOP5 = "top5"
    # TOP6 = "top6"
    # TOP7 = "top7"

    # Keys for the vectors_dict
    VEC_ALL = "vec_all"
    VEC_IN_OUT = "vec_in_out"
    VEC_OUT = "vec_out"
    VEC_AC_OUT_GAIN = "vec_ac_out_gain"


def initialize() -> tuple[
    dict[str, Path], dict[str, spi.Netlist], dict[str, spi.Vectors]
]:
    """All the setup we can do before running the different parts of the project"""
    # read config file and create config dictionary
    with open(CONFIG_FILENAME, "rb") as config_file:
        my_config = tomllib.load(config_file)

    proj_path = Path(my_config[PROJECT_SECTION][Ky.PROJ_PATH_STR])

    # Create paths based on the config dictionary
    ngspice_exe: Path = Path(my_config[Ky.GLOBAL][Ky.NGSPICE_EXE_STR])
    netlists_path: Path = proj_path / my_config[Ky.GLOBAL][Ky.NETLISTS_DIR_STR]
    results_path: Path = proj_path / my_config[Ky.GLOBAL][Ky.RESULTS_DIR_STR]

    # create results directory if it does not exist
    results_path.mkdir(parents=True, exist_ok=True)

    # create simulation transcript file. If it exists, make sure it is empty
    sim_tran_filename: Path = results_path / my_config[Ky.GLOBAL][Ky.SIM_TRANSCRIPT_STR]
    if sim_tran_filename.exists():  # delete and recreate. this makes sure it's empty
        sim_tran_filename.unlink()
    sim_tran_filename.touch()

    # create paths dictionary
    paths_dict = {
        Ky.NGSPICE_EXE: ngspice_exe,
        Ky.PROJ_PATH: proj_path,
        Ky.NETLISTS_PATH: netlists_path,
        Ky.RESULTS_PATH: results_path,
        Ky.SIM_TRANSCRIPT_FILENAME: sim_tran_filename,
    }

    nets_path: Path = paths_dict[Ky.NETLISTS_PATH]  # make shorter alias
    netlists_dict: dict[str, spi.Netlist] = {}  # create empty netlist dictionary

    netlists_dict[Ky.BLANKLINE] = spi.Netlist("")  # blank line for spacing
    netlists_dict[Ky.TITLE] = spi.Netlist("* linear regulator section 1.4.4")
    netlists_dict[Ky.END_LINE] = spi.Netlist(".end")

    # create netlist objects from files and add to netlist dictionary
    netlists_dict[Ky.DUT] = spi.Netlist(nets_path / "dut.cir")
    netlists_dict[Ky.LOAD1] = spi.Netlist(nets_path / "load_resistive.cir")
    netlists_dict[Ky.LOAD2] = spi.Netlist(nets_path / "load_resistive.cir")
    netlists_dict[Ky.LOAD3] = spi.Netlist(nets_path / "load_current_pulse.cir")
    netlists_dict[Ky.LOAD4] = spi.Netlist(nets_path / "load_current_ac.cir")
    netlists_dict[Ky.LOAD5] = spi.Netlist(nets_path / "load_current_ac.cir")
    netlists_dict[Ky.LOAD6] = spi.Netlist(nets_path / "load_current_pulse2.cir")
    netlists_dict[Ky.LOAD7] = spi.Netlist(nets_path / "load_current_pulse2.cir")
    # netlists_dict[Ky.STIMULUS1] = spi.Netlist(nets_path / "stimulus_15v_dc.cir")
    # netlists_dict[Ky.STIMULUS2] = spi.Netlist(nets_path / "stimulus_15v_ramp.cir")
    # netlists_dict[Ky.STIMULUS3] = spi.Netlist(nets_path / "stimulus_15v_dc.cir")
    # netlists_dict[Ky.STIMULUS4] = spi.Netlist(nets_path / "stimulus_15v_dc.cir")
    # netlists_dict[Ky.STIMULUS5] = spi.Netlist(nets_path / "stimulus_15v_dc.cir")
    # netlists_dict[Ky.STIMULUS6] = spi.Netlist(nets_path / "stimulus_15v_dc.cir")
    # netlists_dict[Ky.STIMULUS7] = spi.Netlist(nets_path / "stimulus_15v_dc.cir")
    # netlists_dict[Ky.SUPPLIES] = spi.Netlist(nets_path / "supplies.cir")
    # netlists_dict[Ky.MODELS] = spi.Netlist(nets_path / "models.cir")
    # netlists_dict[Ky.RC] = spi.Netlist(nets_path / "rc_compensation.cir")
    # netlists_dict[Ky.COUT] = spi.Netlist(nets_path / "filter_cap.cir")

    # Define a vector dictionary for simulation and post-simulation analysis
    vectors_dict = {
        Ky.VEC_ALL: spi.Vectors("all"),
        Ky.VEC_IN_OUT: spi.Vectors("in out"),
        Ky.VEC_OUT: spi.Vectors("out"),
        Ky.VEC_AC_OUT_GAIN: spi.Vectors("out-mag"),
    }
    return paths_dict, netlists_dict, vectors_dict


def main() -> None:
    # initialize paths, netlists, and vectors dictionaries
    paths_dict, netlists_dict, vectors_dict = initialize()


if __name__ == "__main__":
    main()
