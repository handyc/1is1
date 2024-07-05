# 1is1

1is1 ("one is one") experimental programming language

The primary distinguishing feature of this language is in its use of the = sign
to indicate both assignment and equality.

In 1is1, variables are created in pairs through the use of equality expressions.

Variables can be simple or complex, and are evaluated to various degrees depending

on requirements for a variable at any given time.

- whitespace does not count
  
- each equation/equality is simultaneously a variable assignment and a truth claim

- each equality is associated with two dynamic variables stored as unicode strings

- each string is evaluated lazily at various resolutions depending on its need within an application

- dynamically and weakly typed
  

# example equality declarations

x=5

x = 5

5=x

5 = x

x + y = 3

x + y = a * 3

f(x) = 1

f(x) = g(y)

x="tree"

https://en.wikipedia.org/wiki/Equals_sign

# program execution

programs are sequences of equalities that execute from top to bottom

# hello world

message = "hello world!"

return = output(message)

# more complexity

/# this program outputs the text "hi everybody!" through a function alias

message = "1is1 demo"            # message and "1is1 demo" are equivalent

f(x) = output(message)           # f(x) and output(message) are equivalent, therefore x takes the same role as message in f(x)

x = "hi everybody!"              # x and "hi everybody!" are equivalent

return = f(x)                    # the value of return is equivalent to the value of resolving f(x) -- since x is known from above, the function is executed

                                 # the text "hi everybody!" is displayed on the screen but "1is1 demo" is not displayed

                                 

