import re

#stao na lec 7 -> blocks

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

        """
        #sorting
        
        exp = sortPriorities(exp, display = True)
        print("Exp after sorting", exp)
        """
        #self.func(exp,env)

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

        if exp[0] == 'begin':

            blockEnv = Environment(parent = self.env)
            return self._evalBlock(exp, blockEnv)

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

    def _evalBlock(self, block, env):

        [_tag, *expressions] = block

        result = None

        for exp in expressions:
            result = self.eval(exp, env)

        return result


    def func(self,input, env):
        for item in input:
            if isinstance(item, list):
                return (self.eval(self.func(item, env)))
                


def sortPriorities(exp, display = False):
        print("Input:", exp)
        try:
            if exp[0] == '*' or exp[0] =='/':
                    if isinstance(exp[2], list) and (exp[2][0] == '+' or exp[2][0] == '-'):
                        rNode = sortPriorities(exp[2])
                        del exp[2]
                        temp = sortPriorities(rNode[1])
                        rNode[1] = exp
                        rNode[1].append(temp)
                        exp = rNode
                        if display: print("returning", exp)
                        return exp
            if display: print("returning", exp)
            return exp
        except:
            if display: print("returning", exp)
            return exp

def sortPriorities1(exp, display = False):
        print("Input:", exp)
        try:

            if isinstance(exp[2], list) and (exp[2][0] == '+' or exp[2][0] == '-'):
                rNode = sortPriorities(exp[2])
                del exp[2]
                temp = sortPriorities(rNode[1])
                rNode[1] = exp
                rNode[1].append(temp)
                exp = rNode
                if display: print("returning", exp)
                return exp
            if display: print("returning", exp)
            return exp
        except:
            if display: print("returning", exp)
            return exp

                    

def run():
    e = Eva(Environment())




    exp = ['+', 2, ['*', 3, ['*', 8, ['-', 8, ['/', 16, 4]]]]]



if __name__ == "__main__":
    run()


