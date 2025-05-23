import os
import asyncio
from flextrade.flextrade_client import Client
from flextrade.constants.markets import BASE_MARKET_ETH_USD, BASE_MARKET_SOL_USD
from flextrade.constants.common import ADDRESS_ZERO
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
  create_market_order = client.private.create_market_order(
    0, BASE_MARKET_ETH_USD, Action.BUY, 10, False, ADDRESS_ZERO
  )
  print(f'Create market ETH/USD order tx: {create_market_order["tx"].hex()}\n')
  await asyncio.sleep(8)

  create_order = client.private.create_trigger_order(
    0, BASE_MARKET_ETH_USD, Action.BUY, 20, 3000, True, False)
  print(f'Create ETH/USD order tx: {create_order["tx"].hex()} id: {create_order["order"]["orderIndex"]}\n')
  await asyncio.sleep(8)

  update_order = client.private.update_trigger_order(
    0, create_order["order"]["orderIndex"], Action.SELL, 5, 2700, True, False, ADDRESS_ZERO)
  print(f'Update ETH/USD order tx: {update_order["tx"].hex()} id: {update_order["order"]["orderIndex"]}\n')
  await asyncio.sleep(20)

  cancel_order = client.private.cancel_trigger_order(
    0, BASE_MARKET_ETH_USD, update_order["order"]["orderIndex"])
  print(f'Cancel ETH/USD order tx: {cancel_order["tx"].hex()} id: {cancel_order["order"]["orderIndex"]}\n')
  await asyncio.sleep(8)

  # SOL
  create_market_order = client.private.create_market_order(
    0, BASE_MARKET_SOL_USD, Action.BUY, 10, False, ADDRESS_ZERO
  )
  print(f'Create market SOL/USD order tx: {create_market_order["tx"].hex()}\n')
  await asyncio.sleep(8)

  create_order = client.private.create_trigger_order(
    0, BASE_MARKET_SOL_USD, Action.BUY, 20, 3000, True, False)
  print(f'Create SOL/USD order tx: {create_order["tx"].hex()} id: {create_order["order"]["orderIndex"]}\n')
  await asyncio.sleep(8)

  update_order = client.private.update_trigger_order(
    0, create_order["order"]["orderIndex"], Action.SELL, 5, 2700, True, False, ADDRESS_ZERO)
  print(f'Update SOL/USD order tx: {update_order["tx"].hex()} id: {update_order["order"]["orderIndex"]}\n')
  await asyncio.sleep(20)

  cancel_order = client.private.cancel_trigger_order(
    0, BASE_MARKET_SOL_USD, update_order["order"]["orderIndex"])
  print(f'Cancel SOL/USD order tx: {cancel_order["tx"].hex()} id: {cancel_order["order"]["orderIndex"]}\n')
  await asyncio.sleep(8)

if __name__ == '__main__':
  asyncio.run(main())
