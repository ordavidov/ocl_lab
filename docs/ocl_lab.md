<!--
# Copyright IBM Corporation 2022
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
-->

# OCL Lab Instructions

Here are the installation instructions for participants of the AAAI 2023 OCL Lab.

They apply more generally

## GLPK Installation

Unless you already have one of the OptiCL supported solvers (e.g., [Gurobi](https://www.gurobi.com/), [CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio/cplex-optimizer)), you will need to install one. We will demonstrate code on the open source solver [GLPK](https://www.gnu.org/software/glpk/).

### Windows 

To install [GLPK on a Windows machine](https://sourceforge.net/projects/winglpk/), follow the instructions below.

1. Go to Control Panel to determine whether you have 32-bit or 64-bit Windows (assume 64-bit from now on).
2. Download the latest version of GLPK (4.65 as of writing these instructions) from [this address](https://sourceforge.net/projects/winglpk/).
3. Extract the Zip folder by right clicking on the folder and then >> 7-Zip >> Extract Here as shown.
4. move the glpk-4.65 folder from your downloads folder to your C: drive.
5. Assuming you’re on a 64-bit Windows, click on the `C:\glpk-4.65` folder in Windows explorer, click on the `w64` folder, and select and copy the file path, which should be `C:\glpk-4.65\w64`.
6. Search and open your Control Panel, select System and Security >> System >> Advanced system settings >> Environment Variables. Then click on `path` in the top window, click the `Edit` button, then `New`.
7. Paste the file path you copied above and save.

### Mac

To install GLPK on a Mac, follow the instructions below.

If you're using [Homebrew](https://brew.sh/), open your Terminal and run
```
brew install glpk
```
Check your installation with
```
glpsol --help
```
If you're not using Homebrew ... maybe it's about time. Otherwise, follow the instructions [here](http://arnab-deka.com/posts/2010/02/installing-glpk-on-a-mac/).

## Google Colab

We offer participants of the [AAAI 2023 Lab **LSHP1: Optimization with Constraint Learning**](https://aaai.org/Conferences/AAAI-23/aaai23tutorials/) the opportunity to run our notebooks in Google Colab.

Follow this[!!!] link. Once you log into Google Drive, right click on our `ocl_lab` folder, then click `Add shortcut to Drive`. This will allow you to access the folder from your drive. More critically, it will allow notebooks to interact with data.

Note that it will be expire 30 days after the lab is over (March 8, 2023).

## Slack

we'll use a dedicated Slack workspace during our AAAI 2023 Lab LSHP1: Optimization with Constraint Learning. 

Follow this[!!!] link to join our OCL Lab Slack workspace. This link will be good for up to 90 days following the AAAI 2023 OCL Lab.

## Optional

You can also run our notebooks the good-old-fashioned way. We recommend starting from a fresh Python 3.8.0 environment.

`pyenv` + `virtualenv` (Mac + Linux users)

If you're using `pyenv` in combination with `virtualenv` as your Python environment manager, you can type the following in your terminal
```
pyenv virtualenv 3.8.0 dof
pyenv local dof
```
[Here](https://realpython.com/intro-to-pyenv/#virtual-environments-and-pyenv "pyenv and virtualenv") is a good source on `pyenv` and `virtualenv` by Logan Jones.

`conda` (All users)

Install Anaconda

Go to Anaconda command prompt

```
conda create -n ocl python=3.8.0
conda activate ocl
```

We'll be cloning from GitHub so make sure you have the git CLI installed ...


## `doframework` Installation

This is redundant if using Goole Colab

Now that you've set up a dedicated Python environment, install
```
pip install doframework
```
Run a simple sanity check with
```
python
>>> import doframework
>>> exit()
```
The import command may take a while. Once it's finished (successfully, hopefully) you can exit.

## `opticl` Installation

This is redundant if using Goole Colab

```
pip install opticl
```
## Clonning

This is redundant if using Goole Colab.

We will be running `doframework` Jupyter Notebooks as well as using other `doframework` material. Therefore, we'll clone a local copy of `doframework`. From your terminal, run

```
git clone https://github.com/ordavidov/ocl_lab.git
```
To launch the OCL lab Jupyter Notebooks, we'll need to add `jupyter` to our new Python environment
```
pip install jupyter
```
Note that `jupyter` does not come with `doframework`. We want to keep `doframework` light for cloud distribution. Once we're done installing `jupyter`, let's launch the OCL Lab notebooks
```
cd notebooks
jupyter notebook
```
Now we can begin ...

## Issues

Report issues in the repos issues sections

