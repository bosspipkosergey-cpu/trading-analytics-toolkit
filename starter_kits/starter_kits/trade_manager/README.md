# Trade Management Module 🛡️

A professional, broker-agnostic Python module for intelligent position management.

## Why use this?
Manual trade management is prone to emotional errors. This module automates the two most critical aspects of risk management:
1. **Break-Even (BE):** Secure your capital once the trade reaches a profitable threshold.
2. **Trailing Stop:** Automatically lock in profits as the market moves in your favor.

## Key Features
* **Broker-Agnostic:** Does not rely on any specific API. Use it with any broker.
* **ATR-Based Logic:** Dynamically adjusts to market volatility using ATR, rather than static ticks.
* **Easy Integration:** A simple `get_new_stop_level` method that integrates into any bot loop in minutes.

## Usage Example
```python
from trade_manager import TradeManager

# Initialize with a fallback SL of 12.0
manager = TradeManager(fallback_sl=12.0)

# Inside your loop:
new_stop = manager.get_new_stop_level(
    current_price=1850.5, 
    entry_price=1848.0, 
    current_sl=1836.0, 
    direction="BUY", 
    atr=1.5
)
# Trade Management Module 🛡️

A professional, broker-agnostic Python module for intelligent position management.

## Why use this?
Manual trade management is prone to emotional errors. This module automates the two most critical aspects of risk management:
1. **Break-Even (BE):** Secure your capital once the trade reaches a profitable threshold.
2. **Trailing Stop:** Automatically lock in profits as the market moves in your favor.

## Key Features
* **Broker-Agnostic:** Does not rely on any specific API. Use it with any broker.
* **ATR-Based Logic:** Dynamically adjusts to market volatility using ATR, rather than static ticks.
* **Easy Integration:** A simple `calculate_stop_adjustment` method that integrates into any bot loop in minutes.

## How to run the demo
1. Ensure you have the `trade_manager.py` file in the same folder.
2. Run the demo script:
   ```bash
   python demo.py
