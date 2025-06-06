# Sample Webhook

This project implements a FastAPI application that listens for GitHub webhook events, specifically for pull requests merged into the `main` branch of the `hammer1209/sample-webhook` repository.

## Features

- FastAPI-based webhook listener
- Handles GitHub pull request merged events
- Configurable via environment variables

## Project Structure

```
sample-webhook
├── src
│   └── sample_webhook
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── api
│       │   ├── __init__.py
│       │   ├── routes.py
│       │   └── webhook.py
│       ├── models
│       │   ├── __init__.py
│       │   └── github.py
│       └── services
│           ├── __init__.py
│           └── webhook_handler.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_webhook.py
├── pyproject.toml
├── .env.example
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hammer1209/sample-webhook.git
   cd sample-webhook
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   poetry install
   ```

4. **Configure environment variables:**
   Copy `.env.example` to `.env` and update the values as needed.

5. **Run the application:**
   ```bash
   uvicorn src/sample_webhook.main:app --reload
   ```

## Usage

Once the application is running, you can set up a GitHub webhook in your repository settings to point to your FastAPI application URL. The application will listen for pull request merged events and process them accordingly.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.