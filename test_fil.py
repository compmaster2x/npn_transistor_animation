from manim import *



print("ja sasy biby");# my new code goes herer


class NPNTransistorAnimation(Scene):
    def construct(self):
        # Области транзистора
        emitter = Rectangle(width=2, height=3, color=BLUE, fill_opacity=0.5).move_to(LEFT * 3)
        base = Rectangle(width=1, height=3, color=PURPLE, fill_opacity=0.5).move_to(LEFT * 1)
        collector = Rectangle(width=2, height=3, color=RED, fill_opacity=0.5).move_to(RIGHT * 1.5)

      

        emitter_label = Text("Эмиттер", color=WHITE).next_to(emitter, DOWN)
        base_label = Text("База", color=WHITE).next_to(base, DOWN)
        collector_label = Text("Коллектор", color=WHITE).next_to(collector, DOWN)

        # Проводники
        collector_wire = Line(collector.get_top(), collector.get_top() + UP * 1.5)
        base_wire = Line(base.get_top(), base.get_top() + UP * 1.5)
        emitter_wire = Line(emitter.get_bottom(), emitter.get_bottom() + DOWN * 1.5)

        # Источники питания
        power_supply1 = Text("+", color=YELLOW).next_to(collector_wire, UP)
        power_supply2 = Text("-", color=YELLOW).next_to(emitter_wire, DOWN)
        power_supply3 = Text("+", color=YELLOW).next_to(base_wire, UP)

        # Электроны (синие точки)
        electrons = VGroup(*[Dot(radius=0.1, color=BLUE) for _ in range(10)])
        for i, e in enumerate(electrons):
            e.move_to(emitter.get_center() + RIGHT * (i % 2) * 0.2 + UP * (i // 2) * 0.2)

        # Добавляем всё на сцену
        self.add(emitter, base, collector)
        self.add(emitter_label, base_label, collector_label)
        self.add(collector_wire, base_wire, emitter_wire)
        self.add(power_supply1, power_supply2, power_supply3)
        self.add(electrons)

        # Анимация электронов
        electron_anims = []
        for e in electrons:
            path = ArcBetweenPoints(e.get_center(), collector.get_center(), angle=-PI/4)
            electron_anims.append(MoveAlongPath(e, path, run_time=2))

        # Анимация стрелок (направление тока)
        arrow_e_to_b = Arrow(emitter.get_right(), base.get_left(), buff=0.1, color=WHITE)
        arrow_b_to_c = Arrow(base.get_right(), collector.get_left(), buff=0.1, color=WHITE)

        # Добавляем и анимируем
        self.play(GrowArrow(arrow_e_to_b))
        self.wait(0.5)
        self.play(GrowArrow(arrow_b_to_c))
        self.wait(0.5)
        self.play(*electron_anims, run_time=2)

        self.wait(2)
        self.play(FadeOut(*self.mobjects))

if __name__ == "__main__":
    pass
