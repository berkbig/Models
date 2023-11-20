#%%
from build123d import *
from ocp_vscode import show, show_object, reset_show, set_port, set_defaults, get_defaults
set_port(3939)

#%%
with BuildPart() as test:
    Box(3,3,3)

show_object(test)
#%%
