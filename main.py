import pandas as pd
from utils.drawline import drawline

# read data
df_EM = pd.read_csv('Phase1-EM.csv')
df_F1 = pd.read_csv('Phase1-F1.csv')
df_AVG = pd.read_csv('Phase1-Avg.csv')

drawline(data=df_EM, x_label="Percentage", save_config=[True, "phase1-horizontal-em.png"])
drawline(data=df_F1, x_label="Percentage", save_config=[True, "phase1-horizontal-f1.png"])
drawline(data=df_AVG, x_label="Percentage", save_config=[True, "phase1-horizontal-avg.png"])