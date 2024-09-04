import os
import asyncio
from hmx2.hmx_client import Client
from hmx2.constants.tokens import BASE_SEPOLIA_COLLATERAL_ETH, BASE_SEPOLIA_COLLATERAL_USDC, BASE_SEPOLIA_COLLATERAL_BTC
from dotenv import load_dotenv
from time import sleep

load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
RPC_URL = os.getenv("RPC_URL")
ACCOUNT = os.getenv("ACCOUNT")


async def main():
  client = Client(
     eth_private_key=PRIVATE_KEY,
     rpc_url=RPC_URL,
   )

  print("# Collateral info")
  # Get Collateral
  collaterial = client.public.get_collaterals(ACCOUNT, sub_account_id=0)
  for symbol, item in collaterial.items():
    print("{:6s} - Amount: {:18.8}, Value USD {:18.8f}, Value Without Factor USD {:18.8f}".format(symbol, item["amount"], item["value_usd"], item["value_without_factor_usd"]))
  print()


  print("# Deposit Collateral")
  client.private.deposit_erc20_collateral(
    sub_account_id=0, token_address=BASE_SEPOLIA_COLLATERAL_BTC, amount=0.08)
  await asyncio.sleep(5)
  print()

  print("# Collateral info")
  collaterial =  client.public.get_collaterals(ACCOUNT, sub_account_id=0)
  for symbol, item in collaterial.items():
    print("{:6s} - Amount: {:18.8}, Value USD {:18.8f}, Value Without Factor USD {:18.8f}".format(symbol, item["amount"], item["value_usd"], item["value_without_factor_usd"]))
  print()

  print("# Withdraw Collateral")
  # # Withdraw ERC20 as collateral. This function will automatically
  client.private.withdraw_collateral(
    sub_account_id=0, token_address=BASE_SEPOLIA_COLLATERAL_BTC, amount=0.1)
  await asyncio.sleep(8)

  print("# Collateral info")
  collaterial =  client.public.get_collaterals(ACCOUNT, sub_account_id=0)
  for symbol, item in collaterial.items():
    print("{:6s} - Amount: {:18.8}, Value USD {:18.8f}, Value Without Factor USD {:18.8f}".format(symbol, item["amount"], item["value_usd"], item["value_without_factor_usd"]))
  print()


  # Deposit ETH as collateral
  client.private.deposit_eth_collateral(sub_account_id=0, amount=0.001)
  await asyncio.sleep(5)

  print("# Collateral info")
  collaterial =  client.public.get_collaterals(ACCOUNT, sub_account_id=0)
  for symbol, item in collaterial.items():
    print("{:6s} - Amount: {:18.8}, Value USD {:18.8f}, Value Without Factor USD {:18.8f}".format(symbol, item["amount"], item["value_usd"], item["value_without_factor_usd"]))

  # Deposit ERC20 as collateral. This function will automatically
  # approve CrossMarginHandler if needed.
  client.private.deposit_erc20_collateral(
    sub_account_id=0, token_address=BASE_SEPOLIA_COLLATERAL_USDC, amount=0.01)

  await asyncio.sleep(5)

  print("# Collateral info")
  collaterial =  client.public.get_collaterals(ACCOUNT, sub_account_id=0)
  for symbol, item in collaterial.items():
    print("{:6s} - Amount: {:18.8}, Value USD {:18.8f}, Value Without Factor USD {:18.8f}".format(symbol, item["amount"], item["value_usd"], item["value_without_factor_usd"]))

  # Withdraw ETH as collateral
  # Can wrap if wanted
  client.private.withdraw_collateral(
    sub_account_id=0, token_address=BASE_SEPOLIA_COLLATERAL_ETH, amount=0.1, wrap=False)

  await asyncio.sleep(5)

  print("# Collateral info")
  collaterial =  client.public.get_collaterals(ACCOUNT, sub_account_id=0)
  for symbol, item in collaterial.items():
    print("{:6s} - Amount: {:18.8}, Value USD {:18.8f}, Value Without Factor USD {:18.8f}".format(symbol, item["amount"], item["value_usd"], item["value_without_factor_usd"]))

  # Withdraw ERC20 as collateral. This function will automatically
  client.private.withdraw_collateral(
    sub_account_id=0, token_address=BASE_SEPOLIA_COLLATERAL_USDC, amount=0.01)

  print("# Collateral info")
  collaterial =  client.public.get_collaterals(ACCOUNT, sub_account_id=0)
  for symbol, item in collaterial.items():
    print("{:6s} - Amount: {:18.8}, Value USD {:18.8f}, Value Without Factor USD {:18.8f}".format(symbol, item["amount"], item["value_usd"], item["value_without_factor_usd"]))

if __name__ == '__main__':
  asyncio.run(main())
