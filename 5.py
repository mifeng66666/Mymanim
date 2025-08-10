from manim import*

class c5(Scene):
    def construct(self):
        only_1=Axes(
            x_range=[-10,10,1],
            y_range=[-2,10,1],
            x_length=13,
            y_length=7,
            tips=True,
            axis_config={"color": BLUE,
                         "include_numbers":True,
                         "font_size": 24
                         })
        self.play(Write(only_1),run_time=1)
        self.wait()
        g1=only_1.plot(lambda x:  x, color=RED,
                   x_range=[-2,8])
        self.play(Create(g1),run_time=2)
        g2=only_1.plot(lambda x: -x, color=GREEN,
                   x_range=[-8,2])
        self.play(Transform(g1,g2),run_time=2)
        self.wait()
