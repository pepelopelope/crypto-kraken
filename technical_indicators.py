class Moving_Average:

    def __init__(self, slot, df):
        self.slot = slot
        self.df = df

    def calculate(self):
        try:
            self.df['moving_average_{}'.format(self.slot)] = self.df['close'].rolling(window=int(self.slot),
                                                                                        min_periods=1).mean()
            return self.df

        except Exception as e:
            print(str(e) + 'has occurred')
            return

class RSI:

    def __init__(self, df):
        self.df = df

    def calculate(self):
        try:
            self.df['diff'] = self.df.close - self.df.open
            self.df['up'] = self.df['diff'][self.df['diff'] > 0]
            self.df['down'] = abs(self.df['diff'][self.df['diff'] <= 0])
            self.df.fillna(value=0, inplace=True)

            self.df['media_up'] = self.df['up'].rolling(window=14).mean()
            self.df['media_down'] = self.df['down'].rolling(window=14).mean()
            self.df['RSI'] = 100 - (100 / (1 + (self.df.media_up / self.df.media_down)))
            self.df.dropna(inplace=True)

            return self.df

        except Exception as e:
            print(str(e) + 'has occurred')
            return

class StochasticOscillator:
    def __init__(self, df, n = 14):
        self.df = df
        self.n = n

    def calculate(self):
        try:
            low_min = self.df['low'].rolling(window=self.n, min_periods=1).min()
            high_max = self.df['high'].rolling(window=self.n, min_periods=1).max()
            self.df['stochastic_osc'] = ((self.df['close'] - low_min) / (high_max - low_min)) * 100
            return self.df
        except Exception as e:
            print(str(e) + 'has occurred')
            return