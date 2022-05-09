import pandas as pd
import string

def clean(df, col=None):

    """
    Trim whitespace from ends of each value across all series in dataframe
    """
    #
    # trim_strings = lambda x: x.replace('[','') if isinstance(x, list) else x
    # # trim_strings = lambda x: x.replace(']', '') if isinstance(x, list) else x
    # # trim_strings = lambda x: x.lstrip("'") if isinstance(x, list) else x
    # # trim_strings = lambda x: x.rstrip("'") if isinstance(x, list) else x

    for i in df.columns:
        if i in col:
            df[i] = df[i].map(lambda x: x.replace('[', ''))
            df[i] = df[i].map(lambda x: x.replace(']', ''))
            df[i] = df[i].str.lstrip("'")
            df[i] = df[i].str.rstrip("'")

            df[i] = df[i].str.translate(str.maketrans('', '', string.punctuation))
            df[i] = df[i].str.lower()


    return df
        # df.applymap(trim_strings)


col = ['artists','name']
df = pd.read_csv('spotify.csv')
print(clean(df,col))