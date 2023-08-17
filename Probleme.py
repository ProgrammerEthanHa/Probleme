import streamlit as st
import pandas as pd
import altair as alt

st.header("Infografik: Wohnen, Klima, Psyche: Damit hat die Jugend zu kämpfen")
st.subheader("Anteil der Befragten, die folgende Probleme als größte Herausforderung für die heutige Jugend sehen (in %)")

source = pd.DataFrame({
        'Prozent(%)': [47, 40, 25, 20, 16, 38, 13, 8],
        'Herausforderung': ['Klimawandel', 'Bezahlbares Wohnen', 'Finanzielle Absicherung', 'Potenzielle weitere Kriege in Europa', 'Gesellschaftlicher Spaltung', 'Mentale Gesundheit', 'Work-Life-Balance', 'Erreichen beruflicher Ziele']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Prozent(%):Q',
        x='Herausforderung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis:2075 Befragte (18-24 Jahren) in Deutschland
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: YouGov")