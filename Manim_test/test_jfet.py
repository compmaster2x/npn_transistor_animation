from manim import *
import random

from manim_physics import *
# use a SpaceScene to utilize all specific rigid-mechanics methods
class JFET(SpaceScene):
    def construct(self):
        electrons = VGroup(*[Dot(radius=0.05, color=BLUE) for _ in range(20)])
        holes = VGroup(*[Dot(radius=0.05, color=RED) for _ in range(20)])
        electrons.arrange_in_grid(buff=0.3)
        
        rect = Square().shift(UP)
        rect.rotate(PI / 4)
        rect.set_fill(YELLOW_A, 1)
        rect.shift(UP * 2)
        rect.scale(0.5)




        ground = Rectangle(width=6, height=0.5, color=BLUE,
                fill_opacity=0.5).move_to(LEFT * 1.5 + DOWN * 0.0),
        wall1 = Line([-4, -3.5, 0], [-4, 3.5, 0])
        wall2 = Line([4, -3.5, 0], [4, 3.5, 0])
        #walls = VGroup(ground, wall1, wall2)
        #Vself.add(walls)
        #self.add(ground)

        self.play(
            DrawBorderThenFill(rect),
        )
        self.make_rigid_body( *[Dot(radius=0.1,
            color=BLUE).shift(UP*random.randint(1,10)*0.3 + LEFT
                *random.randint(-10,10)*0.3) for _ in range(200)])  # Mobjects will move with gravity
        self.make_static_body(ground)  # Mobjects will stay in place
        self.wait(10)
        # during wait time, the circle and rect would move according to the simulate updater
