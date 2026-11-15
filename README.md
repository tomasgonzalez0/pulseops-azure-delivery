# PulseOps

Aplicación de demostración para GitHub → Azure DevOps CI → artefacto → Azure DevOps CD → Azure App Service.

## Equipo

| Integrante | GitHub | Responsabilidad |
|---|---|---|
| Carla Juliana Giraldo Camacho | carlagiraldo09 | Frontend y aplicación |
| Samuel (apellido pendiente) | samuelcuello05 | CI |
| Carolina Arango Escobar | caro-a21 | CD y Azure |
| Daniel Felipe Marin Marin | Dazzlm | QA |
| Tomas Gonzalez Zapata | tomasgonzalez0 | Arquitectura e integración |

El equipo confirmó trabajo conjunto en un mismo PC. Los commits funcionales registran autor y committer con el nombre y correo del responsable indicado. GitHub registra por separado la cuenta que publica y fusiona cada PR. Falta confirmar el nombre completo de Samuel para la entrega.

## Aplicación local

Node.js 22, TypeScript, Express, HTML y CSS. Ejecutar `npm ci`, `npm test` y `npm start`. Abrir http://localhost:3000 y http://localhost:3000/api/health.

## Arquitectura y despliegue

`main` activa [PulseOps CI-CD](https://dev.azure.com/carlagiraldo327724/PulseOps/_build?definitionId=1). CI usa un agente hospedado `ubuntu-22.04`, instala dependencias desde el lockfile, compila, prueba y publica `webapp-drop`. CD descarga exactamente ese artefacto y lo despliega con identidad federada en [pulseops-delivery-itm-2026](https://pulseops-delivery-itm-2026.azurewebsites.net), un App Service Linux Node 22 en un plan F1 gratuito separado. La [ejecución automática #15](https://dev.azure.com/carlagiraldo327724/PulseOps/_build/results?buildId=15&view=results) completó CI y CD; la [API de salud](https://pulseops-delivery-itm-2026.azurewebsites.net/api/health) devolvió versión 2 y el SHA `530c3e7a0025fbeac3f9de70a2b2e5de79605916`. Véase [estado de ejecuciones](docs/estado-ejecuciones.md).

## Evidencias

[Acciones pendientes](docs/acciones-pendientes-github.md), [arquitectura](docs/arquitectura.md), [Azure](docs/configuracion-azure.md), [QA](docs/qa.md), [solución de problemas](docs/troubleshooting.md), [guiones de videos](docs/guiones-videos.md), [evidencias](evidencias/README.md) y [memoria técnica PDF](output/pdf/memoria-tecnica-pulseops.pdf). Los dos videos narrados y la entrega en Teams siguen pendientes; no se presentan como realizados.


