from flextrade.constants.markets import ARBITRUM_MARKET_PROFILE, BLAST_MARKET_PROFILE, BASE_MARKET_PROFILE, DELISTED_MARKET
from flextrade.constants.tokens import TOKEN_PROFILE
from flextrade.constants.contracts import CONTRACT_ADDRESS
from flextrade.helpers.util import is_blast_chain, is_base_chain


def get_collateral_address_asset_map(chain_id: int):
  address_asset_dict = {key: value["asset"]
                        for key, value in TOKEN_PROFILE[chain_id].items()}
  return address_asset_dict


def get_collateral_address_list(chain_id: int):
  address_list = list(set(val["address"]
                      for val in TOKEN_PROFILE[chain_id].values()))
  return address_list


def get_token_profile(chain_id: int):
  return TOKEN_PROFILE[chain_id]


def get_market_profile(chain_id: int):
  if is_blast_chain(chain_id):
    return BLAST_MARKET_PROFILE
  if is_base_chain(chain_id):
    return BASE_MARKET_PROFILE
  return {market: data for market, data in ARBITRUM_MARKET_PROFILE.items() if market not in DELISTED_MARKET}


def get_contract_address(chain_id: int):
  return CONTRACT_ADDRESS[chain_id]
