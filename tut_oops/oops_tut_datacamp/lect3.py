"""
Python OOP Example
An example of where Object-Oriented programming in Python might come in handy is our Python For Finance:
Algorithmic Trading tutorial. In it, we explain how to set up a trading strategy for a stock portfolio.
The trading strategy is based on the moving average of a stock price.
If signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:] is fulfilled,
a signal is created. This signal is a prediction for the stock's future price change.
In the code below, you'll see that there is first an initialization, followed by the moving average calculation
and signal generation. Since this is not object-oriented code, it's just one big chunk that gets executed at once.
 Notice that we're using aapl in the example, which is Apple's stock ticker.
 If you wanted to do this for a different stock, you would have to rewrite the code.
"""

import pandas as pd
import yfinance as yf
import numpy as np
aapl = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
msft = yf.download('MSFT',start='2020-01-01', end='2023-01-01')

# long_window = 100
# signals = pd.DataFrame(index=aapl.index)
# signals['signal'] = 0.0

# short_window = 40
# long_window = 100
# signals = pd.DataFrame(index=aapl.index)
# signals['signal'] = 0.0
#
# signals['short_mavg'] = aapl['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
#
# # Create long simple moving average over the long window
# signals['long_mavg'] = aapl['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
#
# # Create signals
# signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)
#
# # Generate trading orders
# signals['positions'] = signals['signal'].diff()
#
# # Print `signals`
# print(signals)

# print(type(aapl))
# print(aapl.head())
# print(aapl.count())


"""
In an object-oriented approach, you only need to write the initialization and signal generation code once.
You can then create a new object for each stock you want to calculate a strategy on, and call the generate_signals() 
method on it. Notice that the OOP code is very similar to the code above, with the addition of self
"""

class MovingAverage:
    def __init__(self, symbol, bars, short_window, long_window):
        self.symbol = symbol
        self.bars = bars
        self.short_window =short_window
        self.long_window = long_window

    def generate_signals(self):
        signals = pd.DataFrame(index=self.bars.index)
        signals['signal'] = 0.0
        signals['short_mavg'] = self.bars['Close'].rolling(window=self.short_window, min_periods=1, center=False).mean()
        signals['long_mavg'] = self.bars['Close'].rolling(window=self.long_window, min_periods=1, center=False).mean()
        signals['signal'][self.short_window :] = np.where(signals['short_mavg'][self.short_window:] > signals['long_mavg'][self.short_window:], 1.0, 0.0)
        signals['positions'] = signals['signal'].diff()
        return signals


apple = MovingAverage('aapl', aapl, 40, 100)
print(apple.generate_signals())
print(type(apple.bars))
print("------ counting of rows in pandas dataframe ------")
print(apple.bars.count())

print("------- for another stocks via same class  ---------")
microsoft = MovingAverage('msft', msft, 40, 100)
print(microsoft.generate_signals())
print(microsoft.bars.count())

