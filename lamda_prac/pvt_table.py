import pandas as pd

data = {"A": ["foo", "foo", "foo", "foo", "foo",
              "bar", "bar", "bar", "bar"],
        "B": ["one", "one", "one", "two", "two",
              "one", "one", "two", "two"],
        "C": ["small", "large", "large", "small",
              "small", "large", "small", "small",
              "large"],
        "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
        "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]}
df = pd.DataFrame(data)

pivot_table=pd.pivot_table(df, values='D', index=['A', 'B'],columns=['C'],aggfunc='sum')
print(pivot_table)


##############
data = {
    'Date': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02', '2022-01-01', '2022-02-02'],
    'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [10, 15, 20, 25, 12, 18]
}

sales_df = pd.DataFrame(data)
products = sales_df['Date'].unique()

sales_pivot=pd.pivot_table(sales_df,values='Sales',index='Date',columns='Product',aggfunc='sum')
print(sales_pivot)

