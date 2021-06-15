# About the repository

The `reg.py` file contains an algorithm that reads `.png` images from a directory, process it and store the results in output folder.

```
python reg.py input_data output_data
```
Runs the algorithm submitted by participant (reg.py) on `*.png` images stored in input_data. It creates './Reg' folder and expects submitted algorithm to output .txt files inside (H1.txt, H2.txt, ...)

$bash check_reg.sh: runs submitted code (reg.py) on toy dataset (./data/anon004_sample/) and then checks if output files are in the correct format

## To run it directly on Mac/Linux

```
python3 -m virtualenv env1
source env1/bin/activate
git clone https://github.com/UCL/FetReg-2021.git
cd FetReg-2021/
pip install -rrequirements.txt
python input_data output_data
```
