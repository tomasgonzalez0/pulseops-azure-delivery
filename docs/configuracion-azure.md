# Configuración Azure

Organización Azure DevOps: `https://dev.azure.com/carlagiraldo327724`; proyecto `PulseOps`; pipeline `PulseOps CI-CD` (ID 1). Conexión GitHub: `PulseOps GitHub`. Conexión Azure: `PulseOps Azure WIF`, con federación de identidad sin secreto y rol Contributor limitado al recurso App Service.

Suscripción Azure for Students (`c71ccd5a-b297-4b75-92bf-98efe2ae8129`). App Service de producción: `pulseops-delivery-itm-2026`, Linux Node 22, plan LinuxFree F1 `asp-pulseops-f1`, grupo `rg-pulseops-delivery`, región Brazil South. URL: https://pulseops-delivery-itm-2026.azurewebsites.net. No se compró capacidad adicional.

La etapa CD descarga `webapp-drop/pulseops.zip` de la misma ejecución sin recompilarlo. La conexión `PulseOps Azure WIF` tiene Contributor limitado al App Service de PulseOps. El primer despliegue automático exitoso fue el run #13 (versión 1, SHA `cb39e80043a4fc08b6aac298e8ee8bc6bb001473`). El run #15, disparado por el merge del PR #15 en `main`, completó CI y CD y publicó versión 2, SHA `530c3e7a0025fbeac3f9de70a2b2e5de79605916`.

El plan F1 anterior, compartido con `inventario-tienda-itm-tomas-2026`, entró en `QuotaExceeded` para ambas aplicaciones y devolvió HTTP 403. PulseOps se aisló en un plan F1 propio. Después de verificar la versión 2, se eliminó únicamente el App Service antiguo `pulseops-itm-2026` del plan compartido. La aplicación de inventario y su plan permanecen.
