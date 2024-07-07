import os, sys
version="1is1 interpreter 0.741"; print(version)
stack={} # allocate 1is1 stack

def f1is1output(outmsg):
    print(outmsg)

def f1is1resolve(x):
    if('"' in x):
        newstring=(x.split('"')[1])
        stack.update({"message":newstring})
        #print("1")
    if("input" in x):
        xe=x.split("input("); xo=xe[1].split(")"); f1is1input(xo[0])
        #print("2")
    if("output" in x):
        xe=x.split("output("); xo=xe[1].split(")");
        if('"' in xo):
            newstring=(xo.split('"')[1])
            stack.update({xo:newstring})
        #print(stack[(xo[0])])
        if not xo[0] in stack:
            stack.update({xo[0]:xo[0]})
        outmsg=(stack[(xo[0])])
        print(outmsg)
        f1is1output(outmsg)
        print("3")
    if("resolve" in x):
        xe=x.split("resolve("); xo=xe[1].split(")"); f1is1resolve(xo[0])
        print("4")
    if("browser" in x):
        print(x, end="")
        print("5")
    if("f16" in x):
        print(x, end="")
        print("6")
def f1is1browser(x):
    print(x)
def f1is1input(prompt):
    string = input(prompt)
    return string
def f16(x):
    print(x)
dictionary = {}; string = ""; prompt = "\nhello: "
if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(filename, "r"); r = f.readlines(); f.close()
    for line in r:
        f1is1resolve(line)
else:
    while(string != 'quit()'):
        string = input(prompt)
        if "=" in string:
            entry = {}
            equality=string.split("="); print("Creating variables: ", end="")
            neighbor=""
            head=equality[0]
            for variable in equality:
                stripped = variable.strip()
                entry.update({stripped:neighbor})
                print(stripped + ", ", end="")
                neighbor=stripped
                stack.update({head:entry})
            stack.update({string:entry})
            dictionary.update({string:entry})
            f1is1resolve(string)
        else:
            print(string)
print(stack);
print(dictionary);
for entry in dictionary:
    print(entry + " : " + str(dictionary[entry]))
print("1is1"); print("Goodbye!")
