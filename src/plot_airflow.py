import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./output/airflow_jira_bugs.csv')

df.plot.scatter(x = 'version', y = 'count')

plt.savefig('./output/airflow_jira_bugs.png')