from sklearn.datasets import fetch_openml
import pandas as pd

boston = fetch_openml(name='boston', version=1, as_frame=True)
df = boston.frame

df['PRICE'] = boston.target

print("DataFrame created successfully!")

#########################################################################
# print(df.head())

#########################################################################
# print(df.describe())

########################################################################
df['PRICE_category'] = pd.cut(df['PRICE'], bins=3, labels=['Low', 'Medium', 'High'])

print(df['PRICE_category'].value_counts())

