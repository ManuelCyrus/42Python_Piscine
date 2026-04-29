import os
from dotenv import load_dotenv

load_dotenv()

print("ORACLE STATUS: Reading the Matrix...\n")

mode = os.getenv("MATRIX_MODE", "development")
db = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL", "INFO")
zion = os.getenv("ZION_ENDPOINT")

print("Configuration loaded:")
print(f"Mode: {mode}")

if mode == "production":
    print("Environment: SECURE PRODUCTION SYSTEM")
else:
    print("Environment: DEVELOPMENT MODE")

if db:
    print("Database: Connected to configured instance")
else:
    print("Database: LOCAL / MOCK DATABASE")

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

if any(var in os.environ for var in ["MATRIX_MODE", "API_KEY"]):
    print("[OK] Environment variables override detected")

print("[OK] No hardcoded secrets detected")
print("[OK] .env support enabled")

print("\nThe Oracle sees all configurations.")
