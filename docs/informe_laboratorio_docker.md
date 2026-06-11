# Laboratorio: Dockerfile e imagen para servicio ML

**Módulo:** ML-Ops y Puesta en Producción  
**Estudiante:** Ing. Luis Alberto Martínez Barrientos  
**Proyecto:** `proyecto_churn_mlops`  
**Repositorio GitHub:** https://github.com/luchinango/proyecto_churn_mlops  

---

## Entrega adicional

- Enlace al repositorio: https://github.com/luchinango/proyecto_churn_mlops

---

## Evidencia 1 — Estructura del proyecto en VS Code

**Requisito:** Captura del explorador de archivos donde se observen `Dockerfile`, `.dockerignore`, `requirements.txt` y `api/main.py`.

**Ruta del proyecto:**

`C:\Proyectos\UAGRM\Modulo 16 - ML-Ops y Puesta en Produccion\mlops_pruebas\proyecto_churn_mlops`

**Archivos que deben verse:**

- `Dockerfile`
- `.dockerignore`
- `requirements.txt`
- `api/main.py`

**[INSERTAR CAPTURA 1 AQUÍ]**

---

## Evidencia 2 — Contenido de `api/main.py`

**Requisito:** Captura del archivo donde se observe el nombre y apellido en la respuesta de la API.

Fragmento relevante:

```python
@app.get("/")
def inicio():
    return {
        "mensaje": "Servicio ML-Ops activo",
        "estado": "ok",
        "autor": "Luis Alberto Martínez Barrientos",
    }
```

**[INSERTAR CAPTURA 2 AQUÍ — editor con api/main.py abierto]**

---

## Evidencia 3 — Construcción de la imagen Docker

**Requisito:** Terminal con el comando utilizado y resultado satisfactorio.

**Comando ejecutado:**

```powershell
cd "C:\Proyectos\UAGRM\Modulo 16 - ML-Ops y Puesta en Produccion\mlops_pruebas\proyecto_churn_mlops"
docker build -t churn-api-martinez:0.1 .
```

**Resultado esperado:** mensaje final `naming to docker.io/library/churn-api-martinez:0.1 done` sin errores.

**[INSERTAR CAPTURA 3 AQUÍ]**

---

## Evidencia 4 — Listado de imágenes Docker

**Requisito:** Imagen creada con nombre personalizado.

**Comando:**

```powershell
docker images churn-api-martinez
```

**Resultado de referencia:**

| REPOSITORY           | TAG | IMAGE ID   | CREATED   | SIZE  |
|----------------------|-----|------------|-----------|-------|
| churn-api-martinez   | 0.1 | 2cb942475266 | 2 days ago | 691MB |

**[INSERTAR CAPTURA 4 AQUÍ]**

---

## Evidencia 5 — Ejecución del contenedor

**Requisito:** Terminal mostrando el comando utilizado.

**Comando:**

```powershell
docker run -d --name churn-api -p 8000:8000 churn-api-martinez:0.1
```

**Nota:** Si el contenedor ya existía, primero:

```powershell
docker stop churn-api
docker rm churn-api
```

**[INSERTAR CAPTURA 5 AQUÍ]**

---

## Evidencia 6 — Contenedores activos y puerto publicado

**Requisito:** `docker ps` mostrando el contenedor en ejecución y el puerto `8000`.

**Comando:**

```powershell
docker ps --filter name=churn-api
```

**Resultado de referencia:**

| NAMES     | STATUS | PORTS                                      |
|-----------|--------|--------------------------------------------|
| churn-api | Up     | 0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp |

**[INSERTAR CAPTURA 6 AQUÍ]**

---

## Evidencia 7 — Prueba en el navegador

**Requisito:** URL local del servicio con nombre y apellido en la respuesta.

**URL:** http://127.0.0.1:8000

**Respuesta JSON esperada:**

```json
{
  "mensaje": "Servicio ML-Ops activo",
  "estado": "ok",
  "autor": "Luis Alberto Martínez Barrientos"
}
```

**[INSERTAR CAPTURA 7 AQUÍ — navegador en http://127.0.0.1:8000]**

---

## Resumen técnico (opcional para el informe)

| Criterio | Cumplimiento |
|----------|--------------|
| Estructura mínima del proyecto | `Dockerfile`, `.dockerignore`, `requirements.txt`, `api/main.py` |
| Dockerfile y dependencias | Imagen basada en `python:3.12-slim`, instala `requirements.txt`, entrena modelo en build |
| Construcción de imagen | `docker build -t churn-api-martinez:0.1 .` |
| Contenedor y puerto | `docker run -p 8000:8000` |
| API con respuesta personalizada | Campo `autor` con nombre completo |
| Evidencias ordenadas | Este documento + capturas |

---

## Comandos de referencia (sesión completa)

```powershell
# 1. Abrir Docker Desktop y verificar
docker run hello-world

# 2. Ir al proyecto
cd "C:\Proyectos\UAGRM\Modulo 16 - ML-Ops y Puesta en Produccion\mlops_pruebas\proyecto_churn_mlops"

# 3. Construir imagen
docker build -t churn-api-martinez:0.1 .

# 4. Ejecutar contenedor
docker run -d --name churn-api -p 8000:8000 churn-api-martinez:0.1

# 5. Verificar
docker images churn-api-martinez
docker ps --filter name=churn-api

# 6. Probar en navegador
# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs
```
