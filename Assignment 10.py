import numpy as np
import matplotlib
matplotlib.use('Agg') # This is only required to use matplotlib on Cloud9
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("degrees-that-pay-back.csv") # df stands for Data Frame, the main data structure in Pandas
df.head() # This shows you the columns in the data and the top rows

df = df.set_index('Undergraduate Major') # Set the "Undergraduate Majors" as the index, instead of 0,1,2...