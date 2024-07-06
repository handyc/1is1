version="1is1 interpreter 0.2"
print(version)
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
