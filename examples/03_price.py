import os
import asyncio
from flextrade.flextrade_client import Client
from flextrade.constants.markets import BASE_MARKET_ETH_USD
from flextrade.enum import Action
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")


async def main():
  client = Client(
     eth_private_key=PRIVATE_KEY,
     rpc_url=RPC_URL
   )

  dix_price = client.public.get_price(BASE_MARKET_ETH_USD)
  print('Case: Query raw price ')
  print('Market {0}'.format(dix_price["market"]))
  print('Price: {0:.4f}'.format(dix_price["price"]))

  dix_price = client.public.get_price(BASE_MARKET_ETH_USD, Action.SELL, 1000)
  print('Case: Including adaptive price ')
  print('Market {0}'.format(dix_price["market"]))
  print('Price: {0:.4f}'.format(dix_price["price"]))
  print('Adaptive price {0:.4f}'.format(dix_price["adaptive_price"]))
  print('Price impact {0:.4f}%'.format(dix_price["price_impact"]))


if __name__ == '__main__':
  asyncio.run(main())
