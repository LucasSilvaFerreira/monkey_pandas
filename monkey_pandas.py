import re
import pandas as pd

def filter_columns(self, substring='', inplace=False, remove_substring=None):
    '''Return column names filtered by a substring or filter the DataFrame itself.

    Parameters:
    -----------
    substring : str or list of str
        The substrings to filter column names by.
    inplace : bool, default False
        If True, filter the DataFrame in place and return the filtered DataFrame.
        If False, return the filtered column names.
    remove_substring : str or list of str, default None
        Substrings to exclude columns by.

    Returns:
    --------
    list or DataFrame:
        Depending on `inplace`, either a list of column names or a filtered DataFrame.
    '''
    substring_list = [substring] if type(substring) == str else substring
    if remove_substring==None:
      remove_substring_list = []
    else:
        remove_substring_list = [remove_substring] if type(remove_substring) == str else remove_substring

    #print(remove_substring_list)

    columns_detected = [x for  x  in self.columns if any(map(x.__contains__, substring_list))   and not any(map(x.__contains__, remove_substring_list))]

    if inplace:
      return self[columns_detected]
    else:
      return columns_detected

def cols_to_dict(self, key_col, values_col):
  return dict(zip(self[key_col].values, self[values_col].values ))

def patching_pandas():
  # Import the smiling face emoji
  print ("!!!🐒PATHICHING PANDAS WITH NEW FUNCTIONS🐒!!!")
  pd.DataFrame.filter_columns =  filter_columns
  pd.DataFrame.cols_to_dict =  cols_to_dict



patching_pandas()
