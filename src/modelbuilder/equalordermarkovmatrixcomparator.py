from numpy import array

class EqualOrderMarkovMatrixComparator(object):
    """
     The class takes two equal order Markov Model matrixes. The matrixes MUST contain the same transition set.
     It extracts probabilities from both matrixes for the transitions and sets them against each other. 
    """
     
    def __init__(self, matrix_expected, matrix_observed):
        """"
        The constructor takes two matrixes representing Markov Models of the same transition set and the same order.
        As first parameter should go a matrix of expected probabilities. As the second one - observed.
        """
        self.__matrix_expected = matrix_expected
        self.__matrix_observed = matrix_observed
        self.__compared_transitions = []
        
    def get_probabilities_for_transitions(self):
        """
         The method returns a list of triples:
         - transition, - probability in the first matrix, - probability in the latter matrix
        """
        if len(self.__compared_transitions) == 0:
            self.__set_compared_transitions() 
        return self.__compared_transitions
    
    def get_probablilities_expected_and_observed(self):
        """
        Returns two lists: of the expected and observed probabilities in the same order,
        that is probabilities on the same position in both lists refer to the same transition.
        """
        transitions, expected_probabilities, observed_probabilities = zip(*self.__compared_transitions)
        return array(list(expected_probabilities)), array(list(observed_probabilities))
        
    def __set_compared_transitions(self):
        key_set = self.__matrix_expected.keys()
        self.__compared_transitions = map(self.__get_both_probabilities_for, key_set)      
        
    def __get_both_probabilities_for(self, key):
        return (key, self.__matrix_expected[key], self.__matrix_observed[key])
            