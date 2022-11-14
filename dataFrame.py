import pandas as pd
# converting tuple to Series
h = ('AA', '2012-02-01', 100, 10.2)
s = pd.Series(h)
print(type(s))
print(s)


# converting dict to Series
d = {'name' : 'IBM', 'date' : '2010-09-08', 'shares' : 100, 'price' : 10.2}

ds = pd.Series(d)
print(ds)




data  = {
    "name": ["AAA", "IBMs", "GOOGLEs", "TATA"],
    "date": ["2002-12-10", "2002-12-11", "2002-12-11","2002-12-11"],
    "Address":["2002-12-10", "2002-12-11", "2002-12-11","2002-12-11"],

    }
data1  = {
    "name": ["AA", "IBM", "GOOGLE", "Apple"],
    "date": ["2002-12-10", "2002-12-11", "2002-12-11", "2002-12-11"]}

# df = pd.DataFrame(data) 
# print("++Current DataFrame++")   
# print(df)
# print("++ Add Extra column 'Price' into current dataframe+++")
# df['price'] = 2000
# print(df)
# df.index = ("one", "two", "three")

# print(df)
# df =df.set_index('name')
# print(df)

print("++ data access++")

df1 = pd.DataFrame(data, [i for i in range(len(data['name']))])
df2 = pd.DataFrame(data1, [i+len(data['name']) for i in range(len(data1['name']))])
frame = [df1, df2]
resp = pd.concat(frame, axis=1, join='inner')
print(resp)



