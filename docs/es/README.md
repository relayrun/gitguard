# Git Guard — Inicio rápido

[English](../en/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Español](README.md) · [Português (Brasil)](../pt-BR/README.md) · [Русский](../ru/README.md)

[Portada Git Guard](../../README.es.md)

Hay presentación, inicio rápido, los siete manuales detallados y vídeo en español. OneDev y GitHub son ejemplos; los principios pueden adaptarse a otros gestores Git. Esta traducción es un borrador para revisión, no una validación de seguridad real.

Antes de un commit o envío autorizado, sigue la guía para [configurar y ejecutar la comprobación](public-content-review.md#configure-the-public-content-check) e [interpretar y tratar los hallazgos](public-content-review.md#interpret-results-and-handle-findings).

## La IA puede ayudar con la configuración

Puedes seguir el manual o entregar el manual y la habilidad correspondiente a un asistente. **Se recomienda Computer Use con la interfaz visible:** observa las acciones, concede los permisos necesarios y escribe personalmente las credenciales sensibles. Al terminar, cierra la sesión administrativa temporal y devuelve la IA a su identidad cotidiana restringida.

| Entorno | Punto de partida |
| --- | --- |
| OneDev autogestionado | [Manual](onedev.md) · [Habilidad de configuración y aceptación (inglés)](../../skills/gitguard-onedev-safety/SKILL.md) |
| GitHub | [Guía de GitHub](github.md) |
| Otros gestores Git | Adaptar el [flujo común](workflow.md) y la [matriz de aceptación](security-acceptance.md) a sus permisos e interfaces. |

La preparación inicial tiene cuatro partes: definir repositorio, rama principal e identidades separadas; configurar; comprobar operaciones permitidas y rechazadas en un repositorio de prueba aislado y autorizado; organizar las [copias y la recuperación](backup-and-recovery.md). No hay que repetirla en cada cambio. Revisa lo afectado cuando cambien permisos, reglas o entorno.

## Cuatro pasos cotidianos

Usa la [habilidad de colaboración (inglés)](../../skills/gitguard-workflow/SKILL.md) y el procedimiento Git del proyecto.

| Paso | Lo que dices o haces | Lo que hace la IA |
| --- | --- | --- |
| 1. Commit local | «Ejecuta el paso 1 según Git.md». | Lee el procedimiento, revisa los cambios y crea el commit local. Todavía no sube nada. |
| 2. Push y preparación | «Ejecuta el paso 2 según Git.md». | Sube la rama autorizada y prepara título, descripción y resultados de las comprobaciones. |
| 3. Revisión y fusión humanas | Crea la solicitud en la web; comprueba ramas de origen y destino, título, descripción, diferencias y controles; después confirma la fusión. | Explica y ayuda. Una persona realiza la fusión final. |
| 4. Limpieza posterior | «Ya he fusionado. Comprueba el resultado y realiza la limpieza». | Verifica el contenido realmente integrado, sincroniza main de forma segura y elimina solo las ramas confirmadas como terminadas. |

`Git.md` representa el documento real del proyecto; su nombre puede variar. Tú decides cuándo hacer commit, push y fusión. [Flujo completo](workflow.md)

## Seguridad y recuperación

La presencia de una configuración no demuestra que la protección funcione. Realice pruebas de rechazo solo en un repositorio desechable y con autorización específica; marque lo no probado como no verificado. Mantenga sincronización independiente e historial protegido. La compilación limpia y el inicio del programa son verificaciones opcionales según el proyecto.

En el ejemplo OneDev, el correo verificado puede afectar la sugerencia de la rama de origen; no provoca una integración automática. Los prefijos WIP del título pueden impedir la integración en la versión de referencia, pero no se prohíben todos los títulos que empiezan por letras.

## Guías detalladas

- [Flujo diario](workflow.md)
- [Configuración OneDev](onedev.md)
- [Correspondencia GitHub](github.md)
- [Validación de seguridad](security-acceptance.md)
- [Copias y recuperación](backup-and-recovery.md)
- [Revisión del contenido público](public-content-review.md)
- [Animación e idiomas](animation-and-language.md)
- [Skills](../../skills/README.md) · [Templates](../../templates/README.md)

Habilidades, plantillas, ejemplos de despliegue y herramientas de comprobación siguen siendo recursos compartidos en inglés.

La IA prepara los cambios; una persona revisa y realiza la integración final.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
