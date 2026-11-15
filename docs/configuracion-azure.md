# Configuración Azure

Suscripción Azure for Students (`c71ccd5a-b297-4b75-92bf-98efe2ae8129`). App Service: `pulseops-itm-2026`, Linux Node 22, plan F1 existente `asp-inventario-tienda-p3`, grupo `rg-inventario-tienda-p3`. URL: https://pulseops-itm-2026.azurewebsites.net. El recurso está creado, pero aún no hay despliegue CD verificado.

CD descarga `webapp-drop/pulseops.zip` de la misma ejecución sin recompilarlo. Falta una service connection ARM con permiso sobre el recurso y sustituir `PULSEOPS_AZURE_SERVICE_CONNECTION` en el YAML. La identidad Azure actual no mostró organización Azure DevOps.
