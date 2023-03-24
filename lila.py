from manim import *
import numpy as np

config.media_width = "50%"
config.verbosity = "WARNING"
# config.frame_height = 10
config.frame_width = 20

class GetZAxisLabelExample(ThreeDScene):
    
    def construct(self):
        # self.camera.background_color=WHITE
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES,  frame_center=(-0.3,0,0), zoom=1.0)

        # g = Graph([],[], labels=True)
        # g.add_vertices("pump", vertex_type=Rectangle, positions={"pump":(-4,4,0)}, vertex_config={"width": 1, "height": 1, "fill_opacity": 1})
        # g.add_vertices("junction1", vertex_type=Circle, positions={"junction1":(-1,-1,0)}, vertex_config={"radius": 1, "color": WHITE, "fill_opacity": 1})
        # g.add_edges(("pump", "junction1"))

        # g.add_vertices("junction2", vertex_type=Circle, positions={"junction2":(4,0,0)}, vertex_config={"radius": 1, "color": WHITE, "fill_opacity": 1})
        # g.add_edges(("junction1", "junction2"))

        # g.add_vertices("background1", positions={"background1":(2,2,-10)}, vertex_type=Circle, vertex_config={"color": WHITE, "fill_opacity": 0.5, "stroke_opacity": 0.5}) 
        # g.add_edges(("junction2", "background1"), edge_config={"stroke_opacity":0.5})

        # g.add_vertices("background2", positions={"background2":(-7,2,-8)}, vertex_type=Circle, vertex_config={"color": WHITE, "fill_opacity": 0.5, "stroke_opacity": 0.5}) 
        # g.add_edges(("junction1", "background2"), edge_config={"stroke_opacity":0.5})
        # g.add_vertices("background3", positions={"background3":(-7,-3,-8)}, vertex_type=Circle, vertex_config={"color": WHITE, "fill_opacity": 0.5, "stroke_opacity": 0.5}) 
        # g.add_edges(("junction1", "background3"), edge_config={"stroke_opacity":0.5})

        # self.play(Create(g))



        junction1_ax = ThreeDAxes(x_range=(0, 4, 1), x_length=2, y_range=(0,4,1), y_length=2, axis_config={
                "include_ticks": False,
                # "include_tip": False,
            },
            z_axis_config={
                "include_tip":False,
                "stroke_opacity": 0,
                "fill_opacity": 0
            } )
        junction1_ax.set_x(-7)
        junction1_ax.set_y(4)
        junction1_ax.set_z(0)
        labx = junction1_ax.get_x_axis_label(Tex("Time"))
        laby = junction1_ax.get_y_axis_label(Tex("Pressure"))
        line1 = junction1_ax.plot(lambda t: np.cos(t) + 0.5 * np.cos(9 * t) + (1 / 7) * np.cos(12 * t) + 2, color=BLUE,)
        junction1_group = VGroup(junction1_ax, line1)


        junction2_ax = ThreeDAxes(x_range=(0, 4, 1), x_length=2, y_range=(0,4,1), y_length=2, axis_config={
                "include_ticks": False,
                # "include_tip": False,
            },
            z_axis_config={
                "include_tip":False,
                "stroke_opacity": 0,
                "fill_opacity": 0
            } )
        junction2_ax.set_x(7)
        junction2_ax.set_y(0)
        junction2_ax.set_z(0)
        labx = junction2_ax.get_x_axis_label(Tex("Time"))
        laby = junction2_ax.get_y_axis_label(Tex("Pressure"))
        line2 = junction2_ax.plot(lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t) + 2, color=RED,)
        junction2_group = VGroup(junction2_ax, line2)


        junction3_ax = ThreeDAxes(x_range=(0, 4, 1), x_length=2, y_range=(0,4,1), y_length=2, axis_config={
                "include_ticks": False,
                # "include_tip": False,
            },
            z_axis_config={
                "include_tip":False,
                "stroke_opacity": 0,
                "fill_opacity": 0
            } )
        junction3_ax.set_x(-2)
        junction3_ax.set_y(-4)
        junction3_ax.set_z(0)
        
        labx = junction3_ax.get_x_axis_label(Tex("Time"))
        laby = junction3_ax.get_y_axis_label(Tex("Pressure"))
        line3 = junction3_ax.plot(lambda t: np.cos(t) + 0.5 * np.cos(3 * t) + (1 / 7) * np.cos(20 * t) + 2, color=RED,)
        junction3_group = VGroup(junction3_ax, line3)


        self.add(junction3_group, junction1_group, junction2_group)
        # self.play(FadeIn(junction2_ax), FadeIn(labx), FadeIn(laby))
        # self.play(FadeIn(junction1_group), FadeIn(junction2_group), FadeIn(junction3_group))

        # g.remove_vertices("pump", "junction1", "junction2", "background1", "background2", "background3")

        junction1_group.set_x(0)
        junction1_group.set_y(0)

        junction2_group.set_x(0)
        junction2_group.set_y(0)

        junction3_group.set_x(-1.25)
        junction3_group.set_y(0)
        junction3_group.rotate(90, [0,1,0])
        self.remove(junction2_group)
        self.wait()

        dot_1 = Dot3D(point=junction1_ax.coords_to_point(0, 0, 1), color=RED)
        dot_2 = Dot3D(point=junction1_ax.coords_to_point(2, 0, 0), radius=0.1, color=BLUE)
        dot_3 = Dot3D(point=[0, 0, 0], radius=0.1, color=ORANGE)
        self.add(dot_1, dot_2,dot_3)

        self.set_camera_orientation(phi=45 * DEGREES, theta=45 * DEGREES)

        resolution_fa = 10

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 0.4, [0.0, 0.0]
            d = np.linalg.norm(np.array([x - mu[0], y - mu[1]]))
            z = np.exp(-(d ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])

        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-1.5, +1.5],
            u_range=[-1.5, +1.5]
        )
        self.add(gauss_plane)
        self.wait()



# %%
