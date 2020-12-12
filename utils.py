import stackprinter

stackprinter.set_excepthook(style='lightbg')


### STRING ###
def replaceAll(string, repl_tuples):
    for t1, t2 in repl_tuples:
        string = string.replace(t1, t2)
    return string


nums = "0123456789"
hexanums = "0123456789abcdef"


### MATH ###
def multiply(items):
    result = 1
    for i in items:
        result *= i
    return result


### FILES ###
class Opener:
    def raw(self, location):
        with open(location, "rt") as f:
            return f.read()

    def lines(self, location):
        return self.raw(location).split("\n")[:-1]

    def numbers(self, location):
        return [int(x) for x in self.lines(location)]

    def grid(self, location):
        return [list(x) for x in self.lines(location)]

opener = Opener()
