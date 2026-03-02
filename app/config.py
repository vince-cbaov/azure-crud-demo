
import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present (useful for local dev)
load_dotenv()

class Config:
    """Simple configuration holder for DB connection credentials.
    For production, prefer Azure Key Vault or Managed Identity.
    """
    DB_SERVER = os.getenv('DB_SERVER', 'tcp:crud-sql-server.database.windows.net,1433')
    DB_NAME = os.getenv('DB_NAME', 'crud_db')
    DB_USER = os.getenv('DB_USER', 'sqladmin')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '800MCP0J1YYdeMOO759')
    # Optional: Timeout & Encrypt options
    DB_TIMEOUT = int(os.getenv('DB_TIMEOUT', '30'))
