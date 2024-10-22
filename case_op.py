if __name__ != "__dpl__":
    raise Exception("This is a DPL extension")

temp = {
}

@add_method()
def isUpper(_, string):
    return string.isupper(),

@add_method()
def isLower(_, string):
    return string.islower(),

@add_method()
def toUpper(_, string):
    return string.upper(),

@add_method()
def toLower(_, string):
    return string.lower()

@add_method()
def titleCase(_, string):
    return string.title(),

@add_method()
def capitalize(_, string):
    return string.capitalize(),

varproc.modules["py"]["cases"] = temp