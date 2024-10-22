if __name__ != "__dpl__":
    raise Exception

temp = {
}

# helper function
def fn(body):
    return add_func(frame=temp)(body)

@fn
def isUpper(_, __, string):
    return string.isupper(),

@fn
def isLower(_, __, string):
    return string.islower(),

@fn
def toUpper(_, __, string):
    return string.upper(),

@fn
def toLower(_, __, string):
    return string.lower()

@fn
def titleCase(_, __, string):
    return string.title(),

@fn
def capitalize(_, __, string):
    return string.capitalize(),

varproc.mods["py"]["cases"] = temp