from sys import exit as nelxd
try:
    import sys
    import kociemba 
    import argparse

    from utils import combine
    from utils import detectColor
    from utils import normalize
    from stickers import webcam
except ImportError as err:
    nelxd(err)

class cubeSolver: 
    def __init__(self,normalize,language):
        self.ezsolve = normalize
        self.language = (language[0]) if isinstance(language,list) else language

    def run(self): 
            state = webcam.scan()
            if not state: 
                print( 'Solver Error, you didnt scan the 6 sides of the cube.')
                print( 'Make sure you scan all faces of the cube please')
                print( 'try again')
                nelxd(1)
            unsolved = combine.sides(state)
            try: 
                solution = kociemba.solve(unsolved)
                length = len(solution.split(' '))
            except Exception as err: 
                print( 'Solver Error, you didnt scan the 6 sides of the cube.')
                print( 'Make sure you scan all faces of the cube please')
                print( 'try again')
                nelxd(1) 
            
            print( '===================   S O L U T I O N    ===================')
            print('Starting position \n FRONT: GREEN MIDDLE CUBIE /n TOP: WHITE MIDDLE CUBIE')
            print(solution, '({0} moves)'.format(length), '\n')

            if self.ezsolve: 
                handmade = normalize.algorithm(solution, self.language)
                for index,text in enumerate(handmade):
                    print('{}. {}'.format(index+1,text))
            nelxd(0)
if __name__ == '__main__':
    # define argument parser.
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--normalize', default=True, action='store_true',
            help='Shows the solution normalized. For example "R2" would be: \
                    "Turn the right side 180 degrees".')
    parser.add_argument('-l', '--language', nargs=1, default='en',
            help='You can pass in a single \
                    argument which will be the language for the normalization output. \
                    Default is "en".')
    args = parser.parse_args()

    # run Qbr with its arguments.
    cubeSolver(
        args.normalize,
        args.language
    ).run()



        

