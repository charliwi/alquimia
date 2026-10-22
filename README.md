# AlquimIA

Un kit para trabajar con varios agentes de IA sin perder el hilo. Tú decides; los agentes escuchan, ordenan y ejecutan. Todo lo que se decide queda escrito en tu GitHub, y los documentos pesados viven en tu Drive.

Este repo es una **plantilla**. Cópialo a tu cuenta y hazlo tuyo.

## Qué trae

| Archivo | Para qué |
|---|---|
| [REGLAS.md](REGLAS.md) | Las reglas comunes que siguen todos tus agentes |
| [PAPELES.md](PAPELES.md) | Los tres papeles (entrada, orquesta, ejecución) y cuándo dividir un agente |
| [CONEXIONES.md](CONEXIONES.md) | Cómo se conectan GitHub, Drive, Claude, Gemini y correo, y qué sí funciona |
| `espacios/_plantilla/` | La carpeta que copias para cada espacio de trabajo nuevo |
| `espacios/ejemplo/` | Un espacio inventado, para ver cómo se ve lleno |
| `scripts/visor.py` y [VISOR.md](VISOR.md) | Una tabla con el estado de todos tus espacios |
| `retro/` | Dónde escribes qué funcionó y qué no (ver [retro/README.md](retro/README.md)) |

## Arranque paso a paso

1. **Cuenta de Claude.** Entra a claude.ai con tu cuenta. Si vas a usar Claude Code en la nube, abre claude.ai/code.
2. **Tu repo.** En GitHub, en esta plantilla, pulsa **Use this template → Create a new repository**. Hazlo **privado**. Ponle el nombre que quieras (por ejemplo `mi-alquimia`).
3. **Conecta GitHub a Claude.** En claude.ai/code autoriza GitHub y elige tu repo nuevo.
4. **Tu primer espacio.** Copia `espacios/_plantilla/` a `espacios/<nombre>/` (por ejemplo `espacios/trabajo/`) y llena `CONTEXTO.md` en tres líneas: qué es, qué no es, quién decide.
5. **Tu primer agente.** Abre una sesión de Claude Code sobre tu repo y pégale:

   > Eres mi agente de orquesta. Lee REGLAS.md y PAPELES.md. Después lee espacios/*/ESTADO.md y sus bandejas. Dame un resumen corto: qué hay, qué espera de mí, y un solo siguiente paso.

6. **Cierra el día.** Al terminar, pide al agente que reescriba el `ESTADO.md` del espacio con la plantilla, haga commit y push, y corra `python3 scripts/visor.py`.
7. **Retro.** Cada 3 días las primeras 2 semanas, y luego cada semana, escribe un retro en `retro/`.

## Principios

- **Una sola casa** para las reglas: este repo.
- **Nada se manda solo.** Los agentes proponen; tú das el sí.
- **Sin secretos en el repo.** Ni contraseñas, ni datos bancarios, ni datos de clientes. Los números y archivos sensibles viven fuera (Drive, tu hoja de cálculo).
