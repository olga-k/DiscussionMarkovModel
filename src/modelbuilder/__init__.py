# Python version 2.7.5
from pandas import ExcelFile
from markovchain import MarkovChain
from orderstatechainbuilder import OrderStateChainBuilder


xlsx = ExcelFile('dane.xls')
data = xlsx.parse('strona', parse_cols=[1, 7], index_col=None, na_values=['NA'])

order = 2
map(lambda x: MarkovChain(x, order).stdout() , data.groupby('grupa').kto.tolist())



















 


















