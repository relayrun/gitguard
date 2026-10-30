# GitHub: correspondencia resumida de funciones

[English](../en/github.md) · [简体中文](../zh-CN/github.md) · [日本語](../ja/github.md) · [Deutsch](../de/github.md) · [Français](../fr/github.md) · [Español](github.md) · [Português (Brasil)](../pt-BR/github.md) · [Русский](../ru/github.md)

[Portada Git Guard](../../README.es.md) · [Inicio rápido](README.md)

Borrador base 0.1 — contrastado con la documentación enlazada de GitHub el 2026-10-28.

OneDev sigue siendo el ejemplo principal desarrollado de Git Guard. GitHub es el segundo: aplica el mismo [flujo diario](workflow.md), la misma [validación de seguridad](security-acceptance.md) y las mismas [indicaciones de respaldo](backup-and-recovery.md). Este capítulo relaciona capacidades, no describe la configuración actual de un repositorio concreto.

| Requisito común | Correspondencia en GitHub |
| --- | --- |
| Preparación y commit locales | Trabajo Git local habitual; no se sube nada en esta fase |
| Colaboración remota autorizada | Subir una rama de trabajo y preparar el texto; en el ejemplo habitual una persona crea la PR en la web |
| Revisión obligatoria y main protegida | Configurar protecciones/rulesets de rama y requisitos de revisión adecuados |
| Restringir push forzado y borrado de referencias protegidas | Mantener desactivadas las autorizaciones correspondientes e inspeccionar excepciones |
| Integración final humana | Separar identidad/credenciales IA de la autoridad humana; la revisión obligatoria por sí sola no reserva el permiso de integrar |
| Después de la integración humana | Verificar el resultado, sincronizar main local con seguridad y limpiar solo la rama confirmada como terminada |

GitHub documenta ramas protegidas y rulesets de ramas/etiquetas para repositorios públicos en sus planes Free; la disponibilidad en repositorios privados depende del plan. No deduzcas que toda función avanzada o de push rulesets está incluida por estar disponibles las funciones para repositorios públicos. [Ramas protegidas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) · [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).

Las revisiones aprobatorias obligatorias no determinan por sí solas quién puede integrar después. También importan las excepciones administrativas de protección clásica, actores permitidos, listas de bypass de rulesets, permisos de aplicaciones y credenciales humanas accesibles. Las restricciones de push documentadas para repositorios de organización compatibles son un control a evaluar junto con las PR obligatorias; prueba la identidad real antes de afirmar que solo una persona puede integrar. El propietario debe conservar por separado la administración del repositorio, su eliminación y los cambios de reglas.

En el ejemplo habitual, la persona sigue el flujo de creación de pull request: verifica base (destino) y compare (origen), introduce título/descripción, envía, revisa diferencias y comprobaciones y realiza personalmente la integración. Siguen vigentes las aprobaciones independientes exigidas; crear una PR no la aprueba. El [flujo común](workflow.md) explica la variante de creación por IA autorizada por separado.

GitHub también ofrece integración automática; este flujo deja la ejecución final a la persona. No la actives como comodidad incidental. No presupongas que un token permite escribir ramas de trabajo pero impide cualquier integración solo porque su etiqueta dice «restringido».

El ejemplo de proxy inverso de OneDev autoalojado no se convierte en un proxy delante del servicio GitHub. Adapta el objetivo de protección a las identidades, reglas, permisos de aplicaciones y rutas de acceso verificadas propias de GitHub.

Antes de adoptar esta correspondencia, inspecciona el plan real de la cuenta, visibilidad, reglas activas y excepciones; aplica después la matriz común en un entorno desechable autorizado. Redactar este capítulo no cambió configuraciones ni realizó pruebas negativas de seguridad.


<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
