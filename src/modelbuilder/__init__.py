# Python version 2.7.5
from pandas import ExcelFile
from markovchain import MarkovChain
from orderstatemapper import OrderStateMapper
from equalordermarkovmatrixcomparator import EqualOrderMarkovMatrixComparator


xlsx = ExcelFile('dane.xls')
data = xlsx.parse('strona', parse_cols=[1, 7], index_col=None, na_values=['NA'])

#order = 2
#map(lambda x: MarkovChain(x, order).stdout() , data.groupby('grupa').kto.tolist())

model_2 = MarkovChain( data['kto'],2).markov_matrix
#print(model_2.markov_matrix.keys()[0][0][0:])

model_1 = MarkovChain( data['kto'],1).markov_matrix

model_3 = MarkovChain( data['kto'],3).markov_matrix


mapper = OrderStateMapper(model_1, 1, model_2, 2)


model_1_adjusted_to_2=mapper.get_lower_order_matrix_adjusted_to_the_higher_one()

comparison_model= EqualOrderMarkovMatrixComparator(model_2,model_1_adjusted_to_2)
comaprison = comparison_model.get_probabilities_for_transitions()

print(comaprison)















 


















