# FormulaeGenerator

A Python script for generating "mathematical papers"

That looks great to idiots but actually is bullshit

This algorithm goes like this:

```
Generate a monomial
	RECIEVE: Parameter of "recur"
	choose from:
	|	|
	|	---- A single constant
	|	---- An exponent
	|		| Exponent:
	|		---- recur: Recur or not 
	|	---- A base
	|		| Base:
	|		---- recur: Recur or not
	Create a polynomial
```

```
Generate a polynomial
	| create a var named "base" that stores the polynomial and init it with a monomial
	| Recur for a random number between 1 ~ 10 < ------------------------
	|								                               		|
	---- add, minus, or "plus-minus" another generated monomial to base - |
	|
	Create a complex monomial
```

```
Generate a complex monomial < -------------------------------------
	RECIEVE: Parameter of "base"									|
	Override content of base from one of:							|
	|	|						                                    |
	|	---- Generate a polynomial									|
	|	---- Generate a monomial, pass down "it does not recur"		|
	|	---- Does not override	                                    |
	choose from:                        							|
	|  |	                                                		|
	|	---- base	                                            	|
	|	---- choose from:											|
	|		|	                                    				|
	|		---- Create fraction "<base>/Monomial"					|
	|		---- Create fraction "<base>/(Polynomial)"				|
	|		---- Recur -------------------------------------------- |
	Create a expression and pass down default value of "base": ""
```

```
Generate a expression
	| create a var named "base" that stores the polynomial and init it with a complex monomial
	choose from:
	| |
	|	---- Create a cool integral/sigma style expression ^ (<Recur> | generate a complex monomial) _ (<Recur> | generate a complex monomial)
	Generate a final equation
```

```
Generate a final equation
	if it is a equation (developer's note: which it should be):
	|	"<Generate monomial> <some sort of sign that compares or establishes logical relation> <Generate a complex monomial>
```

```
Write file
	| Create one
	| Write header "To prove...."
	| Recur for a random number between 2 ~ 10: < ------------------------------------
	|					                       									 	|
	---- Write a random word, next line, write a generated final equation, next line |
```

And generates sth like this:

```shell
Deleting outdated cache
Running script

Publishin to ~/out.pdf
[WARNING] Unusual conversion: to convert a .tex file to PDF, you get better results by using pdflatex (or lualatex or xelatex) directly, try `pdflatex output.ltx` instead of `pandoc output.ltx -o /Users/makabaka1880/out.pdf`.
```

![A preview of outputed PDF](https://raw.githubusercontent.com/makabaka1880/FormulaeGenerator/main/Screenshot%202022-11-28%20at%2003.46.59.png)
