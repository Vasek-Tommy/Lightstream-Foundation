# full_node.py – Full Node Sync Server (AGPL-3.0)
# © 2025 Lightstream Foundation
# No Chain. Just Stream.

import asyncio
import logging
import json

logging.basicConfig(level=logging.INFO)

class FullNode:
    def __init__(self):
        self.global_stream = []

    async def sync_server(self, host="0.0.0.0", port=5000):
        server = await asyncio.start_server(self.handle_client, host, port)
        logging.info(f"[FULL NODE] Listening on {host}:{port}")
        async with server:
            await server.serve_forever()

    async def handle_client(self, reader, writer):
        try:
            data = await asyncio.wait_for(reader.read(100000), timeout=10.0)
            remote_stream = json.loads(data.decode())
            if len(remote_stream) > len(self.global_stream):
                self.global_stream = remote_stream
                logging.info(f"[SYNC] Updated: {len(self.global_stream)} tx")
            writer.write(json.dumps(self.global_stream).encode())
            await writer.drain()
        except Exception as e:
            logging.error(f"[SYNC ERROR] {e}")
        finally:
            writer.close()

if __name__ == "__main__":
    asyncio.run(FullNode().sync_server())