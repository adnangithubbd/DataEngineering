import pandas as pd

data = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [90, 85, 78],
    'Science': [88, 92, 80],
    'History': [75, 89, 92]
}
df = pd.DataFrame(data)
melted_df = pd.melt(df, id_vars=['ID','Name'], value_vars=['Math', 'Science', 'History'],
                    var_name='Subject',value_name='Score')
print(df)
print('----------------------------------------------')
print(melted_df)
