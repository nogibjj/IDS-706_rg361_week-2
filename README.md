# Pandas Descriptive Statistics Script [![CI](https://github.com/nogibjj/IDS-706_rg361_week-2/actions/workflows/github_actions.yml/badge.svg)](https://github.com/nogibjj/IDS-706_rg361_week-2/actions/workflows/github_actions.yml)

This repo contains the project file which returns the following for the **selected column** from the dataset:
   1. returns the descriptive statistics (mean, median and standard deviation) as a list
   2. prints these results to ``summary.md`` file
   3. generates a histogram of the selcted column and saves it as ``output.png`` file

The code reads the data from the csv and stores it as a [pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) for the analysis.

This repo has been created using the base [Data Engineering Python Template](https://github.com/revanth7667/Duke_IDS_706-DE) created as week-1 mini-project.

Date Created: 2023-09-08

## Instructions

Create a Codespace on main which will initialize the enviroment with the required packages and settings to execute the code.

The ``descriptive_stats`` function in ``main.py`` returns a list which contains the the [mean, median, standard deviation] of the selected column in the data. 

The code also writes these results to a ``summary.md`` file in the ``resources`` folder for future reference

The code stores the histogram as an image in the ``resources`` folder as ``output.png``

Note: The code saves the summary.md and output.png in the resources folder by default, please change this file path within main.py in case required

The function takes in the following 2 parameters:
   - fname (**required**) -  path or link to the csv file with the desired data
   - col (**optional**) - column number for which the statistics needs to be analyzed. if no input is given, the last column in the data is considered for analysis

   **Notes** 
   - Count the column numbers starting at 1
   - The code assumes that the data has a header row, which is the default behaviour of the ``read_csv`` function from pandas which is used to read the data and create a Dataframe 

   
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
   ![Success Build](https://github.com/nogibjj/IDS-706_rg361_week-2/blob/b3ef720f0fd41803c4306ef34420e419f4d58d99/resources/success_build_week2.png)
   
### 4. Makefile
   contains the instructions for the processes used in github actions and .devcontainer for creating the virtual environment
### 5. .devcontainer
   contains the ``dockerfile`` and ``devcontainer.json`` files which are used to build and define the setting of the virtual environment (codespaces - python) for running the code.
### 6. Python files
   - ``main.py`` : contains the ``descriptive_stats`` function which returns the descriptive statistics and wirtes the summary.md and output.png files
   - ``test_main`` : a test file to verify the main.py file which contains a sample DataFrame and the expected results when testing with the  descriptive_stats function

## Sample Outputs
   a sample Dataset of [blood-pressure from Github](https://github.com/Opensourcefordatascience/Data-sets/blob/master/blood_pressure.csv) has been loaded into the resources folder and is used for testing the code.

   Two test cases are run to check the proper functioning of the code:
   1. We specify the column number (in this test, column 4 is passed as argument to the function)
   2. We do not specify a column number (in this test, no argument is passed to the funtion)

   The code runs as expected and the graph and summary are saved in the resources folder:
![test execution](https://github.com/nogibjj/IDS-706_rg361_week-2/blob/3eb40d17417e8b343c0133dfb9374cb5891d1918/resources/test%20output_week2.png)
![test_output](https://github.com/nogibjj/IDS-706_rg361_week-2/blob/b42dfb7ef0450dc0a6b1bcb5cb07fb771497ac29/resources/output.png)
![summary output](https://github.com/nogibjj/IDS-706_rg361_week-2/blob/7cc26b046fac3d1dae1cad0a347f0083e2ab97eb/resources/summary_sample.png)

**Note** : Only the last graph and summary are stored since the test file calls the funtion twice and the function clears the previous output before saving a new one
