import pandas as pd

data = pd.read_csv("nba.csv")
data.dropna(inplace=True)


result = data.columns

# data["Name"] = data["Name"].str.upper()
# data["Name"] = data["Name"].str.lower()
# data["index"] = data["Name"].str.find('a')
# data = data[data.Name.str.contains("Jordan")]
# data = data.Team.str.replace(" ","-").str.replace("*","")
data[["FirstName","LastName"]] = data["Name"].loc[data['Name'].str.split(" ").str.len()==2].str.split(expand=True)


print(result)
print(data.head())