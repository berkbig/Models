#Designed to be used in Visual Studio Code with the ocp_vscode viewer
#installing build123D from the ocP viewer quick start tab is the easiest way
#to get up and running
# %%

from build123d import *
from ocp_vscode import *

# %%

#tweak these to customise MPK MINI PLUS Stand
keyboardangle = 20
standwidth = 10
strutthickness = 4

#Tweak these to support other similar controllers
bottomwidth = 178
frontheight =22
frontoverlap = 3
backheight = 38
backoverlap = 5
backrotateangle = 4
backfudgeoverlap=1

footdiameter = 13.5
footstart1 = 12
footstart2 = 155

with BuildPart() as stand:
    # keyboard mount
    with(Locations(Rotation(keyboardangle,0,0))):
        Box(standwidth,bottomwidth,strutthickness*2,align=[Align.CENTER,Align.MIN,Align.CENTER])
        with(Locations((0,0,-strutthickness))):
            Box(standwidth,strutthickness,frontheight+strutthickness,align=[Align.CENTER,Align.MAX,Align.MIN])
        with(Locations((0,bottomwidth,-strutthickness))):
            Box(standwidth,strutthickness,strutthickness*2,align=[Align.CENTER,Align.MIN,Align.MIN])
            with(Locations((0,0,(strutthickness*2) - backfudgeoverlap))):
                with(Locations(Rotation((backrotateangle,0,0)))):
                    Box(standwidth,strutthickness,backheight,align=[Align.CENTER,Align.MIN,Align.MIN])
                    with(Locations((0,strutthickness,backheight))):
                        Box(standwidth,strutthickness+backoverlap,strutthickness,align=[Align.CENTER,Align.MAX,Align.MIN])
        with(Locations((0,-strutthickness,frontheight))):
            Box(standwidth,3+frontoverlap,strutthickness,align=[Align.CENTER,Align.MIN,Align.MIN])
        #foot slots
        with(Locations((0,footstart1,0),(0,footstart2,0))):
            Box(standwidth,footdiameter,strutthickness,align=[Align.CENTER,Align.MIN,Align.MIN],mode=Mode.SUBTRACT)
    #base geometry
    Start = stand.vertices().sort_by(Axis.Z)[0]
    End = stand.vertices().sort_by(Axis.Y)[-1]
    Start.X = End.X = 0
    Diff = End-Start
    with(Locations((0,Start.Y,Start.Z))):
         Box(standwidth,Diff.Y,strutthickness,align=[Align.CENTER,Align.MIN,Align.MIN])
    with(Locations((0,End.Y,Start.Z))):
         Box(standwidth,strutthickness*2,Diff.Z,align=[Align.CENTER,Align.MAX,Align.MIN])
    with(Locations((0,Start.Y+(Diff.Y*0.5),Start.Z))):
         Box(standwidth,strutthickness*2,strutthickness+Diff.Z*0.5,align=[Align.CENTER,Align.CENTER,Align.MIN])

show(stand, axes=True, axes0=True, grid=(True, True, True), transparent=True)

# %%
export_step(stand.part,'./MPKMiniPlus Stand/stand.step')


# %%
