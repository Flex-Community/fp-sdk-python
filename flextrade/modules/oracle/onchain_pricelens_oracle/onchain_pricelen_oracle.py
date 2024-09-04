from web3 import Web3
from flextrade.helpers.contract_loader import load_contract
from flextrade.helpers.util import convert_asset_to_byte32
from flextrade.modules.oracle.pyth_oracle import PythOracle
from flextrade.constants.contracts import ONCHAIN_PRICELENS_ABI_PATH


class OnchainPricelensOracle(object):
  def __init__(self, onchain_pricelens_address: str, pyth_oracle: PythOracle, eth_provider: Web3) -> None:
    self.pyth_oracle = pyth_oracle
    self.eth_provider = eth_provider
    self.onchain_pricelen_instance = load_contract(
      self.eth_provider, onchain_pricelens_address, ONCHAIN_PRICELENS_ABI_PATH)

  def get_price(self, asset_id: str) -> float:
    price = self.onchain_pricelen_instance.functions.getPrice(
      convert_asset_to_byte32(asset_id)).call()
    return price / 10 ** 18
