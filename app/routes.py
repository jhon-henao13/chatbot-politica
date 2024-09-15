from flask import render_template, request
from app import app
import openai
import os

# Configurar la clave de API desde las variables de entorno
openai.api_key = os.getenv('OPENAI_API_KEY')  # Aquí obtenemos la clave de la variable de entorno

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = openai.Completion.create(
        model="gpt-4o-mini",
        prompt=f"Eres un experto en política global. Responde a las siguientes preguntas con detalles claros y basados en hechos históricos y actuales. {user_input}",
        max_tokens=200
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)
