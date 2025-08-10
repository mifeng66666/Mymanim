from manim import *

class LaplaceEquation(Scene):
    def construct(self):
        # 创建拉普拉斯方程
        equation = MathTex(
            r"\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0",
            font_size=48
        )
        
        # 添加标题
        title = Text("拉普拉斯方程", font_size=36).to_edge(UP)
        
        # 显示标题
        self.play(Write(title))
        self.wait(0.5)
        
        # 显示方程
        self.play(Write(equation))
        self.wait(2)
        
        # 解释方程
        explanation = Text(
            "这是一个描述二维稳态热传导的偏微分方程",
            font_size=24
        ).next_to(equation, DOWN)
        
        self.play(Write(explanation))
        self.wait(2)
