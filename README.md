# Bodhi Alarcón - Truss Software Engineering Interview Submission

## Overview

Hello! Thanks for taking the time to review my submission for the Truss Software Engineering Interview.  

This submission was built on a machine running macOS 10.15.2 running Python 3.7. Please run using the same configuration.

## Running the submission

First clone this repo locally. Next, use pip to install the necessary packages as listed in `requirements.txt`. 

Run the following on the command line:  

    python3 normalizer.py < sample.csv > output.csv

 `output.csv` will contain the normalized csv file, leaving `sample.csv` unmodified.

## Running the tests

This submission was developed using principles of test-driven development. If you'd like to run the tests, make sure you have [PyTest](https://docs.pytest.org/en/latest/) installed.  

Once you have PyTest installed, simply run   

    pytest
    
in the `normalizer` directory on your command line to start the test session. 