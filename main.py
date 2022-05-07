import pandas as pd
from utils.drawline import drawline

# read data
df = pd.read_csv('MLLU.csv')

drawline(data=df, x_label="Percentage")