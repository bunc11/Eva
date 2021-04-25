import re

class Unimplemented(Exception):
    pass

class Environment:

    def __init__(self, record = {}, parent = None):
        self.record = record
        self.parent = parent

    def define(self, name, value):
        self.record[name] = value
        return value

    def retrive(self, name):
        if name in self.record:
            return self.record[name]
        raise ValueError(f"variable {name} not defined")

#interpreter

class Eva:

    def __init__(self, globalEnv = Environment()):
        self.globalEnv = globalEnv

    def eval(self, exp, env = None):

        #print("Evaluating", exp)

        if env == None:
            self.env = self.globalEnv

        # self-evaluating expessions

        if(isinstance(exp, (int, float))):
            return exp

        if(isinstance(exp, str)) and exp[0] == '"' and exp[-1] == '"':
            return exp

        # math operators

        if exp[0] == '+':
            return self.eval(exp[1], env) + self.eval(exp[2], env)

        if exp[0] == '*':
            return self.eval(exp[1], env) * self.eval(exp[2], env)

        if exp[0] == '-':
            return self.eval(exp[1], env) - self.eval(exp[2], env)

        if exp[0] == '/':
            return self.eval(exp[1], env) / self.eval(exp[2], env)

        # evaluate block


        # variable declaration

        if(exp[0] == 'var'):
            [_, name, value] = exp
            return self.env.define(name, self.eval(value, env))
        
        # variable access
        if(self._isVariableName(exp)):
            return self.env.retrive(exp)

        raise Unimplemented(exp)

    def _isVariableName(self, exp):

        return type(exp) == str and re.match(r'[a-zA-Z][a-zA-Z0-9_]*', exp)


def run():
    e = Eva(Environment())

    exp = ['+', 2, ['*', 3, ['*', 8, ['-', 8, ['/', 16, 4]]]]]



if __name__ == "__main__":
    run()


