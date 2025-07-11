# examen2arq-monitor-sistema
Dashboard de monitoreo de sistema usando Django y psutil.
# 📊 Monitor de Sistema con Django y psutil

Este proyecto web permite visualizar en tiempo real el estado del sistema mediante una interfaz sencilla construida con Django. Utiliza la librería `psutil` para recolectar métricas clave como uso del CPU, memoria RAM, espacio en disco y características del sistema operativo.

---

## 🚀 ¿Cómo ejecutar el proyecto localmente?

### 1. Clonar el repositorio
```bash
git clone https://github.com/mvalle25/examen2arq-monitor-sistema.git
cd monitor
2. Crear y activar un entorno virtual
python -m venv env
# Activar entorno virtual (Windows)
.\env\Scripts\Activate.ps1
3. Instalar dependencias
pip install -r requirements.txt
4. Aplicar migraciones
python manage.py migrate
5. Ejecutar el servidor
python manage.py runserver
Abre tu navegador y visita http://127.0.0.1:8000/.
________________________________________
📦 Dependencias principales
•	Django: Framework para aplicaciones web.
•	psutil: Librería para monitorear recursos del sistema.
Instalación manual:
pip install django psutil
