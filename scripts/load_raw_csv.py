import os
import pandas as pd

def load_raw_csv(DATA_DIR=os.path.join(os.path.dirname(os.path.dirname(__file__)),"data"), train_or_test="train.csv"):
  """ 
  Load dataset from csv.
  Input: 
    DATA_DIR: 
    train_or_test: str
  Output: pandas DataFrame
  """
  # This requires the data to be stored in a directory at the same level as 
  # the directory which contains this file (i.e. root/scripts & root/data
  #
  # Kaggle competition is setup with code environment starting in 
  # '/kaggle/working/' directory
  # while the data is contained in 
  # '/kaggle/input/house-prices-advanced-regression-techniques/' directory
  #
  # Hopefully this change can be applied directly into a kaggle notebook and the inputs can be adjusted accordingly
  
  output_df = pd.read_csv(os.path.join(DATA_DIR, train_or_test))
  return output_df
