import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# ------------------------------
# 1. DATA CLEANING & WRANGLING
# ------------------------------

def clean_data(file_path):
    df = pd.read_excel(file_path)
    
    # Fill missing values
    df['Customer ID'].fillna(method='ffill', inplace=True)
    df['Email'].fillna('unknown@email.com', inplace=True)
    df['Name'].fillna('unknown', inplace=True)
    df['Purchase Amount'].fillna(df['Purchase Amount'].mean(), inplace=True)

    
    # Standardize date format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Convert Purchase Amount to numeric
    df['Purchase Amount'] = df['Purchase Amount'].replace({'\$': '', ',': ''}, regex=True).astype(float)
    
    return df
