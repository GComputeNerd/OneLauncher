from os.path import isfile

def checkImage(type, name):
    """
    Checks if the required asset exists, if not returns a default value.

    Arguments:
        type (string): Icon or Widget
        name (string): Name of required asset
    """

    root = ""

    if type == 'icon':
        root = "#@#\Images\\"
    else:
        root = "#@#\Shortcuts\\"
    
    if isfile(root.replace("#@#","@Resources") + name + ".png"):
        return root + name + ".png"
    else:
        return root + "Default.png"

icon_boilerplate = lambda menu: f"""[Rainmeter]
AccurateText=1

[Metadata]
Author=GComputeNerd

[Variables]
buttonSize=40
iconRoot="OneLauncher\IconBar"
widgetRoot="OneLauncher\WidgetArea"

[MeasureOnLoad]
Measure=Calc
Formula=Counter
IfEqualValue=1
IfEqualAction=!SetWallpaper #@#Wallpapers\{menu}.jpg Fill
UpdateDivider=-1"""

widget_boilerplate = f"""[Rainmeter]
Update=1000
AccurateText=1

[Metadata]
Author=GComputeNerd

[Variables]
buttonSize=28

[AppTextStyle]
FontSize=15
FontColor=white
AntiAlias=1

"""

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
LeftMouseDownAction=[!ActivateConfig #widgetRoot# {menu}.ini][!ActivateConfig #iconRoot# {menu}.ini]
"""

get_selected_icon_style = lambda menu, i: f"""

[{menu}Icon]
Meter=Image
Y=3
X={"0" if i == 0 else "25R"}
H=#buttonSize#
ImageName=#@#Images\{menu}.png
"""

bounding_box = lambda n: f"""

[BoundingBox]
Meter=Image
SolidColor=0,0,0,1
W={40*n + 25*(n-1)}
H=45
"""