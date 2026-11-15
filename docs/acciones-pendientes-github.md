# Acciones pendientes

1. Confirmar que el pool Azure Pipelines asigna agentes. La organización tiene 1 trabajo hospedado gratuito y 0 compras, pero los runs 2, 3, 5 y 6 fallaron con `No agent found in pool Azure Pipelines`.
2. Reejecutar la rama de diagnóstico `verify/pipeline-preflight` para probar CI, `webapp-drop` y CD. Esta ejecución manual es de diagnóstico.
3. Confirmar despliegue Version 1 en https://pulseops-itm-2026.azurewebsites.net y `/api/health` con el SHA de la ejecución.
4. Crear PR de Version 2, obtener revisión, integrar en `main` y comprobar trigger automático, artefacto, CD, URL y SHA.
5. Aceptar la invitación pendiente del docente `oalarconpe`; grabar los dos videos narrados con los cinco integrantes; incorporar capturas reales y entregar enlaces y PDF en Teams.

PRs #1, #2, #3, #4, #5 y #11 están integrados. Los cambios de código y documentación están en `main`.
