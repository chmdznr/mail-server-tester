# Simple Mail Tester

Just a simple mail server tester using python.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Clone the repo. Make sure your python env has `smtplib` and `python-dotenv` packages.

## Usage

- Create `.env` file based on `env.example` file
- Fill the `.env` content with your correct info (SMTP server, etc. )
- Run the script: `python3 smtp_server.py`

Notes: the script will automatically use TLS protocol if your SMTP server port is 587, and use SSL if the port is 465.

## Contributing

Contact me personally.

## License

Whatever.
