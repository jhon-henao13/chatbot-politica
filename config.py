import os


class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Esto obtiene la clave API desde las variables de entorno
