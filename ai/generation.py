# stores values for single generation

class Generation (object):
    '''
    stores values for single generation
        value:
            - weights
            - fitnesses
    '''
    def __init__ (self, **kwargs):
        super(Generation, self).__init__(**kwargs)
        print("[evol] created " + str(self.__class__))

        self.weights = []
        self.fitnesses = []
