# Purdue-Algo-Trading

Initially grabs all tickers in the stock market.
Unfortunately it returns all the results in a dictionary
inside the dictionary returned. So for each row in the
dataframe, I took that result and added it to another
Dataframe.

#### Next Steps:
I should be able to loop through each ticker, use
the api to grab whatever piece of data I want and add
that to another dataframe. From there I'll have to
decide how to sort and present the data.