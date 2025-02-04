Playwright Automation with Python

This project is an end-to-end test automation framework built using Playwright, Pytest, and Pytest-BDD for Behavior-Driven Development (BDD) testing.

🚀 Features

Playwright: Modern automation framework for web testing.

Pytest: Simple yet powerful test execution framework.

Pytest-BDD: Enables behavior-driven testing using Gherkin syntax.

Headless & Headed Mode: Run tests in both headless and UI modes.

Parallel Execution: Speed up tests by running in parallel.

HTML Test Reports: Generate detailed test reports.

📂 Project Structure

pytest-python/
│-- tests/               # Test cases
│   │-- features/        # BDD feature files (Gherkin syntax)
│   │-- step_definitions/  # Step definition files for BDD
│-- pages/               # Page Object Model (POM) implementation
│-- utils/               # Helper utilities
│-- pytest.ini           # Pytest configuration file
│-- requirements.txt     # Dependencies list
│-- README.md            # Project documentation

🛠️ Installation

Clone the repository:

git clone https://github.com/henry-49/pytest-python.git
cd pytest-python

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt

Install Playwright browsers:

playwright install

▶️ Running Tests

Run all tests:

pytest --browser_name=chrome --tracing=on --html=report.html

Run a specific test:

pytest tests/test_example.py

Run BDD tests:

pytest --bdd-formatter=pretty

Run tests in headless mode:

pytest --browser_name=chrome --headless

📊 Test Reports

After execution, an HTML report is generated. Open report.html to view test results.

🤝 Contributing

Fork the repository.

Create a new branch (feature/new-feature).

Commit your changes.

Push to the branch and open a PR.

🛠 Troubleshooting

If pytest is not recognized, ensure your virtual environment is activated.

Use pytest -v for verbose logs.

Run playwright install if browsers are missing.

📜 License

This project is licensed under the MIT License.