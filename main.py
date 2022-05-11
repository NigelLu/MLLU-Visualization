import pandas as pd
from utils.drawline import drawline

# read data
df = pd.read_csv('Phase1.csv')

drawline(data=df, x_label="Percentage", save_config=[True, "./test3.png"])