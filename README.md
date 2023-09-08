# Pandas Descriptive Statistics Script [![CI](https://github.com/nogibjj/IDS-706_rg361_week-2/actions/workflows/github_actions.yml/badge.svg)](https://github.com/nogibjj/IDS-706_rg361_week-2/actions/workflows/github_actions.yml)

This repo contains the project file which returns a descriptive statistic (mean) of the selcted column in a [pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html).

This repo has been created using the base [Data Engineering Python Template](https://github.com/revanth7667/Duke_IDS_706-DE) created as week-1 mini-project 
Date Created: 2023-09-08

## Instructions
The ``descriptive_stats`` function in ``main.py`` returns the mean of the selected column in a DataFrame, it takes in the following 2 parameters:
   - df (**required**) -  a pandas DataFrame object
   - col (**optional**) - column number for which the mean needs to be calculated. if no input is given, the mean of the last column in the DataFrame is returned

## Contents
### 1. README.md
   contains the information about the repository and instructions for using it
### 2. requirements.txt
   contains the list of packages and libraries which are required for running the project. 
   
### 3. github_actions.yml
   github actions is used to automate the following 4 actions whenever a change is made to the files in the repository:
   - ``install`` : installs the packages and libraries mentioned in the requirements.txt
   - ``format`` : uses black to format the python files
   - ``lint`` : uses pylint to lint the python files
   - ``test`` : uses pytest to test the python codes using the test_* files to test the main files
     
   **Note** -if all the processes run successfully the following output will be visible in github actions:
   ![Success Build](https://github.com/revanth7667/Duke_IDS_706-DE/blob/91e617109f29e19f2a4392bc4f638c7c4f682457/resources/successfull_build.png)
   
### 4. Makefile
   contains the instructions for the processes used in github actions and devcontainer
### 5. .devcontainer
   contains the ``dockerfile`` and ``devcontainer.json`` files which are used to build and define the setting of the virtual environment (codespaces - python) for running the code.
### 6. Python files
   This repository is used only as a template, however the following 2 files are present which will be used for testing and as an example:
   - ``example.py`` : this file contains the actual code for the project. For this example, we use a simple function which returns the sum of 2 numbers
   - ``test_example.py`` : this file is used for testing and it contains the test conditions and the expected output from the example.py code for the given cases.
Sample execution of test file:
![test_output](https://github.com/revanth7667/Duke_IDS_706-DE/blob/b9458e52425edd27e36ca013af8c894a553c2ac1/resources/test_output.png)
