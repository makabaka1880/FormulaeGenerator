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

signs = constants + [
    "+\infty",
    "-\infty",
    "\pm\infty",
    "\mathrm{d}",
    "\sigma",
    "\delta"
]
funcs = [
    "\sin",
    "\cos",
    "\ln",
    "\log",
    "\lim_{x\\to0^{+}}",
    "\lim_{x\\to0^{-}}",
    "\lim_{x\\to+\infty^{-}}",
    "\lim_{x\\to-\infty^{+}}"
]
coolSigns = [
    "\\Sigma",
    "\\int"
]
compare = [
    "\\neq",
    "\leq",
    "\geq",
    "\lor",
    "\land"
]
causes = [
    "\Rightarrow",
    "\Leftarrow"
]
words = [
    "Becauses of",
    "It is not hard to find out that",
    "It can be implied that",
    "So",
    "Clearly",
    "From that",
    "In summary of the previous equation"
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
    chc = randint(0, 3);
    base = createComplexMonomial();
    if chc == 0:
        return base
    elif chc == 1:
        return choice(coolSigns) + "^{" + createComplexMonomial() + "}_{" +createComplexMonomial() + "}";
    elif chc == 2:
        return createComplexMonomial() + choice(coolSigns) + "^{" + createComplexMonomial() + "}_{" +createComplexMonomial() + "}";
    else:
        chc = randint(0, 2);
        if chc == 0:
            return createComplexMonomial() + choice(coolSigns) + "^{" + createExpression() + "}_{" +createExpression() + "}";
        elif chc == 1:
            return createComplexMonomial() + choice(coolSigns) + "^{" + createComplexMonomial() + "}_{" +createExpression() + "}";
        else:
            return createComplexMonomial() + choice(coolSigns) + "^{" + createComplexMonomial() + "}_{" +createComplexMonomial() + "}";
def createCoolExpressionOrEquation(isEquation):
    if isEquation:
        chc = randint(0, 1);
        if chc:
            return createMonomial(1) + choice(compare) + createExpression()
        else:
            return createMonomial(1) + choice(causes) + createExpression()
def main(times):
    file = open('output.ltx', mode='x');
    file.write("\documentstyle{article}\n\\begin{document}\n")
    file.close()
    file = open ('output.ltx', mode = "a+");
    prep = createCoolExpressionOrEquation(True)
    file.write("This material proves that \n $$ " + prep + " $$\\\\ \n ")
    file.write("\nFirstly, \n $$ " + createCoolExpressionOrEquation(True) + " $$\\\\\n So we can suppose \n $$ " + createCoolExpressionOrEquation(True) + "$$\\\\\n ")
    for i in range(0, times - 1):
        file.write(choice(words) + "\\\\\n$$")
        file.write(createCoolExpressionOrEquation(True) + "$$\\\\\n")
    file.write("\\textbf{The preposition of $" + prep + "$ has been proved.}\n\end{document}");
    file.close()
def run():
    return main(randint(2, 10));
r = run()
