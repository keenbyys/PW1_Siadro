import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

boston = fetch_openml(name='boston', version=1, as_frame=True)
df = boston.frame

# # 5.1.
# numeric_df = df.select_dtypes(include=['float64', 'int64'])
# means = np.mean(numeric_df, axis=0)
# print("Mean values for each attribute:")
# print(means)

# # 5.2.
# plt.figure(figsize=(15, 10))
# for i, column in enumerate(df.columns, 1):
#     plt.subplot(4, 4, i)
#     plt.hist(df[column], bins=30, edgecolor='black')
#     plt.title(column)
#     plt.xlabel(column)
#     plt.ylabel('Frequency')
# plt.tight_layout()
# plt.show()
#
# # 5.3.
# plt.figure(figsize=(15, 10))
# df.boxplot()
# plt.xticks(rotation=45)
# plt.title('Box Plots for All Attributes')
# plt.tight_layout()
# plt.show()
#
# # 5.4.
# df['PRICE_category'] = pd.cut(df['MEDV'], bins=3, labels=['Low', 'Medium', 'High'])
#
# for column in df.columns[:-1]:
#     plt.figure(figsize=(8, 5))
#     for category in df['PRICE_category'].unique():
#         subset = df[df['PRICE_category'] == category]
#         plt.hist(subset[column], bins=30, alpha=0.5, label=category, edgecolor='black')
#     plt.title(f'Distribution of {column} by Price Category')
#     plt.xlabel(column)
#     plt.ylabel('Frequency')
#     plt.legend()
#     plt.show()
#
# 5.5.
correlation_matrix = df.corr()
print("Correlation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(10, 8))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(np.arange(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(np.arange(len(correlation_matrix.index)), correlation_matrix.index)
plt.title('Correlation Matrix Heatmap')
plt.tight_layout()
plt.show()