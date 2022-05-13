import pandas as pd
from utils.drawline import drawline

# read data
df_EM = pd.read_csv('results/performance/Phase1-EM.csv')
df_F1 = pd.read_csv('results/performance/Phase1-F1.csv')
df_AVG = pd.read_csv('results/performance/Phase1-Avg.csv')
df_Convergence = pd.read_csv('results/convergence/csv/convergence.csv')

drawline(data=df_EM, x_label="Percentage", save_config=[
         True, "phase1-horizontal-em.png"])
drawline(data=df_F1, x_label="Percentage", save_config=[
         True, "phase1-horizontal-f1.png"])
drawline(data=df_AVG, x_label="Percentage", save_config=[
         True, "phase1-horizontal-avg.png"])

drawline(data=df_Convergence, hue="Tuning Method", do_melt=False, x_label="Steps", y_label="Average Metrics",
         save_config=[True, "phase1-convergence.png"], facet_grid_config={"col": "Data-ratio", "row": "Dataset"})
