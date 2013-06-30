
class OrderStateMapper(object):
    """
    The class transforms lower order Markov Model to the higher order one.
    """

    def __init__(self, lower_order_matrix, lower_order, higher_order_matrix, higher_order):
        """
        The constructor takes Markov Model matrixes of different order.
        The matrixes should have a form of dictionaries.
        The transitions between states should be represented by tuples.
        For example: {((a,b,c),(b,c,d)):0.3}
        means transition from state (a,b,c) to (b,c,d) occurs with a probability 0.3.
        """
        self.__lower_order_matrix = lower_order_matrix
        self.__higher_order_matrix = higher_order_matrix
        self.__order_difference = higher_order - lower_order
        self._adjusted_to_higher_order_matrix = {}
         
    def get_lower_order_matrix_adjusted_to_the_higher_one(self):
        """
        Returns a Markov Model matrix.
        The matrix has an order and state set of the higher order matrix.
        The probabilities of transitions are derived from the lower order matrix.
        """
        if len(self._adjusted_to_higher_order_matrix) == 0:
            self.__set_adjusted_to_higher_order_matrix()
        return self._adjusted_to_higher_order_matrix
              
    def __set_adjusted_to_higher_order_matrix(self):
        lower_order_transitions = self.__lower_order_matrix.keys()
        map(self.__set_higher_order_transitions_for, lower_order_transitions)
    
    def __set_higher_order_transitions_for(self, lower_order_transition):
        adjusted_transitions = self.__get_matching_higher_order_transitions(lower_order_transition)
        probability = self.__lower_order_matrix[lower_order_transition]
        map(lambda x: self.__set_adjusted_probability_for(x, probability) ,adjusted_transitions)
    
    def __set_adjusted_probability_for(self, transition, probability):
        self._adjusted_to_higher_order_matrix[transition] = probability
      
    def __get_matching_higher_order_transitions(self, lower_order_transition):
        all_transitions = self.__higher_order_matrix.keys()
        return filter(lambda x: self.__are_matching_transitions(lower_order_transition,x), all_transitions)
        
    def __are_matching_transitions(self, lower_order_transition, higher_order_transition):
        return (self.__are_matching_states(lower_order_transition, higher_order_transition,0)
               & self.__are_matching_states(lower_order_transition, higher_order_transition,1) )   
        
    def __are_matching_states(self, lower_order_transition, higher_order_transition, is_to):
        return lower_order_transition[is_to] ==  higher_order_transition[is_to][self.__order_difference:] 
     

        