"""
TradingMath: Lightweight utility library for algorithmic trading.
No dependencies, pure Python.
"""
import math
from typing import List, Tuple

def calculate_linear_regression(prices: List[float], period: int = 9) -> Tuple[float, float]:
    """
    Calculates slope and predicted next price using linear regression.
    Returns: (slope, predicted_price)
    """
    if len(prices) < period:
        return 0.0, prices[-1] if prices else 0.0
    
    y = prices[-period:]
    x = list(range(period))
    n = period
    
    sum_x, sum_y = sum(x), sum(y)
    sum_xy = sum(i * j for i, j in zip(x, y))
    sum_xx = sum(i * i for i in x)
    
    denominator = (n * sum_xx - sum_x**2)
    if denominator == 0:
        return 0.0, y[-1]
    
    slope = (n * sum_xy - sum_x * sum_y) / denominator
    intercept = (sum_y - slope * sum_x) / n
    
    predicted_price = slope * (n + 1) + intercept
    return slope, predicted_price

def calculate_ema(data: List[float], span: int) -> float:
    """Calculates the last EMA value for a given span."""
    alpha = 2.0 / (span + 1.0)
    ema = data[0]
    for val in data[1:]:
        ema = val * alpha + ema * (1.0 - alpha)
    return ema

def calculate_std(data: List[float], ddof: int = 1) -> float:
    """Calculates Standard Deviation."""
    n = len(data)
    if n <= ddof: return 0.0
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - ddof)
    return math.sqrt(variance)