from manim import *

class Example(Scene):
    def construct(self):
        axe1=Axes(
            x_range=[-20,20,3],
            y_range=[-15,15,2],
            x_length=15,
            y_length=10,
            axis_config={"color": BLUE}
        )
        g1=axe1.plot(lambda x: np.sin(x), color=RED)
        g2=axe1.plot(lambda x: np.cos(x), color=GREEN)
        self.play(Write(axe1))
        self.play(Write(g1),run_time=3)
        self.play(Write(g2),run_time=3)
        self.wait()