version="1is1 interpreter 0.1"
print(version)
string = ""
while(string != 'quit()'):
    prompt = "hello: "
    string = input(prompt)
    if "=" in string:
        equality=string.split("=")
        for variable in equality:
            print(variable.strip() + ", ", end="")
        print("")
    else:
        print(string)
print("1is1")
print("goodbye")
