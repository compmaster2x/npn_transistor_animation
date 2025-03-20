from manim import *

class PNJunction(Scene):
    def construct(self):
        # Create semiconductor regions with terminals
        n_region = VGroup(
            Rectangle(width=3, height=3, color=BLUE,
                fill_opacity=0.5).move_to(LEFT * 1.5 + DOWN * 0.0),
            Line(ORIGIN, LEFT).move_to(LEFT * 3.5 + DOWN * 0),
        )
        n_terminal_text = Text("-", color=BLUE).move_to(LEFT * 3.5 + UP * 0.3)
        n_label = Text("N-тип", color=WHITE).next_to(n_region[0], UP)
        
        p_region = VGroup(
            Rectangle(width=3, height=3, color=RED,
                fill_opacity=0.5).move_to(RIGHT * 1.5 + DOWN * 0.0),
            Line(ORIGIN, RIGHT).move_to(RIGHT * 3.5 + DOWN * 0),
        )
        p_terminal_text = Text("+", color=RED).move_to(RIGHT * 3.5 + UP * 0.3)
        p_label = Text("P-тип", color=WHITE).next_to(p_region[0], UP)

        # Create a box representing the PN junction
        junction_box = Rectangle(width=6.2, height=3.2, color=GRAY,
                fill_opacity=0.5).move_to(UP * 0.5)
        junction_label = Text("PN перехід", color=WHITE).next_to(junction_box, UP)

        # Create depletion region
        depletion_region = Rectangle(width=1, height=3, color=YELLOW,
                fill_opacity=0.5).move_to(LEFT * 0.0 + DOWN * 0.0)
        depletion_label = Text("Запираючий \n шар",
                color=WHITE).next_to(depletion_region, DOWN)

        # Create electrons and holes
        electrons = VGroup(*[Dot(radius=0.05, color=BLUE) for _ in range(20)])
        holes = VGroup(*[Dot(radius=0.05, color=RED) for _ in range(20)])
        electrons.arrange_in_grid(buff=0.3)
        holes.arrange_in_grid(buff=0.3)
        electrons.move_to(n_region[0].get_left() + RIGHT * 1.5)
        holes.move_to(p_region[0].get_right() + LEFT * 1.5)

        rtes_logo= ImageMobject("RTES_logo.png")
        rtes_logo.scale(1.2)
        rtes_logo.to_edge(RIGHT+UP, buff=1)
        self.add(rtes_logo)
        nuchp_logo= ImageMobject("NUCHP_logo.png")
        nuchp_logo.scale(0.1)
        nuchp_logo.to_edge(LEFT+UP, buff=1)
        self.add(nuchp_logo)

# Animation: Forward biasing
        self.play(Create(p_region), Write(p_label))
        self.play(Create(n_region), Write(n_label))
        self.play(Create(holes), Write(electrons))
        self.wait(1)

        self.play(Create(depletion_region), Write(depletion_label))
        self.wait(1)

        self.play(Transform(depletion_label, Text("Пряме включення", color=WHITE).next_to(depletion_region, DOWN)),
                  run_time=1)
        self.play(Create(n_terminal_text), Write(p_terminal_text))

        self.play(ApplyMethod(depletion_region.stretch, 1/50, 0),
                  ApplyMethod(n_terminal_text.set_width, 0.7),
                  ApplyMethod(p_terminal_text.set_width, 0.7),
                  run_time=2)
        self.play(ApplyMethod(electrons.shift, RIGHT * 3),
                  ApplyMethod(holes.shift, LEFT * 3),
                  run_time=2)
        self.wait(1)

        electrons.move_to(n_region[0].get_left() + RIGHT * 1.5)
        holes.move_to(p_region[0].get_right() + LEFT * 1.5)

        self.play(
                Transform(depletion_label,
                    Text("Зворотне включення", color=WHITE).next_to(depletion_region, DOWN)),
                  Transform(n_terminal_text, 
                      Text("+", color=RED).move_to(LEFT  * 3.5 + UP * 0.3)),
                  Transform(p_terminal_text, 
                      Text("-", color=BLUE ).move_to(RIGHT * 3.5 + UP * 0.3)),
                  run_time=1)
        # Animation: Reverse biasing
        self.play(
                  ApplyMethod(electrons.shift, LEFT * 0.5),
                  ApplyMethod(holes.shift, RIGHT * 0.5),
                  ApplyMethod(depletion_region.stretch, 50/1, 0),
                  ApplyMethod(n_terminal_text.set_width, 0.7),
                  ApplyMethod(p_terminal_text.set_width, 0.7),
                  run_time=3)
        self.wait(1)

        # Reverse animation: Electrons and holes moving back
        self.play(FadeOut(depletion_region), FadeOut(depletion_label),
                  FadeOut(p_region), FadeOut(p_label),
                  FadeOut(n_region), FadeOut(n_label),
                  FadeOut(n_terminal_text), FadeOut(p_terminal_text),
                  FadeOut(electrons), FadeOut(holes))

if __name__ == "__main__":
    # To render the animation, use:
    # python -m manim your_script_name.py PNJunction -pql
    pass
