# Conexiones

Qué conecta con qué, y lo que sabemos que funciona y lo que no. Probado en octubre de 2026; las herramientas cambian rápido, así que comprueba antes de depender de algo.

| Herramienta | Para qué | Funciona | Ojo |
|---|---|---|---|
| **GitHub** | La memoria: reglas, estados, bandejas, decisiones | Claude Code lee y escribe en tu repo (commit y push) | Un chat de proyecto de Claude **lee** GitHub pero **no escribe**. Para escribir, usa Claude Code |
| **Claude Code (nube)** | Orquesta y ejecución | Sesiones en claude.ai/code sobre tu repo; pueden mandarse mensajes entre sesiones | Cada sesión vive en un contenedor temporal: lo que no se hace commit y push, se pierde |
| **Proyectos de Claude** | Conversaciones con contexto fijo | Bueno para pensar y explorar | Los archivos y conectores no pasan de un proyecto a otro por tener el mismo nombre |
| **Google Drive** | Documentos pesados: PDF, hojas, imágenes | Con el conector de Drive, Claude crea y lee archivos | Revisa con qué cuenta está conectado el conector. El repo sólo guarda el enlace |
| **Gemini** | Trabajar con correos y documentos de Google | Por probar con un encargo pequeño | No le pases datos de terceros sin decidirlo antes |
| **Correo** | Enviar cosas | El agente puede preparar un borrador | Nunca se envía sin tu sí. El agente verifica la dirección |
| **Voz** | Dictar en el camino | La app de voz guarda notas en la bandeja | La voz se prueba aparte: lo que funciona por escrito no siempre funciona en voz |

## Reglas de conexión

- **Sin secretos en el repo.** Las llaves y contraseñas se pasan por otro canal y no se escriben en ningún archivo.
- **Un archivo, un lugar.** El documento vive en Drive; el repo dice dónde está.
- **Verifica la subida.** Después de guardar algo en Drive o hacer push, el agente comprueba que llegó (tamaño, fecha o commit en el remoto) antes de decir «listo».
