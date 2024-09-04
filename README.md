# Python SDK for Flex Perpetual

This library is tested against Python versions 3.6, 3.9, and 3.11.

## Installation

This package is available on PyPI. To install run the command below:

```
$ pip install fp-v2-python
```

## Getting Started

The `Client` object contains two major attributes: Public and Private. As the names suggest, Public is for public functions that don't require an Ethereum private key, and Private is for functions specifically for the given key. For more comprehensive examples, please refer to the [examples](https://github.com/Flex-Community/fp-sdk-python/tree/main/examples) directory as well as the [tests](https://github.com/Flex-Community/fp-sdk-python/tree/main/tests).

### Public functions

```python
from flextrade.flextrade_client import Client
from flextrade.constants.markets import BASE_MARKET_ETH_USD
from flextrade.enum import Action

#
# Using publicly access functions
#
flextrade_client = Client(
    rpc_url=RPC_URL
)
# Get oracle price, adaptive price, and price impact of a new position
flextrade_client.public.get_price(BASE_MARKET_ETH_USD, Action.SELL, 1000)
# Get market information
flextrade_client.public.get_market_info(BASE_MARKET_ETH_USD)
# Get sub account in address format
flextrade_client.public.get_sub_account(1)
# Get position ID
flextrade_client.public.get_position_id(some_account, some_sub_account_id, BASE_MARKET_ETH_USD)
# Get position info
flextrade_client.public.get_position_info(some_account, some_sub_account_id, BASE_MARKET_ETH_USD)
```

### Private function

```python
from flextrade.flextrade_client import Client
from flextrade.constants.markets import BASE_MARKET_ETH_USD
from flextrade.constants.tokens import BASE_SEPOLIA_COLLATERAL_USDC
from flextrade.enum import Action

#
# Initailized client with private key
#
flextrade_client = Client(
    eth_private_key=PRIVATE_KEY,
    rpc_url=RPC_URL
)
# Get public address of the ethereum key
flextrade_client.private.get_public_address()
# Deposit ETH as collateral
flextrade_client.private.deposit_eth_collateral(sub_account_id=0, amount=10.123)
# Deposit ERC20 as collateral. This function will automatically
# approve CrossMarginHandler if needed.
flextrade_client.private.deposit_erc20_collateral(sub_account_id=0, token_address=BASE_SEPOLIA_COLLATERAL_USDC, amount=100.10)
# Create a market order
create_market_order = flextrade_client.private.create_market_order(
  sub_account_id=0, market_index=BASE_MARKET_ETH_USD, buy=Action.BUY, size=100, reduce_only=False
)
print(create_market_order)
# Create a trigger order
# trigger_above_threshold = The current price must go above (if True) or below (if False)
# the trigger price in order for the order to be executed
create_order = flextrade_client.private.create_trigger_order(
  sub_account_id=0,
  market_index=BASE_MARKET_ETH_USD,
  buy=Action.BUY,
  size=100,
  trigger_price=1800,
  trigger_above_threshold=True,
  reduce_only=False)
print(create_order)
# Update the order
update_order = flextrade_client.private.update_trigger_order(
  0, create_order["order"]["orderIndex"], Action.SELL, 50, 1700, True, False)
print(update_order)
# Cancel the order
cancel_order = flextrade_client.private.cancel_trigger_order(
  0, update_order["order"]["orderIndex"])
```

## Running Tests

To run tests, you will need have to clone the repo, update .env, and run:

```
$ make test
```

Please note that to run tests, Tenderly account is required.

## License

The primary license for Flex-Community/fp-sdk-python is the MIT License, see [here](hhttps://github.com/Flex-Community/fp-sdk-python/blob/main/LICENSE).
