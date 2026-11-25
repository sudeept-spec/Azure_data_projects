import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read environment variables
server = os.getenv("DB_SERVER")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

print("Server:", server)
print("Username:", username)
print("Database:", database)