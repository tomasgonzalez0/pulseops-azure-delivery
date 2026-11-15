# Configuración Azure

Organización Azure DevOps: `https://dev.azure.com/carlagiraldo327724`; proyecto `PulseOps`; pipeline `PulseOps CI-CD` (ID 1). Conexión GitHub: `PulseOps GitHub`. Conexión Azure: `PulseOps Azure WIF`, con federación de identidad sin secreto y rol Contributor limitado al recurso App Service.

Suscripción Azure for Students (`c71ccd5a-b297-4b75-92bf-98efe2ae8129`). App Service: `pulseops-itm-2026`, Linux Node 22, plan F1 existente `asp-inventario-tienda-p3`, grupo `rg-inventario-tienda-p3`. URL: https://pulseops-itm-2026.azurewebsites.net.

La etapa CD descarga `webapp-drop/pulseops.zip` de la misma ejecución sin recompilarlo. La publicación automatizada y la URL funcional requieren una ejecución exitosa después de integrar el PR CD.
