from manim import *

class ContinuousMotion(Scene):
    def construct(self):
        # 1. 先只显示背景网格
        grid = NumberPlane()
        self.play(FadeIn(grid, run_time=1.5))
        self.wait(0.5)
        
        # 2. 定义向量场函数
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        
        # 3. 淡入流线动画
        stream_lines = StreamLines(
            func,
            stroke_width=3,
            max_anchors_per_line=30,
            color=[YELLOW, ORANGE, RED],
            stroke_opacity=0.7,
            virtual_time=10
        )
        self.play(FadeIn(stream_lines, run_time=2))
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(1)
        
        # 4. 添加标题和数学公式(提前显示)
        title = Text("连续运动场", font_size=40).to_edge(UP)
        equation = MathTex(r"\vec{F}(x,y) = \sin\left(\frac{x}{2}\right)\hat{i} + \cos\left(\frac{y}{2}\right)\hat{j}", 
                          font_size=30).next_to(title, DOWN)
        self.play(Write(title), Write(equation))
        self.wait(1)
        
        # 5. 添加说明文字
        explanation = Text("正弦和余弦函数创建的向量场", font_size=24).to_edge(DOWN)
        self.play(FadeIn(explanation))
        self.wait(1)
        
        # 6. 添加多个移动粒子展示流场
        dots = VGroup(*[Dot(color=BLUE, radius=0.05) for _ in range(10)])
        dots.arrange_in_grid(rows=2, cols=5, buff=0.5)
        self.play(FadeIn(dots))
        
        # 7. 让粒子沿着流场移动
        for dot in dots:
            self.play(
                dot.animate.move_to(func(dot.get_center())),
                rate_func=linear,
                run_time=3
            )
        
        # 8. 等待动画完成
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
