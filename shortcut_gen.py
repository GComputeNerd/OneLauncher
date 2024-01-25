"""
This program generates the rainmeter skin code for OneLauncher.
"""

from os import system
from rainmeter_code import *

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
rainmeter = lambda cmd: system(f'"{path_to_rainmeter}" {cmd}')

def writeShortcuts(catalog, menuFile):
    """
    This function writes the app shortcuts for a tab

    Arguments:
        catalog (File) : Shortcut-Catalog file, with pointer said to first entry
                        of Section.
        menuFile (File) : WidgetArea .ini file, that is being written to.
    """

    num = 1 # Holds shortcut index
    entry = catalog.readline()

    while entry and entry[0] == '-': # Current line is an entry
        entry = entry[1:].split(',') # Get data

        # Add Shortcut into Widget File
        menuFile.write(get_shortcut_style(num, entry[0], entry[1], entry[2]))

        print("\tAdded", entry[0], "!")
        
        num += 1
        entry = catalog.readline() # Get next entry

def writeIcon(selected, tabList):
    """
    This function writes the iconBar when a given icon is selected

    Arguments:
        selected (str) : Name of tab that is selected
        tabList (list) : List of all tabs in catalog
    """

    with open(f"IconBar/{selected}.ini", 'w') as iconBar:
        # Write boilerplate
        iconBar.write(icon_boilerplate(selected))
        
        # Write Bounding Box
        iconBar.write(bounding_box(len(tabList)))

        # Adding icons for current iconBar
        i = 0 
        while i < len(tabList):
            tab = tabList[i]
            if tab == selected:
                iconBar.write(get_selected_icon_style(tab, i))
            else:
                iconBar.write(get_icon_style(tab, i))
            i += 1


print("opening catalog...")
tabs = []
with open("Shortcut-Catalog", 'r') as catalog:
    print("Reading Tabs...")
    tabs = [entry[1:].strip() for entry in catalog.readlines() if entry[0] == '+']

print("WRITING ICONBARS")
print("----------------")
for tab in tabs:
    print(f"\tWriting iconBar for {tab}...")
    writeIcon(tab, tabs)

print()
print("WRITING SHORTCUTS")
print("-----------------")
catalog = open("Shortcut-Catalog",'r')

entry = catalog.readline()
while entry: # entry is not Empty (EOF)
    if entry[0] == '+':
        # New Section Definition
        menu = entry[1:-1] # Name of Section
        print("Catalog For", menu, "Found!")

        # Open Section File
        menuFile = open('WidgetArea/'+menu+".ini", 'w')

        # Write Boilerplate
        print("\tWriting Boilerplate...")
        menuFile.write(widget_boilerplate)

        print("\tWriting Shortcuts...")
        writeShortcuts(catalog, menuFile)
        menuFile.close()
        entry = catalog.readline()
catalog.close()

# Load Skins in First Tab
rainmeter(f'!DeactivateConfig OneLauncher FirstLaunch.ini')
rainmeter(f'!RefreshApp')
rainmeter(f'!ActivateConfig OneLauncher\IconBar {tabs[0]}.ini')
rainmeter(f'!ActivateConfig OneLauncher\WidgetArea {tabs[0]}.ini')