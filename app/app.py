"""
Notes Info Server
------------------
A tiny Flask web app used as the "task of choice" for the Docker module.

What it does:
- Serves a JSON status page at "/" showing a configurable greeting message,
  the hostname of the container, and how many .txt note files exist in /app/data.
- Serves a "/health" endpoint used by the Docker HEALTHCHECK instruction.

Configuration is done entirely through environment variables (no code changes
needed), which satisfies the "environment-variable based configuration"
best practice required by the assignment:
    APP_MESSAGE  -> greeting text shown on the status page (default: "Hello!")
    APP_PORT     -> port the server listens on (default: 5000)
"""

import os
import socket
from datetime import datetime, timezone
from flask import Flask, jsonify

app = Flask(__name__)

DATA_DIR = os.environ.get("DATA_DIR", "/app/data")
APP_MESSAGE = os.environ.get("APP_MESSAGE", "Hello!")


def count_notes():
    if not os.path.isdir(DATA_DIR):
        return 0
    return len([f for f in os.listdir(DATA_DIR) if f.endswith(".txt")])


@app.route("/")
def status():
    return jsonify({
        "message": APP_MESSAGE,
        "hostname": socket.gethostname(),
        "notes_found": count_notes(),
        "server_time_utc": datetime.now(timezone.utc).isoformat(),
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("APP_PORT", 5000))
    app.run(host="0.0.0.0", port=port)
