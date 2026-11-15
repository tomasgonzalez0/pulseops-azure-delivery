# Solución de problemas

- Si `npm ci` falla, comprobar Node 22 y `package-lock.json`.
- Si la pipeline no arranca, verificar conexión GitHub y trigger `main`.
- Si CD no tiene autorización, revisar service connection y permisos del App Service.
- Si Azure devuelve error, comprobar arranque `npm start`, logs y `/api/health`.
- `No agent found in pool Azure Pipelines` se resolvió con el trabajo hospedado gratuito de la organización y la imagen `ubuntu-22.04`; el run #13 y el #15 terminaron con agente hospedado. No se instaló agente en el PC.
- `Site Disabled (403)` con `QuotaExceeded` afectó al plan F1 compartido. PulseOps se movió a un plan F1 separado, sin subir a un nivel de pago. Comprobar `az webapp show --name pulseops-delivery-itm-2026 --resource-group rg-pulseops-delivery --query "{state:state,usageState:usageState}"`.
- El nivel F1 puede suspender la aplicación al agotar CPU o ancho de banda. Consultar cuotas en Azure y esperar el restablecimiento gratuito; no aumentar el SKU sin autorización de costos.
