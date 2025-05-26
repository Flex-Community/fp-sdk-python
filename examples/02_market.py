import os
import asyncio
from flextrade.flextrade_client import Client
from flextrade.constants.markets import (
    BASE_MARKET_ETH_USD, BASE_MARKET_BTC_USD, BASE_MARKET_BNB_USD,
    BASE_MARKET_SHIB_USD, BASE_MARKET_PEPE_USD, BASE_MARKET_SUI_USD,
    BASE_MARKET_DOGE_USD, BASE_MARKET_AAVE_USD, BASE_MARKET_HBAR_USD,
    BASE_MARKET_VIRTUAL_USD, BASE_MARKET_ADA_USD, BASE_MARKET_PENDLE_USD,
    BASE_MARKET_TRX_USD, BASE_MARKET_AVAX_USD, BASE_MARKET_UNI_USD,
    BASE_MARKET_SOL_USD, BASE_MARKET_LINK_USD, BASE_MARKET_XRP_USD,
    BASE_MARKET_TON_USD
)
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

# List of all markets to test
MARKETS = [
    BASE_MARKET_ETH_USD,
    BASE_MARKET_BTC_USD,
    BASE_MARKET_BNB_USD,
    BASE_MARKET_SHIB_USD,
    BASE_MARKET_PEPE_USD,
    BASE_MARKET_SUI_USD,
    BASE_MARKET_DOGE_USD,
    BASE_MARKET_AAVE_USD,
    BASE_MARKET_HBAR_USD,
    BASE_MARKET_VIRTUAL_USD,
    BASE_MARKET_ADA_USD,
    BASE_MARKET_PENDLE_USD,
    BASE_MARKET_TRX_USD,
    BASE_MARKET_AVAX_USD,
    BASE_MARKET_UNI_USD,
    BASE_MARKET_SOL_USD,
    BASE_MARKET_LINK_USD,
    BASE_MARKET_XRP_USD,
    BASE_MARKET_TON_USD
]

def print_market_info(market_info):
    """Helper function to print market information"""
    print('Market {0}'.format(market_info["market"]))
    print('Price: {0:.4f}'.format(market_info["price"]))
    print('Long: {0:.2f}'.format((market_info["long_size"])))
    print('Short: {0:.2f}'.format((market_info["short_size"])))
    print('Funding rate 1H: {0:.6f}%'.format(
        (market_info["funding_rate"]["1H"])))
    print('Funding rate 8H: {0:.6f}%'.format(
        (market_info["funding_rate"]["8H"])))
    print('Funding rate 24H: {0:.6f}%'.format(
        (market_info["funding_rate"]["24H"])))
    print('Funding rate 1Y: {0:.6f}%'.format(
        (market_info["funding_rate"]["1Y"])))
    print('Borrowing rate 1H: {0:.6f}%'.format(
        (market_info["borrowing_rate"]["1H"])))
    print('Borrowing rate 8H: {0:.6f}%'.format(
        (market_info["borrowing_rate"]["8H"])))
    print('Borrowing rate 24H: {0:.6f}%'.format(
        (market_info["borrowing_rate"]["24H"])))
    print('Borrowing rate 1Y: {0:.6f}%'.format(
        (market_info["borrowing_rate"]["1Y"])))
    print('-' * 50)  # Separator line

async def main():
    client = Client(
        eth_private_key=PRIVATE_KEY,
        rpc_url=RPC_URL
    )

    print("Testing all markets...\n")

    for market in MARKETS:
        try:
            market_info = client.public.get_market_info(market)
            print_market_info(market_info)
        except Exception as e:
            print(f"Error fetching market {market}: {e}")
            print('-' * 50)

if __name__ == '__main__':
    asyncio.run(main())