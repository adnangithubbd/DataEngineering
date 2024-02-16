import pandas as pd

twice = lambda x: x * 2
range_func = lambda x: x.max() - x.min()

df = pd.DataFrame({'A': [1, 2, 3], 'B': [6, 7, 9]})

# Apply the 'twice' function to column 'B'
# df = df.apply(twice)

# Apply the 'range' function to each column
result = df.apply(range_func)

# Print the DataFrame and the result
# print(df)
# print(result)
numbers = [1, 2, 3, 4, 5]
mean_res = sum(numbers) / len(numbers)
print(mean_res)
another = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
mn = lambda x: x.mean()
res = df.apply(mn)

#########
df2 = pd.DataFrame({'A': [1, 2, None], 'B': [None, 5, 6]})

# df2.fillna(0, inplace=True)
replace_missing = lambda x, value: x.fillna(value)
#######comu demo
comuDf = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
cumsum = lambda x: x.cumsum()
res = comuDf.apply(cumsum)

max_val = lambda x: x.max()
res2 = comuDf.apply(max_val)
 