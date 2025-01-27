from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce, OrderType
from alpaca.trading.requests import (
    MarketOrderRequest,
    LimitOrderRequest,
    TrailingStopOrderRequest,
)
from alpaca.trading.stream import TradingStream
from colorama import Fore, Style, init
import config

# * Initialize colorama
init(autoreset=True)

# * Get Account Information
client = TradingClient(config.API_KEY, config.SECRET_KEY)


#! Submit a Market Order
def submit_market_order(symbol: str, qty: int, side: OrderSide):
    order_details = MarketOrderRequest(
        symbol=symbol, qty=qty, side=side, time_in_force=TimeInForce.GTC
    )

    order = client.submit_order(order_data=order_details)
    print(f"\n{Fore.GREEN}{Style.BRIGHT}Market Order Details:{Style.RESET_ALL}")

    order_attributes = vars(order)  # Extract attributes as a dictionary

    for k, v in order_attributes.items():
        print(f"{k:30}{v}")


#! Submit a Limit Order
def submit_limit_order(symbol: str, qty: int, side: OrderSide, limit_price: float):
    limit_order_details = LimitOrderRequest(
        symbol=symbol,
        qty=qty,
        side=side,
        limit_price=limit_price,
        time_in_force=TimeInForce.DAY,
    )

    limit_order = client.submit_order(order_data=limit_order_details)
    print(f"\n{Fore.BLUE}{Style.BRIGHT}Limit Order Details:{Style.RESET_ALL}")

    limit_order_attributes = vars(limit_order)  # Extract attributes as a dictionary

    for k, v in limit_order_attributes.items():
        print(f"{k:30}{v}")


#! Submit a Trailing Stop Order
def submit_trailing_order():
    trailing_order_details = TrailingStopOrderRequest(
        symbol="BTC/USD",
        qty=100,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.GTC,
        trail_percent=1.00,
    )

    trailing_order = client.submit_order(order_data=trailing_order_details)
    print(f"\n{Fore.BLUE}{Style.BRIGHT}trailing Order Details:{Style.RESET_ALL}")

    trailing_order_attributes = vars(
        trailing_order
    )  # Extract attributes as a dictionary

    for k, v in trailing_order_attributes.items():
        print(f"{k:30}{v}")
        
limit_order_data = LimitOrderRequest(
    symbol="BTC/USD",
    qty=0.01,  # Asegúrate de tener al menos esta cantidad de BTC
    side=OrderSide.SELL,
    limit_price=17000,
    time_in_force=TimeInForce.GTC,
)

try:
    limit_order = client.submit_order(order_data=limit_order_data)
    print("Order submitted successfully:", limit_order)
except Exception as e:
    print("Error submitting order:", e)



# * Call Market Order
# submit_market_order(symbol="BTC/USD", qty=100, side=OrderSide.BUY)
# submit_market_order(symbol="MSFT", qty=7, side=OrderSide.BUY)

# submit_trailing_order()

# # * Call Limit Order
# submit_limit_order(symbol="AAPL", qty=12, side=OrderSide.BUY, limit_price=77.00)

# # * Trading Stream
# trades = TradingStream(config.API_KEY, config.SECRET_KEY, paper=True)


# async def trade_status(data):
#     print(f"\n{Fore.YELLOW}{Style.BRIGHT}Trade Update:{Style.RESET_ALL}")
#     # Use model_dump() for Pydantic v2.0+
#     trade_data = data.model_dump()
#     for k, v in trade_data.items():
#         print(f"{k:30}{v}")


# trades.subscribe_trade_updates(trade_status)
# trades.run()
