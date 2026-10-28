import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# 1. Configuración general de la página
# ---------------------------------------------------------
st.set_page_config(
    page_title="Monitor de Agua en México",
    page_icon="🌊",
    layout="wide"
)

# ---------------------------------------------------------
# 2. Carga del conjunto de datos
# ---------------------------------------------------------
@st.cache_data
def cargar_datos():
    # Carga de datos desde la ruta solicitada
    df = pd.read_csv("data/datos.csv")
    df["fecha_monitoreo"] = pd.to_datetime(df["fecha_monitoreo"])
    return df

try:
    df_agua = cargar_datos()
except FileNotFoundError:
    st.error("⚠️ No se encontró el archivo en 'data/datos.csv'. Verifica que exista la carpeta y el archivo.")
    st.stop()

# ---------------------------------------------------------
# 3. Título y Subtítulo llamativos con Emojis
# ---------------------------------------------------------
st.title("🌊💧 Monitor de Calidad del Agua en México (2000 - 2024) 🇲🇽")
st.markdown("### 📊 *Explora 25 años de registros ambientales, niveles de contaminantes y alertas sanitarias en cuencas mexicanas*")
st.write("---")

# ---------------------------------------------------------
# 4. Barra lateral: Filtros interactivos (Dropdown y Checkboxes)
# ---------------------------------------------------------
st.sidebar.header("🔍 Panel de Filtros")

# Filtro Dropdown 1: Región Hidrológica
opciones_region = ["Todas"] + sorted(df_agua["region_hidrologica"].dropna().unique().tolist())
region_seleccionada = st.sidebar.selectbox(
    "🌍 Selecciona una Región Hidrológica:",
    options=opciones_region
)

# Filtro Dropdown 2: Clasificación de Calidad del Agua
opciones_calidad = ["Todas"] + sorted(df_agua["clasificacion_calidad"].dropna().unique().tolist())
calidad_seleccionada = st.sidebar.selectbox(
    "🧪 Filtra por Clasificación de Calidad:",
    options=opciones_calidad
)

# Filtro Checkbox 1: Solo registros con Alerta Sanitaria activa
solo_alerta = st.sidebar.checkbox(
    "🚨 Ver únicamente cuerpos con Alerta Sanitaria",
    value=False
)

# Filtro Checkbox 2: Solo los que cumplen la norma NOM-001
solo_nom001 = st.sidebar.checkbox(
    "✅ Ver únicamente los que cumplen NOM-001",
    value=False
)

# ---------------------------------------------------------
# 5. Aplicar los filtros sobre el DataFrame
# ---------------------------------------------------------
df_filtrado = df_agua.copy()

if region_seleccionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["region_hidrologica"] == region_seleccionada]

if calidad_seleccionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["clasificacion_calidad"] == calidad_seleccionada]

if solo_alerta:
    df_filtrado = df_filtrado[df_filtrado["alerta_sanitaria"] == True]

if solo_nom001:
    df_filtrado = df_filtrado[df_filtrado["cumple_norma_nom001"] == True]

# ---------------------------------------------------------
# 6. Tarjetas de métricas rápidas (KPIs)
# ---------------------------------------------------------
col_m1, col_m2, col_m3, col_m4 = st.columns(4)

with col_m1:
    st.metric("Total de Registros", len(df_filtrado))
with col_m2:
    ica_promedio = round(df_filtrado["indice_calidad_agua_ica"].mean(), 1) if not df_filtrado.empty else 0
    st.metric("ICA Promedio (0-100)", f"{ica_promedio} pts")
with col_m3:
    alertas_totales = int(df_filtrado["alerta_sanitaria"].sum()) if not df_filtrado.empty else 0
    st.metric("Alertas Sanitarias", alertas_totales)
with col_m4:
    aptos_consumo = int(df_filtrado["apto_consumo_humano"].sum()) if not df_filtrado.empty else 0
    st.metric("Aptos para Consumo", aptos_consumo)

st.write("")

# ---------------------------------------------------------
# 7. Checkbox para mostrar/ocultar vista previa del DataFrame
# ---------------------------------------------------------
ver_tabla = st.checkbox("👁️ Mostrar vista previa de los datos filtrados (Primeras 10 filas)", value=False)
if ver_tabla:
    if df_filtrado.empty:
        st.warning("No hay datos disponibles para la combinación de filtros seleccionada.")
    else:
        st.dataframe(df_filtrado.head(10), use_container_width=True)

st.write("---")

# Validar que haya datos antes de generar gráficos
if df_filtrado.empty:
    st.warning("⚠️ No se encontraron registros con los filtros seleccionados. Intenta ajustar los parámetros en la barra lateral.")
    st.stop()

# ---------------------------------------------------------
# 8. Gráficos Interactivos con Plotly Express
# ---------------------------------------------------------

# Fila superior: Gráfico de Barras y Gráfico Circular
col_izq, col_der = st.columns(2)

with col_izq:
    st.subheader("🏭 Gráfico 1: Demanda Bioquímica de Oxígeno (DBO5) por Fuente")
    # Gráfico de Barras Horizontales
    # Agrupamos por fuente para mostrar el promedio de DBO5
    df_barras = (
        df_filtrado.groupby("fuente_principal_contaminacion", as_index=False)["dbo5_mg_l"]
        .mean()
        .sort_values(by="dbo5_mg_l", ascending=True)
    )

    fig_barras = px.bar(
        df_barras,
        x="dbo5_mg_l",
        y="fuente_principal_contaminacion",
        orientation="h",
        color="dbo5_mg_l",
        color_continuous_scale="Reds",
        labels={
            "dbo5_mg_l": "DBO5 Promedio (mg/L)",
            "fuente_principal_contaminacion": "Fuente de Contaminación"
        },
        title="Promedio de DBO5 según la Fuente Principal"
    )
    fig_barras.update_layout(
        template="plotly_white",
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.plotly_chart(fig_barras, use_container_width=True)

with col_der:
    st.subheader("🍩 Gráfico 2: Distribución por Clasificación de Calidad")
    # Gráfico Circular tipo Donut
    conteo_calidad = df_filtrado["clasificacion_calidad"].value_counts().reset_index()
    conteo_calidad.columns = ["clasificacion_calidad", "cantidad"]

    fig_pie = px.pie(
        conteo_calidad,
        names="clasificacion_calidad",
        values="cantidad",
        hole=0.45,
        color="clasificacion_calidad",
        color_discrete_map={
            "Excelente / Buena": "#2ca02c",
            "Aceptable / Moderada": "#1f77b4",
            "Contaminada": "#ff7f0e",
            "Fuertemente Contaminada": "#d62728"
        },
        title="Proporción de Cuerpos de Agua por Calidad"
    )
    fig_pie.update_traces(textposition="inside", textinfo="percent+label")
    fig_pie.update_layout(
        template="plotly_white",
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Fila inferior: Histograma a todo lo ancho
st.write("---")
st.subheader("📈 Gráfico 3: Distribución del Índice de Calidad del Agua (ICA)")

fig_hist = px.histogram(
    df_filtrado,
    x="indice_calidad_agua_ica",
    nbins=20,
    color="tipo_cuerpo",
    marginal="box",  # Añade un boxplot complementario en la parte superior
    opacity=0.8,
    labels={
        "indice_calidad_agua_ica": "Índice de Calidad del Agua (0 - 100)",
        "tipo_cuerpo": "Tipo de Cuerpo"
    },
    title="Frecuencia y Distribución del ICA por Tipo de Cuerpo Hídrico"
)
fig_hist.update_layout(
    template="plotly_white",
    bargap=0.08,
    margin=dict(l=20, r=20, t=40, b=20)
)
st.plotly_chart(fig_hist, use_container_width=True)