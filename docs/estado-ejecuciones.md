# Estado verificado de Azure DevOps

Organización: [carlagiraldo327724](https://dev.azure.com/carlagiraldo327724). Proyecto: `PulseOps`. Pipeline: [PulseOps CI-CD](https://dev.azure.com/carlagiraldo327724/PulseOps/_build?definitionId=1), ID 1. El repositorio GitHub está conectado mediante `PulseOps GitHub`; los runs #13 y #15 tienen causa `individualCI` tras merges en `main`.

| Run | SHA de `main` | Resultado | Evidencia |
|---|---|---|---|
| [#11](https://dev.azure.com/carlagiraldo327724/PulseOps/_build/results?buildId=11&view=results) | `515d2995cc587bb9096fe7408ac8db546691f915` | CI exitosa; CD falló | `webapp-drop` publicado y descargado. App Service del plan F1 compartido devolvió `Site Disabled (403)` por `QuotaExceeded`. |
| [#13](https://dev.azure.com/carlagiraldo327724/PulseOps/_build/results?buildId=13&view=results) | `cb39e80043a4fc08b6aac298e8ee8bc6bb001473` | CI y CD exitosas | Artefacto `webapp-drop`; despliegue en el plan F1 aislado; `/api/health` respondió HTTP 200, versión 1 y el mismo SHA. |
| [#15](https://dev.azure.com/carlagiraldo327724/PulseOps/_build/results?buildId=15&view=results) | `530c3e7a0025fbeac3f9de70a2b2e5de79605916` | CI y CD exitosas | Cambio visible a «PulseOps — Version 2»; build, prueba, artefacto, descarga, despliegue y health check exitosos. |

La verificación HTTP externa del run #15 devolvió `200` en [la API de salud](https://pulseops-delivery-itm-2026.azurewebsites.net/api/health) con `{"status":"ok","app":"PulseOps","version":"2","build":"530c3e7a0025fbeac3f9de70a2b2e5de79605916"}`. La página pública mostró «PulseOps — Version 2».

Los runs iniciales #2–#8 no encontraron agente hospedado. La organización activó un trabajo Microsoft-hosted gratuito de 1.800 minutos mensuales, con 0 trabajos de pago, y el YAML fijó `ubuntu-22.04`. El run #13 usó ese agente y completó ambas etapas. El run #15 repitió la ruta completa automáticamente.
