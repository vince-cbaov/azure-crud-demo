
# Azure CRUD Demo (Python + TDD)

A small, production-ready Python project showing:

- Azure SQL CRUD with parameterised queries (pyodbc)
- TDD with pytest
- Classical algorithms (insertion sort, linear search)
- Modular code and reusable functions
- CI pipelines: Jenkinsfile and Azure DevOps YAML

## 1. Getting Started

### 1.1 Requirements
- Python 3.10+
- ODBC Driver 18 for SQL Server
- `pyodbc`, `pytest`, `python-dotenv`

Install Python dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Install ODBC Driver 18 (examples):

**Ubuntu/Debian**
```bash
# See Microsoft docs for latest repo steps
sudo apt-get update
sudo apt-get install -y msodbcsql18 unixodbc-dev
```

**macOS (Homebrew)**
```bash
brew update
brew install --cask microsoft-odbc-driver-for-sql-server
brew install unixodbc
```

**Windows**
- Install the "Microsoft ODBC Driver 18 for SQL Server" MSI

### 1.2 Configure Environment
Create a `.env` file (or use environment variables):

```bash
cp .env.example .env
```

Edit values:
```
DB_SERVER=tcp:your-sql-server.database.windows.net,1433
DB_NAME=your_db_name
DB_USER=your_user@your-sql-server
DB_PASSWORD=your_password
```

### 1.3 Create Database Objects
Run the schema script against your Azure SQL database:

```sql
-- database/schema.sql
```

Use Azure Data Studio, sqlcmd, or Azure Portal query editor.

## 2. Run

- Algorithms demo (no DB required):
```bash
python -m app.main --algorithms
```

- Database CRUD demo:
```bash
python -m app.main --database
```

## 3. Tests (TDD)
```bash
pytest -v
```

Unit tests mock database I/O. Integration tests can be added separately.

## 4. CI

### Jenkins
- Update `Jenkinsfile` Git URL to your repo.
- Create a Pipeline job pointing to this Jenkinsfile.

### Azure DevOps
- Import repo and enable CI with `azure-pipelines.yml`.

## 5. Repo & Branching
Recommended branches:
- `main` (production)
- `dev` (integration/testing)
- `feature/*`

## 6. Security Notes
Prefer Managed Identity or Azure Key Vault to store secrets in production.

## 7. License
MIT (or adapt to your organisation's policy)
