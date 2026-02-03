# 📍 RutasTj - Explora con Seguridad

> **Tu ciudad, inteligente.**

**RutasTj** es una aplicación web interactiva diseñada para registrar y visualizar puntos de interés en la ciudad de Tijuana. Combina una interfaz moderna y oscura (*Dark Mode*) con mapas dinámicos que permiten la colaboración ciudadana.

---

## 🚀 Cómo correr el proyecto

Sigue estos pasos para ejecutar la aplicación en tu computadora local:

1.  **Clonar el repositorio** (opcional si ya tienes el código):
    ```bash
    git clone [https://github.com/AxelLeyva17/Rutas.git)
    cd Rutas
    ```

2.  **Instalar dependencias:**
    Necesitas tener Python instalado. Instala Flask con el siguiente comando:
    ```bash
    pip install flask
    ```

3.  **Ejecutar el servidor:**
    ```bash
    python main.py
    ```

4.  **Abrir en el navegador:**
    Visita la siguiente dirección en tu navegador web:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛠 Stack Tecnológico

* **Backend:** Python (Flask) - Para el enrutamiento y gestión del servidor.
* **Frontend:** HTML5 + Tailwind CSS (vía CDN) - Para un diseño responsivo y estilizado.
* **Mapas:** Leaflet.js - Librería de mapas interactivos Open Source.
* **Iconografía:** FontAwesome & Lucide Icons.

---

## 🎨 Justificación de Diseño y UX

El diseño de RutasTj se centra en la **Experiencia de Usuario (UX)** y la claridad visual, integrando las mejoras realizadas durante el desarrollo iterativo:

* **Navegación Unificada (Actividad 5):** Se implementó un flujo continuo desde la Landing Page hasta el Mapa. El botón de llamada a la acción ("Explorar Mapa") es prominente, guiando al usuario sin fricción.
* **Maximización del Espacio:** El mapa cuenta con una funcionalidad de **Sidebar Colapsable**. Esto permite al usuario ocultar la lista de puntos para visualizar el mapa a pantalla completa sin distracciones, ideal para la navegación en dispositivos móviles.
* **Feedback Visual:** Al guardar un punto, el usuario recibe retroalimentación inmediata (animación de carga y mensaje de éxito que desaparece automáticamente), reduciendo la incertidumbre del sistema.
* **Familiaridad:** Se diseñaron **pines personalizados estilo Google Maps** (color Ámbar/Negro) para que el usuario reconozca intuitivamente que son marcadores interactivos, mejorando la curva de aprendizaje.

---

## 🤖 Créditos a la IA & Proceso de Desarrollo

Este código fue co-creado, iterado y optimizado con la asistencia de **Gemini Canvas** (Google DeepMind). A continuación, se detalla el flujo de prompts utilizados para cada etapa del desarrollo:

### 🔹 Actividad 1: Landing Page & Identidad
**Objetivo:** Definir el nicho y crear la portada.
> **Prompt utilizado:**
> "Crea una Landing Page HTML para una app de mapas llamada [RutasTj]. Debe tener un 'Hero' con una imagen de fondo de un mapa estilizado o topográfico, un título grande, y un botón CTA prominente que diga 'Explorar Mapa'. Usa Tailwind CSS. El diseño debe inspirar aventura/seguridad. De igual manera hacer un footer y tener en cuenta que es Landing page, ocupo header."

### 🔹 Actividad 2: Integración del Mapa
**Objetivo:** Renderizar el mapa base con Leaflet.
> **Prompt utilizado:**
> "Genera un archivo HTML que incluya la librería Leaflet.js (vía CDN) y Tailwind CSS. Crea un contenedor div 'map' que ocupe el 100% del ancho y 500px de alto (o 'h-screen'). Inicializa el mapa centrado en Tijuana en la colonia 'Del Refugio' con un tilelayer de OpenStreetMap. Asegúrate de que los botones de zoom estén en una posición fácil de alcanzar. Tener en cuenta que es secuencia de la actividad 1, debería tener el mismo header. Hacer el mapa de color blanco y mover los controles de zoom si estorban en móviles."

### 🔹 Actividad 3: Interactividad y Captura de Datos
**Objetivo:** Capturar clics y conectar con Flask.
> **Prompt utilizado:**
> "Escribe un script en JS para Leaflet. Cuando el usuario haga clic en el mapa:
> 1. Ponga un marcador temporal inmediatamente.
> 2. Abra un popup que pregunte '¿Guardar este punto?' con opciones de sí y no.
> 3. Al confirmar, envíe las coordenadas (lat, long) a un endpoint Flask /guardar_punto usando fetch. Muestra un 'toast' o notificación de 'Guardando...' mientras se procesa. En caso de declinar, solo cerrar el popup."

### 🔹 Actividad 4: Lista Dinámica
**Objetivo:** Visualización de datos en lista.
> **Prompt utilizado:**
> "Modifica la interfaz para tener dos columnas (o pestañas en móvil): 'Mapa' y 'Lista de Lugares'. Cuando se agregue un marcador en el mapa, debe aparecer también como un texto descriptivo en la sección de Lista (ej. 'Punto en Lat: X, Long: Y'). Asegúrate de agregar atributos de accesibilidad (aria-label) a los botones."

### 🔹 Actividad 5: Unificación y UX Final (Versión Actual)
**Objetivo:** Flujo completo y mejoras de interfaz (Sidebar colapsable).
> **Prompt utilizado:**
> "Unificar todo: ocupo juntar mi actividad 1, 2, 3, 4. Que mi landing page pueda redirigirme al mapa y ahí mismo pueda guardar los puntos. Agregar una funcionalidad para poder minimizar los puntos guardados (sidebar colapsable) para que se aprecie mejor el mapa. El flujo debe ser: Entrar a Landing -> Click en Mapa -> Guardar punto -> Ocultar lista."
