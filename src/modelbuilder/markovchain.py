from pykov import maximum_likelihood_probabilities
from orderstatechainbuilder import OrderStateChainBuilder


class MarkovChain(object):
    order = 0
    
    def __init__(self, state_chain, order):
        self.order = order
        if order>1:
            state_chain = OrderStateChainBuilder(order).get_order_states(state_chain)
        self.state_probabilities, self.markov_matrix = maximum_likelihood_probabilities(state_chain, lag_time=1, separator='0')
        
    def state_probs_str(self):
        """
        This method prints out the model states.
        The subsequent states are print out as rows, in the following form:
        key \t value     
        """
        result = ''
        for key in self.state_probabilities.keys():
            result += str(key) + '\t' + str(self.state_probabilities[key]) + '\n'
        return result        
        
    def matrix_str(self):
        """
        This method prints out the Markov matrix
        using the following convention: 
        from_state->to_state    value
        """
        result = '' 
        #INFO: przegladamy macierz po indeksach wzietych z wektora stanow        
        for from_state in self.state_probabilities.keys():
            for to_state in self.state_probabilities.keys():
                if from_state != to_state: #nie ma petli 
                    if self.order == 1 or from_state[1:] == to_state[:self.order - 1]: #stany zachodza na siebie tak ze roznia sie tylko jednym elementem (warunek ma sens dla order > 1)
                        value = self.markov_matrix[from_state,to_state] #czytamy wartosc...
                        result += str(from_state) + '->' + str(to_state) + '\t' + str(value) + '\n'#...i wypisujemy
        return result
                                                 
    def stdout(self):
        print '\nState probabilities:'
        print self.state_probs_str()
        print 'Markov matrix:'
        print self.matrix_str()
   
        
             
        
        
