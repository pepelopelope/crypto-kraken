# Definir la clase Moving_Average
class Moving_Average:

    # Constructor de la clase
    def __init__(self, slot, df):
        self.slot = slot  # Número de períodos para la media móvil
        self.df = df      # DataFrame con los datos de precios

    # Método para calcular la media móvil
    def calculate(self):
        try:
            # Calcular la media móvil y añadirla al DataFrame
            # 'rolling' crea un objeto que permite calcular estadísticas móviles
            self.df['moving_average_{}'.format(self.slot)] = self.df['close'].rolling(window=int(self.slot),
                                                                                      min_periods=1).mean()
            # Devolver el DataFrame actualizado
            return self.df

        # Capturar y manejar excepciones
        except Exception as e:
            print(str(e) + 'has occurred')
            return

# Definir la clase StochasticOscillator
class StochasticOscillator:
    # Constructor de la clase
    def __init__(self, df, n=14):
        self.df = df  # DataFrame con los datos de precios
        self.n = n    # Número de períodos para el cálculo del oscilador

    # Método para calcular el oscilador estocástico
    def calculate(self):
        try:
            # Calcular el mínimo y máximo de los precios en el período 'n'
            low_min = self.df['low'].rolling(window=self.n, min_periods=1).min()
            high_max = self.df['high'].rolling(window=self.n, min_periods=1).max()

            # Calcular el oscilador estocástico y añadirlo al DataFrame
            self.df['stochastic_osc'] = ((self.df['close'] - low_min) / (high_max - low_min)) * 100

            # Calcular la media móvil del oscilador estocástico y añadirla al DataFrame
            self.df['stochastic_osc_ma'] = self.df['stochastic_osc'].rolling(window=self.n, min_periods=1).mean()

            # Devolver el DataFrame actualizado
            return self.df

        # Capturar y manejar excepciones
        except Exception as e:
            print(str(e) + 'has occurred')
            return
