# Simulación del sistema solar

Este proyecto muestra una representación animada y sencilla del sistema solar. Fue creado en Python con el módulo `turtle`: el Sol aparece en el centro, los ocho planetas recorren sus órbitas y la Luna gira alrededor de la Tierra.

![Vista del sistema solar](./Sistema%20Solar%20-%20Entorno.png)

## El sistema solar

El sistema solar está formado por el Sol y los cuerpos celestes que se mantienen a su alrededor principalmente por la gravedad. Los ocho planetas, en orden desde el Sol, son Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano y Neptuno.

Los cuatro planetas interiores son rocosos. Júpiter y Saturno son gigantes gaseosos, mientras que Urano y Neptuno se clasifican como gigantes helados. La Tierra también tiene un satélite natural: la Luna. La Luna orbita la Tierra, y ambos cuerpos se desplazan alrededor del Sol.

En astronomía, una órbita es el recorrido de un cuerpo alrededor de otro debido a la gravedad. En la realidad, las órbitas planetarias son elípticas; esta simulación las dibuja como círculos para que el movimiento sea más fácil de visualizar.

## Astronomía y astrología

Este programa representa movimientos astronómicos de forma educativa. La astrología es una tradición cultural que relaciona las posiciones aparentes de los astros con interpretaciones sobre las personas o los acontecimientos. No es una explicación científica del funcionamiento del sistema solar, y este programa no calcula horóscopos ni hace predicciones astrológicas.

## Cómo funciona el programa

- `turtle` dibuja la ventana, el Sol, los planetas, la Luna, las etiquetas y las órbitas.
- `math` calcula posiciones usando seno y coseno.
- La clase `Planeta` guarda el nombre, color, distancia al Sol y velocidad angular de cada planeta.
- La clase `Luna` calcula su posición con respecto a la posición actual de la Tierra y dibuja su órbita alrededor de ella.
- En cada ciclo, el programa actualiza las posiciones y redibuja la pantalla.

Los radios y velocidades del código son valores visuales para la animación, no distancias ni velocidades reales. Los tamaños y colores también se eligieron para que los cuerpos se distingan en pantalla.

## Requisitos y ejecución

- Python 3 con soporte para `turtle` (que usa Tk para la ventana gráfica).
- No se necesitan paquetes externos.

Desde esta carpeta, ejecuta:

```bash
python3 main.py
```

En algunos sistemas, el comando puede ser `python main.py`. Se abrirá una ventana con la animación; ciérrala para terminar el programa.
