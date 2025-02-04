# Playwright Automation with Python

#### This project is an end-to-end test automation framework built using Playwright, Pytest, and Pytest-BDD for Behavior-Driven Development (BDD) testing.

## 🚀 Features

* Playwright: Modern automation framework for web testing.

* Pytest: Simple yet powerful test execution framework.

* Pytest-BDD: Enables behavior-driven testing using Gherkin syntax.

* Headless & Headed Mode: Run tests in both headless and UI modes.

* Parallel Execution: Speed up tests by running in parallel.

* HTML Test Reports: Generate detailed test reports.

## 🛠️ Installation

###  Clone the repository:
```
$ git clone https://github.com/henry-49/pytest-python.git
$ cd pytest-python
```
### Create a virtual environment:
```
$ python3 -m venv venv
$ source venv/bin/activate   # macOS/Linux
$ venv\Scripts\activate      # Windows
```
### Install dependencies:
```
$ pip install -r requirements.txt
```
### Install Playwright browsers:
```
$ playwright install
```
## ▶️ Running Tests

### Run all tests:
```
$ pytest --browser_name=chrome --tracing=on --html=report.html
```
### Run a specific test:
```
$ pytest tests/test_example.py
```
### Run BDD tests:
```
$ pytest --bdd-formatter=pretty
```
### Run tests in headless mode:
```
$ pytest --browser_name=chrome --headless
```
## 📊 Test Reports

#### After execution, an HTML report is generated. 
#### Open report.html to view test results.

## 🛠 Troubleshooting

#### If pytest is not recognized, ensure your virtual environment is activated.

#### Use pytest -v for verbose logs.

#### Run playwright install if browsers are missing.

## 📜 License

#### This project is licensed under the [MIT](#mit) License.