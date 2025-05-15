import pandas as pd
from typing import Iterator
from dataset import Dataset

class ProtectedData:
  """
  Wraps the data to ensure controlled access and prevents mutation.
  """
  def __init__(self, data: pd.DataFrame):
      self._data = data.copy()

  @property
  def data(self):
      return self._data.copy()

class DataLoader:
  """
  Iterates over a Dataset object with support for MultiIndex and 2D DataFrames.
  """
  def __init__(self, dataset: Dataset, window_size: int = 1, step_size: int = 1):
    self.dataset = dataset
    self.window_size = window_size
    self.step_size = step_size

    if (dataset.is_multi_index):
      self.max_idx = len(dataset.data.index.get_level_values(dataset.time_idx).unique())
    else:
      self.max_idx = len(dataset.data.index.unique().values)

  def __iter__(self) -> Iterator[pd.DataFrame]:
    for start in range(0, self.max_idx - self.window_size + 1, self.step_size):
      end = start + self.window_size
      yield ProtectedData(self.dataset.get_data(start, end))

  def __len__(self):
    return max(0, (self.max_idx - self.window_size) // self.step_size + 1)
