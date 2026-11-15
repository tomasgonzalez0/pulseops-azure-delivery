# Acciones pendientes en GitHub y Azure DevOps

1. Carolina (`caro-a21`) revisa [PR #1](https://github.com/tomasgonzalez0/pulseops-azure-delivery/pull/1). Tomás (`tomasgonzalez0`) hace merge tras comprobar diff, checks y aprobaciones aplicables.
2. Carla (`carlagiraldo09`) revisa [PR #2](https://github.com/tomasgonzalez0/pulseops-azure-delivery/pull/2). Tras #1, Tomás integra #2.
3. Daniel (`Dazzlm`) revisa [PR #3](https://github.com/tomasgonzalez0/pulseops-azure-delivery/pull/3). Tras #2, Tomás integra #3.
4. Samuel (`samuelcuello05`) revisa [PR #4](https://github.com/tomasgonzalez0/pulseops-azure-delivery/pull/4). Tras #3, cambiar base de `ci/samuel-pipeline` a `main` y verificar que el diff sólo contiene CD; Tomás integra #4 después de configurar la service connection.
5. Carolina revisa [PR #5](https://github.com/tomasgonzalez0/pulseops-azure-delivery/pull/5). Tomás puede integrarlo tras revisión.

La invitación del docente `oalarconpe` está pendiente de aceptación; debe aceptarla desde GitHub. Los revisores tienen permiso de escritura y las solicitudes figuran en los PRs. Los merges no se ejecutaron porque aún no hay aprobaciones ni checks de Azure DevOps.

Para continuar la automatización: identificar la organización y proyecto Azure DevOps, conectar el repositorio, crear service connection ARM limitada al App Service, sustituir el identificador del YAML, registrar la pipeline y verificar una ejecución activada por push a `main`. Después efectuar un cambio visible en un PR nuevo, integrarlo y seguir su SHA hasta la URL pública. La sesión Azure actual no enumeró organizaciones Azure DevOps.
