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

class StochasticOscillator:
    def __init__(self, df, n = 14):
        self.df = df
        self.n = n

    def calculate(self):
        try:
            low_min = self.df['low'].rolling(window=self.n, min_periods=1).min()
            high_max = self.df['high'].rolling(window=self.n, min_periods=1).max()
            self.df['stochastic_osc'] = ((self.df['close'] - low_min) / (high_max - low_min)) * 100
            self.df['stochastic_osc_ma'] = self.df['stochastic_osc'].rolling(window=self.n, min_periods=1).mean()
            return self.df
        except Exception as e:
            print(str(e) + 'has occurred')
            return