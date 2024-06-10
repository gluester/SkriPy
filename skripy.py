from ch.njol.skript.lang.function import Functions
from ch.njol.skript.variables import Variables

# again, EXTREMELY BASIC

def getSkriptVar(variableName):
    return Variables.getVariable(variableName, None, False)
def setSkriptVar(variableName, setTo):
    print("Set skript var " + variableName + " to " + setTo)
    return Variables.setVariable(variableName, setTo, None, False)
def runFunc(funcName, *args):
    func = Functions.getGlobalFunction(funcName)
    if not args:
        ranVersion = func.execute()
    else:
        skArgs = [[arg] for arg in args]
        print(skArgs)
        try:
            ranVersion = func.execute(skArgs)
        except:
            print("SKRIPY ERROR: Failed to execute function " + funcName + "()")
    print("Ran Skript function: " + str(ranVersion))
    try:
        returns = list(ranVersion)
    except:
        returns = []
    if returns != []:
        return returns
