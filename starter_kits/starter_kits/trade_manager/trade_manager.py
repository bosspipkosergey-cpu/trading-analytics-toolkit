"""
TradeManager: Professional module for Trailing Stop & Break-Even logic.
"""

class TradeManager:
    def __init__(self, fallback_sl: float):
        self.fallback_sl = fallback_sl

    def calculate_initial_stop(self, price: float, direction: str, atr: float) -> float:
        """Рассчитывает первичный уровень стоп-лосса."""
        dist = max(atr * 1.5, self.fallback_sl)
        return price - dist if direction == "BUY" else price + dist

    def get_new_stop_level(self, 
                           current_price: float, 
                           entry_price: float, 
                           current_sl: float, 
                           direction: str, 
                           atr: float) -> float:
        """
        Основной метод логики: 
        Возвращает обновленный уровень стоп-лосса или None, если двигать не нужно.
        """
        profit = (current_price - entry_price) if direction == 'BUY' else (entry_price - current_price)
        
        # Параметры (можно вынести в конфиг)
        be_trigger = max(atr * 1.5, self.fallback_sl * 0.8)
        trail_start = max(atr * 1.2, self.fallback_sl * 1.0)
        trail_step = max(atr * 0.4, self.fallback_sl * 0.3)
        
        # 1. Логика безубытка (Break-Even)
        if profit >= be_trigger:
            # Устанавливаем стоп в безубыток + небольшой отступ
            be_level = entry_price + (atr * 0.1) if direction == 'BUY' else entry_price - (atr * 0.1)
            # Возвращаем, если текущий стоп еще не там
            if (direction == 'BUY' and current_sl < be_level) or (direction == 'SELL' and current_sl > be_level):
                return be_level

        # 2. Логика трейлинга (Trailing Stop)
        if profit >= trail_start:
            target = current_price - trail_step if direction == 'BUY' else current_price + trail_step
            # Двигаем стоп только в сторону прибыли
            if (direction == 'BUY' and target > current_sl) or (direction == 'SELL' and target < current_sl):
                return target

        return current_sl # Стоп остается без изменений
