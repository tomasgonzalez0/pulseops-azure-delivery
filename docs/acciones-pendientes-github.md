# Acciones pendientes en GitHub y Azure DevOps

Estado comprobado el 14 de noviembre de 2026: [PR #3 de CI](https://github.com/tomasgonzalez0/pulseops-azure-delivery/pull/3) aprobado e integrado en `main`. [PR #4 de CD](https://github.com/tomasgonzalez0/pulseops-azure-delivery/pull/4) aprobado, abierto y con base actualizada a `main`; aún contiene una referencia de service connection pendiente de configurar.

1. Carolina (`caro-a21`) revisa [PR #1](https://github.com/tomasgonzalez0/pulseops-azure-delivery/pull/1). Tomás (`tomasgonzalez0`) hace merge tras comprobar diff, checks y aprobaciones aplicables.
2. Carla (`carlagiraldo09`) revisa [PR #2](https://github.com/tomasgonzalez0/pulseops-azure-delivery/pull/2). Tras #1, Tomás integra #2.
3. Identificar organización y proyecto Azure DevOps, conectar GitHub, registrar la pipeline y verificar CI con frontend y pruebas en `main`.
4. Crear service connection ARM limitada al App Service, sustituir el identificador en el YAML del [PR #4](https://github.com/tomasgonzalez0/pulseops-azure-delivery/pull/4), comprobar la aprobación vigente y luego integrar CD.
5. Carolina revisa [PR #5](https://github.com/tomasgonzalez0/pulseops-azure-delivery/pull/5). Tomás puede integrarlo tras revisión.
6. Preparar un PR nuevo con cambio visible Version 2, integrarlo y seguir el mismo SHA por CI, artefacto, CD y URL pública.

La invitación del docente `oalarconpe` sigue pendiente de aceptación. Los merges #1, #2, #4 y #5 no se han ejecutado. La sesión Azure CLI de Carla está activa; el acceso web Azure DevOps requiere completar su inicio de sesión para determinar la organización.
