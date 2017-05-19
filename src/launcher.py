#!/usr/bin/python3

#
#   FOX LAUNCHER
#
#   Created for Fur Desktop Environment
#   http://github.com/krushndayshmookh/fur-box
#
#   Created by Krushn Dayshmookh
#   http://krushndayshmookh.github.io
#
#




import sys
# import subprocess
from os import system
from os import listdir


files = listdir("/usr/share/applications")
files.sort()

#print (files)


appList = []

class AnApp:
    """An app information object"""
    name = "no name"
    executable = "true"
    icon = "folder-new"
    category = "unknown"

def readAppName (desktopFile):
    x = AnApp()
    file = open (desktopFile,"r")
    lines = file.readlines()
    shouldAppBeShown = True
    for data in lines:
        prop = data.split("=")

        if prop[0] == "Name":
            prop[1] = prop[1].replace("\n","")
            prop[1] = prop[1].replace(" ","-")
            x.name = prop[1]

        if prop[0] == "Exec":
            prop[1] = prop[1].replace("\n","")
            x.executable = prop[1]

        if prop[0] == "Icon":
            prop[1] = prop[1].replace("\n","")
            x.icon = prop[1]
            #print (appIcon + "\n")

        if prop[0] == "Categories":
            prop[1] = prop[1].replace("\n","")
            categories = prop[1].split(";")
            x.category = categories

        if prop[0] == "NoDisplay":
            prop[1] = prop[1].replace("\n","")
            if prop[1] == "true":
                shouldAppBeShown = False

        #app = AnApp(appName, appExec, appIcon)

        #
    #print (x.name)
    if shouldAppBeShown:
        appList.append(x)

    #print (appList[0].name,appList[0].executable,appList[0].icon,)
    file.close()


for filename in files:
    readAppName("/usr/share/applications"+"/"+filename)
#readAppName("deluge.desktop")


def list():
    for app in appList:
        print (app.name)


#print (appList)

def runProgram(program):
    for app in appList:
        if app.name == program:
            print (app.name)
            system(app.executable)








# --------------      CATEGORIES        -----------------------



def addCategory (categoryName, program, categoryKey):
    for x in program.category:
        if x  == categoryKey:
            categoryName.append(program)



network = []
development = []

for app in appList:
    addCategory(network, app, "Network")
    addCategory(network, app, "Internet")
    addCategory(development, app, "Development")

#for app in network:
#    print (app.name)







# -------------------------------------------------------------

#if __name__ == __main__:
#    if sys.argv[1] == "run":
#        runProgram(sys.argv[2])
#
#    if sys.argv[1] == "list":
#        list()

#print sys.argv[0]
#print sys.argv[1]
#print sys.argv[2]


# -------------------------------------------------------------------------------------------------
#
#       USAGE INSTRUCTIONS
#
#   use "python launcher.py list"  to list all applications in /usr/share/applications
#
#
#   after that to run "app-name" from the list use "python launcher.py run app-name"
#
#
#   This is currently very much in development.
#   It may not work at all some times.
#
#
#
#
#
#
#
#
#
#
