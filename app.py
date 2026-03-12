from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator

st.title('Análisis Semántico')
image = Image.open('emoticones.jpg')
st.image(image)
st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

translator = Translator()

with st.sidebar:
               st.subheader("Polaridad, Subjetividad y Modalidad")
               ("""
                Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
                Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
                
               Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.

               Modalidad gramatical: Indica la intención comunicativa del texto, se diferencia entre las siguientes modalidades: enunciativa,
               exclamativa, imperativa, interrogativa y dubitativa.

                 """
               ) 

def detectar_modalidad(texto):
    texto = texto.lower().strip()

    imperativos = ["haz", "ve", "dime", "cierra", "abre", "escucha", "mira", "ven"]
    dubitativos = ["quizás", "quizas", "tal vez", "probablemente", "puede que"]

    if "¿" in texto or "?" in texto:
        return "Interrogativa"
    elif "¡" in texto or "!" in texto:
        return "Exclamativa"
    elif any(texto.startswith(v) for v in imperativos):
        return "Imperativa"
    elif any(p in texto for p in dubitativos):
        return "Dubitativa"
    else:
        return "Enunciativa"

with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    if text:

      translation = translator.translate(text, src="es", dest="en")
      trans_text = translation.text
      blob = TextBlob(trans_text)
  
      st.write('Polarity: ', round(blob.sentiment.polarity,2))
      st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
  
      modalidad = detectar_modalidad(text)
      st.write("Modalidad gramatical:", modalidad)
  
      x = round(blob.sentiment.polarity,2)
  
      if x > 0:
          st.write('Es un sentimiento Positivo 😊')
      elif x < 0:
          st.write('Es un sentimiento Negativo 😔')
      else:
          st.write('Es un sentimiento Neutral 😐')
