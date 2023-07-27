import pandas as pd

df1 = pd.read_csv('./california_housing_test.csv')

print(df1['median_house_value'].max())
print(df1['median_house_value'].min())

print(df1.loc[df1['median_income'] == 3.1250, ['median_house_value']].max())

print(df1.loc[df1['median_house_value'] == df1['median_house_value'].min(), ['population']].max())
