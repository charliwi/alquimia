# Papeles

Tres papeles. Pueden ser tres agentes o uno solo al principio. Lo que importa es que cada cosa tenga dueño.

| Papel | Qué hace | Qué no hace | Dónde suele vivir |
|---|---|---|---|
| **Entrada** | Escucha (voz o chat), guarda lo que dices en `bandeja/`, te cuenta cómo van los espacios | No decide ni produce; canaliza | Una app de voz o chat en el celular |
| **Orquesta** | Revisa lo que llega contra las reglas, señala tensiones, ordena pendientes y manda encargos a cada espacio | No ejecuta el trabajo del espacio | Claude Code sobre tu repo |
| **Ejecución** | Produce el entregable (documento, hoja, página, código), lo guarda donde va y deja acuse | No inventa encargos ni envía nada sin tu sí | Claude Code, una sesión por encargo |

## El ciclo

1. Dices algo a **Entrada**. Queda una nota en `bandeja/` con fecha.
2. **Orquesta** la lee, la contrasta con las reglas y te propone un encargo cerrado.
3. Das el sí. Orquesta deja el encargo en la bandeja del espacio.
4. **Ejecución** lo produce, te lo muestra y deja su acuse en la sección «Recepción» del encargo.
5. Al cerrar, cada uno actualiza su `ESTADO.md`. El visor junta todo.

## Pareja por espacio

Un espacio que crece puede tener su propia pareja: uno que **nutre** (investiga, junta contexto, propone) y uno que **ejecuta**. La pareja lee las reglas comunes y su propio `CONTEXTO.md`.

## Cuándo dividir un agente

Divide cuando pasa alguna de estas cosas:

- El agente mezcla contextos de dos espacios y se equivoca de uno a otro.
- Un espacio tiene trabajo diario propio y llena la bandeja común.
- Hay información que un espacio no debe ver (de un cliente, por ejemplo).

No dividas por adelantado: cada agente nuevo es otro ESTADO que mantener.

## Nombres

Ponle nombre a cada agente. Ayuda a saber quién dijo qué en el historial. Si cambias un nombre, anótalo en REGLAS.md para que los demás lo reconozcan.
