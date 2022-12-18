#import matplotlib
import pandas as pd
import numpy as np
import matplotlib

TEC = 'Total Electricity Consumption.xlsx' # Total Electricity Consumption
TEC_W = 'Total energy consumption_World.xlsx' # Total energy consumption_World

TEC_df = pd.read_excel(TEC)
TEC_W_df = pd.read_excel(TEC_W)

print(TEC_df)