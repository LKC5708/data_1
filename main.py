import pandas as pd
import matplotlib
header = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = pd.read_csv('./data/1_pima.csv', names=header)
(data.describe().to_csv('./result/describe.csv'))
data.hist(figsize=(10,10), bins=5)
plt.show()