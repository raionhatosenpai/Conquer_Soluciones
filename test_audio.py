#!/usr/bin/env python
"""
Script de prueba simplificado para el convertidor de artículos a audio MP3
"""

import sys
sys.path.insert(0, './Portafolios_proyectos.py')

from texto_a_voz import convertir_articulo_a_audio

# Ejemplo de uso: convertir un artículo
if __name__ == "__main__":
    # URL de prueba - usando un artículo de Wikipedia
    url_prueba = "https://es.wikipedia.org/wiki/Python_(lenguaje_de_programación)"
    
    print("\n" + "="*60)
    print("PRUEBA: Convertidor de Artículos a Audio MP3")
    print("="*60)
    print(f"URL de prueba: {url_prueba}\n")
    
    try:
        # Convertir artículo a audio
        ruta_archivo = convertir_articulo_a_audio(
            url=url_prueba,
            nombre_salida="prueba_python",
            idioma="es",
            velocidad_lenta=False
        )
        
        print("\n✓ Prueba completada exitosamente!")
        print(f"Archivo de audio disponible en: {ruta_archivo}")
        
    except Exception as e:
        print(f"\n✗ Error en la prueba: {str(e)}")
        sys.exit(1)
