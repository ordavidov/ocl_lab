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

Here are the installation instructions for participants of the OCL Lab.

## Requirements

We recommend installing on a designated Python 3.8.0 environment.

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

## GLPK Installation

....

## Google Co-lab

put in the links to google colab.

the link will only be good for a week after the lab.

## Slack

we'll have a slack channel for the OCL Lab which will be good up to 90 days after the lab

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

