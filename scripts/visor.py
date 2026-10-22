#!/usr/bin/env python3
"""Genera VISOR.md en la raíz del repo a partir de espacios/*/ESTADO.md.

Sólo librería estándar. Uso: python3 scripts/visor.py
Lee la plantilla de REGLAS.md (regla 5). Los ESTADO que no la usan
aparecen con su primera línea y la marca «formato viejo».
"""
import datetime
import pathlib
import re

RAIZ = pathlib.Path(__file__).resolve().parent.parent
DIAS_ROJO = 2
CAMPOS = ("Actualizado", "Lleva", "Hecho hoy", "Decidió", "Espera de", "Sigue",
          "Documentos")


def leer_campos(texto):
    campos = {}
    for linea in texto.splitlines():
        m = re.match(r"\s*\**(%s)[^:]*?\**\s*:\s*(.*)" % "|".join(CAMPOS), linea)
        if m and m.group(1) not in campos:
            campos[m.group(1)] = m.group(2).strip()
    return campos


def fecha(actualizado):
    m = re.search(r"(\d{4}-\d{2}-\d{2})", actualizado or "")
    return datetime.date.fromisoformat(m.group(1)) if m else None


def agente(actualizado):
    m = re.search(r"\bpor\s+(.+?)(?:[,.(]| al | con |$)", actualizado or "")
    return m.group(1).strip() if m else "–"


def celda(texto, largo=180):
    texto = (texto or "–").replace("|", "/").replace("`", "")
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto if len(texto) <= largo else texto[: largo - 1].rstrip() + "…"


def primera_linea(texto):
    for linea in texto.splitlines():
        linea = linea.strip()
        if linea and not linea.startswith(("#", "```", "Actualizado")):
            return linea.replace("**", "")
    return "(vacío)"


def main():
    hoy = datetime.datetime.now(datetime.timezone.utc).date()
    filas = []
    for ruta in sorted(RAIZ.glob("espacios/*/ESTADO.md")):
        if ruta.parent.name.startswith("_"):
            continue
        espacio = ruta.parent.name
        texto = ruta.read_text(encoding="utf-8")
        c = leer_campos(texto)
        f = fecha(c.get("Actualizado"))
        dias = (hoy - f).days if f else None
        rojo = dias is None or dias > DIAS_ROJO
        marca = "🔴 " if rojo else ""
        cuando = (f.isoformat() if f else "sin fecha") + (
            " (%d días)" % dias if dias is not None else "")
        enlace = "[%s](espacios/%s/ESTADO.md)" % (espacio, espacio)
        if all(k in c for k in ("Lleva", "Espera de", "Sigue")):
            filas.append((enlace, agente(c.get("Actualizado")), celda(c["Lleva"]),
                          celda(c["Espera de"]), celda(c["Sigue"]),
                          marca + cuando))
        else:
            filas.append((enlace, agente(c.get("Actualizado")),
                          "formato viejo: " + celda(primera_linea(texto), 80),
                          "–", "–", marca + cuando))

    salida = [
        "# Visor",
        "",
        "Generado por `scripts/visor.py` el %s (UTC) desde `espacios/*/ESTADO.md`. "
        "No se llena a mano: se corrige el ESTADO y se vuelve a generar." % hoy.isoformat(),
        "",
        "🔴 = más de %d días sin actualizar o sin fecha. «formato viejo» = el ESTADO "
        "no usa la plantilla de [REGLAS](REGLAS.md) (regla 5)." % DIAS_ROJO,
        "",
        "| Espacio | Agente | Qué lleva | Espera de ti | Qué sigue | Última actualización |",
        "|---|---|---|---|---|---|",
    ]
    salida += ["| " + " | ".join(f) + " |" for f in filas]
    (RAIZ / "VISOR.md").write_text("\n".join(salida) + "\n", encoding="utf-8")
    print("VISOR.md: %d espacios" % len(filas))


if __name__ == "__main__":
    main()
