## Setting up project development

1. Clone this repository
2. Download the dependencies
3. Start the server

### Dependencies

+ Backend: Python 3.6
+ Database: Postgres

#### Python

1. Set up virtual environment
    1.1. download [Homebrew](https://brew.sh/)
    1.2. download [pyenv](https://github.com/pyenv/pyenv) with homebrew
    1.3. download [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) with homebrew
    1.4. setup and activate the virtual environment
    

2. Downloading dependencies
    2.1. download requirements in requirements.txt with the script. 
    `pip install -r requirements.txt`

#### Postgres

1) Simply set it up and create a database for this project
2) Open file `[PROJECT_DIRECTORY]/src/api/config.py` in your editor
3) Under the class `DevelopmentConfig`, modify `SQLALCHEMY_DATABASE_URI` to match your database URI
4) cd to `[PROJECT_DIRECTORY]`
5) execute `python -m src.dbManage db migrate` to **generate the code** to create the database
6) execute `python -m src.dbManage db upgrade` to create the database

### Running the program

1) make sure you are using the correct virtual environment
2) cd to `[PROJECT_DIRECTORY]`
3) execute `python -m src.api.app`

### Running tests

+ Test Driver: python unittest

*I have yet figure out how to run from command line, but if you're using visual studio code it should be fairly easy*