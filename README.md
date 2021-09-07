# Stock Market Screener
<p>
  <img width = 800 height = 450 src ="https://mediacloud.kiplinger.com/image/private/s--x2_BoIgn--/v1604352227/Investing/stock-market-today-110220.jpg">
    </p>
  
Used to monitor stock price data in order to identify pullbacks in stock prices and find the days where indications of good buy-ins would be with rising stock prices. I modeled the strategies from [this youtube video](https://www.youtube.com/watch?v=KO7lX7-Fi7U&t=1030s&ab_channel=TheTradingChannel) where pullbacks are identified and then rising prices indicate a possible buy in option. When possible buy ins are identified, they are printed out for me to analyze and possibly buy into. 

Tools/packages used include:
- Pandas
- NumPy
- yFinanace

The data is imported into the program in one month segments at a time where I first attribute each day to either a green day (Closing price is greater than opening price) or a red day (Closing price is lower than opening price). 
<p>
  <img width = 400 height = 200 src = "https://bpcdn.co/images/2020/04/18151947/Heikin-Ashi-traditional-GBPJPY-daily-chart-example.png">
  </p>

Then the program iterates througout the data in order to identify pullbacks, which are identified as two consecutive red days followed by a green day. The green day shows the possible end to the pullback and a possible rising trend in the stock prices - but not certain for sure. The second red candlestick is then used to create a range using the low price and the closing price. Following days stock prices must reenter the range with either the opening or closing price, but the opening or closing price must not cross below the range. If it crosses below the range, then the strategy is terminated. If it doesn't, then the stock is considered "retested" and the next green day hints at the start of rising stock prices for certain. 

Stocks which fulfill the retest and have 1 or 2 green days in a row are printed out. Anything more isn't because the optimal buy in day would've passed already. The stocks that are printed out show which ones I should carefully watch to possibly invest in.

![Screenshot (14)](https://user-images.githubusercontent.com/69808907/132273910-70f811b3-9b41-4ff0-b8f8-61cfa3ca252d.png)
