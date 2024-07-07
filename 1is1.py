import os, sys
version="1is1 interpreter 0.73"; print(version)
stack={} # allocate 1is1 stack

def f1is1resolve(x):
    if('"' in x):
        newstring=(x.split('"')[1])
        stack.update({"message":newstring})
    if("input" in x):
        xe=x.split("input("); xo=xe[1].split(")"); f1is1input(xo[0])
    if("output" in x):
        xe=x.split("output("); xo=xe[1].split(")");
        #print(stack[(xo[0])])
        outmsg=(stack[(xo[0])])
        f1is1output(outmsg)
    if("resolve" in x):
        xe=x.split("resolve("); xo=xe[1].split(")"); f1is1resolve(xo[0])
    if("browser" in x):
        print(x, end="")
    if("f16" in x):
        print(x, end="")
def f1is1browser(x):
    print(x)
def f1is1input(prompt):
    string = input(prompt)
    return string
def f1is1output(x):
    print(x)
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
            for variable in equality:
                stripped = variable.strip()
                entry.update({stripped:neighbor})
                print(stripped + ", ", end="")
                neighbor=stripped
            dictionary.update({string:entry})
        else:
            print(string)
print(dictionary);
for entry in dictionary:
    print(entry + " : " + str(dictionary[entry]))
print("1is1"); print("Goodbye!")
