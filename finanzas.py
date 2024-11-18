import streamlit as st
import pandas as pd
from datetime import datetime

# Función para calcular las diferencias entre lo presupuestado y lo real
def calcular_diferencias(df, tipo="semanal"):
    df['Fecha'] = pd.to_datetime(df['Fecha'])

    # Verificar si el presupuesto es semanal o mensual
    if tipo == "semanal":
        df['Semana'] = df['Fecha'].dt.isocalendar().week
        period_col = 'Semana'
    else:
        df['Mes'] = df['Fecha'].dt.month
        period_col = 'Mes'

    df_summary = df.groupby(period_col).agg({
        'Ingresos': 'sum',
        'Gastos': 'sum',
        'Presupuesto': 'sum',
        'Meta de Ahorro': 'sum'
    }).reset_index()

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

# Crear una variable para almacenar el tipo de presupuesto
if 'tipo_presupuesto' not in st.session_state:
    st.session_state.tipo_presupuesto = None  # Ningún presupuesto definido por defecto

# Menú desplegable para seleccionar la funcionalidad
opcion = st.selectbox(
    "Selecciona una opción:",
    ("Registrar nuevo gasto/ingreso", "Establecer presupuesto", "Establecer metas de gasto", "Modificar registros previos", "Ver reporte")
)

# Función para ingresar nuevos datos de gasto/ingreso
def registrar_gasto_ingreso():
    fecha = st.date_input("Fecha", min_value=datetime(2020, 1, 1), value=datetime.today())
    ingresos = st.number_input("Ingresos", min_value=0.0, step=1.0, format="%.2f")
    gastos = st.number_input("Gastos", min_value=0.0, step=1.0, format="%.2f")
    meta_ahorro = st.number_input("Meta de Ahorro", min_value=0.0, step=1.0, format="%.2f")

    if st.button("Registrar"):
        nueva_entrada = {
            'Fecha': fecha,
            'Ingresos': ingresos,
            'Gastos': gastos,
            'Presupuesto': st.session_state.presupuesto if st.session_state.presupuesto else 0.0,
            'Meta de Ahorro': meta_ahorro
        }
        st.session_state.finanzas = pd.concat([st.session_state.finanzas, pd.DataFrame([nueva_entrada])], ignore_index=True)
        st.success("¡Datos registrados con éxito!")

# Función para establecer el presupuesto (semanal o mensual)
def establecer_presupuesto():
    tipo = st.radio("Selecciona el tipo de presupuesto", ("Semanal", "Mensual"))
    presupuesto = st.number_input(f"Establece tu presupuesto {tipo.lower()}", min_value=0.0, step=1.0, format="%.2f")
    
    st.session_state.tipo_presupuesto = tipo
    st.session_state.presupuesto = presupuesto
    st.success(f"Presupuesto {tipo.lower()} establecido en ${presupuesto}")

# Función para establecer metas de gasto
def establecer_metas_gasto():
    tipo = st.radio("Selecciona el tipo de meta de gasto", ("Semanal", "Mensual"))
    meta_gasto = st.number_input(f"Establece tu meta de gasto {tipo.lower()}", min_value=0.0, step=1.0, format="%.2f")
    
    st.session_state.meta_gasto = meta_gasto
    st.success(f"Meta de gasto {tipo.lower()} establecida en ${meta_gasto}")

# Función para modificar registros previos
def modificar_registros():
    if not st.session_state.finanzas.empty:
        st.subheader("Modificar o Eliminar Datos")
        index = st.number_input("Selecciona el índice de la transacción a modificar/eliminar", min_value=0, max_value=len(st.session_state.finanzas)-1)
        
        if st.button("Eliminar transacción"):
            st.session_state.finanzas = st.session_state.finanzas.drop(index)
            st.success("¡Transacción eliminada!")
        elif st.button("Modificar transacción"):
            nueva_fecha = st.date_input("Nueva Fecha", value=st.session_state.finanzas.loc[index, 'Fecha'])
            nuevos_ingresos = st.number_input("Nuevos Ingresos", value=st.session_state.finanzas.loc[index, 'Ingresos'])
            nuevos_gastos = st.number_input("Nuevos Gastos", value=st.session_state.finanzas.loc[index, 'Gastos'])
            nueva_meta_ahorro = st.number_input("Nueva Meta de Ahorro", value=st.session_state.finanzas.loc[index, 'Meta de Ahorro'])
            
            if st.button("Guardar cambios"):
                st.session_state.finanzas.loc[index] = [nueva_fecha, nuevos_ingresos, nuevos_gastos, st.session_state.presupuesto, nueva_meta_ahorro]
                st.success("¡Datos modificados con éxito!")
    else:
        st.warning("No hay datos registrados.")

# Función para ver el reporte (semanal o mensual)
def ver_reporte():
    if not st.session_state.finanzas.empty:
        # Pedir al usuario el presupuesto si no lo ha establecido
        if 'presupuesto' not in st.session_state or st.session_state.presupuesto is None:
            st.session_state.presupuesto = st.number_input("Ingresa tu presupuesto para generar el reporte", min_value=0.0, step=1.0, format="%.2f")
        
        # Pedir la meta de ahorro si no ha sido definida, con valor predeterminado 0
        if 'meta_ahorro' not in st.session_state or st.session_state.meta_ahorro is None:
            st.session_state.meta_ahorro = 0.0

        # Selección de tipo de reporte
        tipo_reporte = st.radio("Selecciona el tipo de reporte", ("Semanal", "Mensual"))
        df_resumen = calcular_diferencias(st.session_state.finanzas, tipo_reporte.lower())
        st.subheader(f"Reporte {tipo_reporte}")
        st.write(df_resumen)
        st.line_chart(df_resumen.set_index(tipo_reporte.lower())[['Diferencia Ingresos', 'Diferencia Gastos', 'Diferencia Ahorro']])
    else:
        st.warning("No hay datos registrados.")

# Dependiendo de la opción seleccionada en el menú desplegable
if opcion == "Registrar nuevo gasto/ingreso":
    registrar_gasto_ingreso()
elif opcion == "Establecer presupuesto":
    establecer_presupuesto()
elif opcion == "Establecer metas de gasto":
    establecer_metas_gasto()
elif opcion == "Modificar registros previos":
    modificar_registros()
elif opcion == "Ver reporte":
    ver_reporte()
