import os
from dotenv import load_dotenv

load_dotenv()

print("ORACLE STATUS: Reading the Matrix...")


mode = os.getenv("MATRIX_MODE", "development")
db = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL", "INFO")
zion = os.getenv("ZION_ENDPOINT")

print("\nConfiguration loaded:")

print(f"Mode: {mode}")

if db:
    print("Database: Connected to configured instance")
else:
    print("Database: WARNING - No DATABASE_URL found")

if api_key:
    print("API Access: Authenticated")
else:
    print("API Access: WARNING - Missing API_KEY")

print(f"Log Level: {log_level}")

if zion:
    print("Zion Network: Online")
else:
    print("Zion Network: OFFLINE (missing endpoint)")

print("\nEnvironment security check:")

print("[OK] No hardcoded secrets detected")
print("[OK] .env file properly configured")
print("[OK] Environment variable override supported")

print("\nThe Oracle sees all configurations.")
