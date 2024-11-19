# Speech-to-Text y Text-to-Speech en Español

Este es un mini proyecto en Python que convierte el habla a texto y el texto a voz utilizando las bibliotecas `speech_recognition` y `pyttsx3`. El proyecto está configurado para entender y procesar el idioma español.

## Descripción

El programa:
- Escucha la entrada de voz del usuario.
- Transcribe el audio a texto.
- Reproduce el texto transcrito en voz alta.
- Permite salir del bucle de escucha con el comando de voz "salir".

## Características

- Reconocimiento de voz en español.
- Conversión de texto a voz con voces en español (si están disponibles en el sistema).
- Manejo de errores para solicitudes y entradas de voz desconocidas.
- Configuración de velocidad y volumen de la salida de voz.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación.
- **speech_recognition**: Biblioteca para reconocimiento de voz.
- **pyttsx3**: Biblioteca para síntesis de texto a voz.

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tintayadev/speech-to-text-proof.git
    cd speech-to-text-proof
    ```

2. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa env\Scripts\activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Asegúrate de tener instaladas las bibliotecas requeridas:
    ```bash
    pip install SpeechRecognition pyttsx3 pyaudio
    ```

## Uso

Ejecuta el script principal:
```bash
python main.py
