version="1is1 interpreter 0.3"
print(version)

def f1is1resolve(x):
    print(x)

def f1is1browser(x):
    print(x)

def f1is1input(x):
    print(x)

def f1is1output(x):
    print(x)

string = ""
prompt = "hello: "
while(string != 'quit()'):
    string = input(prompt)
    if "=" in string:
        equality=string.split("=")
        print("Creating new variables: ", end="")
        for variable in equality:
            print(variable.strip() + ", ", end="")
        print("")
    else:
        print(string)
print("1is1")
print("goodbye")
