## Setup, install dependencies.

Here, pipenv is used instead of pip. Run in command line:

1. Install Python 3.12.0
2. Run in command line: `pip install pipenv`
3. Run in command line: `pipenv install` (if the virtualenv is already activated, you can also use `pipenv sync`).
   Consider `pipenv install --dev` and `pipenv sync --dev` in case of dev dependencies.
4. to update `pip install --upgrade pip`
5. run `pipenv shell` to activate virtual environment

in case ' No module named 'pip' run `python -m ensurepip`

Why pipenv?

Putting the dependencies into a requirements.txt and then using pip will work but is not really necessary. The whole
point of using pipenv
for most people is to avoid the need to manage a requirements.txt or to use pip.
Note: to add new library run `pipenv install lib_name`

To configure the Python interpreter in PyCharm, follow these steps:

1. Go to PyCharm -> Preferences (on macOS) or File -> Settings (on Windows/Linux).
2. In the Settings/Preferences dialog, navigate to Project: <your_project_name> -> Python Interpreter.
3. Click on the dropdown menu. If the interpreter you want to use is listed, select it. If not, click on Show All....
4. In the Project Interpreters dialog, click on the + button to add a new interpreter.
5. In the Add Python Interpreter dialog, you can choose to add a new interpreter using a virtual environment, Conda
   environment, system interpreter, or Docker. Choose the option that suits your needs.
6. Fill in the necessary details for the chosen option and click OK.

---

## Environment variables.

By default, in config folder you will find .json config files. It is required to create .env file and save
ENV=configname in it. In case you
have different configuration .json - set it in .env respectively.

## Project structure.

- configs - package with all configuration files for all test environments and methods to read them into code
- drivers - web_drivers to run browsers
- models - classes for Data Transfer Objects
- services - core for http, db, etc. base clients and their realizations for all required services
- services/enums -- all enums for example: url paths, status codes, methods, etc.
- utils - collection of helper modules - e.g. logging setup is there
- web_pages - selenium page objects implementations are there

- tests - package which contains all api, ui, mobile, etc. tests separated by packages
- tests/fixtures - package with setup\teardown things you need in your project - e.g. webdriver run\stop is there
- tests/resources - dor with all required files, images etc. for tests

---

## Run code static analysis.

- Run flake8: `pipenv run flake8 .`
- Make sure that you have no code style violations before passing PR to review

---

## Run tests locally.

- Create ".env" file with "ENV=qa" row in it in the root directory based on example.env file content.
- Create "qa.json" config file and place to src/configs/envs/
- Run all tests: `pipenv run pytest`
- Run project related tests: `pipenv run pytest tests/{project_name}`
- Run project related tests subset: `pipenv run pytest tests/{project_name}/{tests_file}.py`
- Run project related test: `pipenv run pytest tests/{project_name}/{tests_file}.py::{test_name}`
- You can start tests by providing markers: `pipenv run pytest -m {marker}`

---

## Run tests locally with generating report

- Run tests with creating results for allure report `pipenv run pytest tests --alluredir=allure-results`
- See report: `allure serve allure-results` or if you want to get a html
  report: `allure generate -c ./allure-results -o ./allure-report`

---

## To run web UI tests.

1. You should have driver placed in the src/drivers directory. Naming is {driver}_{system}.{extension}
2. Set its corresponding name in .env file, `WEB_DRIVER` variable, set to CHROME now.
3. In config, `HEADLESS` is set to False now.

---

## Run tests parallel execution

- used for tests that can NOT be run in a parallel execution
- used for tests that can be run in a parallel execution

- Run test in a parallel `pytest tests -m parallel_group -n auto`

---

## Run tests with Test Rail results

- testrail_config.cfg is used for TestRail configs
- to run with integration with Test Rail add: `--testrail --tr-config=testrail_config.cfg` while executing running tests

---

## Run with docker

- dowload repo
- add .env file in root according to example.com. adbjust src/configs/envs/example.json to env that you need
- delete folders /allure-results and /allure-report if exist(usually after test run)
- build an image `docker build -t aqa_tests -f test.dockerfile .`
- run container  `docker run --rm -v ${PWD}:/app aqa_tests  `
- run separate test `docker run --rm -v ${PWD}:/app aqa_tests tests/test_api/pets_test/add_pet/test_create_pet.py`


- run
  report `docker run --rm -v ${PWD}/allure-results:/app/allure-results -v ${PWD}/allure-reports:/app/default-reports frankescobar/allure-docker-service:2.17.2 allure generate -c allure-results -o default-reports/latest`
- in IDEA right click on index.html and open in browser(open as a static file)


- run allure
  server `docker run --rm -v ${PWD}/allure-results:/app/allure-results -p 8080:8080  frankescobar/allure-docker-service:2.17.2 allure serve -p 8080 /app/allure-results`
- and open in browser on localhost:8080

## Description of GitLab CI file

### Stages description

- `testing` stage is for tests execution
- `history_copy` stage copies previous test run for history timeline in report
- `reports` stage generates test execution report
- `notify` stage will publish link for generated report to slack
- `deploy` stage will publish report to gitlab pages

### Jobs description:

- `docker_job` is for running tests in docker. initial docker image and setting up all configs
- `history_copy` is for copying previous test run for history timeline in report
- `allure_report` is for generating test execution report
- `pages` job for publishing report to gitlab pages
- `API_develop` is for running tests for API on dev
- `API_smoke_develop` is for running tests for API only smoke tests on dev
- `API_staging` is for running tests for API only smoke tests on stage