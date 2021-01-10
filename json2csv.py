import json
import pandas as pd
import numpy as np



#if you are going to import a json file from your computer, Address your Json File Path to Python and convert it to dictionary first
with open("your file path") as json_file:
     a = json.load(json_file)

# # Sample Dict :
# a = {'a' : [1,2,3,4,5,6],
# 'b' : [7,8,9],
# 'c' : [10,11],
# 'd' : [11,22],
# 'e' : [12,45,23]
# }


#Convert your dictionary file to a pandas dataframe
df = pd.DataFrame.from_dict(a, orient='index').transpose()

#Generate a column names for the csv file you will generate (if there is more than 2 columns than add more)
column_names = ['a' ,'b']
df2 = pd.DataFrame(columns = column_names)

#Add each
c= 0
for i in range(0, len(df.columns)):
    column = df.columns[i]
    for k in range(0, len(df.index)):
          c += 1
          if np.isnan(df[column][k]):
              c-1
          else:
               df2.loc[c] = [column] + [df[column][k]]

# in the end your Dataframe will look alike:
#     a     b
# 1   a   1.0
# 2   a   2.0
# 3   a   3.0
# 4   a   4.0
# 5   a   5.0
# 6   a   6.0
# 7   b   7.0
# 8   b   8.0
# 9   b   9.0
# 13  c  10.0
# 14  c  11.0
# 19  d  11.0
# 20  d  22.0
# 25  e  12.0
# 26  e  45.0
# 27  e  23.0

# print(df2)
df2.to_csv("json2csv.csv")

