# xama11

[![Wiki](https://img.shields.io/badge/docs-wiki-blue)](https://github.com/xama11/framework/wiki)
[![Discord.py](https://img.shields.io/badge/discord.py-2.6.0-blue.svg)](https://pypi.org/project/discord.py/)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)

A robust and modular framework for developing Discord bots using **discord.py v2**. This project includes a powerful CLI for scaffolding and a Web Dashboard for management.

## � Features

- **Modular Architecture**: Built with scalability in mind using Cogs and Containers.
- **CLI Tool (`octapus`)**: Easily generate commands, models, migrations, and more.
- **Web Dashboard**: Integrated Flask-based dashboard for managing your bot.
- **Database Support**: Built-in support for SQLite3 and MySQL with a custom ORM and Migration system.
- **Task Scheduling**: Integrated `APScheduler` for handling background tasks.
- **Decorator System**: Custom decorators for command handling (e.g., cooldowns, admin checks).

## 📋 Prerequisites

- Python 3.12+
- `pip`

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/xama11/framework.git
   cd framework
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory with the following content:
   ```env
   DISCORD_TOKEN=your_discord_bot_token
   PREFIX=!
   DB_DRIVE=sqlite3
   # For MySQL, add:
   # DB_HOST=localhost
   # DB_USER=root
   # DB_PASSWORD=password
   # DB_DATABASE=dbname
   ```

## 💻 Usage

### Running the Bot
To start the Discord bot:
```bash
python main.py
```

### Running the Web Dashboard
To start the web interface (default port 5000):
```bash
python web.py
```

### Using the CLI (`octapus`)
The `octapus.py` script provides various commands to speed up development.

**Syntax:**
```bash
python octapus.py <command>:<area> <name>
```

**Available Commands:**

| Command | Description | Example |
|---------|-------------|---------|
| `make:command` | Create a new command cog | `python octapus.py make:command Ping` |
| `make:container` | Create a new container | `python octapus.py make:container User` |
| `make:components` | Create a new component | `python octapus.py make:components Button` |
| `make:decorator` | Create a new decorator | `python octapus.py make:decorator IsAdmin` |
| `make:migration` | Create a new database migration | `python octapus.py make:migration CreateUsersTable` |
| `make:model` | Create a new database model | `python octapus.py make:model User` |
| `make:scheduler` | Create a new scheduled task | `python octapus.py make:scheduler DailyReward` |

**Database Migrations:**

To run migrations:
```bash
python octapus.py load:migrate fresh
# OR
python octapus.py load:migrate refresh
```

## 📂 Project Structure

```
xama11/
├── application/         # Bot logic (Cogs, Containers, Decorators)
├── database/            # Database Models and Migrations
├── provider/            # Framework Core (CLI, ORM, Web, Loaders)
├── main.py              # Bot Entry Point
├── web.py               # Web Dashboard Entry Point
├── octapus.py           # CLI Tool Entry Point
└── requirements.txt     # Project Dependencies
```

## 🤝 Contributing

This is a community-driven project, and any help is welcome. If you contribute, please get in touch to receive credit for your work.
