# from alpaca.trading.client import TradingClient
# from alpaca.trading.requests import GetAssetsRequest
# from alpaca.trading.enums import AssetClass
import config


# # search for US equities
# search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
# appl_assets = dict(trading_client.get_asset('AAPL'))
# for k, v in appl_assets.items():
#     print(f"{k:40}{v}")

# if appl_assets["tradable"]:
#     print('We can trade AAPL.')
# # assets = trading_client.get_all_assets(search_params)

# # print(appl_assets)


from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient(config.API_KEY, config.SECRET_KEY)

market_order_data = MarketOrderRequest(
    symbol="SPY", qty=1, side=OrderSide.SELL, time_in_force=TimeInForce.GTC
)

# Market order
market_order = trading_client.submit_order(order_data=market_order_data)
