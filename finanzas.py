import streamlit as st
import pandas as pd
from datetime import datetime

# Función para calcular las diferencias entre lo presupuestado y lo real
def calcular_diferencias(df, tipo="semanal"):
    # Asegurarse de que la columna 'Fecha' está en formato de fecha
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Establecer el periodo (semanal o mensual)
    if tipo == "semanal":
        df['Semana'] = df['Fecha'].dt.isocalendar().week
        period_col = 'Semana'
    else:
        df['Mes'] = df['Fecha'].dt.month
        period_col = 'Mes'

    # Calcular las diferencias
    df_summary = df.groupby(period_col).agg({
        'Ingresos': 'sum',
        'Gastos': 'sum',
        'Presupuesto': 'sum',
        'Meta de Ahorro': 'sum'
    }).reset_index()

    # Calcular las diferencias
    df_summary['Diferencia Ingresos'] = df_summary['Ingresos'] - df_summary['Presupuesto']
    df_summary['Diferencia Gastos'] = df_summary['Gastos'] - df_summary['Presupuesto']
    df_summary['Diferencia Ahorro'] = df_summary['Meta de Ahorro'] - (df_summary['Ingresos'] - df_summary['Gastos'])

    return df_summary

# Configuración de la página
st.set_page_config(page_title="Registro de Finanzas Personales", layout="wide")

# Título de la app
st.title("Registro de Finanzas Personales")
st.write("Esta aplicación permite gestionar tus finanzas personales, registrar ingresos, gastos, presupuestos y metas de ahorro.")

# Crear un DataFrame vacío para almacenar los datos
if 'finanzas' not in st.session_state:
    st.session_state.finanzas = pd.DataFrame(columns=['Fecha', 'Ingresos', 'Gastos', 'Presupuesto', 'Meta de Ahorro'])

# Función para ingresar nuevos datos
def ingresar_datos():
    fecha = st.date_input("Fecha", min_value=datetime(2020, 1, 1), value=datetime.today())
    ingresos = st.number_input("Ingresos", min_value=0.0, step=1.0, format="%.2f")
    gastos = st.number_input("Gastos", min_value=0.0, step=1.0, format="%.2f")
    presupuesto = st.number_input("Presupuesto", min_value=0.0, step=1.0, format="%.2f")
    meta_ahorro = st.number_input("Meta de Ahorro", min_value=0.0, step=1.0, format="%.2f")
    
    if st.button("Registrar"):
        nueva_entrada = {
            'Fecha': fecha,
            'Ingresos': ingresos,
            'Gastos': gastos,
            'Presupuesto': presupuesto,
            'Meta de Ahorro': meta_ahorro
        }
        # Agregar la nueva entrada al DataFrame
        st.session_state.finanzas = pd.concat([st.session_state.finanzas, pd.DataFrame([nueva_entrada])], ignore_index=True)
        st.success("¡Datos registrados con éxito!")

# Mostrar formulario de ingresos
ingresar_datos()

# Mostrar los datos ingresados
st.subheader("Datos Ingresados")
st.write(st.session_state.finanzas)

# Calcular y mostrar reportes
if not st.session_state.finanzas.empty:
    # Filtrar las fechas para la visualización de los reportes
    tipo_reporte = st.radio("Selecciona el tipo de reporte", ("Semanal", "Mensual"))
    df_resumen = calcular_diferencias(st.session_state.finanzas, tipo_reporte.lower())
    
    st.subheader(f"Reporte {tipo_reporte} de Finanzas")
    st.write(df_resumen)

    # Graficar las diferencias
    st.subheader("Gráfico de Diferencias")
    st.line_chart(df_resumen.set_index(tipo_reporte.lower())[['Diferencia Ingresos', 'Diferencia Gastos', 'Diferencia Ahorro']])

# Nota final
st.write("""
**Nota:** El reporte muestra las diferencias entre lo que habías presupuestado y lo que realmente gastaste o ahorraste.
""")
