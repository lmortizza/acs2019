
#import packages 
import pandas as pd
import requests




#````````PULLILNG ACS DATA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#host url 
host_url = "https://api.census.gov/data"


#dataset criteria 
year = "2019"
dataset = "acs/acs5"
base_url = "/".join([host_url, year, dataset])


#filtering criteria  (variables & State)

# TOTAL POPULATION
# Estimate!!Total:!!White alone
# FAMILY INCOME IN THE PAST 12 MONTHS (IN 2019 INFLATION-ADJUSTED DOLLARS)
# MEANS OF TRANSPORTATION TO WORK BY TRAVEL TIME TO WORK :Estimate!!Total:!!35 to 44 minutes
# MEANS OF TRANSPORTATION TO WORK BY TRAVEL TIME TO WORK :Estimate!!Total:!!45 to 59 minutes
# MEANS OF TRANSPORTATION TO WORK BY TRAVEL TIME TO WORK :Estimate!!Total:!!60 or more minutes
# MEANS OF TRANSPORTATION TO WORK
# Estimate!!Median household income in the past 12 months (in 2019 inflation-adjusted dollars) --!!Total:
get_vars = "B01003_001E,B02001_002E,B19101_001E,B08134_008E,B08134_009E,B08134_010E,B08301_002E,B19049_001E"

#select State (Maine)
state="23"

#full url w/specifications
url = base_url+'?get='+get_vars+'&for='+"block%20group:*&in=state:"+state+"&in=county:*&in=tract:*"


#pull down data
r = requests.get(url)

#begin creating dataframe
col_names = r.json()[0] #pull column names
df=pd.DataFrame(columns =col_names, data = r.json()[1:]) #create df

df.columns = ['totalpop', 'whitepop', 'income12months',
              'transport3544', 'transport4559', 
              'transport60more', 'transpmode','medianincome', 'state', 'county', 'tract', 'blockgroup'] #rename column names

df['key'] =df['county']+ df['tract']+df['blockgroup'] #create unique key

any(df['key'].duplicated()) #check if there are any duplicates


#changing variable types

# for var in df.columns:
#     df[var] = df[var].astype(str).astype(int)


#creating a tuple that contains lists of row data
records = df.to_records(index=False)
data = list(records)

#df.dtypes
#df['totalpop'].astype(str).astype(int)