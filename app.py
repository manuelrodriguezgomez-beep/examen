import streamlit as st

# 1. EL ARCHIVADOR (Base de datos de preguntas PER)
preguntas = [
    {
        "texto": "1. ¿Quien es nuestro tutor?",
        "opciones": ["Don Paco", "Don Josemaria", "Don Diego", "Don Nathael"],
        "correcta": "Don Josemaria"
    },
    {
        "texto": "2. ¿Porque se repitio el examen?",
        "opciones": ["Porque si", "Porque lo robaron", "Porque salio muy mal", "Porque estaba de mal humor el profe"],
        "correcta": "Porque lo robaron"
    },
    {
        "texto": "3. Cual fue la clase que mas suspendio",
        "opciones": ["El c", "El a", "El d", "El e"],
        "correcta": "El D"
    },
    {
        "texto": "4. ¿Cuanto duro Beltran?",
        "opciones": ["1 dia", "1 semana", "2 semanas", "0,5 horas"],
        "correcta": "2 semanas"
    },
    {
        "texto": "5. Quien hace dibujos en su cuaderno",
        "opciones": ["Tata", "Nadie", "raul", "Manea"],
        "correcta": "Tata"
    },
    {
        "texto": "6. ¿Quien es Beltran?",
        "opciones": ["Un caracol", "Un perro", "un gusano", "algo"],
        "correcta": "un gusano"
    },
    {
        "texto": "7. ¿Que asignatura ha suspendido casi todo el mundo?",
        "opciones": ["Mates", "Lengua", "Fisica", "Todo"],
        "correcta": "Lengua"
    },
    {
        "texto": "8. Elige la b",
        "opciones": ["c", "b", "d", "a"],
        "correcta": "b"
    }
]

# Configuración de la interfaz
st.title("Examen")
st.write("Responde a las siguientes 9 preguntas. Recuerda: **Los fallos restan** y las blancas no suman.")

# Formulario de examen
with st.form("examen_per"):
    respuestas_usuario = []
    
    for i, p in enumerate(preguntas):
        st.subheader(f"Pregunta {i+1}")
        # Añadimos "Dejar en blanco" como opción inicial
        opciones_con_blanco = ["Dejar en blanco"] + p["opciones"]
        res = st.radio(p["texto"], opciones_con_blanco, key=f"p{i}")
        respuestas_usuario.append(res)
    
    boton_enviar = st.form_submit_button("Corregir Examen")

# Lógica de corrección
if boton_enviar:
    aciertos = 0
    fallos = 0
    blancos = 0
    
    for i, res in enumerate(respuestas_usuario):
        if res == "Dejar en blanco":
            blancos += 1
        elif res == preguntas[i]["correcta"]:
            aciertos += 1
        else:
            fallos += 1
    
    # Cálculo de la nota sobre 10
    # Cada acierto vale 1.11. Cada fallo resta 0.37 (1/3 de un acierto)
    puntos_por_pregunta = 10 / len(preguntas)
    nota_final_raw = (aciertos * puntos_por_pregunta) - (fallos * (puntos_por_pregunta / 3))
    nota_final_raw = max(0, nota_final_raw) # Evitar notas negativas
    nota_redondeada = round(nota_final_raw)

    # Mostrar resultados
    st.divider()
    st.header(f"Tu nota: {nota_redondeada}/10")
    
    # Feedback dinámico
    if nota_redondeada < 3:
        st.error(f"Nota: {nota_redondeada} - Muy insuficiente. Tienes {aciertos} aciertos y {fallos} fallos.")
    elif 3 <= nota_redondeada < 5:
        st.warning(f"Nota: {nota_redondeada} - Insuficiente. Necesitas estudiar mas tontolava")
    elif 5 <= nota_redondeada < 6:
        st.info(f"Nota: {nota_redondeada} - Suficiente. Aprobado, aunque intenta mejorar.")
    elif 6 <= nota_redondeada < 7:
        st.success(f"Nota: {nota_redondeada} - Bien. Buen trabajo, sigue así.")
    elif 7 <= nota_redondeada < 9:
        st.success(f"Nota: {nota_redondeada} - Notable. Tienes un conocimiento sólido.")
    elif 9 <= nota_redondeada < 10:
        st.success(f"Nota: {nota_redondeada} - Sobresaliente. ¡Casi perfecto!")
    elif nota_redondeada == 10:
        st.balloons()
        st.success(f"Nota: {nota_redondeada} - Excelente.")

 
