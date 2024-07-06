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

```
# this program outputs the text "hi everybody!" through a function alias

message = "1is1 demo"            # message and "1is1 demo" are equivalent

f(x) = output(message)           # f(x) and output(message) are equivalent,
                                 # therefore x takes the same role as message in f(x)

x = "hi everybody!"              # x and "hi everybody!" are equivalent

return = f(x)                    # value of return is equivalent to resolving f(x) --
                                 # x is known from above, so the function is executed

                                 # the text "hi everybody!" is displayed on the screen
                                 # but "1is1 demo" is not displayed
```

# still more complexity

```
# this program outputs the text "hi everybody!" through a function alias

url = "http://www.example.com"   # url and "http://www.example.com" are equivalent
message = browser(url)           # message and browser(url) are equivalent
                                 # browser(x) is a built in function to return the
                                 # contents of a webpage

return = output(message)         # output the contents of the webpage to the screen
```
                    

# logic

```
x = 1 + 5        # x is equal to 1 + 5 which evaluates to 6, so x = 6

a = "hamburgers"
b = "pizza"
y = a AND b     # y is equivalent to "hamburgers and pizza"

c = 1
d = 0
z = c AND d     # z is equivalent to c AND d, so z is false
```
 
# 16 operators

```
0 null (false)
1 AND
2 inhibition A AND NOT-B
3 transfer (A)
4 inhibition B AND NOT-A
5 transfer (B)
6 XOR
7 OR
8 NOR
9 equivalence (XNOR), iff A then B
10 NOT-B
11 implication (if B then A)
12 NOT-A
13 implication (if A then B)
14 NAND
15 identity (true)
```

```
A [0]op B returns false
A [1]op B returns A AND B
A [2]op B returns A AND NOT-B
...
```

# variables and functions are both first class entities

- equivalences as first class entities

# automatic object creation

```
x.size = 16      # implies there is an object x

```

# built in functions

```

input(x)       # take value for x from stdin / keyboard
output(x)      # display value in x to stdout / screen

browser(x)     # query internal headless browser
               # and return contents at x URL

resolve(x)     # force x to resolve to the most simplified level

f16(func, a, b) # execute boolean function func on a, b

```

examples:
```
keypress = input(x)                       # the x is not necessary? wait for keypress and store in keypress
return = output("Hey buddy")              # displays "Hey buddy" on the screen
page = browser("https://example.com")     # requests page at example.com and stores contents in page
answer = resolve(7 + 3)     # resolves to 10 and stores 10 in answer
potato = resolve(output("hi") + browser("https://example.com"))

f16(6, 1, 3) # execute boolean function 6 on 1, 3 meaning 1 XOR 3
f16("inhibition", 1, 3) # execute boolean function "inhibition" on 1, 3 meaning 1 AND !3
f16("implication", 1, 3) # execute boolean function "implication" on 1, 3 meaning 1->3            
```

# nameless, fuzzy equivalences

You can equate two strings without explaining why or providing any name for the equivalence

Equivalences do not have to evaluate as true in order to be well formed

Examples:

"This dog is sleepy" = "this dog is tired"

"I love you" = "我愛你"

"5" = "4"

# boolean functions on nameless equivalences

"This dog is sleepy" = "this dog is tired"   # equate the two phrases

answer = resolve("This dog is tired" -> "This dog is sleepy")  # determine if this dog is tired implies this dog is sleepy
                                                               # yes, it does
                                                               # store true in answer

return = output(answer)                                        # display true to screen, store success in return

# seriously?

Yes but it's an experimental language, you may or may not get anything out of it

It's not meant to make commercial products, don't expect to make your next website with it

