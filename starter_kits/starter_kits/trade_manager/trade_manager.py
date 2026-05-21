"""
TradeManager: Intelligent position management (Break-Even & Trailing Stop).
Designed to be broker-agnostic.
"""

class TradeManager:
    def __init__(self, fallback_sl: float, max_losses: int = 3):
        self.fallback_sl = fallback_sl
        self.max_losses = max_losses
        self.consecutive_losses = 0

    def calculate_stop_adjustment(self, 
                                  current_price: float, 
                                  entry_price: float, 
                                  curr_sl: float, 
                                  direction: str, 
                                  atr: float,
                                  be_trigger: float,
                                  trail_start: float,
                                  trail_step: float) -> float:
        """
        Возвращает новый уровень Stop Loss или None, если изменения не нужны.
        """
        profit = (current_price - entry_price) if direction == 'BUY' else (entry_price - current_price)
        be_offset = max(atr * 0.1, self.fallback_sl * 0.1)
        
        # 1. Logic for Break-Even
        is_be_set = (direction == 'BUY' and curr_sl >= entry_price + be_offset * 0.9) or \
                    (direction == 'SELL' and curr_sl <= entry_price - be_offset * 0.9)

        if profit >= be_trigger and not is_be_set:
            return entry_price + be_offset if direction == 'BUY' else entry_price - be_offset

        # 2. Logic for Trailing Stop
        if profit >= trail_start:
            safe_step = max(trail_step, self.fallback_sl * 0.5)
            target = current_price - safe_step if direction == 'BUY' else current_price + safe_step
            
            if (direction == 'BUY' and target > curr_sl) or (direction == 'SELL' and target < curr_sl):
                return target

        return None # No change
