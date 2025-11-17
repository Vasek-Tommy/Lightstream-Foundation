# core/airdrop.py
# © 2025 Lightstream Foundation

from .lightstream_sdk_core import SmartLightKey

def airdrop_lst(count: int = 10):
    for i in range(count):
        key = SmartLightKey(f"star_{i:04d}")
        key.add_transaction({
            "type": "lst_airdrop",
            "lst_amount": 100.0,
            "reason": "GitHub Star"
        })
        key.export_stream()
    print(f"[AIRDROP] {count * 100} LST an {count} Stars")

if __name__ == "__main__":
    airdrop_lst()