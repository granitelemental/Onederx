import os

REDIS_HOST = os.environ.get("REDIS_HOST", "0.0.0.0")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
API_HOST = os.environ.get("API_HOST", "0.0.0.0")
API_PORT = os.environ.get("API_PORT", "8080")
SOCKET_HOST = os.environ.get("SOCKET_HOST", "0.0.0.0")
SOCKET_PORT = os.environ.get("SOCKET_PORT", "3000")