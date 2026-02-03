# 📍 RutasTj - Explora con Seguridad
> **Tu ciudad, inteligente.**

RutasTj es una aplicación web interactiva diseñada para registrar y visualizar puntos de interés en la ciudad de Tijuana. Combina una interfaz moderna y oscura ("Dark Mode") con mapas dinámicos que permiten la colaboración ciudadana.

---

## 🚀 Cómo correr el proyecto

Sigue estos pasos para ejecutar la aplicación en tu computadora local:

1. **Clonar el repositorio (opcional si ya tienes el código):**
   ```bash
   git clone [https://github.com/TU_USUARIO/RutasTj-Proyecto.git](https://github.com/TU_USUARIO/RutasTj-Proyecto.git)
   cd RutasTj-Proyecto
2.- pip install flask
3.- python main.py
4.-Abrir en el navegador: Visita la siguiente dirección: http://127.0.0.1:5000


🛠 Stack Tecnológico
Backend: Python (Flask) - Para el enrutamiento y gestión del servidor.

Frontend: HTML5 + Tailwind CSS (vía CDN) - Para un diseño responsivo y estilizado.

Mapas: Leaflet.js - Librería de mapas interactivos Open Source.

Iconografía: FontAwesome & Lucide Icons.

🎨 Justificación de Diseño y UX
El diseño de RutasTj se centra en la Experiencia de Usuario (UX) y la claridad visual, integrando las actividades realizadas durante el desarrollo:

Navegación Unificada (Actividad 5): Se implementó un flujo continuo desde la Landing Page hasta el Mapa. El botón de llamada a la acción ("Explorar Mapa") es prominente y claro.

Maximización del Espacio: El mapa cuenta con una funcionalidad de Sidebar Colapsable. Esto permite al usuario ocultar la lista de puntos para visualizar el mapa a pantalla completa sin distracciones, ideal para dispositivos móviles.

Feedback Visual: Al guardar un punto, el usuario recibe retroalimentación inmediata (animación de carga y mensaje de éxito), reduciendo la incertidumbre del sistema.

Créditos a la IA
Este código fue co-creado y optimizado con la asistencia de Gemini Canvas (Google DeepMind).

Prompt principal para cada actividad:
Actividad 1
Investigación: Define el nicho de tu mapa (ej. "RutasTj").
Prompt sugerido: "Crea una Landing Page HTML para una app de mapas llamada [RutasTj]. Debe tener un 'Hero' con una imagen de fondo de un mapa estilizado o topográfico, un título grande, y un botón CTA prominente que diga 'Explorar Mapa'. Usa Tailwind
De igual manera hacer un footer tener en cuenta que es Langing page ocupo header 
CSS. El diseño debe inspirar aventura/seguridad."
Refinamiento UX:
¿El CTA "Explorar Mapa" es lo más visible de la pantalla?
Verifica que la iconografía utilizada sea universal (ej. el ícono de ubicación).
Integración Flask: Estructura en templates/index.html.

Actividad 2
Prompt:"Genera un archivo HTML que incluya la librería Leaflet.js (vía CDN) y Tailwind CSS. Crea un contenedor div 'map' que ocupe el 100% del ancho y 500px de alto (o 'h-screen'). Inicializa el mapa centrado en Tijuana en la colonia "Del regugio" con un tilelayer de OpenStreetMap. Asegúrate de que los botones de zoom estén en una posición fácil de alcanzar.Tener en cueneta que esta en una landing page es decir que  es secuencia de la actividad 1 deberia de tener el mismo header.
De igual manera hacer el mapa de color blanco mover los controles de zoom si están muy arriba a la izquierda (zona difícil en móviles grandes), o que los haga más grandes temabien Asegura que el mapa no quede bloqueado por menús flotantes excesivos.
Integración: Ruta /mapa en Flask que renderice este template.


ACTIVIDAD 3
Objetivo Técnico:
Usar Leaflet para capturar clics (coordenadas), enviarlos a Flask con fetch, y mostrar un marcador con feedback visual inmediato.

Escribe un script en JS para Leaflet. Cuando el usuario haga clic en el mapa: 
1. Ponga un marcador temporal inmediatamente. 
2. Abra un popup que pregunte '¿Guardar este punto?' con opciones de si y no 
3. Al confirmar, envíe las coordenadas (lat, long) a un endpoint Flask /guardar_punto usando fetch. Muestra un 'toast' o notificación de 'Guardando...' mientras se procesa. en caso de declinar no hacer nada mas que cerrar el poput"

ACTIVIDAD 4
Modifica la interfaz para tener dos columnas (o pestañas en móvil): 'Mapa' y 'Lista de Lugares'. Cuando se agregue un marcador en el mapa, debe aparecer también como un texto descriptivo en la sección de Lista (ej. 'Punto en Lat: X, Long: Y'). Asegúrate de que los botones del mapa tengan atributos 'aria-label' como 'Acercar mapa' o 'Alejar mapa'." 
-Puedes agregar un boton arriba del zoom o en algun lugar donde tu creas conveniente pero ocupo que si se aprecie lo requerido


ACTIVIDAD 5
Unificar todo es decir ocupo juntar mi actividad 1,2,3,4 mi landing page pueda redirigirme al mapa y ahi mismo puede guardar los puntos como lo hacia la actividad 4 solamete agregar una funcionalidad para poder minimizar los puntos guardados.Flujo

Entrar a la landig page 
Al hacer click al mapa
Entrar al mapa 
Poder guardar punto en mapa
Poder ocultar todo el apartado de los puntos guardados dejando solamente el mapa



Familiaridad: Se diseñaron pines personalizados estilo Google Maps (color Ámbar/Negro) para que el usuario reconozca intuitivamente que son marcadores interactivos, mejorando la curva de aprendizaje.
