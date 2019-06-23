class Output(object):
    def __init__(self):
        self.message = 'Dude'

    def print_to_console(self, token='hey!'):
        print (token, ' : ',  self.message)