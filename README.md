# 🛒 E-Commerce Automation Framework (Selenium + Python)

A professional-grade automation suite designed for a clothing e-commerce platform. This framework uses **Page Object Model (POM)** and **Data-Driven Testing** to ensure high stability and easy maintenance.

## Framework Architecture
The project is structured to follow the **Single Responsibility Principle**:
- **config/**: Environment-specific configurations.
- **locators/**: Centralized UI selectors to handle UI changes easily.
- **pages/**: Business logic and page actions.
- **tests/**: Functional and End-to-End test suites.
- **utils/**: Logging and configuration readers.

##  Key Features
- **POM Design**: Separation of test logic and UI interactions.
- **JavaScript Click Layer**: Custom utility to bypass Google Ad overlays and dynamic UI blocks.
- **Auto-Generated Reports**: Professional HTML reports with execution status.
- **Detailed Logging**: Comprehensive audit trails in `.log` files for rapid debugging.
- **Explicit Waits**: Zero `time.sleep` usage; all synchronization is handled via `WebDriverWait`.

## Setup & Execution
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/Pytest_Selenium_ECommerce_Framework.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest -v -s --html=reports/report.html`

## Test Coverage
- User Authentication (Positive & Negative)
- End-to-End Checkout Flow
- Product Search Functionality
- Contact Form (File Upload & Alert Handling)
