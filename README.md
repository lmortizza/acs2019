# ACS 2019 Maine Data (block group level)

Goal: Create postgress database table with State data at the block level using the most recent American Community Survey (ACS). 


## Downloading ACS data

The ACS_data file uses the census.gov API (and the requests package) to pull data for the state of Maine at the block group level. There was a census package available that would have made this process easier, but I opted for this process to practice using a website's API directly (the only other time I had done this was in my intermediate python course last year). By using this method, I pulled the data for the following variables:

* B01003_001E: total population 
* B02001_002E: total population: White Alone
* B19101_001E: family income in the past 12 months (in 2019 inflation adjusted dollars) 
* B08134_008E: travel time to work: 35 to 44 minutes
* B08134_009E: travel time to work: 45 to 60 minutes
* B08134_010E: travel time to work: 60 or more minutes
* B08301_002E: means of transportation: Car, truck, or van
* B19049_001E: median household income in the past 12 months (in 2019 inflation adjusted dollars)
* state
* county
* tract
* block group


The state of Maine was chosen because it is the state where I grew up, it's where I call home. Total population was chosen as a general variable that always tends to be important and highlighted. Variables related to income (B19101_001E and B19049_001E) were selected because at the block level it can often be an indicator for the number of resources available. Additionally, certain counties tend to suffer with poverty. Thus, exploring income at a more granular level would be interesting. Lastly, the variables related to transportation are simply for interest purposes. Being that most of Maine is pretty rural, I wondered how common it is to travel for more than 35 minutes (essentially cross town/city lines). Lastly, the mode of transportation was intriguing. I would hypothesize that this would be the most common means of transportation due to the limited public transportation. 

Once the data was successfully pulled, I created a dataframe. I then changed the variable names to be more clear. I also created a key that would serve as the primary key when loading the data into database table. I then created a nested list, where each list contained row information (making it easier to add the data to the database table in later steps). 

## Creating Table and Loading Data

In a new script (databaseLoad), I called data (nested lists) from the ACS_Data file. I change the data type from objects to strings. Next, I changed the first 7 variables into integers. The data was now ready to be added to the database table. Thus, I proceeded to connect to the database using the psycopg2 package. Once connected, I created the table mortizza_acs_data with the CREATE command and specifying variable names and types. I then used the executemany to insert the values from the nested list. I finalized the command by committing and closing connection. 


