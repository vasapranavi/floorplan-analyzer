# floorplan-analyzer

This is a command line tool that reads in flor plan text file and outputs the following information:
- Number of different chair types for the apartment
- Number of different chair types per room
The different types of chairs are as follows:
W: wooden chair
P: plastic chair
S: sofa chair
C: China chair


# Project layout
    .
    ├── floorplan-analyzer        # Application Files 
    │   ├── process               # process files
    │   ├── schemas               # data classes
    │   ├── utils                 # utility functions
    │   ├── main.py               # Launch point of the Application
    ├── requirements              # Requirements for the Development and Production stages 
    ├── tests                     # Unit tests
    │   ├── process               # tests for process
    │   ├── utils                 # tests for utils
    ├── resources                # Resources for development stage
    ├── dockerfile               # For creating the docker image    
    └── README.md
    
# Setup Instructions
To run floorplan-analyzer algorithm you will need to have docker installed.
The development environment can be started by running:

`docker-compose up dev`

enter the filepath of floorplan text file, it outputs the result as per objective

# Unit tests
Code is also covered with unit tests same can be found in tests folder of the project

# Instructions to run with command prompt and Sample output
1. Checkout/clone the repo form github
2. navigate to floor_plan_puzzle directory
3. run `py main.py`
4. enter the file name, in this case the floorplan file is located in resources directory, hence the value given as `../resources/floorplan01.txt`
5. output follows

![image](https://user-images.githubusercontent.com/46113594/164204815-f165c159-137f-470d-9ab6-d3581082ccb2.png)

below is the sample output from the program

![image](https://user-images.githubusercontent.com/46113594/163732487-6f6d0eaa-8cf2-45b2-886c-1cccec5b6f1f.png)


