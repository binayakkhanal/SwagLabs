# Hybrid Automation Framework

## Overview
This is a hybrid automation framework that supports UI (Selenium), API, and Database validation.

## Setup
1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`

## Running Tests
### UI Tests
Run all tests:
```bash
pytest -n 4 --html=report.html
```

Run E2E tests:
```bash
pytest automation_framework/tests/
```

### API Tests
```bash
pytest automation_framework/api/
```

### Database Tests
```bash
pytest automation_framework/database/
```

## Environment Variables
- `HEADLESS`: Set to `true` to run in headless mode (default: `false`).
- `BROWSER`: Set to `chrome` (default: `chrome`).

## Directory Structure
- `core/`: Core framework components (BasePage, Config, Logger).
- `pages/`: Page Object Models.
- `api/`: API client and tests.
- `database/`: Database client and tests.
- `tests/`: UI tests.
- `data/`: Test data.
