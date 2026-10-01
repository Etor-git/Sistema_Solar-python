# Importamos las librerías necesarias
import turtle  # Para dibujar y crear la interfaz gráfica
import math    # Para usar funciones matemáticas (seno, coseno, radianes)

# ==========================================
# 1. CONFIGURACIÓN DE LA PANTALLA PRINCIPAL
# ==========================================
pantalla = turtle.Screen()
pantalla.setup(width=1200, height=900)  # Ancho y alto de la ventana
pantalla.bgcolor("black")               # Color de fondo (simula el espacio)
pantalla.title("Sistema Solar")         # Título de la ventana

# IMPORTANTE: Desactiva la animación automática de Turtle.
# Esto evita que la pantalla parpadee y hace que la animación sea fluida.
pantalla.tracer(0) 

# ==========================================
# 2. CONFIGURACIÓN DEL SOL
# ==========================================
sol = turtle.Turtle()
sol.shape("circle")       # Forma de círculo
sol.color("yellow")       # Color amarillo
sol.shapesize(3)          # Tamaño del Sol (un solo número lo hace redondo)
sol.penup()               # Levanta el lápiz para que no dibuje líneas al moverse

# ==========================================
# 3. FUNCIÓN PARA DIBUJAR LAS ÓRBITAS
# ==========================================
def crear_orbitas(radio: float) -> None:
    """
    Dibuja un círculo gris que representa la órbita de un planeta.
    :param radio: Distancia desde el centro (el Sol) hasta la órbita.
    """
    orbita = turtle.Turtle()
    orbita.hideturtle()    # Oculta la flecha de la tortuga
    orbita.speed(0)        # Máxima velocidad de dibujo
    orbita.color("gray")   # Color gris para las líneas de la órbita
    orbita.penup()
    
    # Movemos la tortuga hacia abajo (eje Y negativo) según el radio
    orbita.goto(x=0, y=-radio) 
    
    orbita.pendown()
    # Dibuja un círculo completo. Si la tortuga está abajo, 
    # el círculo se dibuja alrededor del centro (0,0)
    orbita.circle(radio)   

# Lista con los radios de cada órbita (ajustado para que coincida con los planetas)
distancias = [80, 120, 180, 260, 320, 380, 420, 460]

# Bucle para crear todas las órbitas
for r in distancias:
    crear_orbitas(r)

# ==========================================
# 4. CLASE PLANETA (El molde para crear planetas)
# ==========================================
class Planeta:
    def __init__(self, nombre: str, color: str, radio: float, velocidad: float, tamaño: float):
        """
        Constructor de la clase. Se ejecuta al crear un nuevo planeta.
        """
        # Guardamos los datos del planeta en sus propiedades (atributos)
        self.nombre = nombre
        self.color = color
        self.radio = radio        # Distancia al Sol
        self.velocidad = velocidad # Qué tan rápido gira
        self.angulo = 0           # Ángulo inicial (0 grados)
        self.luna = None

        # --- Creamos el cuerpo del planeta ---
        self.cuerpo = turtle.Turtle()
        self.cuerpo.shape("circle")
        self.cuerpo.color(self.color)
        self.cuerpo.shapesize(tamaño) # Tamaño visual del planeta
        self.cuerpo.penup()

        # --- Creamos la etiqueta de texto (el nombre) ---
        self.etiqueta = turtle.Turtle()
        self.etiqueta.hideturtle()
        self.etiqueta.color("white")
        self.etiqueta.penup()

    def mover(self) -> None:
        """
        Calcula y actualiza la posición del planeta y su etiqueta.
        Se llamará repetidamente en el bucle principal.
        """
        # Fórmula matemática para movimiento circular:
        # x = radio * cos(ángulo), y = radio * sin(ángulo)
        # Usamos math.radians() porque math.cos y math.sin esperan radianes, no grados.
        x = self.radio * math.cos(math.radians(self.angulo))
        y = self.radio * math.sin(math.radians(self.angulo))

        # Movemos el cuerpo del planeta a las nuevas coordenadas
        self.cuerpo.goto(x, y)
        
        # Actualizamos la etiqueta del nombre
        self.etiqueta.clear()               # Borra la posición anterior del texto
        self.etiqueta.goto(x + 15, y + 15)  # Mueve el texto un poco al lado del planeta
        self.etiqueta.write(self.nombre, font=("Arial", 20, "bold"))
        
        # Aumentamos el ángulo para que en el siguiente ciclo se mueva de posición
        self.angulo += self.velocidad

# ==========================================
# 5. CREACIÓN DE LOS PLANETAS
# ==========================================
# Instanciamos (creamos) cada planeta con sus datos reales aproximados
mercurio = Planeta("Mercurio", "gray", 80, 0.04, 0.5)
venus = Planeta("Venus", "orange", 120, 0.03, 0.7)
tierra = Planeta("Tierra", "blue", 180, 0.04, 0.8)
marte = Planeta("Marte", "red", 260, 0.01, 0.7)
jupiter = Planeta("Júpiter", "brown", 320, 0.03, 1.4)
saturno = Planeta("Saturno", "pink", 380, 0.02, 1.4)
urano = Planeta("Urano", "yellow", 420, 0.02, 1.4)
neptuno = Planeta("Neptuno", "green", 460, 0.01, 1.4)

# Guardamos todos los planetas en una lista para poder recorrerlos fácilmente
planetas = [mercurio, venus, tierra, marte, jupiter, saturno, urano, neptuno]

# ==========================================
# 6. BUCLE PRINCIPAL DE ANIMACIÓN
# ==========================================
while True:
    # Recorremos la lista de planetas
    for planeta in planetas:
        planeta.mover()  # Cada planeta actualiza su posición
        
    # Actualizamos la pantalla para mostrar los cambios del fotograma actual
    pantalla.update()
