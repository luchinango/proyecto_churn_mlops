# Instrucciones de ejecución

Desde la carpeta raíz del módulo (`mlops_pruebas`), activar el entorno virtual y entrar al proyecto:

```powershell
.\.venv\Scripts\Activate.ps1
cd proyecto_churn_mlops
```

## 1. Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

## 2. Flujo del modelo

```powershell
python src\preparar_datos.py
python src\entrenar_modelo.py
python src\evaluar_modelo.py
```

## 3. Levantar la API

```powershell
uvicorn api.main:app --reload
```

- Raíz: http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs

## 4. Pruebas automáticas

Detener la API con `Ctrl+C` y ejecutar:

```powershell
pytest
```
## Nota sobre trazabilidad

Cada cambio importante del proyecto debe registrarse mediante commits claros y descriptivos.

Esto permite conocer la evolución del código, la documentación, las pruebas y la configuración del proyecto.