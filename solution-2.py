'''
Poniżej znajduje się implementacja CLI (command line interface) do modułu
turtle, czyli Pythonowego odpowiednika LOGO. Wykorzystano tutaj wzorzec Template
Method (metoda szablonowa).

W pierwszym, obowiązkowym zadaniu, należy dodać wsparcie dla makr, tak aby można
było nagrać ciąg komend, a następnie odtworzyć ten sam ciąg przy pomocy
komendy "playback". W tym celu, należy dodać następujące komendy: 

- record -- rozpoczyna nagrywanie makra
- stop -- kończy nagrywanie makra
- playback -- wykonuje makro, tzn. wszystkie komendy po komendzie "record", aż
  do komendy "stop". 

Podpowiedź: Użyj wzorca Command (polecenie).

W drugim, nieobowiązkowym zadaniu, zastanów się, jak można zastosować wzorzec
Composite (kompozyt) do tych makr i spróbuj zastosować go.

Rozwiązania wysyłamy tak samo, jak prework, tylko że w jednym Pull Requeście.
'''

import cmd
import turtle


class Command(object):
    def __init__(self, f, *args, **kwargs):
        self.f = f
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        return self.f(*self.args, **self.kwargs)


class Makro(object):
    def __init__(self):
        self.cmds = []

    def append(self, cmd):
        self.cmds.append(cmd)

    def __call__(self):
        for cmd in self.cmds:
            cmd()


class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '

    # ----- basic turtle commands -----
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        self.execute(Command(turtle.forward, int(arg)))
    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        self.execute(Command(turtle.right, int(arg)))
    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        self.execute(Command(turtle.left, int(arg)))
    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
        self.execute(Command(turtle.home))
    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        self.execute(Command(turtle.circle, int(arg)))
    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        def print_position():
            print('Current position is %d %d\n' % turtle.position())
        self.execute(Command(print_position))
    def do_heading(self, arg):
        'Print the current turtle heading in degrees:  HEADING'
        def print_heading():
            print('Current heading is %d\n' % (turtle.heading(),))
        self.execute(Command(print_heading))
    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        self.execute(Command(turtle.reset))
    def do_bye(self, arg):
        'Close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        turtle.bye()
        return True

    ### Rozwiązanie

    def __init__(self):
        super(TurtleShell, self).__init__()
        self.recording = False
        self.makro = Makro()
    
    def do_record(self, arg):
        self.recording = True
        self.makro = Makro()
    
    def do_stop(self, arg):
        self.recording = False
    
    def do_playback(self, arg):
        self.makro()  # self.makro.__call__()
    
    def execute(self, cmd):
        if self.recording:
            self.makro.append(cmd)
        cmd()

if __name__ == '__main__':
    TurtleShell().cmdloop()    