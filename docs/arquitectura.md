# Arquitectura

GitHub `main` dispara Azure Pipelines. CI instala dependencias desde lockfile, compila, prueba, empaqueta y publica `webapp-drop`. CD descarga el mismo ZIP, lo despliega mediante service connection y consulta `/api/health`. El SHA permite comparar GitHub, ejecución y despliegue.
