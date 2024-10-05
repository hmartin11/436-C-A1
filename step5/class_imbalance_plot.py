import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# load the dataset
df = pd.read_excel("https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls", skiprows=1)

# rename column to get rid of spaces
df.rename(columns = {"default payment next month":"default.payment.next.month"}, inplace = True)

# Plot class imbalance 
plt.figure(figsize=(6,4))

default_plot = sns.countplot(x = "default.payment.next.month",data = df)
plt.ylim(0,25000)
total = float(len(df))
for p in default_plot.patches:
    default_plot.annotate((str(100* p.get_height()/total) + "%"), (p.get_x()+0.32, p.get_height()+1000), ha="center")


plt.show()
plt.savefig("imbalance_plot.png")