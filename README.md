# Example Python script using py4spice package
A linear power supply circuit simulated with Ngspice, utilizing the py4spice package. The example circuit is from *Switch-Mode Power Supplies: Spice Simulations and Practical Design, 2nd Edition* by Christophe P. Basso. It uses example 1.4.4, theoretical linear regulator. The python script sets up and launches Ngspice simulations, converts the results to numpy arrays, performs post-simulation calculations, and creates matplotlib plots.

## Cloning the Repository
This respository can be cloned and run on a local computer. Ngspice and the py4spice package must be installed.

## Running with Codespace
This example is set up to use GitHub Codespaces,enabling you to run the example remotely on GitHub. Simply select *Codespace* instead of *clone*. A ready-to-use VS Code IDE will be created, ready to run the script and Ngspice simulation. Basic knowledge of VS Code and Linux is required.

## Local Installation

### Install Ngspice
Ngspice must be [installed](https://ngspice.sourceforge.io/download.html). For most Linux distributions, Ngspice can be installed with a package manager. As an example, for Debian use the following commands:

```bash
sudo apt update
sudo apt install ngspice
ngspice -v
```
For Microsoft Windows and macOS see the [Ngspice](https://ngspice.sourceforge.io/download.html) repo for instructions.

### Install py4spice
py4spice is installed in the customary way for a PyPI package.
```bash
pip install py4spice
```
