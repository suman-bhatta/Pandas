import pandas as pd
import matplotlib.pyplot as plt

try:
	df = pd.read_csv('data.csv')
except FileNotFoundError:
	print("The file 'data.csv' was not found.")
	exit()

if 'Duration' not in df.columns or 'Maxpulse' not in df.columns:
	print("The required columns 'Duration' and 'Maxpulse' are not in the CSV file.")
	exit()

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()