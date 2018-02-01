## BITCOIN-PRICE-PREDICTION-USING-SENTIMENT-ANALYSIS ##
### Team: 201712-5 ###
### Members: ###
##### Chandra S Narain Kappera - ck2840 #####
##### Venkata Sai Sriharsha Sammeta - vs2626 #####
##### Ketan M Mehta - kmm2304 #####


##### Usage Details: #####
The entire setup works on Google cloud.

##### Part 1: Data Gathering: #####
In order to capture the real-time data, we run the following two python programs in background to continuously fetch the data. 
a) Continuous_Stream_Data.py 
b) Continuous_Stream_Sentiment.py

The two code do the preprocessing of data and store them in “live_tweet.csv” and “live_bitcoin.csv” files.

##### Part 2: Core Engine: #####
From the experiments we found LSTM based model to be performing better than ARIMA (discussed in detail in next section). We have set our best model parameters in engine.py file and once it is run it gathers data from the “live_bitcoin.csv” and “live_tweet.csv”, and generate features in real-time and is fed into the model.

The model outputs the next price. It also does a computation based on the threshold set in the code (this is fed from the settings file). 

The information about the time stamp, predicted price, current real price and buy/sell decision is then written into a mysql database


##### Part 3: Tableau and Notification system: #####

We have used Tableau to generate plots in real-time form the sql-database mentioned in previous section. 
