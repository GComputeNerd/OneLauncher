# This python script generates shortcuts for this rainmeter skin

from os import system

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

path_to_rainmeter = "C:\Program Files\Rainmeter\Rainmeter.exe"

rainmeter = lambda cmd: system(f"{path_to_rainmeter} {cmd}")

# This gets the actual rainmeter style
# For an entry
get_shortcut_style = lambda num, name, img_path, launch_cmd: f"""
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

get_icon_style = lambda menu,i: f"""

[{menu}Icon]
Meter=Image
Y=3
X={"0" if i == 0 else "25R"}
H=#buttonSize#
ImageAlpha=130
ImageName=#@#Images\{menu}.png
LeftMouseDownAction=[!ActivateConfig #widgetRoot# {menu}.ini][!ActivateConfig #iconRoot# {menu}.ini][!SetWallpaper #@#Wallpapers\{menu}.jpg Fill]

"""

get_selected_icon_style = lambda menu, i: f"""

[{menu}Icon]
Meter=Image
Y=3
X={"0" if i == 0 else "25R"}
H=#buttonSize#
ImageName=#@#Images\{menu}.png

"""

def writeBoilerplate(menuFile):
    with open('boilerplates/widget_boilerplate', 'r') as boilerplate:
        menuFile.writelines(boilerplate.readlines())

def writeShortcuts(catalog, menuFile):
    num = 1
    entry = catalog.readline()
    while entry and entry[0] == '-':
        entry = entry[1:].split(',')
        menuFile.write(get_shortcut_style(num, entry[0], entry[1], entry[2]))
        print("Added", entry[0], "!")
        num += 1
        entry = catalog.readline()

def writeIcon(menuName, tabList):
    with open(f"IconBar/{menuName}.ini", 'w') as iconBar:
        # Write boilerplate
        with open("boilerplates/icon_boilerplate", 'r') as boilerplate:
            print(f"Writing iconBar Boilerplate for {menuName}")
            iconBar.writelines(boilerplate.readlines())

        i = 0        
        while i < len(tabList):
            tab = tabList[i]
            if tab == menuName:
                iconBar.write(get_selected_icon_style(tab, i))
            else:
                iconBar.write(get_icon_style(tab, i))
            i += 1


print("opening catalog")
print("Reading Tabs")
tabs = []

with open("Shortcut-Catalog", 'r') as catalog:
    tabs = [entry[1:].strip() for entry in catalog.readlines() if entry[0] == '+']

for tab in tabs:
    print(f"Writing iconBar for {tab}...")
    writeIcon(tab, tabs)

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
            writeShortcuts(catalog, menuFile)
            entry = catalog.readline()

# Load Skins in First Tab
rainmeter(f'!DeactivateConfig "OneLauncher" FirstLaunch.ini')
rainmeter(f'!ActivateConfig "OneLauncher\IconBar" {tabs[0]}.ini')
rainmeter(f'!ActivateConfig "OneLauncher\WidgetArea" {tabs[0]}.ini')
rainmeter(f'!SetWallpaper "OneLauncher\@Resources\Wallpapers\{tabs[0]}.jpg" Fill')

"""
!ActivateConfig #widgetRoot# {menu}.ini
!ActivateConfig #iconRoot# {menu}.ini
!SetWallpaper #@#Wallpapers\{menu}.jpg Fill"""