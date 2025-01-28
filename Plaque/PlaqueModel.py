#%%
from build123d import *
from ocp_vscode import show, show_object, reset_show, set_port, set_defaults, get_defaults
set_port(3939)
#%%
#%%

def svgtosketch(svg_file):
    fp = import_svg(svg_file)
    fp=list(fp)
    with BuildSketch() as sk:
        for f in fp:
            add(f)
    return sk.sketch

def StringToPart(textstring,font="Copperplate Gothic Bold",font_size=11,align=(Align.CENTER, Align.MIN),extrudeamount=1):
    with BuildPart() as TextMesh:
        with BuildSketch() as ns:
            Text(textstring,font="Copperplate Gothic Bold", font_size=font_size, align=align)
        extrude(amount=extrudeamount)
    return TextMesh.part
# %%
backplate_thickess=3
text_extrude_amount=2
borderthickness=2
# %%
Name = StringToPart("Joe Bloggs",font="Copperplate Gothic Bold", font_size=11,align=(Align.CENTER, Align.MIN),extrudeamount=text_extrude_amount)
Date = StringToPart("November 2023",font="Copperplate Gothic Bold", font_size=6, align=(Align.CENTER, Align.MIN),extrudeamount=text_extrude_amount)
#%%
backplate = svgtosketch("./Plaque/SVG/backplate.svg")
with BuildPart() as plaque:
    add(backplate)
    extrude(amount=backplate_thickess)
# %%
bsk = svgtosketch("./Plaque/SVG/border.svg")
with BuildPart() as border:
    add(bsk)
    extrude(amount=text_extrude_amount)
    topf = border.faces().filter_by(Axis.Z)
    offset(amount=-1,openings=topf)
#%%
plaquebox=plaque.part.bounding_box()
plaquewidth = plaquebox.size.X
centerX = plaquewidth/2
with BuildPart() as assemble:
    add(plaque.part)
    with Locations((0,0,backplate_thickess)):
        add(border.part)
    with Locations((centerX,15,backplate_thickess)):
        add(Name)
    with Locations((centerX,7,backplate_thickess)):
        add(Date)
reset_show()
show_object(assemble)
# %%
export_step(assemble.part,"plaque.step")
# %%

# %%

# %%
