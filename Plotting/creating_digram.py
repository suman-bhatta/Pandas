import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv('data.csv')

# Plot the data
df.plot()

# Show the plot
plt.show()
