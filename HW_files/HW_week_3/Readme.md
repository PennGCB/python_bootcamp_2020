This directory contains five question entitled q1.py (or q1.ipynb), q2.py (q2.ipynb)
Each question has multiple parts, and involve implementing functions that process data using pandas.

There are test cases for some components of each question.
These test cases are stored in test.py, and will be run automatically when you run the main code for that question.

As always, if you have any questions, feel free to ask on Piazza or during office hours.
Good luck, and have fun!

To setup your environment perform the following steps (following the example from Piazza):

1. If you have not already, download and install [miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. Copy and paste the HW3 files from github to your local machine
3. Using the terminal and the `cd` command, navigate to the directory where you have copied your HW3 files

Option 1:
4. Set up conda environment by running the following command in the terminal:
```bash
$ conda env create -f environment.yml
$ conda activate hw3_env
```
5. Work in the editor of your choosing

Option 2:
4. Set up conda environment by running the following command in the terminal:
```bash
$ conda env create -f environment.yml
$ conda activate hw3_env
$ jupyter notebook
```
5. Copy and paste the url link that appears in the terminal into your browser
6. Select `hw3_env` as your kernel when prompted. If not prompted, then the kernel can be selected from `Kernel`>`Change kernel` dropdown menu
6. Start editing the `.ipynb` files