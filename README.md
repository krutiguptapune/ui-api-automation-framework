
# UI and API Automation Framework

![CI Pipeline](https://github.com/krutiguptapune/ui-api-automation-framework/actions/workflows/ci.yml/badge.svg)

A Python-based UI and API automation framework built using Playwright and Pytest. The framework automates real-world e-commerce workflows, validates REST APIs, generates HTML reports, captures failure evidence, and runs automated tests through GitHub Actions.

## Project Overview

This project demonstrates a reusable automation framework covering:

- UI automation using Playwright.
- REST API testing using Playwright APIRequestContext.
- Page Object Model (POM).
- Data-driven testing using JSON.
- API response schema validation.
- Reusable API client with retry handling.
- Centralized configuration and logging.
- Failure screenshots and Playwright traces.
- HTML test reports.
- Continuous Integration using GitHub Actions.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Playwright | UI and API automation |
| Pytest | Test execution and test management |
| JSON | Test data and schema storage |
| JSON Schema | API response validation |
| python-dotenv | Environment configuration |
| pytest-html | HTML test reports |
| Git and GitHub | Version control |
| GitHub Actions | CI/CD automation |

## Project Structure

```text
ui-api-automation-framework/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── config/
│   └── settings.py
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── api/
│   └── ui/
│
├── test_data/
│   ├── login_data.json
│   ├── api_test_data.json
│   └── post_schema.json
│
├── utils/
│   ├── api_client.py
│   └── logger.py
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
└── README.md
```

## UI Automation

Website: https://www.saucedemo.com/

Automated scenarios include:

- Homepage validation.
- Valid login.
- Invalid login scenarios.
- Locked-out user validation.
- Product sorting (A-Z and Z-A).
- Price sorting (low-to-high and high-to-low).
- Adding products to cart.
- Removing products from cart.
- Successful checkout.
- Checkout form validation.

## API Automation

API services used:

- JSONPlaceholder
- Restful Booker

Automated scenarios include:

- GET, POST, PUT, PATCH and DELETE requests.
- Authentication and invalid authentication.
- Invalid endpoint validation.
- Query parameter validation.
- API response schema validation.
- Response header validation.
- Boundary and negative scenarios.
- Data-driven testing using JSON.
- Response field and data type validation.

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/krutiguptapune/ui-api-automation-framework.git
```

### 2. Navigate to the project

```bash
cd ui-api-automation-framework
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install Playwright Chromium

```bash
python -m playwright install chromium
```

### 7. Configure environment variables

Copy `.env.example` to `.env` and configure the required URLs and practice credentials.

Never commit your actual `.env` file.

### 8. Run all tests

```bash
pytest -v
```

### 9. Generate an HTML report

```bash
pytest -v --html=reports/full-report.html --self-contained-html
```

## Test Execution Options

Run only UI tests:

```bash
pytest -m ui -v
```

Run only API tests:

```bash
pytest -m api -v
```

Run smoke tests:

```bash
pytest -m smoke -v
```

Run regression tests:

```bash
pytest -m regression -v
```

## Reporting and Debugging

The framework supports:

- HTML execution reports.
- Automatic screenshots on UI test failures.
- Playwright trace recordings for failed UI tests.
- Centralized logging.
- API request retry handling for temporary connection errors.

View a saved Playwright trace:

```bash
python -m playwright show-trace reports/test-name-trace.zip
```

## CI/CD Pipeline

GitHub Actions automatically executes the test suite on pushes and pull requests to the main branch.

The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs dependencies.
4. Installs Playwright Chromium.
5. Executes the automation suite.
6. Generates an HTML report.
7. Uploads reports and available failure evidence as artifacts.

## Project Highlights

- Built a reusable UI and API automation framework.
- Implemented Page Object Model for maintainable UI tests.
- Used JSON-driven parameterization for multiple test scenarios.
- Implemented API schema validation.
- Added logging and controlled retry handling.
- Integrated automated execution with GitHub Actions.

## Author

Kruti Gupta

GitHub: https://github.com/krutiguptapune
