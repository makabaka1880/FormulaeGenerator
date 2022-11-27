from random import *;

constants = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
];

funcs = [
    "\sin",
    "\cos",
    "\ln",
    "\log",
    "\lim_{x\\to0^{+}}",
    "\lim_{x\\to0^{-}}",
    "\lim_{x\\to+infty^{-}}",
    "\lim_{x\\to-infty^{+}}"
]
coolSigns = [
    "\\Sigma",
    "\\int"
]   
def createMonomial(recur):
    chc = randint(0, 2);
    base = choice(constants);
    
    if chc == 0:
        pass;
    elif chc == 1:
        if recur == 0:
            base = base + "^{" + createMonomial(chc) + "}"
        else: 
            base = base + "^{" + choice(constants) + "}"
    else:
        if recur == 0:
            base = base + "_{" + createMonomial(chc) + "}"
        else: 
            base = base + "_{" + choice(constants) + "}"
    if randint(0, 1) == 0:
        return "\sqrt{" + base + "}"
    else:
        return choice(funcs) + "(" + base + ")"
        
def createPolynomial():
    pol = createMonomial(0);
    for i in range(0, randint(1, 10)):
        pol += choice(["+", "-", "\pm"]) + " " + createMonomial(0);
    return pol

def createComplexMonomial(base = ""):
    _chc = randint(0, 2);
    if _chc == 0:
        base = createPolynomial();
    elif _chc == 1:
        base = createMonomial(0);
    chc = randint(0, 1);
    recur = randint(0, 1)
    if chc == 0:
        return base
    elif chc == 1:
        if recur == 0:
            if _chc != 0:
                return "\\frac{" + base + "}{" + createMonomial(chc) + "}"
            else:
                return "\\frac{ (" + base + ") }{ " + createComplexMonomial() + " }"
        else: 
            return createComplexMonomial();
        
print(createComplexMonomial());

def createExpression():
    return 
def createCoolExpressionOrEquation(isEquation):
    if isEquation:
        return createComplex
def main():
    return createComplexMonomial();
def run():
    u = "https://latex.codecogs.com/svg.image?" + main();
    print(u);
print("------\n------\nMAIN PROGRAM:\n")
print("Please open the following url in a web browser:")
print("------")
print(run())
print("------")
print("------\nMAIN PROGRAM ENDED\n")
