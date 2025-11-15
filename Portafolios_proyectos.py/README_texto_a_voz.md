# Convertidor de Artículos a Audio MP3

## Descripción del Proyecto

Este proyecto permite convertir artículos web en archivos de audio reproducibles en formato MP3. El programa extrae el contenido de una URL, procesa el texto y lo convierte a voz usando tecnología Text-to-Speech de Google.

## Características

- ✅ Extracción automática de contenido desde URLs
- ✅ Conversión de texto a voz en múltiples idiomas
- ✅ Generación de archivos MP3
- ✅ Interfaz de usuario interactiva
- ✅ Manejo robusto de errores
- ✅ Reintentos automáticos en caso de fallos de conexión

## Requisitos

- Python 3.7+
- Conexión a Internet

## Instalación

### 1. Instalar Dependencias

```bash
pip install nltk newspaper3k gtts requests lxml_html_clean
```

### 2. Descargar Recursos de NLTK (Opcional)

```bash
python -c "import nltk; nltk.download('punkt')"
```

## Uso

### Opción 1: Interfaz Interactiva

Ejecuta el programa principal:

```bash
python texto_a_voz.py
```

Luego sigue las instrucciones en pantalla:
- Ingresa la URL del artículo
- Define el nombre del archivo de salida (opcional)
- Selecciona el idioma
- Elige si deseas reproducción lenta

### Opción 2: Uso Programático

```python
from texto_a_voz import convertir_articulo_a_audio

# Convertir un artículo a audio
ruta = convertir_articulo_a_audio(
    url="https://es.wikipedia.org/wiki/Python_(lenguaje_de_programación)",
    nombre_salida="articulo_python",
    idioma="es",  # Código de idioma (es, en, fr, pt, etc.)
    velocidad_lenta=False  # True para reproducción más lenta
)

print(f"Archivo guardado en: {ruta}")
```

## Funciones Principales

### `extraer_articulo(url: str) -> dict`
Extrae el contenido de un artículo desde una URL.

**Parámetros:**
- `url`: URL del artículo

**Retorna:** Diccionario con `titulo`, `autores`, `texto` y `url`

### `procesar_texto(texto: str) -> list`
Procesa el texto dividiéndolo en párrafos y limpiándolo.

**Parámetros:**
- `texto`: Texto a procesar

**Retorna:** Lista de párrafos limpios

### `convertir_texto_a_voz(texto: str, nombre_archivo: str, idioma: str = 'es', velocidad_lenta: bool = False) -> str`
Convierte texto a voz y guarda como archivo MP3.

**Parámetros:**
- `texto`: Texto a convertir
- `nombre_archivo`: Nombre del archivo MP3 (sin extensión)
- `idioma`: Código de idioma (por defecto: 'es')
- `velocidad_lenta`: Si True, reproduce más lentamente

**Retorna:** Ruta del archivo creado

### `convertir_articulo_a_audio(url: str, nombre_salida: str = None, idioma: str = 'es', velocidad_lenta: bool = False) -> str`
Flujo principal que convierte un artículo completo a audio.

**Parámetros:**
- `url`: URL del artículo
- `nombre_salida`: Nombre para el archivo (opcional, usa título si no se especifica)
- `idioma`: Código de idioma
- `velocidad_lenta`: Si True, reproduce más lentamente

**Retorna:** Ruta del archivo MP3 creado

## Idiomas Soportados

Los códigos de idioma más comunes:
- `es` - Español
- `en` - Inglés
- `fr` - Francés
- `pt` - Portugués
- `de` - Alemán
- `it` - Italiano
- `ja` - Japonés
- `zh-cn` - Chino Simplificado

Para una lista completa, consulta la documentación de gTTS.

## Estructura de Archivos

```
Portafolios_proyectos.py/
├── texto_a_voz.py              # Archivo principal del proyecto
├── verificar_importaciones.py   # Script de verificación
├── prueba_texto_a_voz.py       # Script de prueba
└── audios/                      # Carpeta de salida para archivos MP3
```

## Ejemplos de Uso

### Ejemplo 1: Convertir un artículo de Wikipedia

```python
from texto_a_voz import convertir_articulo_a_audio

url = "https://es.wikipedia.org/wiki/Inteligencia_artificial"
ruta = convertir_articulo_a_audio(
    url=url,
    nombre_salida="IA_explicada",
    idioma="es"
)
print(f"Audio creado: {ruta}")
```

### Ejemplo 2: Convertir en diferentes idiomas

```python
urls = {
    "español": "https://es.wikipedia.org/wiki/Python",
    "inglés": "https://en.wikipedia.org/wiki/Python",
    "francés": "https://fr.wikipedia.org/wiki/Python"
}

idiomas = {"español": "es", "inglés": "en", "francés": "fr"}

for nombre, url in urls.items():
    convertir_articulo_a_audio(
        url=url,
        nombre_salida=f"python_{nombre}",
        idioma=idiomas[nombre]
    )
```

## Solución de Problemas

### Error: "No se puede conectar a Google Text-to-Speech"
- Verifica tu conexión a Internet
- gTTS puede tener limitaciones de velocidad. Intenta esperar unos minutos y reintentar
- Algunos artículos muy largos pueden causar timeout. Intenta con URLs más cortas

### Error: "lxml.html.clean module is now a separate project"
- Instala: `pip install lxml_html_clean`

### Error: "URL inválida"
- Asegúrate de incluir `http://` o `https://` en la URL

### El archivo MP3 no se crea
- Verifica que tienes permisos de escritura en la carpeta del proyecto
- Comprueba que la carpeta `audios/` existe o tiene permisos para ser creada

## Notas Importantes

1. **Límites de gTTS**: Google Text-to-Speech tiene límites de velocidad. No intentes procesar demasiados artículos simultáneamente.

2. **Tamaño de archivos**: Los artículos muy largos pueden generar archivos MP3 grandes.

3. **Privacidad**: El texto se envía a los servidores de Google. Si tienes datos sensibles, considera alternativas locales como `pyttsx3`.

4. **Idiomas**: El idioma del artículo debe coincidir con el código de idioma especificado para mejores resultados.

## Mejoras Futuras

- [ ] Soporte para síntesis local con pyttsx3
- [ ] Procesar múltiples artículos en paralelo
- [ ] Agregar control de volumen
- [ ] Interfaz gráfica (GUI)
- [ ] Almacenamiento en caché de audios
- [ ] Exportar a otros formatos (WAV, OGG)

## Licencia

Este proyecto está disponible para uso educativo y personal.

## Autores

Desarrollado como proyecto educativo de Python Avanzado.
