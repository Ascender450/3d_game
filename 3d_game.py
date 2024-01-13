from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

FirstPersonController()



Sky(texture="sky_day")

boxes = []
for n in range(20):
    for k in range(20):
        box = Button(
            model="cube",
            color="white",
            texture="miney.png",
            position=(k,0,n),
            parent=scene,
            origin_y=0.5

        )
        boxes.append(box)


hand = Entity(
    model="cube",
    color="peach",
    position=(0.5, -0.6),
    rotation=(30,-40),
    parent=camera.ui,
    scale=(0.1,1, 0.1)

)


app.run()