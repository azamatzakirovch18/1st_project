import pandas as pd

df = pd.read_csv('6.csv')
def clean():
    df.drop(['Unnamed: 0','Unnamed: 0.1','track_id'], axis=1, inplace=True)
    floats = []
    objects = []
    columns = df.columns

    for i in columns:
        if df[i].dtype == 'object':
            objects.append(i)
        else:
            floats.append(i)
    for i in floats:
        mean = df[i].mean()
        df[i] = df[i].fillna(mean)
    for i in objects:
        mode = df[i].mode()[0]
        df[i] = df[i].fillna(mode)

    return df
#