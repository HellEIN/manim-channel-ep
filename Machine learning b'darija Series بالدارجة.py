from manim import *

# 1st -> to 2nd frame
class FirstVid(MovingCameraScene):
    def construct(self):
        # plain = NumberPlane()
        # self.add(plain)

        # Colors
        tiel = "#0fd2c3"
        darkish_blue = "#337493"
        green_light = "#F4F269"
        green_dark= "#99fb99"


        # Text Creation:
        ml_txt = Text('ML',gradient=(tiel,darkish_blue), font_size=120, stroke_width=2.4, stroke_color= WHITE)
        ml_full_txt = Text('Machine Learning',gradient=(tiel,darkish_blue), font_size=120, stroke_width=2.4, stroke_color= WHITE)


        # Animation:

        #! 1st frame
            #* Animation:
        self.wait(1)
        self.play(DrawBorderThenFill(ml_txt), run_time = 2)
        self.wait(1)

        #! 2nd frame
            #* Animation:
        self.play(Transform(ml_txt, ml_full_txt), run_time = 1.3)
        self.wait(2)

        #! 3rd frame
            #* Animation:
        self.play(ml_txt.animate.scale(0.25,scale_stroke=True).to_edge(UL), run_time = 1.3)
        self.wait(2)

        #! 4th frame

            #? dots attributes
        dot_g = VGroup(*[Dot(color=WHITE) for _ in range(3)])
        dot_g.arrange(DOWN, buff=0.5)
        dot_g.scale(0.5)

            #? text attribut
        ml_type = Text('Machine Learning Types:',gradient=(green_light,green_dark), weight=BOLD,font_size= 20,disable_ligatures=True)

        ml_type.to_edge((UP*2.8)+(LEFT*2))
            # headers content:
        type_content = VGroup(
            Text('Supervised Learning', font_size=17,disable_ligatures=True,line_spacing=-3),
            Text('Unsupervised Learning', font_size=17,disable_ligatures=True,line_spacing=-3),
            Text('Reinforcement Learning', font_size=17,disable_ligatures=True,line_spacing=-3))
            #? aligning text
        type_content.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        type_content.next_to(ml_type,(DOWN*1))


            #? Align dots with text
        for dot, text in zip(dot_g, type_content):
            dot.next_to(text, LEFT, buff=0.2)

            #* Animation:
        self.play(Write(ml_type, run_time=1))
        self.play(Create(dot_g),Write(type_content, run_time=1))
        self.wait(3)

        #! 5th frame
        #? text attribut
        algo = Text('Machine Learning Algorithms:',gradient=(green_light,green_dark), weight=BOLD,font_size= 20,disable_ligatures=True)
        algo.to_edge((UP*7)+(LEFT*2))

        algo_content = VGroup(
            Text('Linear Regression', font_size=17,disable_ligatures=True,line_spacing=-3),
            Text('Logistic Regression', font_size=17,disable_ligatures=True,line_spacing=-3),
            Text('k-nearest neighbors (KNN)', font_size=17,disable_ligatures=True,line_spacing=-3),
            Text('(...etc)', font_size=17,disable_ligatures=True,line_spacing=-3),
            )

        #? Align algo centent with algo
        algo_content.arrange(DOWN,aligned_edge=LEFT, buff=0.2)
        algo_content.next_to(algo,(DOWN))
        algo_content.align_to(type_content,LEFT)


        dot_alg = VGroup(*[Dot(color=WHITE) for _ in range(4)])
        dot_alg.scale(0.5)

        #? Align algo centent with dots
        for dot, text in zip(dot_alg,algo_content):
            dot.next_to(text,LEFT,buff=0.2)

        #* Animation:
        self.play(Write(algo, run_time= 1))
        self.play(Create(dot_alg),Write(algo_content), run_time=1)
        self.wait(2)
        ################## The code above is perferct dont touch it  ######################

        self.play(FadeOut(VGroup(dot_alg,dot_g,type_content,algo_content,algo,ml_type)),runtime=2)
        self.wait(2)
        #! 6th frame

        math_text = Text("Math Prerequisite:", gradient=(green_light,green_dark),font_size=90, stroke_width=2.4, stroke_color= WHITE, disable_ligatures=True, weight=BOLD)

        #* Animation:
        self.play(Write(math_text))
        self.wait(3)

        self.play(math_text.animate.scale(0.25,scale_stroke=True).to_edge(LEFT*2 + UP*3), run_time = 1)
        self.wait(3)




        ##########################!Circle scene ############################




        #! Circles
        # Define colors
        blue = BLUE
        green = GREEN
        white = WHITE

        # Create circles
        circle_left = Circle(radius=2, color=blue, fill_opacity=0.5).shift(DOWN*0.5)
        circle_right = Circle(radius=2, color=green, fill_opacity=0.5).shift(DOWN*0.5)
        circle_right.shift(RIGHT * 2)
        circle_right.scale(1.3)

        # Text labels
        stats_text = Tex("Statistics").shift(DOWN*0.5)
        prob_text = Tex("Probability").shift(DOWN*0.5)
        prob_text.shift(RIGHT * 3)

        # Add to scene
        # Circle statistics
        self.play(DrawBorderThenFill(circle_left), run_time=2)
        self.play(Write(stats_text), run_time=2)
        self.wait(2)

        # Shift circle statistics
        self.play(circle_left.animate.scale(1.3).shift(LEFT * 1), stats_text.animate.scale(1).shift(LEFT * 2))

        # Circle probability
        self.play(DrawBorderThenFill(circle_right), run_time=2)
        self.play(Write(prob_text), run_time=2)
        self.wait(2)

        # Create the "ML" text to be placed exactly in the middle of the two circles
        ml_text = Text("ML").move_to((circle_left.get_center() + circle_right.get_center()) / 2)

        # Write "ML" in the exact middle of the overlap
        self.play(Write(ml_text), run_time=2)
        self.play(Indicate(ml_text), run_time=2)
        self.wait(3)

        # Zoom
        circle_ml = Circle(radius=0.1, color=RED, fill_opacity=0.5).move_to((circle_left.get_center() + circle_right.get_center()) / 2)
        circle_ml.shift(DOWN * 1)
        # Set stroke opacity to 0, making the border invisible
        circle_ml.set_stroke(width=0.1, opacity=7)

        # Create the text "AI" and place it at the center of the red circle
        AI_text = Text("AI", font= 'Ariel').move_to(circle_ml.get_center()).scale(0.1)

        # Draw the red circle
        self.play(DrawBorderThenFill(circle_ml))

        # Write "AI" in the middle of the red circle
        self.play(Write(AI_text))

        self.wait(2)

        # Zoom into the red circle by adjusting the camera frame center and width
        self.play(self.camera.frame.animate.move_to(circle_ml.get_center()).scale(0.1))

        # Wait to show the final zoomed-in view
        self.wait(3)

        # Indicat AI text
        self.play(Indicate(ml_text), run_time=2)

        self.wait(3)

