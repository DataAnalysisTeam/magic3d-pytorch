import  magic3d_pytorch as magic3d
import torch

prompt="A blue car driving on a highway"

mesh=magic3d.generate(prompt)


mesh.export("mesh.obj")

render= magic3d.render.PerspectiveCompare(fov=75, aspet=16/9, near=1, far=100)
render.render(mesh,camera=render.cameras[0])


magic3d.visulaize.show_mesh(mesh)