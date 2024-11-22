
# DB Telegram Backup

A Python-based solution to backup data via Telegram with an easy setup process and periodic task scheduling using `crontab`.

# Supported databases

- `PostgreSQL`
- `MySQL`
- `MariaDB`

## Installation

Follow the steps below to install the project:

1. Navigate to the `/opt` directory:
    ```bash
    cd /opt
    ```
2. Clone the repository:
    ```bash
    sudo git clone https://github.com/kanewi11/db-telegram-backup.git
    ```
3. Enter the project directory:
    ```bash
    cd /opt/db-telegram-backup
    ```
4. Update the package list and install Python pip:
    ```bash
    sudo apt-get update -y && sudo apt-get install python3-pip -y
    ```
5. Install Poetry (Python dependency manager):
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
6. Add Poetry to the system path:
    ```bash
    export PATH="$HOME/.local/bin:$PATH"
    ```
7. Configure Poetry to use project-local virtual environments:
    ```bash
    sudo poetry config virtualenvs.in-project true
    ```
8. Install the project dependencies using Poetry:
    ```bash
    sudo poetry install
    ```


## Setting Up Before Starting

Prepare the environment and perform a functional check:

1. Navigate to the project directory:
    ```bash
    cd /opt/db-telegram-backup
    ```
2. Create a `.env` file from the example template:
    ```bash
    sudo cp .envs/.env.example .envs/.env
    ```
3. Open the `.env` file for editing:
    ```bash
    sudo nano .envs/.env
    ```
4. Activate the virtual environment:
    ```bash
    sudo poetry shell
    ```
5. Run the main script to verify functionality:
    ```bash
    sudo python main.py
    ```

## Automating with Crontab

Set up a cron job to automate the backup process:

1. Open the crontab editor:
    ```bash
    sudo crontab -e
    ```
2. Add the following line to schedule the script to run hourly:
    ```
    0 * * * * cd /opt/db-telegram-backup/ && .venv/bin/python main.py
    ```
    This runs the script at the start of every hour.


## Contributing

Feel free to contribute by submitting issues or pull requests to the GitHub repository. I won't answer or respond to them anyway :) 
