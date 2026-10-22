# AlquimIA

Un kit para trabajar con varios agentes de IA sin perder el hilo. Tú decides; los agentes escuchan, ordenan y ejecutan. La voz va por ChatGPT; la orquesta y la ejecución, por Claude. Todo lo que se decide queda escrito en tu GitHub, y los documentos pesados viven en tu Drive.

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

**Antes de empezar:** si te invitaron a este repo, acepta la invitación desde el correo de GitHub o en github.com/notifications. Sin eso no puedes ver la plantilla.

1. **Tu repo.** En esta página pulsa **Use this template → Create a new repository**. Elige **tu** cuenta como dueña, hazlo **privado** y ponle el nombre que quieras (por ejemplo `mi-alquimia`). Tu copia sale limpia y es tuya: ahí trabajas todos los días.
2. **Claude.** Entra a claude.ai/code con **tu** cuenta de Claude. Autoriza GitHub e instala la app de Claude **sólo en tu repo nuevo**.
3. **ChatGPT para la voz.** En tu celular usa **tu** ChatGPT en modo voz como entrada: dicta ideas y encargos. Lo que dictes lo pasas a `bandeja/` de tu repo (lo pegas en tu sesión de Claude o lo sube Codex).
4. **Tu primer espacio.** En tu repo, copia `espacios/_plantilla/` a `espacios/<nombre>/` (por ejemplo `espacios/trabajo/`) y llena `CONTEXTO.md` en tres líneas: qué es, qué no es, quién decide. Borra `espacios/ejemplo/` cuando ya no lo necesites.
5. **Tu primer agente.** Abre una sesión de Claude Code sobre tu repo y pégale:

   > Eres mi agente de orquesta. Lee REGLAS.md y PAPELES.md. Después lee espacios/*/ESTADO.md y sus bandejas. Dame un resumen corto: qué hay, qué espera de mí, y un solo siguiente paso.

6. **Cierra el día.** Al terminar, pide al agente que reescriba el `ESTADO.md` del espacio con la plantilla, haga commit y push, y corra `python3 scripts/visor.py`.
7. **Retro.** Cada 3 días las primeras 2 semanas y luego cada semana. El retro va en la carpeta `retro/` **de esta plantilla original** (no de tu copia): así llega a quien mantiene el kit. Ver [retro/README.md](retro/README.md).

## Si te invitaron a este repo

- Aquí **sólo escribes en `retro/`**. El resto (reglas, papeles, scripts) no se toca: si quieres cambiar algo, propónlo en tu retro.
- Tu trabajo diario, tus espacios y tus agentes viven en **tu** copia, no aquí.
- Nada de lo que hagas en tu copia llega a este repo.

## Principios

- **Una sola casa** para las reglas: este repo.
- **Nada se manda solo.** Los agentes proponen; tú das el sí.
- **Sin secretos en el repo.** Ni contraseñas, ni datos bancarios, ni datos de clientes. Los números y archivos sensibles viven fuera (Drive, tu hoja de cálculo).
