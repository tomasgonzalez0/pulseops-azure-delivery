# Estado de ejecuciones Azure DevOps

Organización: https://dev.azure.com/carlagiraldo327724. Proyecto: PulseOps. Pipeline: `PulseOps CI-CD` (ID 1). Repositorio GitHub conectado mediante `PulseOps GitHub`; trigger `main` comprobado por ejecuciones `individualCI`.

| Run | Rama | SHA | Causa | Resultado |
|---|---|---|---|---|
| 1 | main | `aaa1cc12d404a1238b29f0d698efa9e7ad8199ec` | manual | Falló validación: conexión Azure provisional no existía. |
| 2 | main | `fb7c8bd10d6ec2fda70113024bd32fa341157c9f` | individualCI | Falló antes de ejecutar: no se encontró agente hospedado. |
| 3 | verify/pipeline-preflight | `73d4ae3bb6b5fc36b82ae81d2858edf871b09f92` | manual | Falló antes de ejecutar: no se encontró agente hospedado. |
| 5 | main | `ae239c25caff13581a9662aed4e40bf114977d51` | individualCI | Falló antes de ejecutar: no se encontró agente hospedado. |
| 6 | verify/pipeline-preflight | `73d4ae3bb6b5fc36b82ae81d2858edf871b09f92` | manual | Falló antes de ejecutar: no se encontró agente hospedado. |

La organización muestra 1 trabajo Microsoft-hosted gratuito de hasta 1.800 minutos/mes, 0 consumidos y 0 comprados. La asignación de agentes sigue pendiente; no hay build, prueba, artefacto ni CD remotos exitosos. La conexión `PulseOps Azure WIF` usa federación sin secreto y rol Contributor limitado al App Service `pulseops-itm-2026`.

Enlaces de runs: https://dev.azure.com/carlagiraldo327724/PulseOps/_build?definitionId=1. Para cada run, abrir el ID indicado y consultar el timeline. Una ejecución local `npm test` pasó 1/1 prueba; no sustituye las ejecuciones remotas.
