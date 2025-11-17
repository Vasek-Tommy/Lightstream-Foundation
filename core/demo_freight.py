# core/demo_freight.py
# © 2025 Lightstream Foundation

from .lightstream_sdk_core import SmartLightKey

if __name__ == "__main__":
    key = SmartLightKey("Planzer-ZH")
    key.add_transaction({
        "freight": "ABC123",
        "temp": 4.2,
        "status": "DELIVERED",
        "location": "Zürich"
    })
    key.export_stream()
    print("Freight Demo gespeichert!")