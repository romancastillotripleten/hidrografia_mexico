# 🌊 Monitor de Calidad del Agua en México (2000–2024) 🇲🇽

> *"El agua es el principio de todas las cosas y el termómetro más honesto de nuestro impacto ambiental."* — Una iniciativa de analítica de datos aplicada a la sostenibilidad hídrica nacional.

---

## 📌 Descripción del Proyecto

El **Monitor de Calidad del Agua en México** es una plataforma analítica interactiva diseñada para examinar y visualizar la evolución del estado de los principales ríos, lagos, acuíferos y lagunas costeras del país a lo largo de un cuarto de siglo (2000–2024).

A través de un dataset curado con métricas físico-químicas y microbiológicas esenciales (como **DBO₅**, **DQO**, **SST**, **Oxígeno Disuelto**, **Coliformes Fecales** y metales pesados), este dashboard permite:
* 🔍 Identificar focos críticos de contaminación por actividad económica (industrial, agrícola, textil, minera y urbana).
* 🚨 Monitorear alertas sanitarias y evaluar el cumplimiento de la norma federal **NOM-001-SEMARNAT**.
* 📊 Explorar correlaciones multivariadas para fundamentar decisiones informadas en materia de conservación y gestión de recursos hídricos.

Este repositorio forma parte de mi portafolio profesional en **Ciencia de Datos** y **Frontend Analytics**, demostrando habilidades en limpieza de datos, modelado analítico y creación de aplicaciones interactivas accesibles para el usuario final.

---

## 🛠️ Tecnologías Utilizadas

El ecosistema tecnológico fue seleccionado para garantizar rapidez, diseño responsivo y escalabilidad visual:

* **Lenguaje:**
  * ![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white) — Procesamiento numérico, estructuración y manipulación de series temporales.
* **Manipulación y Análisis de Datos:**
  * ![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white) — Agrupación, filtrado y transformación vectorial de registros de calidad hídrica.
* **Visualización Dinámica:**
  * ![Plotly](https://img.shields.io/badge/Plotly_Express-5.0%2B-3F4F75?style=for-the-badge&logo=plotly&logoColor=white) — Creación de histogramas marginales, gráficos de dona y comparativas de barras interactivas con tooltips detallados.
* **Frontend y Despliegue de Dashboard:**
  * ![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) — Arquitectura de paneles reactivos con filtros multinivel y KPIs en tiempo real.

---

## 🚀 Guía de Instalación y Ejecución Local

Sigue estos sencillos pasos para clonar el repositorio, preparar el entorno y correr la aplicación en tu computadora:

### 1. Clonar el repositorio
Abre tu terminal o consola de comandos y descarga el código:
```bash
git clone https://github.com/tu-usuario/monitor-agua-mexico.git
cd monitor-agua-mexico
```

### 2. Crear y activar un entorno virtual (recomendado)
Mantén tus dependencias aisladas y ordenadas:
* **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **En Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

### 3. Instalar las dependencias
Instala los paquetes necesarios definidos en `requirements.txt`:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **Nota:** Si aún no has creado tu archivo `requirements.txt`, puedes crearlo con este contenido:
> ```text
> streamlit>=1.28.0
> pandas>=2.0.0
> plotly>=5.15.0
> ```

### 4. Verificar la estructura de carpetas
Asegúrate de que el conjunto de datos se encuentre en la ruta esperada:
```text
monitor-agua-mexico/
├── app.py
├── data/
│   └── datos.csv
├── requirements.txt
└── README.md
```

### 5. Iniciar la aplicación
Ejecuta el servidor de Streamlit con el siguiente comando:
```bash
streamlit run app.py
```

Tu navegador predeterminado se abrirá automáticamente en `http://localhost:8501`. ¡Listo para interactuar con los datos! 🎉

---

## 💡 Próximas Mejoras (Roadmap)
1. Integración de capas geográficas con mapas coropléticos interactivos vía **Folium** o **Mapbox**.
2. Módulo de predicción de niveles de DBO₅ a 12 meses utilizando modelos de series temporales.
3. Exportación automatizada de reportes ejecutivos en formato PDF.

---

## 🤝 Contacto y Conexiones

¿Tienes sugerencias, ideas de colaboración o deseas charlar sobre proyectos de datos orientados a impacto ambiental?

* **Portafolio:** [tu-portafolio.dev](https://tu-portafolio.dev)
* **LinkedIn:** [linkedin.com/in/tu-perfil](https://linkedin.com/in/tu-perfil)
* **Email:** `tu-correo@dominio.com`