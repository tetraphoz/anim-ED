from manim import *


class IntroduccionEDO(Scene):
    def construct(self):
        # Título principal
        title = Text("Reducción de Orden en EDOs", font_size=48)
        subtitle = Text("Lineales Homogéneas", font_size=36)
        title_group = VGroup(title, subtitle).arrange(DOWN)

        # Ecuación de ejemplo
        edo_example = MathTex(
            "a_n(x)y^{(n)} + a_{n-1}(x)y^{(n-1)} + ... + a_1(x)y' + a_0(x)y = 0"
        )

        # Animación de entrada
        self.play(Write(title_group))
        self.wait()
        self.play(
            title_group.animate.scale(0.8).to_edge(UP),
        )

        # Puntos clave en forma de bullets
        bullets = VGroup(
            Text("• Encontrar soluciones fundamentales", font_size=24),
            Text("• Verificar independencia lineal", font_size=24),
            Text("• Usar el Wronskiano", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(title_group, DOWN, buff=1)

        for bullet in bullets:
            self.play(FadeIn(bullet))
            self.wait(0.5)

        # Transición a la ecuación
        self.play(
            FadeOut(bullets),
            Write(edo_example.next_to(title_group, DOWN, buff=1))
        )
        self.wait()

        # Destacar la importancia del orden
        brace = Brace(edo_example, DOWN)
        order_text = Text("Ecuación de orden n", font_size=24).next_to(brace, DOWN)

        self.play(
            GrowFromCenter(brace),
            Write(order_text)
        )
        self.wait(2)

class IndependenciaLineal(Scene):
    def construct(self):
        # Título de la sección
        title = Text("Independencia Lineal", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Definición formal
        definition = MathTex(
            r"c_1y_1 + c_2y_2 + ... + c_ny_n = 0",
            r"\implies c_1 = c_2 = ... = c_n = 0"
        ).arrange(DOWN)

        self.play(Write(definition))
        self.wait()

        # Mover definición a un lado
        self.play(definition.animate.scale(0.8).to_edge(LEFT))

        # Visualización geométrica con vectores 2D
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"include_tip": True}
        ).scale(0.5)

        # Vectores independientes
        vector1 = Arrow(axes.get_origin(), axes.c2p(2, 0), color=BLUE)
        vector2 = Arrow(axes.get_origin(), axes.c2p(0, 2), color=RED)

        vectors_indep = VGroup(axes, vector1, vector2).next_to(definition, RIGHT, buff=1)

        self.play(Create(vectors_indep))
        self.wait()

        # Texto explicativo
        explanation = Text(
            "Los vectores son linealmente\nindependientes si ninguno puede\nobtenerse como múltiplo del otro",
            font_size=24
        ).next_to(vectors_indep, DOWN)

        self.play(Write(explanation))
        self.wait(2)

        # Transformación a vectores dependientes
        vector2_dep = Arrow(axes.get_origin(), axes.c2p(4, 0), color=RED)

        self.play(
            ReplacementTransform(vector2, vector2_dep),
            explanation.animate.become(
                Text(
                    "Estos vectores son linealmente\ndependientes: uno es múltiplo del otro",
                    font_size=24
                ).next_to(vectors_indep, DOWN)
            )
        )
        self.wait(2)

class Wronskiano(Scene):
    def construct(self):
        # Título
        title = Text("El Wronskiano", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Definición del Wronskiano como determinante
        wronskian = MathTex(
            r"W(y_1, y_2) = \begin{vmatrix} y_1 & y_2 \\ y_1' & y_2' \end{vmatrix}"
        )

        # Ejemplo específico con cos(x) y sin(x)
        example = MathTex(
            r"W(\cos x, \sin x) = \begin{vmatrix} \cos x & \sin x \\ -\sin x & \cos x \end{vmatrix}"
        )

        # Cálculo del determinante
        calculation = MathTex(
            r"= (\cos x)(\cos x) - (-\sin x)(\sin x)",
            r"= \cos^2 x + \sin^2 x = 1"
        )

        # Organizar ecuaciones
        equations = VGroup(wronskian, example, calculation).arrange(DOWN, buff=0.5)

        # Animación de entrada
        self.play(Write(wronskian))
        self.wait()
        self.play(Write(example))
        self.wait()
        self.play(Write(calculation))
        self.wait()

        # Mover ecuaciones a un lado
        self.play(equations.animate.scale(0.7).to_edge(LEFT))

        # Interpretación geométrica
        # Crear un sistema de coordenadas 3D para mostrar el "volumen"
        axes = ThreeDAxes(
            x_range=[-2, 2],
            y_range=[-2, 2],
            z_range=[-2, 2]
        ).scale(0.5)

        # Crear un paralelepípedo para representar el "volumen"
        cube = Cube(side_length=2, fill_opacity=0.3, stroke_width=2)
        cube.set_color(BLUE)

        geom_group = VGroup(axes, cube).next_to(equations, RIGHT, buff=1)

        # Texto explicativo
        explanation = Text(
            "El Wronskiano mide el 'volumen'\ngenerado por las funciones\ny sus derivadas",
            font_size=24
        ).next_to(geom_group, DOWN)

        self.play(
            Create(geom_group),
            Write(explanation)
        )

        # Rotación del cubo para mejor visualización
        self.play(
            Rotate(cube, angle=PI/4, axis=UP),
            run_time=2
        )
        self.wait(2)


class EjemplosPracticos(Scene):
    def construct(self):
        # Título
        title = Text("Ejemplos Prácticos", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Ejemplo 1: y'' + y = 0
        example1 = VGroup(
            MathTex(r"y'' + y = 0"),
            MathTex(r"y_1 = \cos x,\, y_2 = \sin x")
        ).arrange(DOWN)

        self.play(Write(example1))
        self.wait()

        # Wronskiano para este ejemplo
        wronskian1 = MathTex(
            r"W = \begin{vmatrix} \cos x & \sin x \\ -\sin x & \cos x \end{vmatrix} = 1"
        ).next_to(example1, DOWN)

        self.play(Write(wronskian1))
        self.wait()

        # Mover primer ejemplo
        self.play(
            VGroup(example1, wronskian1).animate.scale(0.8).to_edge(LEFT)
        )

        # Ejemplo 2: Caso dependiente
        example2 = VGroup(
            MathTex(r"y_1 = e^x,\, y_2 = 3e^x"),
            MathTex(r"W = \begin{vmatrix} e^x & 3e^x \\ e^x & 3e^x \end{vmatrix} = 0")
        ).arrange(DOWN).next_to(wronskian1, DOWN, buff=1)

        self.play(Write(example2))
        self.wait()

        # Gráficas de las funciones
        axes = Axes(
            x_range=[-2, 2],
            y_range=[-2, 2],
            axis_config={"include_tip": True}
        ).scale(0.5).next_to(example1, RIGHT, buff=1)

        # Funciones para graficar
        cos_graph = axes.plot(lambda x: np.cos(x), color=BLUE)
        sin_graph = axes.plot(lambda x: np.sin(x), color=RED)

        self.play(
            Create(axes),
            Create(cos_graph),
            Create(sin_graph)
        )

        # Etiquetas para las gráficas
        labels = VGroup(
            MathTex(r"\cos x", color=BLUE),
            MathTex(r"\sin x", color=RED)
        ).arrange(DOWN).next_to(axes, RIGHT)

        self.play(Write(labels))
        self.wait(2)


class TeoremaFundamental(Scene):
    def construct(self):
        # Título
        title = Text("Teorema Fundamental del Wronskiano", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Enunciado del teorema
        theorem = VGroup(
            Text("Si ", font_size=30),
            MathTex(r"W(x_0) \neq 0"),
            Text(" en algún punto ", font_size=30),
            MathTex(r"x_0"),
            Text(", entonces las funciones son", font_size=30),
            Text("linealmente independientes en todo el intervalo.", font_size=30)
        ).arrange(RIGHT).next_to(title, DOWN, buff=1)

        self.play(Write(theorem))
        self.wait()

        # Nota importante
        note = VGroup(
            Text("¡Importante!", color=RED, font_size=30),
            Text("La recíproca no es cierta:", font_size=30),
            MathTex(r"W \equiv 0"),
            Text("no implica necesariamente dependencia lineal", font_size=30)
        ).arrange(RIGHT).next_to(theorem, DOWN, buff=1)

        self.play(Write(note))
        self.wait()

        # Conclusión
        conclusion = VGroup(
            Text("El Wronskiano nos permite:", font_size=30),
            BulletedList(
                "Verificar independencia lineal",
                "Construir conjuntos fundamentales de soluciones",
                "Garantizar la completitud de nuestras soluciones",
                buff=0.5,
                font_size=24
            )
        ).arrange(DOWN, aligned_edge=LEFT).next_to(note, DOWN, buff=1)

        self.play(Write(conclusion))
        self.wait()

        # Fade out final
        self.play(
            FadeOut(conclusion),
            FadeOut(note),
            FadeOut(theorem),
            FadeOut(title)
        )

        # Mensaje final
        final_message = Text(
            "¡Gracias por su atención!",
            font_size=40
        ).center()

        self.play(Write(final_message))
        self.wait(2)
