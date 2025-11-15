import asyncio
import logging
from .config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sampo.worker")


async def worker_loop():
    logger.info("Sampo worker starting in %s environment", settings.environment)
    while True:
        # TODO: connect to Alpaca WebSocket, maintain watchlist, evaluate rules
        logger.info("Worker heartbeat...")
        await asyncio.sleep(10)


def main():
    asyncio.run(worker_loop())


if __name__ == "__main__":
    main()
