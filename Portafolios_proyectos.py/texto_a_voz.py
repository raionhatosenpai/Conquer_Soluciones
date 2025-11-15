"""
Proyecto: Convertidor de Artículos a Audio MP3
Descripción: Este programa convierte artículos web en archivos de audio MP3.
Bibliotecas utilizadas:
- newspaper3k: Extrae contenido de artículos web
- gtts (Google Text-to-Speech): Convierte texto a voz
- nltk: Procesamiento de lenguaje natural
- requests: Manejo de solicitudes HTTP
"""

import os
import re
from pathlib import Path
from urllib.parse import urlparse
from newspaper import Article
from gtts import gTTS
import nltk

# Descargar recursos de NLTK (solo la primera vez)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    try:
        nltk.download('punkt', quiet=True)
    except:
        pass  # Continuar incluso si falla la descarga


def extraer_articulo(url: str) -> dict:
    """
    Extrae el contenido de un artículo desde una URL.
    
    Args:
        url (str): URL del artículo a extraer
    
    Returns:
        dict: Diccionario con título, autores y texto del artículo
    
    Raises:
        Exception: Si la URL es inválida o no se puede acceder al contenido
    """
    try:
        # Validar URL
        resultado_url = urlparse(url)
        if not all([resultado_url.scheme, resultado_url.netloc]):
            raise ValueError("URL inválida. Asegúrate de incluir http:// o https://")
        
        # Crear objeto Article y descargar contenido
        articulo = Article(url)
        articulo.download()
        articulo.parse()
        
        # Extraer información
        if not articulo.text:
            raise ValueError("No se pudo extraer contenido del artículo")
        
        return {
            'titulo': articulo.title or 'Sin título',
            'autores': articulo.authors,
            'texto': articulo.text,
            'url': url
        }
    
    except Exception as e:
        raise Exception(f"Error al extraer artículo: {str(e)}")


def procesar_texto(texto: str) -> list:
    """
    Procesa el texto dividiéndolo en párrafos y limpiándolo.
    
    Args:
        texto (str): Texto a procesar
    
    Returns:
        list: Lista de párrafos limpios
    """
    # Dividir por párrafos (líneas vacías)
    parrafos = [p.strip() for p in texto.split('\n') if p.strip()]
    
    # Limpiar párrafos (remover caracteres especiales problemáticos)
    parrafos_limpios = []
    for parrafo in parrafos:
        # Remover referencias de URLs dentro del texto
        parrafo_limpio = re.sub(r'http\S+|www\S+', '', parrafo)
        # Remover múltiples espacios
        parrafo_limpio = re.sub(r'\s+', ' ', parrafo_limpio).strip()
        if parrafo_limpio:  # Solo agregar si no está vacío
            parrafos_limpios.append(parrafo_limpio)
    
    return parrafos_limpios


def dividir_en_fragmentos(texto: str, max_chars: int = 100) -> list:
    """
    Divide el texto en fragmentos por límite de caracteres para gTTS.
    
    Args:
        texto (str): Texto a dividir
        max_chars (int): Máximo de caracteres por fragmento
    
    Returns:
        list: Lista de fragmentos de texto
    """
    palabras = texto.split()
    fragmentos = []
    fragmento_actual = []
    caracteres_actuales = 0
    
    for palabra in palabras:
        caracteres_palabra = len(palabra) + 1  # +1 por el espacio
        
        if caracteres_actuales + caracteres_palabra > max_chars and fragmento_actual:
            fragmentos.append(' '.join(fragmento_actual))
            fragmento_actual = [palabra]
            caracteres_actuales = caracteres_palabra
        else:
            fragmento_actual.append(palabra)
            caracteres_actuales += caracteres_palabra
    
    if fragmento_actual:
        fragmentos.append(' '.join(fragmento_actual))
    
    return fragmentos


def convertir_texto_a_voz(texto: str, nombre_archivo: str, idioma: str = 'es', velocidad_lenta: bool = False) -> str:
    """
    Convierte texto a voz y guarda como archivo MP3.
    
    Args:
        texto (str): Texto a convertir
        nombre_archivo (str): Nombre del archivo MP3 (sin extensión)
        idioma (str): Código de idioma para gTTS (ej: 'es', 'en', 'fr')
        velocidad_lenta (bool): Si True, reproduce más lentamente
    
    Returns:
        str: Ruta del archivo creado
    
    Raises:
        Exception: Si hay error en la conversión de texto a voz
    """
    try:
        # Crear carpeta de salida si no existe
        carpeta_salida = Path(__file__).parent / 'audios'
        carpeta_salida.mkdir(exist_ok=True)
        
        # Dividir texto en fragmentos si es muy largo
        fragmentos = dividir_en_fragmentos(texto, max_chars=100)
        
        # Crear objeto gTTS con reintentos
        max_intentos = 3
        intento = 0
        tts = None
        
        while intento < max_intentos and tts is None:
            try:
                tts = gTTS(text=texto[:5000], lang=idioma, slow=velocidad_lenta)  # Usar primeros 5000 caracteres para conexión
                break
            except Exception as e:
                intento += 1
                if intento < max_intentos:
                    print(f"  Reintentando conexión ({intento}/{max_intentos})...")
                    import time
                    time.sleep(2)  # Esperar 2 segundos antes de reintentar
                else:
                    raise Exception(f"No se pudo conectar a Google Text-to-Speech después de {max_intentos} intentos. Error: {str(e)}")
        
        # Guardar archivo
        ruta_archivo = carpeta_salida / f"{nombre_archivo}.mp3"
        tts.save(str(ruta_archivo))
        
        return str(ruta_archivo)
    
    except Exception as e:
        raise Exception(f"Error al convertir texto a voz: {str(e)}")


def convertir_articulo_a_audio(url: str, nombre_salida: str = None, idioma: str = 'es', velocidad_lenta: bool = False) -> str:
    """
    Flujo principal: convierte un artículo completo a audio MP3.
    
    Args:
        url (str): URL del artículo
        nombre_salida (str): Nombre para el archivo de salida (opcional)
        idioma (str): Código de idioma para la voz
        velocidad_lenta (bool): Si True, reproduce más lentamente
    
    Returns:
        str: Ruta del archivo MP3 creado
    """
    print("=" * 60)
    print("CONVERTIDOR DE ARTÍCULOS A AUDIO MP3")
    print("=" * 60)
    
    try:
        # Paso 1: Extraer artículo
        print("\n[1/4] Extrayendo contenido del artículo...")
        info_articulo = extraer_articulo(url)
        print(f"✓ Artículo extraído: '{info_articulo['titulo']}'")
        print(f"  Cantidad de caracteres: {len(info_articulo['texto'])}")
        
        # Paso 2: Procesar texto
        print("\n[2/4] Procesando texto...")
        parrafos = procesar_texto(info_articulo['texto'])
        print(f"✓ Texto procesado: {len(parrafos)} párrafos encontrados")
        
        # Paso 3: Preparar nombre de salida
        if nombre_salida is None:
            # Usar título del artículo (limpio)
            nombre_salida = re.sub(r'[^\w\s-]', '', info_articulo['titulo'])
            nombre_salida = re.sub(r'[-\s]+', '_', nombre_salida)[:50]  # Limitar a 50 caracteres
        
        print(f"  Nombre del archivo: {nombre_salida}.mp3")
        
        # Paso 4: Convertir a voz
        print("\n[3/4] Convirtiendo texto a voz...")
        texto_completo = ' '.join(parrafos)
        ruta_archivo = convertir_texto_a_voz(texto_completo, nombre_salida, idioma, velocidad_lenta)
        print(f"✓ Archivo de audio creado")
        
        # Información final
        print("\n[4/4] Proceso completado")
        print("=" * 60)
        print(f"✓ Archivo guardado en: {ruta_archivo}")
        print(f"  Tamaño aproximado: {os.path.getsize(ruta_archivo) / 1024:.1f} KB")
        print("=" * 60)
        
        return ruta_archivo
    
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        raise


def interfaz_usuario():
    """
    Interfaz interactiva para que el usuario ingrese los datos necesarios.
    """
    print("\n" + "=" * 60)
    print("CONVERTIDOR DE ARTÍCULOS A AUDIO MP3")
    print("=" * 60)
    
    # Solicitar URL
    while True:
        url = input("\nIngresa la URL del artículo: ").strip()
        if url:
            break
        print("Por favor, ingresa una URL válida")
    
    # Solicitar nombre de salida (opcional)
    nombre_salida = input("Nombre del archivo de salida (opcional, Enter para usar título): ").strip()
    if not nombre_salida:
        nombre_salida = None
    
    # Solicitar idioma
    print("\nIdiomas disponibles: es (español), en (inglés), fr (francés), pt (portugués)")
    idioma = input("Idioma para la voz (por defecto: es): ").strip().lower() or 'es'
    
    # Solicitar velocidad
    velocidad = input("¿Reproducción lenta? (s/n, por defecto: n): ").strip().lower() == 's'
    
    try:
        ruta = convertir_articulo_a_audio(url, nombre_salida, idioma, velocidad)
        print(f"\n✓ ¡Conversión exitosa! Archivo guardado en: {ruta}")
    except Exception as e:
        print(f"\n✗ Error durante la conversión: {str(e)}")


if __name__ == "__main__":
    # Ejecutar interfaz de usuario
    interfaz_usuario()