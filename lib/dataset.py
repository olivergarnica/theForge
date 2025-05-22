import pandas as pd
from typing import Optional

class Dataset:
  """
  Requires:
    - At least one index to be called time_idx.
    - If multiple features per asset, each feature must be a column, and there must
      be an additional index called asset_idx. Otherwise each asset must be a column.
  """
  time_idx: str

  def __init__(self, data: pd.DataFrame, asset_idx: Optional[str], time_idx: str = 'datetime'):
    self.data = data
    self.time_idx = time_idx

    self.is_multi_index = asset_idx is not None
    if (self.is_multi_index):
      self.asset_idx = asset_idx

    self.data = self.data.sort_index()

  def get_data(self, start_idx, end_idx):
    """
    Return a slice (window) of the data from start_idx to end_idx.
    Assumes data is sorted by index and MultiIndex is set with time and asset.
    """

    unique_values = self.data.index.get_level_values(self.time_idx).unique()
    start_value = unique_values[start_idx]
    end_value = unique_values[end_idx - 1]

    if self.is_multi_index:
        return self.data.loc[
            self.data.index.get_level_values(self.time_idx).to_series().between(start_value, end_value)
        ]

    return self.data.iloc[start_idx:end_idx]
