
class EqualOrderMarkovMatrixComparator(object):
    """
     The class takes two equal order Markov Model matrixes.
     The matrixes MUST contain the same transition set.
     It extracts probabilities from both matrixes for the transitions and sets them against each other. 
    """
     
    def __init__(self, matrix_1, matrix_2):
        """"
        The constructor takes two matrixes representing Markov Models 
        of the same transition set and the same order.
        """
        self.__matrix_1 = matrix_1
        self.__matrix_2 = matrix_2
        self.__compared_transitions = []
        
    def get_probabilities_for_transitions(self):
        """
         The method returns a list of triples:
         - transition, - probability in the first matrix, - probability in the latter matrix
        """
        if len(self.__compared_transitions) == 0:
            self.__set_compared_transitions() 
        return self.__compared_transitions
    
    def __set_compared_transitions(self):
        key_set = self.__matrix_1.keys()
        self.__compared_transitions = map(self.__get_both_probabilities_for, key_set)      
        
    def __get_both_probabilities_for(self, key):
        return (key, self.__matrix_1[key], self.__matrix_2[key])
            