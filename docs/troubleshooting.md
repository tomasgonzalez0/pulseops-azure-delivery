# Solución de problemas

- Si `npm ci` falla, comprobar Node 22 y `package-lock.json`.
- Si la pipeline no arranca, verificar conexión GitHub y trigger `main`.
- Si CD no tiene autorización, revisar service connection y permisos del App Service.
- Si Azure devuelve error, comprobar arranque `npm start`, logs y `/api/health`.
