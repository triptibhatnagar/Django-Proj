# Q29. 29. Build a CLI program to load a dataset, describe it, and plot.
import pandas as pd
import matplotlib.pyplot as plt
def describe_and_plot(file):
    df = pd.read_csv(file)
    print(df.describe()) # Ye numerical columns ka summary statistics calculate karta hai.
    df.hist()
    plt.show()
describe_and_plot('data.csv')