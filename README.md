# Dictionary Application

## Purpose

This is an application that uses the dictionary api to look up a word the user inputs and returns definition. Simple and straight to the point.


## Installing

##### If using Ubuntu,

1. Create a new directory and cd into it
2. Clone git repo
3. If not running python 3.8, run the following bash commands
    1. `sudo apt update`
    2. `sudo apt install python3.8`
4. Create a virtual enviornment
    1. `sudo apt-get install python3-pip`
    2. `sudo apt-get install python3-venv`
    3. `python3 -m venv venv`
    4. `source venv/bin/activate`
5. Install the modules in requirements.txt
    1. `cd Dictionary-app`
    2. `pip install -r requirements.txt`
6. Run the Program
    1. `python main.py`


## Features

The application comes with a Json file that will keep all the definitions that you look up. This cache will reduce time if you want to look up again a word you already have, avoiding doing another API call.

This will also benefit if you want to look up a word you already have and no longer have an internet connection.


## Enjoy!