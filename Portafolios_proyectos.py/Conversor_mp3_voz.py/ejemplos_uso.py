"""
Ejemplos de uso del convertidor de artículos a audio MP3

Este archivo contiene varios ejemplos de cómo usar el módulo texto_a_voz
en diferentes escenarios.
"""

from texto_a_voz import (
    extraer_articulo,
    procesar_texto,
    convertir_texto_a_voz,
    convertir_articulo_a_audio
)


# ============================================================================
# EJEMPLO 1: Uso básico - Convertir un artículo simple
# ============================================================================

def ejemplo_1_basico():
    """Convertir un artículo simple a audio"""
    print("\n" + "="*60)
    print("EJEMPLO 1: Conversión Básica")
    print("="*60)
    
    url = "https://es.wikipedia.org/wiki/Inteligencia_artificial"
    
    try:
        ruta = convertir_articulo_a_audio(
            url=url,
            nombre_salida="ejemplo1_IA"
        )
        print(f"✓ Archivo creado: {ruta}")
    except Exception as e:
        print(f"✗ Error: {e}")


# ============================================================================
# EJEMPLO 2: Conversión con opciones personalizadas
# ============================================================================

def ejemplo_2_opciones():
    """Convertir un artículo con opciones personalizadas"""
    print("\n" + "="*60)
    print("EJEMPLO 2: Conversión con Opciones")
    print("="*60)
    
    url = "https://es.wikipedia.org/wiki/Python_(lenguaje_de_programación)"
    
    try:
        ruta = convertir_articulo_a_audio(
            url=url,
            nombre_salida="ejemplo2_python",
            idioma="es",
            velocidad_lenta=True  # Reproducción más lenta
        )
        print(f"✓ Archivo creado: {ruta}")
    except Exception as e:
        print(f"✗ Error: {e}")


# ============================================================================
# EJEMPLO 3: Extración y procesamiento manual
# ============================================================================

def ejemplo_3_manual():
    """Procesar artículo paso a paso"""
    print("\n" + "="*60)
    print("EJEMPLO 3: Procesamiento Manual")
    print("="*60)
    
    url = "https://es.wikipedia.org/wiki/Programación_orientada_a_objetos"
    
    try:
        # Paso 1: Extraer
        print("\n[1] Extrayendo artículo...")
        info = extraer_articulo(url)
        print(f"  Título: {info['titulo']}")
        print(f"  Caracteres: {len(info['texto'])}")
        
        # Paso 2: Procesar
        print("\n[2] Procesando texto...")
        parrafos = procesar_texto(info['texto'])
        print(f"  Párrafos: {len(parrafos)}")
        
        # Paso 3: Convertir a voz
        print("\n[3] Convirtiendo a voz...")
        texto_completo = ' '.join(parrafos)
        ruta = convertir_texto_a_voz(
            texto=texto_completo[:1000],  # Solo primeros 1000 caracteres
            nombre_archivo="ejemplo3_POO"
        )
        print(f"  Archivo: {ruta}")
        
    except Exception as e:
        print(f"✗ Error: {e}")


# ============================================================================
# EJEMPLO 4: Múltiples idiomas
# ============================================================================

def ejemplo_4_idiomas():
    """Convertir el mismo artículo en diferentes idiomas"""
    print("\n" + "="*60)
    print("EJEMPLO 4: Múltiples Idiomas")
    print("="*60)
    
    urls = {
        "Wikipedia ES": {
            "url": "https://es.wikipedia.org/wiki/Matemáticas",
            "idioma": "es"
        },
        "Wikipedia EN": {
            "url": "https://en.wikipedia.org/wiki/Mathematics",
            "idioma": "en"
        },
        "Wikipedia FR": {
            "url": "https://fr.wikipedia.org/wiki/Mathématiques",
            "idioma": "fr"
        }
    }
    
    for nombre, datos in urls.items():
        try:
            print(f"\n  Procesando {nombre}...")
            ruta = convertir_articulo_a_audio(
                url=datos["url"],
                nombre_salida=f"ejemplo4_{nombre.replace(' ', '_')}",
                idioma=datos["idioma"]
            )
            print(f"  ✓ {nombre}: {ruta}")
        except Exception as e:
            print(f"  ✗ {nombre}: {e}")


# ============================================================================
# EJEMPLO 5: Procesar solo partes de un artículo
# ============================================================================

def ejemplo_5_parcial():
    """Procesar solo una parte del artículo"""
    print("\n" + "="*60)
    print("EJEMPLO 5: Procesamiento Parcial")
    print("="*60)
    
    url = "https://es.wikipedia.org/wiki/Física"
    
    try:
        # Extraer artículo
        print("\n  Extrayendo artículo...")
        info = extraer_articulo(url)
        
        # Procesar solo los primeros 3000 caracteres
        print("  Procesando primeros 3000 caracteres...")
        texto_parcial = info['texto'][:3000]
        parrafos = procesar_texto(texto_parcial)
        
        # Convertir a voz
        print("  Convirtiendo a voz...")
        texto_completo = ' '.join(parrafos)
        ruta = convertir_texto_a_voz(
            texto=texto_completo,
            nombre_archivo="ejemplo5_fisica_parcial"
        )
        print(f"\n✓ Archivo creado: {ruta}")
        
    except Exception as e:
        print(f"✗ Error: {e}")


# ============================================================================
# EJEMPLO 6: Comparar velocidades
# ============================================================================

def ejemplo_6_velocidades():
    """Crear dos versiones: normal y lenta"""
    print("\n" + "="*60)
    print("EJEMPLO 6: Comparar Velocidades")
    print("="*60)
    
    url = "https://es.wikipedia.org/wiki/Historia"
    
    try:
        # Versión normal
        print("\n  [1] Creando versión a velocidad normal...")
        ruta1 = convertir_articulo_a_audio(
            url=url,
            nombre_salida="ejemplo6_historia_normal",
            velocidad_lenta=False
        )
        print(f"  ✓ Normal: {ruta1}")
        
        # Versión lenta
        print("\n  [2] Creando versión a velocidad lenta...")
        ruta2 = convertir_articulo_a_audio(
            url=url,
            nombre_salida="ejemplo6_historia_lenta",
            velocidad_lenta=True
        )
        print(f"  ✓ Lenta: {ruta2}")
        
        print("\n  Puedes comparar ambas versiones para elegir la que prefieras")
        
    except Exception as e:
        print(f"✗ Error: {e}")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("EJEMPLOS DE USO: Convertidor de Artículos a Audio MP3")
    print("="*60)
    
    print("\nSelecciona un ejemplo para ejecutar:")
    print("1. Conversión Básica")
    print("2. Conversión con Opciones")
    print("3. Procesamiento Manual")
    print("4. Múltiples Idiomas")
    print("5. Procesamiento Parcial")
    print("6. Comparar Velocidades")
    print("0. Salir")
    
    opcion = input("\nIngresa tu opción (0-6): ").strip()
    
    ejemplos = {
        "1": ("Conversión Básica", ejemplo_1_basico),
        "2": ("Conversión con Opciones", ejemplo_2_opciones),
        "3": ("Procesamiento Manual", ejemplo_3_manual),
        "4": ("Múltiples Idiomas", ejemplo_4_idiomas),
        "5": ("Procesamiento Parcial", ejemplo_5_parcial),
        "6": ("Comparar Velocidades", ejemplo_6_velocidades),
    }
    
    if opcion in ejemplos:
        nombre, funcion = ejemplos[opcion]
        try:
            funcion()
            print("\n" + "="*60)
            print("✓ Ejemplo completado correctamente")
            print("="*60)
        except Exception as e:
            print(f"\n✗ Error al ejecutar ejemplo: {e}")
    elif opcion != "0":
        print("Opción inválida. Por favor, ingresa un número entre 0 y 6.")
    
    print("\n¡Gracias por usar el Convertidor de Artículos a Audio MP3!")
