import pandas as pd

df = pd.read_csv('./data/a.csv', index_col='Country/Region')
print(df.columns) # first at 1/22/20 ; last at 3/29/21
a = []
for i, b in enumerate(df.loc['US'][(3 + 61):int(7*30.5)]):
    if not i % 5:
        print(b, end=" ")