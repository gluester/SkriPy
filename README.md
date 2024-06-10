# SkriPy
EXTREMELY basic skript integration with PySpigot
keep in mind I've only learned pyspigot like...today
# Usage

Variables:
```
# Bukkit imports...
import skripy
def setVarToPlayer(sender, label, args):
    array = list(args)
    skripy.setSkriptVar("favoriteWord::{}".format(sender.getName()), array[0])
    Bukkit.broadcastMessage(skripy.getSkriptVar("favoriteWord::{}".format(sender.getName())))
```
Function:
```
# imports/function/whatever 
skripy.runFunc("doAThing")

skripy.runFunc("doAThingThatHasParameters", sender.getName(), "Wow!")
# Would run doAThingThatHasParameters(player, "Wow!"). You can also send runFunc() to get whatever that function returns
```
