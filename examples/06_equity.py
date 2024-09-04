import os
import asyncio
from flextrade.flextrade_client import Client
from flextrade.constants.markets import BASE_MARKET_ETH_USD
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")


async def main():
  client = Client(
     eth_private_key=PRIVATE_KEY,
     rpc_url=RPC_URL
   )
  equity = client.public.get_equity(
    client.private.get_public_address(), 1)
  print(f'Equity: {equity}')

if __name__ == '__main__':
  asyncio.run(main())
