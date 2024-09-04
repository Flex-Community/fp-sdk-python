import os
import asyncio
from hmx2.hmx_client import Client
from hmx2.constants.markets import BASE_MARKET_ETH_USD, BASE_MARKET_BTC_USD
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")


async def main():
  client = Client(
     eth_private_key=PRIVATE_KEY,
     rpc_url=RPC_URL
   )

  print("#### Getting position ID from one market ETHUSD (get_position_id) ####")
  position_id = client.public.get_position_id(
    client.private.get_public_address(), 0, BASE_MARKET_ETH_USD)
  print(''.join(format(x, '02x') for x in position_id))

  print("#### Getting position ID from one market BTCUSD (get_position_id) ####")
  position_id = client.public.get_position_id(
    client.private.get_public_address(), 0, BASE_MARKET_BTC_USD)
  print(''.join(format(x, '02x') for x in position_id))


  print("#### Getting all positions info (get_all_position_info) ####")
  positions = client.public.get_all_position_info(
    client.private.get_public_address(), 0)

  for position in positions:
    print(
      f'Account: {position["primary_account"]}-{position["sub_account_id"]}')
    print(f'Market: {position["market"]}')
    print('Size: {0:.4f}'.format(position["position_size"]))
    print('Entry price: {0:.6f}'.format(position["avg_entry_price"]))
    print('Pnl: {0:.4f}'.format(position["pnl"]))


  print("#### Getting positions from one market (get_position_info) ####")
  position = client.public.get_position_info(
    client.private.get_public_address(), 0, BASE_MARKET_ETH_USD)
  print(
    f'Account: {position["primary_account"]}-{position["sub_account_id"]}')
  print(f'Market: {position["market"]}')
  print('Size: {0:.4f}'.format(position["position_size"]))
  print('Entry price: {0:.6f}'.format(position["avg_entry_price"]))
  print('Pnl: {0:.4f}'.format(position["pnl"]))


if __name__ == '__main__':
  asyncio.run(main())
