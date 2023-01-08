# OCL Lab Instructions

Here are the installation instructions for participants of the OCL Lab.

## Google Colab

We offer participants of the AAAI 2023 Lab [**Optimization with Constraint Learning**](https://aaai.org/Conferences/AAAI-23/aaai23tutorials/) the opportunity to run our notebooks in Google Colab.

To run our notebooks on Google Colab:
1. Follow [this](https://drive.google.com/drive/folders/1J90aP5_3HuZJ1pEJWAjeeX4vrlNXSbbl?usp=share_link) link.
2. Sign into with Google account. You will be directed to your Google Drive.
3. Right-click on the `ocl_lab` folder (see image below). Choose `Download` from the drop-down menu. This will download a zipped copy of `ocl_lab` into your local machine. 
4. Unzip your downloaded copy of `ocl_lab`.
5. Go back to your Google Drive `HOME` folder and right-click on any open UI space. Pick `Folder upload` from the drop-down menu. Navigate to your local unzipped `ocl_lab` folder and upload. Upload may take a while. Go ahead with the rest of the instructions while upload is in progress.
6. You will now have a copy of `ocl_lab` in Google Drive owned by YOU. This will give you full permissions to run our interactive notebooks.
7. Navigate to the `notebooks` sub-folder of YOUR copy of `ocl_lab`. You don't have to wait for upload to finish!
8. The `notebooks` sub-folder includes: `WFP`, `Chemotherapy`, `POI`, and `DOFramework`. Look for the notebooks (the `.ipynb` files) under each. 
9. To run a notebook, right-click on the `.ipynb` file and choose `Open with` from the drop-down menu. Choose `Google Colaboratory` to open it with. If you don't see `Google Colaboratory` in your list of options, click on `Connect more apps` and  install `Google Colaboratory` from the app menu. Now you will see `Google Colaboratory` appear under `Open with`.
10. Once you open a notebook in Google Colab, click on `Runtime` in the top bar and choose `Run all` from the drop-down menu. When prompted, click `Allow` to mount your Drive.

<div>
<img src="https://raw.githubusercontent.com/ordavidov/ocl_lab/main/docs/figures/right_click.png" width="400"/>
</div>

NOTE: The Google Colab link will **expire** 30 days after the AAAI 2023 lab is over (March 8, 2023). You can still run our notebooks following the instructions below (under Advanced).

NOTE: If you are getting `Read-only file system` errors while running our notebooks, it means you are not using YOUR owned copy of `ocl_lab`.

## Slack

We'll use a Slack workspace during the AAAI 2023 OCL Lab as a space to answer questions, interact with participants, etc.

Follow [this](https://join.slack.com/t/ocl-lab/shared_invite/zt-1m0d7h44w-EB_MmmS7j_5_Hfa1vkGPfA) link to join our OCL Lab Slack workspace. 

This link will **expire** 30 days after the AAAI 2023 OCL Lab is over (March 8, 2023).

## Advanced

If you prefer, you can run our OCL Lab materials on your local system.

### ++ GLPK

Unless you already have a solver installed (e.g., [Gurobi](https://www.gurobi.com/), [CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio/cplex-optimizer)), you will need to install one. 

We will demonstrate code on the open-source solver [GLPK](https://www.gnu.org/software/glpk/).

#### --> Mac

We'll use [Homebrew](https://brew.sh/) to install GLPK. Open your Terminal and run
```
brew install glpk
```
Check your installation with
```
glpsol --help
```
If you don't wish to use Homebrew, follow the instructions [here](http://arnab-deka.com/posts/2010/02/installing-glpk-on-a-mac/).

#### --> Windows

To install [GLPK on a Windows machine](h#ttps://sourceforge.net/projects/winglpk/), follow the instructions below.

1. Go to Control Panel to determine whether you have 32-bit or 64-bit Windows (assume 64-bit from now on).
2. Download the latest version of GLPK (4.65 as of writing these instructions) from [this address](https://sourceforge.net/projects/winglpk/).
3. Extract the Zip folder by right clicking on the folder and then >> 7-Zip >> Extract Here as shown.
4. move the glpk-4.65 folder from your downloads folder to your C: drive.
5. Assuming you’re on a 64-bit Windows, click on the `C:\glpk-4.65` folder in Windows explorer, click on the `w64` folder, and select and copy the file path, which should be `C:\glpk-4.65\w64`.
6. Search and open your Control Panel, select System and Security >> System >> Advanced system settings >> Environment Variables. Then click on `path` in the top window, click the `Edit` button, then `New`.
7. Paste the file path you copied above and save.

### ++ Environment

We recommend working in a fresh Python 3.8.0 environment.

#### --> Mac / Linux

Using `pyenv` in combination with `virtualenv`, type the following in your terminal
```
pyenv virtualenv 3.8.0 ocl
pyenv local ocl
```

[Here](https://realpython.com/intro-to-pyenv/#virtual-environments-and-pyenv "pyenv and virtualenv") is a good source on `pyenv` and `virtualenv` by Logan Jones.

To switch back to your default Python environment, use
```
pyenv local .
```

#### --> Windows

Assuming you have [Anaconda](https://www.anaconda.com/) installed, go to the Anaconda Command Prompt and type
```
conda create -n ocl python=3.8.0
conda activate ocl
```

### ++ Installation

Now that you've set up a dedicated Python environment, install `opticl` and `doframework` 
```
pip install --upgrade pip
pip install opticl
pip install doframework
```

### ++ Clone

Clone the `ocl_lab` repo to have your own local copy of the OCL Lab notebooks and data. From the command line, run
```
git clone https://github.com/ordavidov/ocl_lab.git
cd ocl_lab
```

### ++ DOFramework Setup

`doframework` relies on [`rayvens`](https://github.com/project-codeflare/rayvens) for event streaming, which, in turn, relies on [`camel`](https://github.com/apache/camel-k/releases?page=3). Therefore, we need to get `camel` and make sure we have Java and [`maven`](https://maven.apache.org/) on our system. 

#### --> Mac

First, use [Homebrew](https://brew.sh/) to install `camel` and `maven`.

```
brew install kamel
brew install maven
```

Now, you ALSO need to have [Java](https://www.oracle.com/java/technologies/downloads/) installed. If you don't, follow the instructions [here](https://docs.oracle.com/en/java/javase/19/install/overview-jdk-installation.html#GUID-8677A77F-231A-40F7-98B9-1FD0B48C346A).

Check your installations with
```
java -version
mvn -version
kamel version
```

#### --> Windows

...

#### --> Linux

Download the `camel-k` client and un-tar.
```
wget https://github.com/apache/camel-k/releases/download/v1.5.1/camel-k-client-1.5.1-linux-64bit.tar.gz
tar zxvf camel-k-client-1.5.1-linux-64bit.tar.gz
```
Copy the binary
```
cp ./kamel /usr/local/bin
```

Make sure you have [Java](https://www.oracle.com/java/technologies/downloads/) and [`maven`](https://maven.apache.org/)
```
apt update
apt-get install -y openjdk-11-jdk-headless -qq
apt-get install -y maven
```

Set up the Java environment variable (via Python)
```
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
```

Check your installations with
```
java -version
mvn -version
kamel version
```

### ++ Notebooks

To launch the OCL Lab jupyter notebooks, you'll need to first add `jupyter` to our new Python environment
```
pip install jupyter
```
Then
```
cd notebooks
jupyter notebook
```
You're now ready to run our notebooks. Enjoy!

## Issues

Please report OptiCL issues [here](https://github.com/hwiberg/OptiCL/issues) and DOFramework issues [here](https://github.com/IBM/doframework). We greatly appreciate your help!
