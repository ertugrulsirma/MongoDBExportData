import pandas as pd

df = pd.read_json ('androidOutput.json')
df.to_csv ('androidOutput.csv', index = None)
