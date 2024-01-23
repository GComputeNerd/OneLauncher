# This python script generates shortcuts for this rainmeter skin

header = """========================================================================
  ____  ____                            _       _   _              _ 
 / ___|/ ___|___  _ __ ___  _ __  _   _| |_ ___| \ | | ___ _ __ __| |
| |  _| |   / _ \| '_ ` _ \| '_ \| | | | __/ _ \  \| |/ _ \ '__/ _` |
| |_| | |__| (_) | | | | | | |_) | |_| | ||  __/ |\  |  __/ | | (_| |
 \____|\____\___/|_| |_| |_| .__/ \__,_|\__\___|_| \_|\___|_|  \__,_|
                           |_|                                       
                        OneLauncher Shortcut Gen
                        
                        Author : Afras Ashraf
                        Github : @GComputeNerd
========================================================================
"""

print(header)

# This gets the actual rainmeter style
# For an entry
get_style = lambda num, name, img_path, launch_cmd: f"""
[App{num}Box]
Meter=Shape
Y={"24R" if num != 1 else 0}
Shape=Rectangle 0,R,300,45,10 | extend Modifiers1 | extend Modifiers2
Modifiers1=Fill color 0,0,0,100
Modifiers2=strokewidth 1 | stroke color 255,255,255,180
Modifiers3=strokewidth 3 | stroke color 255,255,255,180
LeftMouseDownAction=[{launch_cmd.strip()}]
MouseOverAction=!SetOption App{num}Box Shape "Rectangle 0,0,300,45,10 | extend Modifiers1 | extend Modifiers3"
MouseLeaveAction=!SetOption App{num}Box Shape "Rectangle 0,0,300,45,10 | extend Modifiers1 | extend Modifiers2"

[App{num}Icon]
Meter=Image
Y=8r
X=15
W=#buttonSize#
H=#buttonSize#
ImageName=#@#\Shortcuts\{img_path}

[App{num}Text]
Meter=String
X=55
Y=3r
MeterStyle=AppTextStyle
Text="{name}"

"""

def writeBoilerplate(menuFile):
    with open('boilerplate.ini', 'r') as boilerplate:
        menuFile.writelines(boilerplate.readlines())

def writeIcons(catalog, menuFile):
    num = 1
    entry = catalog.readline()
    while entry and entry[0] == '-':
        entry = entry[1:].split(',')
        menuFile.write(get_style(num, entry[0], entry[1], entry[2]))
        print("Added", entry[0], "!")
        num += 1
        entry = catalog.readline()

print("opening catalog")
with open("Shortcut-Catalog",'r') as catalog:
    entry = catalog.readline()
    while entry: # entry is not Empty (EOF)
        if entry[0] == '+':
            # New Section Definition
            menu = entry[1:-1] # Name of Section
            print("Catalog For", menu, "Found!")

            # Open Section File
            menuFile = open('WidgetArea/'+menu+".ini", 'w')

            # Write Boilerplate
            print("Writing Boilerplate...")
            writeBoilerplate(menuFile)

            print("Writing Shortcuts...")
            writeIcons(catalog, menuFile)
            entry = catalog.readline()