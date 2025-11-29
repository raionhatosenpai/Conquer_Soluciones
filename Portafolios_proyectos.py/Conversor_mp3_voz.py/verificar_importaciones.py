#!/usr/bin/env python
# Script de verificación de importación

import sys
import traceback

try:
    from newspaper import Article
    print("✓ newspaper3k importado correctamente")
except ImportError as e:
    print(f"✗ Error importando newspaper3k: {e}")
    traceback.print_exc()

try:
    from gtts import gTTS
    print("✓ gtts importado correctamente")
except ImportError as e:
    print(f"✗ Error importando gtts: {e}")
    traceback.print_exc()

try:
    import nltk
    print("✓ nltk importado correctamente")
except ImportError as e:
    print(f"✗ Error importando nltk: {e}")
    traceback.print_exc()

print("\nIntentando importar texto_a_voz...")
try:
    import texto_a_voz
    print("✓ texto_a_voz importado correctamente")
    print(f"Funciones disponibles: {[x for x in dir(texto_a_voz) if not x.startswith('_')]}")
except Exception as e:
    print(f"✗ Error importando texto_a_voz: {e}")
    traceback.print_exc()
