
class OrderStateChainBuilder(object):

    def __init__(self, order):
        if order < 2 : raise ValueError("Order must be equal or more than 2.")
        self.order = order
        
    def get_order_states(self, state_chain):
        length = len(state_chain) - self.order + 1
        if length < 2 : raise ValueError("State chain must be equal or more than order + 1.")
        return [ tuple(state_chain[x:(x + self.order)]) for x in range(length) ]
         
        
