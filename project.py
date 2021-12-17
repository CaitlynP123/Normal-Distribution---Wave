import plotly.figure_factory as pf
import pandas as pd

data = pd.read_csv('C:/Users/C/OneDrive/Desktop/Coding/python/Normal Distribution/data.csv')

figure = pf.create_distplot([data['Avg Rating'].tolist()],['Mobile Brand Rating'])
figure.show()