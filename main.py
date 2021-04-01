import pandas as pd

df = pd.read_csv('./data/a.csv', index_col='Country/Region')
# print(df.columns)  first at 1/22/20 ; last at 3/29/21 start at apr 4, at start=87
a = []
def printData(country, start=86, end=87, sep=5):
    iout = ''
    bout = ''
    for i, b in enumerate(df.loc[country][start:-end]):
        if not i % sep:
            iout += f' {i}'
    for i, b in enumerate(df.loc[country][start:-end]):
        print(i, b)
        if not i % sep:
            bout += f' {b}'
    with open('./out/out.txt', 'a') as f:
        f.write(f'{country}\n{iout}\n{bout}\n')

def getDifferenciatedList(l):
    newlist = []
    for k, i in enumerate(l):
        if k == 0:
            newlist.append(0)
        else:
            newlist.append(i - l[k - 1])
    return newlist

def getNewCases(country, start=86, end=87, sep=1):
    iout = ''
    bout = ''
    for i, b in enumerate(getDifferenciatedList(df.loc[country])[start:-end]):
        if not i % sep:
            iout += f' {i}'
            bout += f' {b}'
    with open('./out/new.txt', 'a') as f:
        f.write(f'\n{country}\n{iout}\n{bout}')


printData('Singapore', sep=1)
printData('US', sep=1)
printData('Taiwan*', sep=1)
getNewCases('Singapore')
getNewCases('US')
getNewCases('Taiwan*')

