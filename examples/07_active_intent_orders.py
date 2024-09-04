import os
import asyncio
import requests
from hmx2.hmx_client import Client
from hmx2.constants.markets import BASE_MARKET_ETH_USD
from dotenv import load_dotenv


load_dotenv()

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")


async def main():
  client = Client(
     eth_private_key=PRIVATE_KEY,
     rpc_url=RPC_URL
   )

  try:
    response = client.public.get_active_intent_orders(
        client.private.get_public_address(), 1)
    print(response)

    response = client.public.get_active_limit_orders(
        client.private.get_public_address())
    print(response)
    for sub_account_id, orders in response.items():
      print(f'Sub Account id: {sub_account_id}')
      for order_index, order in enumerate(orders):
        print(f"\tOrder index: {order_index}")
        for k, v in order.items():
          print(f"\t\t{k}: {v}")


  except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Handle HTTP errors
  except requests.exceptions.ConnectionError as conn_err:
    print(f'Connection error occurred: {conn_err}')  # Handle connection errors
  except requests.exceptions.Timeout as timeout_err:
    print(f'Timeout error occurred: {timeout_err}')  # Handle timeout errors
  except requests.exceptions.RequestException as req_err:
    print(f'An error occurred: {req_err}')  # Handle any other request errors


if __name__ == '__main__':
  asyncio.run(main())
