
# App Dash - Serie Temporal por Variable

Esta es una aplicación web desarrollada con Dash y Plotly para visualizar series temporales de variables ambientales, separadas por estación.

## 📊 ¿Qué hace esta app?

- Carga datos de series temporales desde `datos_agrupados_sem.csv`.
- Permite seleccionar una variable (`Descripción`) desde un menú desplegable.
- Muestra un gráfico interactivo con la evolución de dicha variable, separada por estación (`NombreEstacion`).
- Exportada con `Dash`, lista para ser desplegada en [Render.com](https://render.com).

---

## 🚀 Cómo desplegar en Render.com

1. **Crea un repositorio en GitHub** y sube estos archivos:
   - `app.py`
   - `requirements.txt`
   - `datos_agrupados_sem.csv`
   - `README.md`

2. **Ingresa a [https://render.com](https://render.com)** y crea una cuenta.

3. Clic en **“New Web Service”** y conecta tu cuenta de GitHub.

4. Usa estas configuraciones:
   - **Build Command:**  
     ```
     pip install -r requirements.txt
     ```
   - **Start Command:**  
     ```
     python app.py
     ```

5. Selecciona región, runtime (Python 3.10 o similar), y espera el despliegue.

---

## ✅ Requisitos

- `dash`
- `plotly`
- `pandas`

Instalados automáticamente por `requirements.txt`.

---

## 📁 Estructura

```
📦 dash_app_render/
├── app.py                  # Código principal de la app Dash
├── datos_agrupados_sem.csv # Datos de entrada
├── requirements.txt        # Librerías necesarias
└── README.md               # Este archivo
```

---

## ✉️ Contacto

Desarrollado por Daniel Osorio.  
Soporte adicional: [https://chat.openai.com](https://chat.openai.com)

---
