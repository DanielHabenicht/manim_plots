from manim import *

class WaterNetwork(Scene):
    def construct(self):
        # Create nodes for the water network
        node_A = Dot().move_to(LEFT * 2)
        node_B = Dot().move_to(UP)
        node_C = Dot().move_to(RIGHT * 2)
        node_D = Dot().move_to(DOWN)

        # Create pipes connecting the nodes
        pipe_AB = Line(node_A, node_B)
        pipe_BC = Line(node_B, node_C)
        pipe_CD = Line(node_C, node_D)
        pipe_DA = Line(node_D, node_A)

        # Create labels for the nodes
        label_A = Tex("A").next_to(node_A, LEFT)
        label_B = Tex("B").next_to(node_B, UP)
        label_C = Tex("C").next_to(node_C, RIGHT)
        label_D = Tex("D").next_to(node_D, DOWN)

        # Create labels for the pipes
        label_AB = Tex("1").next_to(pipe_AB, UP)
        label_BC = Tex("2").next_to(pipe_BC, RIGHT)
        label_CD = Tex("3").next_to(pipe_CD, DOWN)
        label_DA = Tex("4").next_to(pipe_DA, LEFT)

        # Add everything to the scene
        self.play(
            Create(node_A),
            Create(node_B),
            Create(node_C),
            Create(node_D),
            Create(pipe_AB),
            Create(pipe_BC),
            Create(pipe_CD),
            Create(pipe_DA),
            Write(label_A),
            Write(label_B),
            Write(label_C),
            Write(label_D),
            Write(label_AB),
            Write(label_BC),
            Write(label_CD),
            Write(label_DA),
        )

        # Add animation to show flow of water
        flow_animation = VGroup(
            VGroup(node_A, label_A),
            VGroup(node_B, label_B),
            VGroup(node_C, label_C),
            VGroup(node_D, label_D),
            pipe_AB,
            pipe_BC,
            pipe_CD,
            pipe_DA,
            label_AB,
            label_BC,
            label_CD,
            label_DA,
        ).animate.shift(RIGHT * 4).scale(0.8)

        self.play(flow_animation)

        self.wait(2)