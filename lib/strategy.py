from dataset import Dataset
from datetime import datetime
import pandas as pd

class StrategyModule:
    def __init__(self,
                 prices: pd.DataFrame,
                 data: Dataset,
                 iter_window: int,
                 start_time: datetime,
                 end_time: datetime,
                 **kwargs):
        self.prices = prices
        self.data = data
        self._data = data
        self.iter_window = iter_window
        self.start_time = start_time
        self.end_time = end_time

        for key, val in kwargs.items():
            setattr(self, key, val);

    def x():
