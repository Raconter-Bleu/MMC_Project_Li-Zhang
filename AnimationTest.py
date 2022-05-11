from manim import *
import math

#manim -pqh AnimationTest.py Section7

eqa_section_1 = [
                [r"(\frac{\partial f}{\partial x},\frac{\partial f}{\partial x},\frac{\partial f}{\partial x} )|_{x=x_0,y=y_0,z=z_0}",2],
                [r"\nabla f = \begin{pmatrix} \vec{i} & \vec{j} & \vec{k}\end{pmatrix}\begin{pmatrix} \frac{\partial}{\partial x} \\\frac{\partial}{\partial y} \\\frac{\partial }{\partial z} \end{pmatrix}= \vec{i}\cdot\frac{\partial f}{\partial x}+\vec{j}\cdot\frac{\partial f}{\partial x}\cdot+\vec{k}\cdot\frac{\partial f}{\partial x}",12],
                ]

eqa_section_2 = [
                [r"d\vec{l}=\begin{pmatrix} e_1 & e_2 & e_3\end{pmatrix} \begin{pmatrix} f_1de_1 \\ f_2de_2 \\ f_3de_3\end{pmatrix} = \sum_{i}\hat{e_i}f_ide_i",6],
                [r"dT=\sum_i \frac{\partial T}{\partial e_i}de_i",2],
                [r"dT= \nabla T \cdot d\vec{l} =\sum_i (\nabla T)_if_ide_i",2],
                [r"\nabla T=\sum_i \frac{1}{f_i}\frac{\partial T}{\partial e_i}",2],
                [r"\nabla T=\sum_i \hat{e_i} \frac{1}{f_i}\frac{\partial T}{\partial e_i}",2],
                ]

eqa_section_3 = [
                [r"ds^2=\sum_{i j}g_{ij}de_ide_j",13],
                [r"L = \int_a^b\sqrt{\sum_{i j}g_{ij}\frac {dx_i}{dt}\frac {dx_j}{dt}}dt",6],
                [r"G = J^TJ",4],
                [r"\left\{ \begin{array}{lr} x=  \rho cos\phi \\  y= \rho sin\phi\end{array} \right.",2],
                [r"J = \frac{\partial (x,y)}{\partial (\rho,\phi)} = \begin{pmatrix} cos\theta & -\rho sin\theta \\ sin\theta&\rho cos\theta \end{pmatrix}",2],
                [r"G = J^TJ = \begin{pmatrix} cos\theta &  sin\theta \\ -\rho sin\theta&\rho cos\theta \end{pmatrix} \begin{pmatrix} cos\theta & -\rho sin\theta \\ sin\theta&\rho cos\theta \end{pmatrix} =  \begin{pmatrix} 1 & 0 \\ 0&\rho^2 \end{pmatrix}",2],
                [r"f_1=1,f_2=\rho",2.5],
                [r"f_1=1,f_2=\rho,f_3=1",8],
                [r"f_1=1,f_2=r,f_3=r sin\theta",8]
                ]

eqa_section_4 = [
                [r"-\iiint\limits_{CV} \frac{\partial\rho}{\partial t}dB= \varoiint \rho(\vec{V}\cdot\vec{n})dA",9],
                [r"\frac{\partial \rho}{\partial t}+\nabla\cdot(\rho\vec{V})=0",5.5],
                [r"-\frac{\partial m }{\partial t}=-\frac{\partial\rho}{\partial t}dxdydz",2],
                [r"\frac{\partial (\rho u)}{\partial x}dxdydz",2],
                [r"\frac{\partial (\rho v)}{\partial y}dxdydz",2],
                [r"\frac{\partial (\rho w)}{\partial z}dxdydz",2],
                [r"[\frac{\partial (\rho u)}{\partial x}+\frac{\partial (\rho v)}{\partial y}+\frac{\partial (\rho w)}{\partial z}]dxdydz",2]
                ]

eqa_section_5 = [
                [r"\Phi_A(\Sigma) = \oint_\Sigma \vec{A}\cdot \vec{n}dS",40]
                ]

eqa_section_6 = [
                [r"\nabla^2f \quad or \quad \nabla \cdot \nabla",4]
                ]

eqa_section_7 = [
                [r"\nabla^2u = \frac{d^2u}{dx^2}",2],
                [r"\Delta ^n u = f^{(n)}(\xi_n)\Delta x^n",2],
                [r"\frac{d^2u}{dx^2} = \frac{d^2u}{dx^2}",2],
                [r"\frac{d^2u}{dx^2} = \frac{\Delta^2u}{\Delta x^2} = \frac{[u(x+\Delta x)-u(x)]-[u(x)-u(x-\Delta x)]}{\Delta x^2}\\ =  \frac{2}{\Delta x^2} [\frac{u(x+\Delta x)+u(x-\Delta x)}{ 2}-u(x)]",18],
                [r"\delta = \frac{1}{r^2}[\frac{\oint_{S_{r}(x)}u(x+\vec{r})dS}{S}-u(x)]",9],
                [r"\begin{aligned}&\delta=\frac{1}{r^2}[\frac{\oint_{S_{r}(x)}u(x+\vec{r})dS}{S}-u(x)]\\ &=\frac{1}{Sr^2} \oint_{S_{r}(x)}[u(x+\vec{r})-u(x)]dS\\ &\approx \frac{1}{Sr^2} \oint_{S_{r}(x)}\nabla u(x+\vec{r})\cdot \vec{r}dS\\ &= \frac{1}{Sr^2} \oint_{S_{r}(x)}\nabla u\cdot r\vec{n}dS\end{aligned}",7],
                [r"\int^b_au'(x)dx = u(b)-u(a)",4],
                [r"\int_V u_{x_i}dV = \int_{\partial V}un^idS",2],
                [r"\delta = \frac{1}{Sr^2} \oint_{S_{r}(x)}\nabla u\cdot r\vec{n}dS \approx \frac{1}{Sr} \oint_{B_{r}(x)}\nabla ^2 udV",4],
                [r"\int_V\nabla ^2 udV \to \nabla^2u(x)\times V",6.5],
                [r"V = \frac{Sr}{n}",3],
                [r"\delta=\frac{1}{n}\nabla^2u",3.5],
                [r"\nabla^2\phi = 0",21.5],
                [r"\phi(x) = \frac{1}{|S_r(x)|}\oint_{S_r(x)}udS =  \frac{1}{|B_r(x)|}\int_{B_r(x)}udV",33.5]
                ]

eqa_section_8 = [
                [r"\frac{\partial T}{\partial t} = \alpha\nabla^2T(\alpha>0)",39]
                ]

def Sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1;
    elif x < 0:
        return -1

def Distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def DotCpy(dot1, dot2):
    if dot1.get_x()==dot2.get_x() and dot1.get_y() == dot2.get_y():
        return True
    return False

myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{esint}")

class Section1(Scene):
    def construct(self):
        title = Text("Nabla Operator", font_size=70)
        self.wait(1)
        self.play(FadeIn(title), run_time=1)
        self.wait(7)
        self.play(FadeOut(title), run_time=1)
        section = eqa_section_1
        for i in range(len(section)):
            tex_eqa = MathTex(section[i][0],tex_template=myTemplate)
            delay = section[i][1]
            self.play(Write(tex_eqa), run_time=2)
            self.wait(delay)
            self.play(FadeOut(tex_eqa), run_time=1)

class Section2(Scene):
    def construct(self):
        title = VGroup(
                      Text("Nabla operator", font_size=70),
                      Text("and coordinate transformation", font_size=70)
                      ).arrange(DOWN)
        self.wait(1)
        self.play(FadeIn(title), run_time=1)
        self.wait(9)
        self.play(FadeOut(title), run_time=1)
        section = eqa_section_2
        for i in range(len(section)):
            tex_eqa = MathTex(section[i][0],tex_template=myTemplate)
            delay = section[i][1]
            self.play(Write(tex_eqa), run_time=2)
            self.wait(delay)
            self.play(FadeOut(tex_eqa), run_time=1)

class Section3(Scene):
    def construct(self):
        title = Text("Metric tensors", font_size=70)
        self.wait(1)
        self.play(FadeIn(title), run_time=1)
        self.wait(2.5)
        self.play(FadeOut(title), run_time=1)
        section = eqa_section_3
        for i in range(len(section)):
            tex_eqa = MathTex(section[i][0],tex_template=myTemplate)
            delay = section[i][1]
            self.play(Write(tex_eqa), run_time=2)
            self.wait(delay)
            self.play(FadeOut(tex_eqa), run_time=1)

class Section4(Scene):
    def construct(self):
        title = Text("Physical meaning", font_size=70)
        self.wait(1)
        self.play(FadeIn(title), run_time=1)
        self.wait(9)
        self.play(FadeOut(title), run_time=1)
        section = eqa_section_4
        for i in range(len(section)):
            tex_eqa = MathTex(section[i][0],tex_template=myTemplate)
            delay = section[i][1]
            self.play(Write(tex_eqa), run_time=2)
            self.wait(delay)
            self.play(FadeOut(tex_eqa), run_time=1)

class Section5(Scene):
    def construct(self):
        title = Text("Laplace operator", font_size=70)
        subtitle = Text("Divergence", font_size=70)
        self.wait(1)
        self.play(FadeIn(title), run_time=1)
        self.wait(3)
        self.play(FadeOut(title), run_time=1)
        self.wait(1)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(5)
        self.play(FadeOut(subtitle), run_time=1)
        section = eqa_section_5
        for i in range(len(section)):
            tex_eqa = MathTex(section[i][0],tex_template=myTemplate)
            delay = section[i][1]
            self.play(Write(tex_eqa), run_time=2)
            self.wait(delay)
            self.play(FadeOut(tex_eqa), run_time=1)

class Section6(Scene):
    def construct(self):
        title = Text("Laplacian", font_size=70)
        self.wait(1)
        self.play(FadeIn(title), run_time=1)
        self.wait(6)
        self.play(FadeOut(title), run_time=1)
        section = eqa_section_6
        for i in range(len(section)):
            tex_eqa = MathTex(section[i][0],tex_template=myTemplate)
            delay = section[i][1]
            self.play(Write(tex_eqa), run_time=2)
            self.wait(delay)
            self.play(FadeOut(tex_eqa), run_time=1)

class Section7(Scene):
    def construct(self):
        title = Text("Math meaning", font_size=70)
        self.wait(1)
        self.play(FadeIn(title), run_time=1)
        self.wait(14)
        self.play(FadeOut(title), run_time=1)
        section = eqa_section_7
        for i in range(len(section)):
            tex_eqa = MathTex(section[i][0],tex_template=myTemplate)
            delay = section[i][1]
            self.play(Write(tex_eqa), run_time=2)
            self.wait(delay)
            self.play(FadeOut(tex_eqa), run_time=1)

class Section8(Scene):
    def construct(self):
        title = Text("Heat conduction equation", font_size=70)
        self.wait(1)
        self.play(FadeIn(title), run_time=1)
        self.wait(6)
        self.play(FadeOut(title), run_time=1)
        section = eqa_section_8
        for i in range(len(section)):
            tex_eqa = MathTex(section[i][0],tex_template=myTemplate)
            delay = section[i][1]
            self.play(Write(tex_eqa), run_time=2)
            self.wait(delay)
            self.play(FadeOut(tex_eqa), run_time=1)

class New3DCoord(ThreeDScene):
    def construct(self):
        resolution_fa = 42
        self.set_camera_orientation(phi=75 * DEGREES, theta=10 * DEGREES)
        axes = ThreeDAxes(x_range=(-5, 5, 1), y_range=(-5, 5, 1), z_range=(-5, 5, 1))

        e1 = Arrow3D(start=ORIGIN, end=[1,1,1], color=RED)
        e2 = Arrow3D(start=ORIGIN, end=[-1,1,-1], color=GREEN)
        e3 = Arrow3D(start=ORIGIN, end=[2,0.5,-0.8], color=BLUE)
        newBasis = VGroup(e1,e2,e3)

        self.play(Create(axes))
        self.wait(2)
        self.add(newBasis)
        self.wait()
        self.play(Uncreate(axes))

        text_newBasis = Tex(r" $\begin{pmatrix} \hat{e_1} & \hat{e_2} & \hat{e_3}\end{pmatrix}^T$")
        self.add_fixed_in_frame_mobjects(text_newBasis.to_corner(RIGHT+UP))
        self.play(FadeIn(text_newBasis))
        self.wait()
        self.play(newBasis.animate.shift(DOWN*4))
        text_coord = VGroup(Tex(r"$\begin{pmatrix} e_1 & e_2 & e_3\end{pmatrix}^T$").shift(RIGHT*2), Tex(r"$\begin{pmatrix} e_1+de_1 & e_2+de_2 & e_3+de_3\end{pmatrix}^T$").shift(RIGHT*2+DOWN*1))
        self.add_fixed_in_frame_mobjects(text_newBasis.to_corner(RIGHT+UP), text_coord)
        
        self.play(FadeIn(text_coord))
        

class FcVectorField(Scene):
    @staticmethod
    def Fc(des, src, pol):
        deltax = src[0]-des[0]
        deltay = src[1]-des[1]
        if deltax == 0:
            angle = math.pi/2;
        else:
            angle = math.atan(abs(deltay)/abs(deltax))
        dis = Distance(src[0], src[1], des[0], des[1])
        Fc = 2/(dis**2)
        ret = np.array([Sign(deltax)*pol*Fc*math.cos(angle), Sign(deltay)*pol*Fc*math.sin(angle)])
        return ret

    def construct(self):
        ax = Axes(
            x_range=[0, 12, 0.5], y_range=[0, 12, 0.5], axis_config={"include_tip": False}
        )
        coordCP = (6, 4.5)
        coordNP1 = (3, 7.5)
        coordNP2 = (3, 1.5)
        coordNP3 = (9, 1.5)
        coordNP4 = (9, 7.5)
        cp = Dot(point=[ax.coords_to_point(6, 4.5)], radius=0.04)   #charge positive
        np1 = Dot(point=[ax.coords_to_point(3, 7.5)], radius=0.04)  #charge negative
        np2 = Dot(point=[ax.coords_to_point(3, 1.5)], radius=0.04)
        np3 = Dot(point=[ax.coords_to_point(9, 1.5)], radius=0.04)
        np4 = Dot(point=[ax.coords_to_point(9, 7.5)], radius=0.04)

        self.play(Create(ax))
        self.wait()
        self.add(cp, np1, np2, np3, np4)
        self.wait()

        for i in np.arange(0.5, 11, 0.5):
            for j in np.arange(0.5, 11, 0.5):
                coordDot = (i, j)
                dot = Dot(ax.coords_to_point(i, j))
                if  DotCpy(dot, cp) or DotCpy(dot, np1) or DotCpy(dot, np2) or DotCpy(dot, np3) or DotCpy(dot, np4):
                    continue
                else:
                    F = self.Fc(coordDot, coordCP, -1) + self.Fc(coordDot, coordNP1, 1) + self.Fc(coordDot, coordNP2, 1) + self.Fc(coordDot, coordNP3, 1) + self.Fc(coordDot, coordNP4, 1)
                    length = math.sqrt(F[0]**2+F[1]**2)
                    if length>0.5 :
                        ratio = length/0.4
                        F[0] /= ratio
                        F[1] /= ratio
                        length = 0.4
                    vector = Arrow(start = [ax.coords_to_point(i, j)], end = [ax.coords_to_point(i+F[0], j+F[1])])
                    vector.set_color(BLUE_D)
                    self.add(vector)
        self.wait(3)
        redCircle = Circle(radius=0.8, color=RED).move_to(ax.c2p(3,7.5))
        greenCircle = Circle(radius=0.8, color=GREEN).move_to(ax.c2p(6,4.5))
        self.play(FadeIn(redCircle, greenCircle))
        self.wait(7)
        self.play(redCircle.animate.scale(0.2), greenCircle.animate.scale(0.2), run_time=4)
        self.wait(5.5)
        self.play(FadeIn(Tex(r"$\nabla A = \lim\limits_{\delta V \to x}\frac{\Phi_A(\Sigma)}{\delta V}$", font_size=40).shift(UP*3.2)))
        self.wait(25)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects],
            run_time=1
        )

class Gradient(ThreeDScene):
    def construct(self):
        resolution_fa = 42
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        axes = ThreeDAxes(x_range=(-5, 5, 1), y_range=(-5, 5, 1), z_range=(-10, 10, 2))
        def param_surface(u, v):
            x = u
            y = v
            z = 1.6**(4-u**2)*math.sin(v)
            return z
        surface_plane = Surface(
            lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=[-4, 4],
            u_range=[-4, 4],
            )
        surface_plane.set_style(fill_opacity=1)
        surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        self.play(Create(surface_plane))
        self.wait(3.5)
        for i in np.arange(-4, 4, 2):
            for j in np.arange(-4, 4, 2):
                value = 1.6**(4-i**2)*math.sin(j)
                partial_z_x = 100*(1.6**(4-(i+0.01)**2)*math.sin(j)-value)
                partial_z_y = 100*(1.6**(4-i**2)*math.sin(j+0.01)-value)
                #partial_z_x = -2*i*value*math.log(1.6)
                #partial_z_y = 1.6**(4-i**2)*math.cos(j)
                self.add(Arrow(start = axes.c2p(i, j, value), end = axes.c2p(i+partial_z_x, j+partial_z_y, value-1)))
        self.wait()

        theta_init = 45
        delta_theta = 180/480
        for i in range(480):
            theta_init += delta_theta
            self.set_camera_orientation(phi=60 * DEGREES, theta=theta_init * DEGREES)
            self.wait(1/60)
        self.wait(10)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class Divergence(ThreeDScene):
    def construct(self):
        resolution_fa = 42
        self.set_camera_orientation(phi=75 * DEGREES, theta=10 * DEGREES)
        axes = ThreeDAxes(x_range=(-5, 5, 1), y_range=(-5, 5, 1), z_range=(-10, 10, 2))
        box = Cube(side_length=3, fill_opacity=0.5, fill_color = BLUE)
        
        text_dx = Text("dx",  font_size=30).shift(DOWN*1.5+RIGHT*1.8)
        text_dy = Text("dy",  font_size=30).shift(LEFT*0.5+DOWN*2.2)
        text_dz = Text("dz",  font_size=30).shift(RIGHT*1)
        text_coord = VGroup(text_dx, text_dy, text_dz)

        text_mass_reduction = VGroup(
                                    Text("mass reduction", font_size=35).shift(RIGHT*4.8+UP*3),
                                    Tex(r"$-\frac{\partial m }{\partial t}=-\frac{\partial\rho}{\partial t}dxdydz$").shift(RIGHT*4.8+UP*2)
                                    )

        arrow_init__x_in = Arrow3D(start=[3, 0, 0], end=[2.6, 0, 0])
        debit_x_in = Arrow3D(start=[3, 0, 0], end=[1.8, 0, 0])
        arrow_init__x_out = Arrow3D(start=[-1.8, 0, 0], end=[-2.2, 0, 0])
        debit_x_out = Arrow3D(start=[-1.8,0, 0], end=[-3, 0, 0])

        arrow_init__y_in = Arrow3D(start=[0,-3, 0], end=[0, -2.6, 0])
        debit_y_in = Arrow3D(start=[0,-3, 0], end=[0, -1.8, 0])
        arrow_init__y_out = Arrow3D(start=[0, 1.8, 0], end=[0, 2.2, 0])
        debit_y_out = Arrow3D(start=[0, 1.8, 0], end=[0, 3, 0])

        arrow_init__z_in = Arrow3D(start=[0, 0, -3], end=[0, 0, -2.6])
        debit_z_in = Arrow3D(start=[0, 0, -3], end=[0, 0, -1.8])
        arrow_init__z_out = Arrow3D(start=[0, 0, 1.8], end=[0, 0, 2.2])
        debit_z_out = Arrow3D(start=[0, 0, 1.8], end=[0, 0, 3])

        arrow_debit = VGroup(debit_x_in, debit_x_out, debit_y_in, debit_y_out, debit_z_in, debit_z_out)

        eqa_x_in = Tex(r"$\rho udydz$", font_size=25).shift(DOWN*0.8+RIGHT*0.3)
        eqa_x_out = Tex(r"$\left[ \rho u+ \frac{\partial \left( \rho u \right) }{\partial x} dx \right] dydz$", font_size=25).shift(RIGHT*3+UP*1)
        eqa_y_in = Tex(r"$\rho vdxdz$", font_size=25).shift(LEFT*2.5+DOWN*0.3)
        eqa_y_out = Tex(r"$\left[ \rho v+ \frac{\partial \left( \rho v \right) }{\partial y} dy \right] dxdz$", font_size=25).shift(RIGHT*3+DOWN*0.6)
        eqa_z_in = Tex(r"$\rho wdxdy$", font_size=25).shift(DOWN*2.5+RIGHT*0.7)
        eqa_z_out = Tex(r"$\left[ \rho w+ \frac{\partial \left( \rho w \right) }{\partial z} dz \right] dxdy$", font_size=25).shift(UP*2.5+RIGHT*1.5)
        eqa_debit = VGroup(eqa_x_in, eqa_x_out, eqa_y_in, eqa_y_out, eqa_z_in, eqa_z_out)

        self.add_fixed_in_frame_mobjects(text_coord)
        self.play(FadeIn(box, text_coord), run_time = 2)
        self.wait(2)
        self.add_fixed_in_frame_mobjects(text_mass_reduction)
        self.play(FadeIn(text_mass_reduction))
        self.wait()
        self.play(ReplacementTransform(arrow_init__x_in, debit_x_in), ReplacementTransform(arrow_init__x_out, debit_x_out))
        self.play(ReplacementTransform(arrow_init__y_in, debit_y_in), ReplacementTransform(arrow_init__y_out, debit_y_out))
        self.play(ReplacementTransform(arrow_init__z_in, debit_z_in), ReplacementTransform(arrow_init__z_out, debit_z_out))
        self.add_fixed_in_frame_mobjects(eqa_debit)
        self.play(FadeIn(eqa_debit), run_time = 2)
        self.play(box.animate.shift(DOWN*5).scale(0.7), arrow_debit.animate.shift(DOWN*5).scale(0.7),
                  text_dx.animate.shift(LEFT*5.2+UP*0.6).scale(0.7),
                  text_dy.animate.shift(LEFT*4.6+UP*0.9).scale(0.7),
                  text_dz.animate.shift(LEFT*5.4).scale(0.7),
                  eqa_x_in.animate.shift(LEFT*5.2+UP*0.3).scale(0.7),
                  eqa_x_out.animate.shift(LEFT*5.5).scale(0.7),
                  eqa_y_in.animate.shift(LEFT*4+UP*0.3).scale(0.7),
                  eqa_y_out.animate.shift(LEFT*5.3+UP*0.4).scale(0.7),
                  eqa_z_in.animate.shift(LEFT*4.9+UP*1).scale(0.7),
                  eqa_z_out.animate.shift(LEFT*5.2+DOWN*0.5).scale(0.7),
                  text_mass_reduction.animate.move_to(UP*2+RIGHT*2)
                  )
        self.wait()

        text_total_net_outflow = VGroup(
                                        Text("total net outflow", font_size=35),
                                        Tex(r"$[\frac{\partial (\rho u)}{\partial x}+\frac{\partial (\rho v)}{\partial y}+\frac{\partial (\rho w)}{\partial z}]dxdydz$").shift(DOWN*1)
                                        ).shift(RIGHT*2)
        self.add_fixed_in_frame_mobjects(text_total_net_outflow)
        self.play(FadeIn(text_total_net_outflow))
        self.wait(10)
        self.play(FadeOut(box, arrow_debit, text_coord, eqa_debit))
        self.play(FadeOut(text_mass_reduction, text_total_net_outflow))

class ControlObject(Scene):    ###not added
    def construct(self):
        object= ImageMobject("Objet.png")
        object.scale(1.3)
        champ_arrow = VGroup(CurvedArrow(start_point=[-3, 1.1, 0], end_point=[3, 2.1, 0], radius = -20),
                       CurvedArrow(start_point=[-3, -0.5, 0], end_point=[3, 0, 0], radius = -20),
                       CurvedArrow(start_point=[-3, -2.1, 0], end_point=[3, -2, 0], radius = -20))
        dA = VGroup(ArcBetweenPoints(start=[0.7,1,0], end=[1.2,1.1,0], radius = -1.5),
                    ArcBetweenPoints(start=[1.2,1.1,0], end=[1.33,0.8,0], radius = -1.5),
                    ArcBetweenPoints(start=[1.33,0.8,0], end=[0.83,0.7,0], radius = 1.5),
                    ArcBetweenPoints(start=[0.83,0.7,0], end=[0.7,1,0], radius = 1.8)).shift(UP*0.3+RIGHT*0.3)
        dB = VGroup(Line(start=[0,-1,0], end=[0.4,-1,0]),
                    Line(start=[0.4, -1, 0], end=[0.4,-1.4,0]),
                    Line(start=[0.4,-1.4,0], end=[0,-1.4,0]),
                    Line(start=[0,-1.4,0], end=[0,-1,0]),
                    Line(start=[0,-1,0],end=[0.15,-0.9,0]),
                    Line(start=[0.15,-0.9,0],end=[0.55,-0.9,0]),
                    Line(start=[0.55,-0.9,0],end=[0.4,-1,0]),
                    Line(start=[0.55,-0.9,0],end=[0.55,-1.3,0]),
                    Line(start=[0.55,-1.3,0],end=[0.4,-1.4,0])).set_opacity(0.5).shift(LEFT*0.5+UP*0.2)
        arrow_n = Arrow(start=[1.13,1.07, 0], end=[2.28,1.82, 0])
        self.play(FadeIn(object))
        self.play(Create(champ_arrow[0]), Create(champ_arrow[1]), Create(champ_arrow[2]))
        self.play(Create(dA))
        self.play(FadeIn(Text("dA", font_size=30).shift(UP*1.2+RIGHT*0.7)))
        self.play(GrowArrow(arrow_n),FadeIn(Tex(r"$\vec n$", font_size=40).shift(UP*1.4+RIGHT*2.1)))
        self.play(FadeIn(dB, Text("dB", font_size=30).shift(DOWN*0.9+RIGHT*0.5)))