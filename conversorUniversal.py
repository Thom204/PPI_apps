import streamlit as st

# Funciones de conversión para cada categoría

# Temperatura
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

# Longitud
def pies_a_metros(pies):
    return pies * 0.3048

def metros_a_pies(metros):
    return metros / 0.3048

def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54

def centimetros_a_pulgadas(centimetros):
    return centimetros / 2.54

# Peso/Masa
def libras_a_kilogramos(libras):
    return libras * 0.453592

def kilogramos_a_libras(kilogramos):
    return kilogramos / 0.453592

def onzas_a_gramos(onzas):
    return onzas * 28.3495

def gramos_a_onzas(gramos):
    return gramos / 28.3495

# Volumen
def galones_a_litros(galones):
    return galones * 3.78541

def litros_a_galones(litros):
    return litros / 3.78541

def pulgadas_cubicas_a_centimetros_cubicos(pulgadas_cubicas):
    return pulgadas_cubicas * 16.387

def centimetros_cubicos_a_pulgadas_cubicas(centimetros_cubicos):
    return centimetros_cubicos / 16.387

# Tiempo
def horas_a_minutos(horas):
    return horas * 60

def minutos_a_segundos(minutos):
    return minutos * 60

def dias_a_horas(dias):
    return dias * 24

def semanas_a_dias(semanas):
    return semanas * 7

# Velocidad
def millas_por_hora_a_kilometros_por_hora(millas_por_hora):
    return millas_por_hora * 1.60934

def kilometros_por_hora_a_metros_por_segundo(kilometros_por_hora):
    return kilometros_por_hora / 3.6

def nudos_a_millas_por_hora(nudos):
    return nudos * 1.15078

def metros_por_segundo_a_pies_por_segundo(metros_por_segundo):
    return metros_por_segundo * 3.28084

# Área
def metros_cuadrados_a_pies_cuadrados(metros_cuadrados):
    return metros_cuadrados * 10.7639

def pies_cuadrados_a_metros_cuadrados(pies_cuadrados):
    return pies_cuadrados / 10.7639

def kilometros_cuadrados_a_millas_cuadradas(kilometros_cuadrados):
    return kilometros_cuadrados * 0.386102

def millas_cuadradas_a_kilometros_cuadrados(millas_cuadradas):
    return millas_cuadradas / 0.386102

# Energía
def julios_a_calorias(julios):
    return julios * 0.239006

def calorias_a_kilojulios(calorias):
    return calorias * 0.004184

def kilovatios_hora_a_megajulios(kilovatios_hora):
    return kilovatios_hora * 3600

def megajulios_a_kilovatios_hora(megajulios):
    return megajulios / 3600

# Presión
def pascales_a_atmósferas(pascales):
    return pascales / 101325

def atmosferas_a_pascales(atmósferas):
    return atmósferas * 101325

def barras_a_libras_por_pulgada_cuadrada(barras):
    return barras * 14.5038

def libras_por_pulgada_cuadrada_a_bares(libras_por_pulgada_cuadrada):
    return libras_por_pulgada_cuadrada / 14.5038

# Tamaño de datos
def dtUp(data_in):
    return data_in / 1024

# Interfaz de usuario en Streamlit
st.title("Conversor de Unidades")
st.header("por Thomas Monnier Granda")

# Categoría de conversión
categoria = st.selectbox(
    "Selecciona el tipo de conversión",
    ["Temperatura", "Longitud", "Peso/Masa", "Volumen", "Tiempo", "Velocidad", "Área", "Energía", "Presión", "Tamaño de Datos"]
)

# Según la categoría seleccionada, desplegar los campos y conversiones correspondientes
if categoria == "Temperatura":
    tipo_conversion = st.selectbox(
        "Selecciona la conversión",
        ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"]
    )
    valor = st.number_input("Ingresa el valor")
    if tipo_conversion == "Celsius a Fahrenheit":
        st.write(f"{valor} °C = {celsius_a_fahrenheit(valor)} °F")
    elif tipo_conversion == "Fahrenheit a Celsius":
        st.write(f"{valor} °F = {fahrenheit_a_celsius(valor)} °C")
    elif tipo_conversion == "Celsius a Kelvin":
        st.write(f"{valor} °C = {celsius_a_kelvin(valor)} K")
    elif tipo_conversion == "Kelvin a Celsius":
        st.write(f"{valor} K = {kelvin_a_celsius(valor)} °C")

elif categoria == "Longitud":
    tipo_conversion = st.selectbox(
        "Selecciona la conversión",
        ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"]
    )
    valor = st.number_input("Ingresa el valor")
    if tipo_conversion == "Pies a metros":
        st.write(f"{valor} pies = {pies_a_metros(valor)} metros")
    elif tipo_conversion == "Metros a pies":
        st.write(f"{valor} metros = {metros_a_pies(valor)} pies")
    elif tipo_conversion == "Pulgadas a centímetros":
        st.write(f"{valor} pulgadas = {pulgadas_a_centimetros(valor)} centímetros")
    elif tipo_conversion == "Centímetros a pulgadas":
        st.write(f"{valor} centímetros = {centimetros_a_pulgadas(valor)} pulgadas")

elif categoria == "Peso/Masa":
    tipo_conversion = st.selectbox(
        "Selecciona la conversión",
        ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"]
    )
    valor = st.number_input("Ingresa el valor")
    if tipo_conversion == "Libras a kilogramos":
        st.write(f"{valor} libras = {libras_a_kilogramos(valor)} kilogramos")
    elif tipo_conversion == "Kilogramos a libras":
        st.write(f"{valor} kilogramos = {kilogramos_a_libras(valor)} libras")
    elif tipo_conversion == "Onzas a gramos":
        st.write(f"{valor} onzas = {onzas_a_gramos(valor)} gramos")
    elif tipo_conversion == "Gramos a onzas":
        st.write(f"{valor} gramos = {gramos_a_onzas(valor)} onzas")

elif categoria == "Volumen":
    tipo_conversion = st.selectbox(
        "Selecciona la conversión",
        ["Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"]
    )
    valor = st.number_input("Ingresa el valor")
    if tipo_conversion == "Galones a litros":
        st.write(f"{valor} galones = {galones_a_litros(valor)} litros")
    elif tipo_conversion == "Litros a galones":
        st.write(f"{valor} litros = {litros_a_galones(valor)} galones")
    elif tipo_conversion == "Pulgadas cúbicas a centímetros cúbicos":
        st.write(f"{valor} pulgadas cúbicas = {pulgadas_cubicas_a_centimetros_cubicos(valor)} centímetros cúbicos")
    elif tipo_conversion == "Centímetros cúbicos a pulgadas cúbicas":
        st.write(f"{valor} centímetros cúbicos = {centimetros_cubicos_a_pulgadas_cubicas(valor)} pulgadas cúbicas")

elif categoria == "Tiempo":
    tipo_conversion = st.selectbox(
        "Selecciona la conversión",
        ["Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"]
    )
    valor = st.number_input("Ingresa el valor")
    if tipo_conversion == "Horas a minutos":
        st.write(f"{valor} horas = {horas_a_minutos(valor)} minutos")
    elif tipo_conversion == "Minutos a segundos":
        st.write(f"{valor} minutos = {minutos_a_segundos(valor)} segundos")
    elif tipo_conversion == "Días a horas":
        st.write(f"{valor} días = {dias_a_horas(valor)} horas")
    elif tipo_conversion == "Semanas a días":
        st.write(f"{valor} semanas = {semanas_a_dias(valor)} días")

elif categoria == "Velocidad":
    tipo_conversion = st.selectbox(
        "Selecciona la conversión",
        ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", "Nudos a millas por hora", "Metros por segundo a pies por segundo"]
    )
    valor = st.number_input("Ingresa el valor")
    if tipo_conversion == "Millas por hora a kilómetros por hora":
        st.write(f"{valor} millas por hora = {millas_por_hora_a_kilometros_por_hora(valor)} kilómetros por hora")
    elif tipo_conversion == "Kilómetros por hora a metros por segundo":
        st.write(f"{valor} kilómetros por hora = {kilometros_por_hora_a_metros_por_segundo(valor)} metros por segundo")
    elif tipo_conversion == "Nudos a millas por hora":
        st.write(f"{valor} nudos = {nudos_a_millas_por_hora(valor)} millas por hora")
    elif tipo_conversion == "Metros por segundo a pies por segundo":
        st.write(f"{valor} metros por segundo = {metros_por_segundo_a_pies_por_segundo(valor)} pies por segundo")

elif categoria == "Área":
    tipo_conversion = st.selectbox(
        "Selecciona la conversión",
        ["Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados", "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"]
    )
    valor = st.number_input("Ingresa el valor")
    if tipo_conversion == "Metros cuadrados a pies cuadrados":
        st.write(f"{valor} metros cuadrados = {metros_cuadrados_a_pies_cuadrados(valor)} pies cuadrados")
    elif tipo_conversion == "Pies cuadrados a metros cuadrados":
        st.write(f"{valor} pies cuadrados = {pies_cuadrados_a_metros_cuadrados(valor)} metros cuadrados")
    elif tipo_conversion == "Kilómetros cuadrados a millas cuadradas":
        st.write(f"{valor} kilómetros cuadrados = {kilometros_cuadrados_a_millas_cuadradas(valor)} millas cuadradas")
    elif tipo_conversion == "Millas cuadradas a kilómetros cuadrados":
        st.write(f"{valor} millas cuadradas = {millas_cuadradas_a_kilometros_cuadrados(valor)} kilómetros cuadrados")

elif categoria == "Energía":
    tipo_conversion = st.selectbox(
        "Selecciona la conversión",
        ["Julios a calorías", "Calorías a kilojulios", "Kilovatios-hora a megajulios", "Megajulios a kilovatios-hora"]
    )
    valor = st.number_input("Ingresa el valor")
    if tipo_conversion == "Julios a calorías":
        st.write(f"{valor} julios = {julios_a_calorias(valor)} calorías")
    elif tipo_conversion == "Calorías a kilojulios":
        st.write(f"{valor} calorías = {calorias_a_kilojulios(valor)} kilojulios")
    elif tipo_conversion == "Kilovatios-hora a megajulios":
        st.write(f"{valor} kilovatios-hora = {kilovatios_hora_a_megajulios(valor)} megajulios")
    elif tipo_conversion == "Megajulios a kilovatios-hora":
        st.write(f"{valor} megajulios = {megajulios_a_kilovatios_hora(valor)} kilovatios-hora")

elif categoria == "Presión":
    tipo_conversion = st.selectbox(
        "Selecciona la conversión",
        ["Pascales a atmósferas", "Atmósferas a pascales", "Barras a libras por pulgada cuadrada", "Libras por pulgada cuadrada a bares"]
    )
    valor = st.number_input("Ingresa el valor")
    if tipo_conversion == "Pascales a atmósferas":
        st.write(f"{valor} pascales = {pascales_a_atmósferas(valor)} atmósferas")
    elif tipo_conversion == "Atmósferas a pascales":
        st.write(f"{valor} atmósferas = {atmosferas_a_pascales(valor)} pascales")
    elif tipo_conversion == "Barras a libras por pulgada cuadrada":
        st.write(f"{valor} barras = {barras_a_libras_por_pulgada_cuadrada(valor)} libras por pulgada cuadrada")
    elif tipo_conversion == "Libras por pulgada cuadrada a bares":
        st.write(f"{valor} libras por pulgada cuadrada = {libras_por_pulgada_cuadrada_a_bares(valor)} bares")

elif categoria == "Tamaño de Datos":
    tipo_conversion = st.selectbox(
        "Selecciona la conversión",
        ["Megabytes a gigabytes", "Gigabytes a Terabytes", "Kilobytes a megabytes", "Terabytes a petabytes"]
    )
    valor = st.number_input("Ingresa el valor")
    if tipo_conversion == "Megabytes a gigabytes":
        st.write(f"{valor} megabytes = {dtUp(valor)} gigabytes")
    elif tipo_conversion == "Gigabytes a Terabytes":
        st.write(f"{valor} gigabytes = {dtUp(valor)} terabytes")
    elif tipo_conversion == "Kilobytes a megabytes":
        st.write(f"{valor} kilobytes = {dtUp(valor)} megabytes")
    elif tipo_conversion == "Terabytes a petabytes":
        st.write(f"{valor} terabytes = {dtUp(valor)} petabytes")
