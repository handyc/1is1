import os, sys
version="1is1 interpreter 0.6"; print(version)
def f1is1resolve(x):
    print(x, end="")
def f1is1browser(x):
    print(x)
def f1is1input(x):
    print(x)
def f1is1output(x):
    print(x)
def f16(x):
    print(x)
string = ""; prompt = "\nhello: "
if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(filename, "r"); r = f.readlines()
    for line in r:
        f1is1resolve(line)
    f.close()
else:
    while(string != 'quit()'):
        string = input(prompt)
        if "=" in string:
            equality=string.split("="); print("Creating variables: ", end="")
            for variable in equality:
                print(variable.strip() + ", ", end="")
        else:
            print(string)
print("1is1"); print("Goodbye!")
print(sys.argv[0])
