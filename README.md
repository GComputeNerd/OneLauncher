![Home Page](Screenshots/HomePage.png)
# One Launcher
This is an Application Launcher for Rainmeter.

## Features
- Different Tabs for your different applications.
- Each Tab can have different wallpapers
- Automatically Generate app shortcuts for different tabs from file.

## Working

There are two skins in this root config.
-   IconBar
-   WidgetArea

IconBar is what you see in the top right, WidgetArea is what holds the shortcuts. You generate these using the `shortcut_gen.py` file.

## How to Install
### Part 1 : Loading The Skin
1. Install Rainmeter, and make sure you can run python3.
2. Download The `OneLauncher.rmskin` file.
3. Once Loaded you should see this.
![First Launch Screenshot](Screenshots/FirstLaunch.png)
_Congratulations ! You Made it Here!_

### Part 2 : Adding the Shortcuts
In the root folder, you will find a `Shortcut-Catalog` file. In this file, you will describe each of the different sections and what apps are included in them.

```
+Section1
-App1Name,PathToImage,PathToShortcut
-App2Name,PathToImage,PathToShortcut

+Section2
-App1Name,PathToImage,PathToShortcut
```

When you start a line with a `+`, that means You are making a new tab/section. i.e, To make a Game Tab. Write `+Game`.

When you start a line with a `-`, that means you are cataloging an app shortcut that you want in this menu. You have to write this information seperated by commas, Without any spaces. For example, to add notepad, I might write.

```
-Notepad,notepad.png,notepad.exe
```