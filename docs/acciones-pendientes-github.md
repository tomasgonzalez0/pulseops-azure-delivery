# Acciones pendientes de entrega

Los PR #1–#5 y #11–#15 están integrados. El PR [#15](https://github.com/tomasgonzalez0/pulseops-azure-delivery/pull/15) llevó la versión 2 a `main`; el [run automático #15](https://dev.azure.com/carlagiraldo327724/PulseOps/_build/results?buildId=15&view=results) completó CI y CD. No hay un merge técnico pendiente para la demostración.

| Orden | Acción | Responsable | Enlace | Estado |
|---|---|---|---|---|
| 1 | Aceptar la invitación de lectura al repositorio | Docente `oalarconpe` | [Invitaciones GitHub](https://github.com/tomasgonzalez0/pulseops-azure-delivery/invitations) | Invitación pendiente al consultar la API el 15-11-2026. |
| 2 | Grabar y subir video narrado de CI con los cinco integrantes | Equipo | [Guion CI](guiones-videos.md) | Pendiente. |
| 3 | Grabar y subir video narrado de CD con los cinco integrantes | Equipo | [Guion CD](guiones-videos.md) | Pendiente. |
| 4 | Incorporar capturas reales y enlaces de ambos videos a la memoria PDF | Equipo | [Memoria técnica](../output/pdf/memoria-tecnica-pulseops.pdf) | Pendiente de material audiovisual. |
| 5 | Entregar repositorio, videos y memoria PDF en Microsoft Teams | Equipo | — | Pendiente; no se conoce el enlace de la actividad de Teams. |

Si se agrega un nuevo cambio a `main`, el trigger de `azure-pipelines.yml` inicia CI; CD corre después de CI exitosa y descarga `webapp-drop` de esa misma ejecución. Comprobar el ID de run, el SHA y la respuesta de `/api/health` antes de declarar un nuevo despliegue verificado.
