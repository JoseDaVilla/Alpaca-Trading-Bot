echo "# Trading Bot 🐍📈

This project is an automated trading bot developed with Python and the Alpaca API, designed to efficiently and quickly execute market orders in the financial market.

## Features 🚀
- Support for Market Orders, Limit Orders, and Trailing Stop Orders.
- Integration with the Alpaca API for real-time trading.
- Stream updates to monitor the status of your trades.
- Simple and customizable Python interface.

## Requirements 🛠️
- **Python 3.8** or higher.
- An [Alpaca](https://alpaca.markets/) account with API keys.
- Dependencies listed in the \`requirements.txt\` file.

## Installation 💻
1. Clone this repository:
   \`\`\`bash
   git clone https://github.com/JoseDaVilla/Alpaca-Trading-Bot.git
   cd trading-bot
   \`\`\`

2. Create a virtual environment and install dependencies:
   \`\`\`bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   \`\`\`

3. Configure your API keys in a \`config.py\` file:
   \`\`\`python
   # config.py
   API_KEY = \"YOUR_API_KEY_HERE\"
   SECRET_KEY = \"YOUR_SECRET_KEY_HERE\"
   \`\`\`

4. Run the bot:
   \`\`\`bash
   python trading_bot.py
   \`\`\`

## Usage 📊
This bot allows you to perform different types of trades by modifying or calling the existing functions as needed:
- **Market Orders**: Buy or sell at the best available price.
- **Limit Orders**: Buy or sell at a specified price.
- **Trailing Stop Orders**: Automatically adjust the stop price based on a fixed amount or percentage.

Example of placing a market order:
\`\`\`python
submit_market_order(symbol=\"AAPL\", qty=1, side=OrderSide.BUY)
\`\`\`

