[![Build Status](https://travis-ci.com/HopeNUS/examtt-backend.svg?branch=master)](https://travis-ci.com/HopeNUS/examtt-backend)

## Setting up project development

1. Clone this repository
2. Download the dependencies
3. Start the server

### Dependencies

+ Backend: Python 3.6
+ Database: [Postgres](https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3)

### Python

1. Set up virtual environment

    1.1. download [Homebrew](https://brew.sh/)
  
    1.2. download [pyenv](https://github.com/pyenv/pyenv) with homebrew
  
    1.3. download [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) with homebrew
  
    1.4. setup and activate the virtual environment
    
2. Downloading dependencies
    
    2.1. download requirements in requirements.txt with the script. `pip install -r requirements.txt`
    
    2.2. download Postgres with homebrew following [this](https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3) link

### Postgres

1) Download and Install Postgres
2) Set up database named `examtt`
3) Create a superuser named `postgres` with no password
4) cd to `[PROJECT_DIRECTORY]`
5) execute `python -m src.dbManage db migrate` to **generate the code** to create the database
6) execute `python -m src.dbManage db upgrade` to create the database

## Starting the server

1) cd to `[PROJECT_DIRECTORY]`
2) execute `python -m src.api.app`

## Running tests

1) Set up testing database named `test_examtt`
2) Run `python -m tests.setup_test_db` to setup test database
3) Run `python -m tests.runner` to execute tests
4) Navigate to `[PROJECT_DIRECTORY]/reports` for the test reports
