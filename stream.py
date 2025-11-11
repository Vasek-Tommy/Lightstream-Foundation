import json
import time
from typing import List, Optional

class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float, data: dict = None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.data = data or {}
        self.timestamp = time.time()
        self.prev_hash: Optional[str] = None
        self.signature: Optional[str] = None

    def hash(self) -> str:
        tx_str = f"{self.sender}{self.receiver}{self.amount}{self.timestamp}{self.prev_hash}{json.dumps(self.data)}"
        return str(hash(tx_str))

    def to_json(self) -> str:
        return json.dumps(vars(self), indent=2)

class LightStream:
    def __init__(self, genesis_tx: Transaction):
        self.txs: List[Transaction] = [genesis_tx]

    def add_tx(self, tx: Transaction) -> bool:
        if self.txs:
            tx.prev_hash = self.txs[-1].hash()
        self.txs.append(tx)
        return True

    def validate(self) -> bool:
        for i in range(1, len(self.txs)):
            if self.txs[i].prev_hash != self.txs[i-1].hash():
                return False
        return True

# Demo
genesis = Transaction("genesis", "alice", 1000)
stream = LightStream(genesis)
tx1 = Transaction("alice", "bob", 10)
stream.add_tx(tx1)
print(stream.txs[-1].to_json())
print("Valid:", stream.validate())
