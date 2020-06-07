import pandas as pd

print("""
İbrahim Halil Bayat
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 

Adjusted Gross Income (AGI) Estimation
""")

df = pd.read_csv("agi.csv")

df = df.loc[(df['zipcode'] != 0) & (df['zipcode'] != 99999), ['STATE', 'zipcode', 'agi_stub', 'N1']]

medians = {1: 12500, 2: 37500, 3: 62500, 4: 87500, 5: 112500, 6: 212500}
df['agi_stub'] = df.agi_stub.map(medians)


groups = df.groupby(by='zipcode')

df = pd.DataFrame(groups.apply(lambda x: sum(x['N1']*x['agi_stub'])/sum(x['N1']))).reset_index()

df.columns = ['zipcode', 'agi_estimate']

print(df.head())

print("--------- Check if is is correct ------------")

print(df[df['zipcode'] == 63017])

