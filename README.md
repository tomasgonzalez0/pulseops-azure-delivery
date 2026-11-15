# PulseOps

Aplicación de demostración del flujo GitHub → Azure DevOps CI → artefacto → Azure DevOps CD → Azure App Service.

## Equipo y responsabilidades asignadas

| Integrante | GitHub | Área |
|---|---|---|
| Carla (apellido por confirmar) | carlagiraldo09 | Frontend |
| Samuel (apellido por confirmar) | samuelcuello05 | CI |
| Carolina (apellido por confirmar) | caro-a21 | CD y Azure |
| Daniel (apellido por confirmar) | Dazzlm | QA |
| Tomás (apellido por confirmar) | tomasgonzalez0 | Arquitectura e integración |

Las contribuciones humanas y los nombres completos requieren verificación del equipo. Los cambios iniciales fueron preparados por Codex con la identidad Git configurada localmente.

## Ejecución local

Node.js 22: `npm ci`, `npm test`, `npm start`. Visite `http://localhost:3000` y `http://localhost:3000/api/health`.

## CI/CD

`azure-pipelines.yml` ejecuta build y pruebas, publica `webapp-drop` y pasa ese artefacto a la etapa de despliegue. La configuración de Azure DevOps y la URL pública se documentarán cuando estén verificadas.

## Evidencias y videos

Véase `evidencias/README.md` y `docs/guiones-videos.md`. Los enlaces de ejecuciones y videos están pendientes de generar; no se presentan como realizados.
