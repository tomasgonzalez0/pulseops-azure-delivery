# Verificación QA

- `npm test`: compila TypeScript y comprueba HTTP 200 y campos de identidad del endpoint.
- Tras CD, consultar la URL pública y `/api/health`; comparar el SHA `build` con el commit del pipeline.
- Guardar captura y URL de la ejecución en `evidencias/`.
