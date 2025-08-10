from manim import *
from manim.utils.tex_templates import TexTemplate

class HeatEquation(Scene):
    def construct(self):
        
        # 使用MiKTeX渲染的数学公式表示
        tex_template = TexTemplate()
        tex_template.tex_command = "xelatex"
        equation = Tex(
            r"Heat Equation: $\partial_t u = \alpha \Delta u$",
            color=WHITE,
            tex_template=tex_template
        )
        
        # 添加标题
        title = Text("热传导方程", font_size=40).to_edge(UP)
        
        # 创建初始温度分布
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=4,
        )
        
        # 初始温度分布函数
        def temp_func(x):
            return 4 * np.exp(-(x-5)**2 / 4)
        
        # 创建温度曲线
        initial_temp = axes.plot(
            temp_func,
            color=BLUE,
        )
        
        # 动画序列
        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(equation))
        self.wait(1)
        self.play(equation.animate.to_edge(UP, buff=1.5))
        self.play(Create(axes))
        self.play(Create(initial_temp))
        
        # 模拟热传导过程
        for t in np.arange(0.1, 2, 0.2):
            new_temp = axes.plot(
                lambda x: temp_func(x) * np.exp(-t),
                color=BLUE,
            )
            self.play(Transform(initial_temp, new_temp), run_time=0.5)
        
        self.wait(2)
