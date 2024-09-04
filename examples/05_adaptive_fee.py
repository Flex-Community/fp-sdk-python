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
  is_increase_position = True
  size_delta = 800000 * (10**30)
  fee = client.public.get_adaptive_fee(
    size_delta, BASE_MARKET_ETH_USD, is_increase_position)
  print(f'Market: SOL')
  print(f'Size: {size_delta}')
  print(f'Adaptive Fee: {fee}')

if __name__ == '__main__':
  asyncio.run(main())
