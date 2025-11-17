# lightstream_sdk_core.py – OPEN SOURCE CORE (AGPL-3.0)
# © 2025 Lightstream Foundation
# No Chain. Just Stream.
#
# This file is part of Lightstream Foundation.
# Licensed under AGPL-3.0-only. See LICENSE for full text.

import json
import hashlib
import time
import uuid
from typing import Dict, List

class Transaction:
    def __init__(self, sender: str, data: dict):
        self.sender = sender
        self.data = data
        self.timestamp = time.time()
        self.hash = hashlib.sha3_256(json.dumps(data, sort_keys=True).encode()).hexdigest()

    def to_dict(self) -> Dict:
        return {
            "sender": self.sender,
            "data": self.data,
            "timestamp": self.timestamp,
            "hash": self.hash
        }

class SmartLightKey:
    def __init__(self, identity: str):
        self.identity = identity
        self.stream: List[Transaction] = []

    def add_transaction(self, data: dict):
        tx = Transaction(self.identity, data)
        self.stream.append(tx)
        print(f"[TX] {data} – Hash: {tx.hash[:8]}...")

    def export_stream(self) -> str:
        filename = f"stream_{uuid.uuid4().hex[:8]}.json"
        with open(filename, "w") as f:
            json.dump([tx.to_dict() for tx in self.stream], f, indent=2)
        print(f"[EXPORT] {filename}")
        return filename

# Demo
if __name__ == "__main__":
    key = SmartLightKey("user_001")
    key.add_transaction({"freight": "ABC123", "status": "DELIVERED"})
    key.export_stream()