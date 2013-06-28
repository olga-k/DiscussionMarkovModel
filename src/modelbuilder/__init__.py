# UWAGA: wersja Pythona 2.7.5
from pandas import ExcelFile
from markovchain import MarkovChain
from orderstatechainbuilder import OrderStateChainBuilder


xlsx = ExcelFile('dane.xls')
data = xlsx.parse('strona', parse_cols=[1, 7], index_col=None, na_values=['NA'])
# INFO: parse_cols=[1, 7] - numery wczytywanych kolumn; 1 to grupa, 7 to kto

# INFO: obliczenia dla markova order 1 czyli normalny markov
#map(lambda x: MarkovChain(x).stdout() , data.groupby('grupa').kto.tolist())

# INFO: obliczenia dla markova order 2 lub dowlonego innego >1, po prostu zmien order na taki ktory potrzebujesz
order = 2
map(lambda x: MarkovChain(x, order).stdout() , data.groupby('grupa').kto.tolist())



















 


















