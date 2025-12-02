# Learn Ngspice with Python
## Why Ngspice?
### Spice is the standard for analog simulation
Since 1972, analog simulation of electrical circuits has been dominated by Spice. Several commercial programs in wide use today have been spawned from original Spice ([HSPICE](https://www.synopsys.com/implementation-and-signoff/ams-simulation/primesim-hspice.html), [Spectre](https://www.cadence.com/en_US/home/tools/custom-ic-analog-rf-design/circuit-simulation/spectre-x-simulator.html), [QSPICE](https://www.qorvo.com/design-hub/design-tools/interactive/qspice)).

[Ngspice](https://ngspice.sourceforge.io/) is the only FOSS (Free and Open-Source Software) version available today. Understanding Ngspice gives you a fundemental understanding of Spice-level circuit simulation. Further, using Ngspice with Python gives you an endless set of tools enabling optimization, statistical analysis, and other advanced tools for thorough analysis of your circuit design.

### Why not QSPICE?
[QSPICE](https://www.qorvo.com/design-hub/design-tools/interactive/qspice) is a free Spice tool that is more intuitive than Ngspice. With a schematic frontend and easy plotting, it offers an excellent way to get familiar with Spice. However, there are some aspects of QSPICE that may lead you to use Ngspice instead.
- QSPICE is not open source. It is owned by Quovo, and therefore subject to changes in pricing, staffing, and availability.
- QSPICE only runs on Microsoft Windows (at the date of this writing)
- It is more difficult to interface QSPICE to third-party tools such as [KiCad](https://www.kicad.org/) schematic capture and Python [NumPy](https://numpy.org/) arrays.

## Ngspice structure

Ngspice is challenging to use directly. The GUI provided is not well-maintained and best avoided. Though Ngspice can be used interactively in a terminal session, it works best as a batch process, or by using the API.

In batch mode, the primary input to Ngspice is a *netlist*. In most cases, the *netlist* contains all the input needed to run the simulation, including:
- Component values and interconnections
- Stimulus
- Analyses to execute
- Output formatting
- Variables

Creating a *netlist* is complicated and error-prone. Schematic capture tools are invaluable, especially for component connectivity.

## Learning Ngspice through examples
As mentioned, there are several ways to access Ngspice. Our ***opinionated*** method is to use Python scripts. To facilitate, we will use the [py4spice](https://github.com/astorguy/py4spice) module. There are multiple examples showing increasing levels of advancing application.

We'll use [Jupyter Notebooks](https://jupyter.org/) as an effective way to present the tutorial examples. [KiCad](https://www.kicad.org/) is the schematic capture used to generate the netlist for the DUT (design under test).

Each example consist of the following subdirectories:
| Subdirectory | Contents |
|--------------|----------|
| `python` | Jupyter Notebooks or python scripts |
| `netlists`| Netlists for input to Ngspice |
| `results` | All the output from Ngspice simulations and post-simulation processes` |
| `schematics` | KiCad Schematics |

Here is a list of the examples. Start with the divider, as that introduces in more detail the underlying structure for all the examples.

| Example | Description |
|--------|-------------|
| `divider` | Simple resistor divider. Introduction to using py4spice and Ngspice. No schematic. |
| `sec_1_04_lin_reg` | Power supply example |

## Running with Codespace
These examples are set up to use GitHub Codespaces, enabling you to run remotely on GitHub. Simply select *Codespace* instead of *clone*. A VS-Code IDE will be created within your browser, ready to run the scripts and Ngspice simulations. Basic knowledge of VS-Code and Linux is required.

## Local Installation

### Install Ngspice
Ngspice must be [installed](https://ngspice.sourceforge.io/download.html). For most Linux distributions, Ngspice can be installed with a package manager. As an example, for Debian-based distros use the following commands:

```bash
sudo apt update
sudo apt install ngspice
```
For Microsoft Windows and macOS see the [Ngspice](https://ngspice.sourceforge.io/download.html) repo for instructions.

### Install py4spice
py4spice is installed in the customary way for a PyPI package.
```bash
pip install py4spice
```






