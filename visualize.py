import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import matplotlib
from pyecharts.charts import Line
from pyecharts import options as opts

filename1 = r"C:\Users\28634\Desktop\600505.csv"
data1 = pd.read_csv(filename1)
df1 = pd.DataFrame(data1)
df1['Date'] = df1.index
filename2 = r"C:\Users\28634\Desktop\600505predict.csv"
data2 = pd.read_csv(filename2)
df2 = pd.DataFrame(data2)
df2['Date'] = df2.index
# df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

# sns.set()
# warnings.filterwarnings('ignore')
# plt.figure(figsize=(8, 6), dpi=80, num=4)
# x = df['Date']
# y = df['Closing price']
# plt.plot(x, y, color='r', label='股票实际收盘价', linewidth=2)
# plt.show()

line = Line()
line.add_xaxis(df1.index.tolist())
# line.add_yaxis('Open', df1['Opening price'].round(2).tolist())
line.add_yaxis('Close', df1['Closing price'].round(2).tolist())
line.add_yaxis('Close_predict', df2['Closing price'])
line.set_global_opts(
    title_opts=opts.TitleOpts(title='600505'),
    tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross')
)
line.render('predict.html')
