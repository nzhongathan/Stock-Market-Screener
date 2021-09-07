!pip install yfinance
import numpy as np
import pandas as pd
import yfinance as yf

sp100 = ['AAPL','ABBV','ABT','ACN','ADBE','AIG','ALL','AMGN','AMT','AMZN','AXP','BA','BAC','BIIB','BK','BKNG','BLK','C','CAT','CHTR','CL','CMCSA','COF','COP','COST','CRM',
        'CSCO','CVS','CVX','DD','DHR','DIS','DOW','DUK','EMR','EXC','F','FB','FDX','GD','GE','GILD','GM','GOOG','GOOGL','GS','HD','HON','IBM','INTC','JNJ','JPM','KHC','KMI',
        'KO','LLY','LMT','LOW','MA','MCD','MDLZ','MDT','MET','MMM','MO','MRK','MS','MSFT','NEE','NFLX','NKE','NVDA','ORCL','PEP','PFE','PG','PM','PYPL','QCOM','RTX','SBUX',
        'SLB','SO','SPG','T','TGT','TMO','TSLA','TXN','UNH','UNP','UPS','USB','V','VZ','WBA','WFC','WMT','XOM']


def test_cases (close, low, close1, low1):
    if (low1 > close):
        return 0
    elif (close < close1):
        if (low1 < close):
            #print ("YES1")
            return 1
    elif (close1 <= close and close1 > low):
        if (low1 < close):
            #print("YES")
            return 1
    return 2

for s in sp100:
    stock = yf.Ticker(s)
    df = stock.history(period='1d',start='2021-6-28',end='2021-7-28')
    df = df.drop(columns=['Volume','Dividends','Stock Splits'])
    
    color = []
    for i in range (0,len(df)):
        if (df.Open[i] > df.Close[i]):
            color.append('red')
        else:
            color.append('green')
    
    df['color'] = color
    
    pullbacks = []
    close = []
    low = []
    for i in range (2, len(df)):
        if df.color[i] == 'green':
            if df.color[i-1]=='red' and df.color[i-2] == 'red':
                pullbacks.append(i)
                close.append(df.Open[i])
                low.append(df.Low[i])
    
    ok = -1
    for i in range (0,len(pullbacks)):
        second_test = False
        final = True
        idx = -1
        for j in range (pullbacks[i]+1, len(df)):
            if (df.color[j]=='green'):
                continue
            ok = test_cases(close[i],low[i],df.Close[j], df.Low[j])
            if ok == 2:
                break;
            if ok == 1:
                second_test = True
                idx = j
                break;
        if second_test == True:
            for a in range (j, len(df)):
                if df.color[a] == 'green' and a != len(df)-1:
                    final = False
                    break
                if df.color[a] == 'red':
                    ok = test_cases (close[i], low[i], df.Close[a], df.Low[a])
                    #print(j)
                    #print (ok)
                    if ok == 2:
                        final = False
                        break;
        #print('------')
        if final == True and second_test == True:
            print (s + ": Buy")
            break

