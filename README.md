# Traductor Multilenguaje con Interfaz Gráfica

Este proyecto es una aplicación de traducción multilenguaje que utiliza la API de OpenAI para traducir textos de un idioma de origen a un idioma intermedio, y finalmente al español. La interfaz gráfica está construida con `tkinter` y es fácilmente adaptable al tamaño de la ventana.

## Características

- Traducción de textos desde cualquier idioma de origen a un idioma intermedio.
- Traducción automática del idioma intermedio al español.
- Interfaz gráfica sencilla y funcional con diseño responsivo.
- Utiliza la API de OpenAI (requiere clave API).

## Requisitos

- Python 3.x
- Clave API de OpenAI
- Bibliotecas requeridas:
  - `tkinter`
  - `openai`
  - `python-dotenv`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/AlvaroG001/Traductor_API_ChatGPT.git
   
2. Instala las dependencias en un entorno virtual:
  ```bash
  python3 -m venv myenv
  source myenv/bin/activate
  pip install -r requirements.txt

3. Crea un archivo .env en el directorio principal con tu clave API de OpenAI:
  ```bash
  OPENAI_API_KEY=tu_clave_api_aqui

## Uso

Ejecuta el script principal:
  ```bash
  python script_traductor.py

Ingresa el idioma de origen, el idioma al que deseas traducir, y el texto a traducir.
Haz clic en el botón "Traducir" para obtener las traducciones.

## Personalización

Puedes ajustar los idiomas de origen y destino cambiando los valores en los campos correspondientes en la interfaz gráfica.

Licencia
Este proyecto está bajo la Licencia MIT.





