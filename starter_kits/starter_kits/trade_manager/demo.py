from trade_manager import TradeManager

# 1. Инициализация менеджера
# Мы задаем минимальный стоп-лосс, который будет использоваться
manager = TradeManager(fallback_sl=12.0)

# 2. Имитация сделки
atr = 1.5
entry = 1850.0
curr_sl = 1838.0  # Твой текущий стоп-лосс

# Симуляция изменения цены
current_price = 1855.0 

# Рассчитываем, нужно ли нам подвинуть стоп
new_sl = manager.calculate_stop_adjustment(
    current_price=current_price,
    entry_price=entry,
    curr_sl=curr_sl,
    direction="BUY",
    atr=atr,
    be_trigger=2.0,   # Порог для перехода в безубыток
    trail_start=3.0,  # Порог для старта трейлинга
    trail_step=0.5    # Шаг трейлинга
)

print(f"Текущая цена: {current_price}")
print(f"Новый уровень стоп-лосса: {new_sl}")
