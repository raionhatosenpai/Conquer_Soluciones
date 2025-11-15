"""
Aplicación de registro de horas de trabajo con autenticación básica.

- Usuarios con contraseña (hash + salt).
- Sesión persistente entre ejecuciones (no pide usuario cada vez).
- Registro de jornadas (horas) y ausencias.
- Corrección, borrado y listado de registros.
- Cálculo de horas por semana ISO actual o mes actual.
- Exportación a CSV.
- Persistencia en JSON con escritura atómica.
"""

from __future__ import annotations

import json
import os
import sys
import secrets
from datetime import datetime, timedelta
from getpass import getpass
from hashlib import sha256
from typing import Dict, Optional, Union

# Archivos de persistencia
ARCHIVO_DATOS = "registro_trabajo.json"
ARCHIVO_SESION = ".session.json"

# ---------------------------------------------------------------------
# Utilidades de persistencia
# ---------------------------------------------------------------------


def _hash_password(password: str) -> str:
    """Hash simple (legacy). Se usa solo para migración de usuarios antiguos."""
    return sha256(password.encode("utf-8")).hexdigest()


def _hash_password_with_salt(password: str, salt: str) -> str:
    """Hash robusto con sal (recomendado)."""
    return sha256((salt + password).encode("utf-8")).hexdigest()


def cargar_datos() -> Dict[str, Dict[str, dict]]:
    """
    Carga la base de datos desde el JSON.
    Estructura esperada:
    {
        "usuarios": {
            "<nombre>": {
                "password": "<hash>",
                "salt": "<hex>|None",
                "registros": {
                    "YYYY-MM-DD": <float_horas> | "Ausente"
                }
            }
        }
    }
    """
    if not os.path.exists(ARCHIVO_DATOS):
        return {"usuarios": {}}

    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            datos = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print("No se pudieron cargar los datos existentes. Se crea base nueva.")
        print(f"Detalle: {e}")
        return {"usuarios": {}}

    if not isinstance(datos, dict):
        return {"usuarios": {}}

    usuarios = datos.get("usuarios", {})
    # Migración desde estructuras antiguas (sin credenciales)
    if isinstance(usuarios, dict):
        for nombre, payload in list(usuarios.items()):
            if not isinstance(payload, dict):
                usuarios[nombre] = {"password": None, "salt": None, "registros": {}}
            else:
                payload.setdefault("password", None)
                payload.setdefault("salt", None)
                payload.setdefault("registros", {})
        return {"usuarios": usuarios}

    # Estructura muy antigua: { "nombre": {....registros...} }
    usuarios_migrados: Dict[str, dict] = {}
    for nombre, registros in datos.items():
        if isinstance(registros, dict):
            usuarios_migrados[nombre] = {"password": None, "salt": None, "registros": registros}
    return {"usuarios": usuarios_migrados}


def _escritura_atomica(ruta: str, contenido: dict) -> None:
    """Guarda JSON de forma atómica (tmp + replace)."""
    tmp = ruta + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(contenido, f, indent=2, ensure_ascii=False)
    os.replace(tmp, ruta)


def guardar_datos() -> None:
    """Guarda la base de datos (atómico)."""
    try:
        _escritura_atomica(ARCHIVO_DATOS, base_datos)
    except OSError as e:
        print(f"No se pudieron guardar los datos: {e}")


def guardar_sesion(usuario: Optional[str]) -> None:
    try:
        _escritura_atomica(ARCHIVO_SESION, {"usuario": usuario})
    except OSError:
        pass


def cargar_sesion() -> Optional[str]:
    try:
        with open(ARCHIVO_SESION, "r", encoding="utf-8") as f:
            data = json.load(f)
        u = data.get("usuario")
        return u if isinstance(u, str) and u.strip() else None
    except (OSError, json.JSONDecodeError):
        return None


# ---------------------------------------------------------------------
# Autenticación
# ---------------------------------------------------------------------


def solicitar_password(confirmar: bool = True) -> Optional[str]:
    """Solicita una contraseña y opcionalmente la confirma."""
    try:
        password = getpass("Contraseña: ")
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada cancelada.")
        return None

    if not password:
        print("La contraseña no puede estar vacía.")
        return None

    if confirmar:
        try:
            confirmacion = getpass("Confirmar contraseña: ")
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada cancelada.")
            return None
        if password != confirmacion:
            print("Las contraseñas no coinciden.")
            return None

    return password


def crear_perfil(nombre: str, password: str) -> None:
    usuarios = base_datos.setdefault("usuarios", {})
    if nombre in usuarios and usuarios[nombre].get("password"):
        print("El perfil ya existe.")
        return

    salt = secrets.token_hex(16)
    usuarios[nombre] = {
        "password": _hash_password_with_salt(password, salt),
        "salt": salt,
        "registros": {},
    }
    guardar_datos()
    print(f"Perfil '{nombre}' creado con éxito.")


def iniciar_sesion() -> Optional[str]:
    usuarios = base_datos.get("usuarios", {})
    nombre = input("Nombre de usuario: ").strip()
    if not nombre:
        print("El nombre de usuario no puede estar vacío.")
        return None

    usuario = usuarios.get(nombre)
    if not usuario:
        print("Perfil no encontrado.")
        return None

    password_guardado = usuario.get("password")
    salt = usuario.get("salt")  # puede ser None en usuarios antiguos

    # Si el usuario no tiene contraseña (migración antigua)
    if not password_guardado:
        print("Este usuario no tiene contraseña. Define una nueva.")
        password = solicitar_password(confirmar=True)
        if not password:
            return None
        # Guardar ya con sal
        salt = secrets.token_hex(16)
        usuario["salt"] = salt
        usuario["password"] = _hash_password_with_salt(password, salt)
        guardar_datos()
        print("Contraseña creada. Vuelve a iniciar sesión.")
        return None

    try:
        password_ingresado = getpass("Contraseña: ")
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada cancelada.")
        return None

    ok = False
    if salt:  # formato nuevo
        ok = _hash_password_with_salt(password_ingresado, salt) == password_guardado
    else:
        # Compatibilidad con hash antiguo sin sal
        ok = _hash_password(password_ingresado) == password_guardado
        if ok:
            # Migrar a sal en cuanto pase
            salt = secrets.token_hex(16)
            usuario["salt"] = salt
            usuario["password"] = _hash_password_with_salt(password_ingresado, salt)
            guardar_datos()
            print("(Perfil migrado a almacenamiento seguro.)")

    if ok:
        print(f"Bienvenido de nuevo, {nombre}.")
        guardar_sesion(nombre)
        return nombre

    print("Contraseña incorrecta.")
    return None


def autenticar_usuario() -> Optional[str]:
    # Intenta sesión persistente
    ultimo = cargar_sesion()
    if ultimo and ultimo in base_datos.get("usuarios", {}):
        print(f"Sesión recordada: {ultimo}")
        # Si no quieres pedir password siempre, descomenta la línea siguiente
        # return ultimo

    while True:
        print("\n--- Autenticación ---")
        print("1. Iniciar sesión")
        print("2. Crear usuario")
        print("3. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            usuario = iniciar_sesion()
            if usuario:
                return usuario
        elif opcion == "2":
            nombre = input("Elige un nombre de usuario: ").strip()
            if not nombre:
                print("El nombre de usuario no puede estar vacío.")
                continue
            if nombre in base_datos.setdefault("usuarios", {}):
                print("El usuario ya existe.")
                continue
            password = solicitar_password(confirmar=True)
            if not password:
                continue
            crear_perfil(nombre, password)
        elif opcion == "3":
            return None
        else:
            print("Opción inválida.")


# ---------------------------------------------------------------------
# Utilidades de entrada/validación
# ---------------------------------------------------------------------


def solicitar_entero(mensaje: str, minimo: int = 1) -> Optional[int]:
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"Debes ingresar un número mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada cancelada.")
            return None


def solicitar_confirmacion(mensaje: str) -> Optional[bool]:
    while True:
        try:
            r = input(mensaje).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada cancelada.")
            return None
        if r in {"s", "si", "sí"}:
            return True
        if r in {"n", "no"}:
            return False
        print("Responde con 's' o 'n'.")


def solicitar_fecha(mensaje: str) -> Optional[str]:
    while True:
        try:
            fecha = input(mensaje).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada cancelada.")
            return None
        if not fecha:
            print("La fecha no puede estar vacía.")
            continue
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Formato de fecha incorrecto. Usa YYYY-MM-DD.")


def solicitar_hora(mensaje: str) -> Optional[str]:
    while True:
        try:
            hora = input(mensaje).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada cancelada.")
            return None
        if not hora:
            print("La hora no puede estar vacía.")
            continue
        try:
            datetime.strptime(hora, "%H:%M")
            return hora
        except ValueError:
            print("Formato de hora incorrecto. Usa HH:MM.")


# ---------------------------------------------------------------------
# Operaciones de negocio
# ---------------------------------------------------------------------


def obtener_registros(nombre: str) -> Optional[Dict[str, Union[float, str]]]:
    usuarios = base_datos.setdefault("usuarios", {})
    usuario = usuarios.get(nombre)
    if not usuario:
        print("Perfil no encontrado.")
        return None
    return usuario.setdefault("registros", {})


def registrar_dia(nombre: str, fecha: str, inicio: Optional[str], fin: Optional[str]) -> None:
    registros = obtener_registros(nombre)
    if registros is None:
        return

    if not inicio and not fin:
        registros[fecha] = "Ausente"
        guardar_datos()
        print(f"Se registró ausencia el {fecha}.")
        return

    try:
        hora_inicio = datetime.strptime(inicio, "%H:%M")
        hora_fin = datetime.strptime(fin, "%H:%M")
    except (TypeError, ValueError):
        print("Formato de hora incorrecto. Usa HH:MM")
        return

    if hora_fin <= hora_inicio:
        print("La hora de salida debe ser posterior a la de inicio.")
        return

    horas = (hora_fin - hora_inicio).seconds / 3600
    if horas > 16:
        print("No se permiten más de 16 horas en un día.")
        return

    registros[fecha] = round(horas, 2)
    guardar_datos()
    print(f"Se registraron {horas:.2f} horas el {fecha}.")


def calcular_horas(nombre: str, periodo: str = "semana") -> None:
    registros = obtener_registros(nombre)
    if not registros:
        print("No hay registros.")
        return

    hoy = datetime.today()
    if periodo == "semana":
        # Semana ISO actual (lunes-domingo) según 'hoy'
        delta = hoy.isoweekday() - 1  # 0 => lunes
        inicio = datetime(hoy.year, hoy.month, hoy.day) - timedelta(days=delta)
        fin = inicio + timedelta(days=6)
        etiqueta = f"semana ISO ({inicio.date()} a {fin.date()})"
    elif periodo == "mes":
        inicio = datetime(hoy.year, hoy.month, 1)
        if hoy.month == 12:
            fin = datetime(hoy.year + 1, 1, 1) - timedelta(days=1)
        else:
            fin = datetime(hoy.year, hoy.month + 1, 1) - timedelta(days=1)
        etiqueta = f"mes actual ({inicio.date()} a {fin.date()})"
    else:
        print("Periodo no válido ('semana' | 'mes').")
        return

    total = 0.0
    for fecha_str, val in registros.items():
        try:
            f = datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            continue
        if inicio.date() <= f.date() <= fin.date() and isinstance(val, (int, float)):
            total += float(val)

    print(f"Total de horas en {etiqueta}: {total:.2f} h")


def listar_registros(nombre: str) -> None:
    registros = obtener_registros(nombre)
    if not registros:
        print("Sin registros.")
        return
    print("\nFecha        Valor")
    for fch, v in sorted(registros.items()):
        print(f"{fch:10}   {v}")


def corregir_registro(nombre: str) -> None:
    registros = obtener_registros(nombre)
    if registros is None:
        return
    fecha = solicitar_fecha("Fecha a corregir (YYYY-MM-DD): ")
    if not fecha:
        return
    if fecha not in registros:
        print("No existe registro para esa fecha.")
        return

    presente = solicitar_confirmacion("¿Debe quedar como presente? (s/n): ")
    if presente is None:
        return
    if presente:
        inicio = solicitar_hora("Nueva hora de inicio (HH:MM): ")
        if not inicio:
            return
        fin = solicitar_hora("Nueva hora de salida (HH:MM): ")
        if not fin:
            return
        registrar_dia(nombre, fecha, inicio, fin)
    else:
        registrar_dia(nombre, fecha, None, None)


def borrar_registro(nombre: str) -> None:
    registros = obtener_registros(nombre)
    if registros is None:
        return
    fecha = solicitar_fecha("Fecha a borrar (YYYY-MM-DD): ")
    if not fecha:
        return
    if fecha in registros:
        del registros[fecha]
        guardar_datos()
        print(f"Registro del {fecha} eliminado.")
    else:
        print("No existe registro para esa fecha.")


def exportar_csv(nombre: str, archivo: str = "registros.csv") -> None:
    registros = obtener_registros(nombre)
    if not registros:
        print("No hay registros.")
        return
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write("fecha,valor\n")
            for fch, val in sorted(registros.items()):
                f.write(f"{fch},{val}\n")
        print(f"Exportado a {archivo}")
    except OSError as e:
        print(f"No se pudo exportar: {e}")


def registrar_jornadas(nombre: str) -> None:
    cantidad = solicitar_entero("¿Cuántos días deseas registrar?: ")
    if cantidad is None:
        return
    for _ in range(cantidad):
        fecha = solicitar_fecha("Fecha (YYYY-MM-DD): ")
        if not fecha:
            return
        presente = solicitar_confirmacion("¿Estuvo presente este día? (s/n): ")
        if presente is None:
            return
        if presente:
            inicio = solicitar_hora("Hora de inicio (HH:MM): ")
            if not inicio:
                return
            fin = solicitar_hora("Hora de salida (HH:MM): ")
            if not fin:
                return
            registrar_dia(nombre, fecha, inicio, fin)
        else:
            registrar_dia(nombre, fecha, None, None)


# ---------------------------------------------------------------------
# Menú principal
# ---------------------------------------------------------------------


def menu() -> None:
    usuario_actual = autenticar_usuario()
    if not usuario_actual:
        print("Hasta luego.")
        return

    while True:
        print("\n--- Registro de Horas de Trabajo ---")
        print(f"Usuario activo: {usuario_actual}")
        print("1. Registrar jornada/ausencia")
        print("2. Ver horas semanales")
        print("3. Ver horas mensuales")
        print("4. Listar registros")
        print("5. Corregir registro")
        print("6. Borrar registro")
        print("7. Exportar CSV")
        print("8. Cambiar de usuario")
        print("9. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            registrar_jornadas(usuario_actual)
        elif opcion == "2":
            calcular_horas(usuario_actual, periodo="semana")
        elif opcion == "3":
            calcular_horas(usuario_actual, periodo="mes")
        elif opcion == "4":
            listar_registros(usuario_actual)
        elif opcion == "5":
            corregir_registro(usuario_actual)
        elif opcion == "6":
            borrar_registro(usuario_actual)
        elif opcion == "7":
            exportar_csv(usuario_actual)
        elif opcion == "8":
            nuevo_usuario = autenticar_usuario()
            if nuevo_usuario:
                usuario_actual = nuevo_usuario
            else:
                print("No se ha cambiado de usuario.")
        elif opcion == "9":
            print("Sesión finalizada. ¡Hasta luego!")
            guardar_sesion(usuario_actual)
            break
        else:
            print("Opción inválida.")


# ---------------------------------------------------------------------
# Punto de entrada
# ---------------------------------------------------------------------

base_datos = cargar_datos()

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nEjecución interrumpida por el usuario.")
        sys.exit(0)
