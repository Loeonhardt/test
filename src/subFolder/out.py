class Output(object):
    def __init__(self):
        self.message = 'dude'

    def print_to_console(self, token='hey!'):
        print (token, ' : ',  self.message)
