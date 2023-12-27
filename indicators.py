import pandas as pd

class MovingAverageCalculator:
    def __init__(self, df):
        self.df = df

    def calculate(self, slot):
        try:
            self.df['moving_average_{}'.format(slot)] = self.df['close'].rolling(window=int(slot), min_periods=1).mean()
            return self.df

        except Exception as e:
            print(str(e) + ' has occurred')
            return self.df

class RSICalculator:
    def __init__(self, df):
        self.df = df

    def calculate(self):
        try:
            self.df['diff'] = self.df['close'] - self.df['open']
            self.df['up'] = self.df['diff'][self.df['diff'] > 0]
            self.df['down'] = abs(self.df['diff'][self.df['diff'] <= 0])
            self.df.fillna(value=0, inplace=True)

            self.df['media_up'] = self.df['up'].rolling(window=14).mean()
            self.df['media_down'] = self.df['down'].rolling(window=14).mean()
            self.df['RSI'] = 100 - (100 / (1 + (self.df['media_up'] / self.df['media_down'])))
            self.df.dropna(inplace=True)

            return self.df

        except Exception as e:
            print(str(e) + ' has occurred')
            return self.df