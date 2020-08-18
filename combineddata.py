import pandas as pd

df1 = pd.read_excel("data_sample1.xlsx")
df2 = pd.read_excel("data_sample2.xlsx")

# df = pd.merge(df1,df2,how='left')
# print(df.head(25))

sub_df = df2[['STATE','POSTALCODE','COUNTRY','TERRITORY',"CONTACTLASTNAME",'CONTACTFIRSTNAME','DEALSIZE']]
#merged_df = pd.merge(df1,sub_df,on= '', how='outer')
pd.set_option('display.max_columns',100)
result = pd.concat([df1, sub_df], axis=1)

print(result.head())
result.to_excel('output.xlsx',index=False)
