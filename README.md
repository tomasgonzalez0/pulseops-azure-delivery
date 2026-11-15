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

El equipo confirmó trabajo conjunto en un mismo PC. Los commits de cada rama llevan el nombre y correo del responsable indicado. Falta registrar revisiones humanas en los PRs y confirmar los nombres completos para la entrega.

## Aplicación local

Node.js 22, TypeScript, Express, HTML y CSS. Ejecutar `npm ci`, `npm test` y `npm start`. Abrir http://localhost:3000 y http://localhost:3000/api/health.

## Arquitectura y despliegue

`main` activa `azure-pipelines.yml`. CI instala dependencias desde lockfile, compila, prueba y publica `webapp-drop`. CD descarga exactamente ese artefacto y lo despliega en Azure App Service. Pipeline registrada en Azure DevOps; conexión federada configurada. El agente hospedado aún no está disponible. App Service creado: [pulseops-itm-2026](https://pulseops-itm-2026.azurewebsites.net) en plan F1; aún no contiene PulseOps verificado. Véase docs/estado-ejecuciones.md para runs y fallos.

## Evidencias

[Acciones pendientes](docs/acciones-pendientes-github.md), [arquitectura](docs/arquitectura.md), [Azure](docs/configuracion-azure.md), [QA](docs/qa.md), [solución de problemas](docs/troubleshooting.md), [guiones de videos](docs/guiones-videos.md) y [evidencias](evidencias/README.md). Ejecuciones fallidas: véase docs/estado-ejecuciones.md. Videos: pendientes. No se presentan como realizados.


