# Git Guard: colaboración con IA y Git bajo revisión humana

[Sitio oficial](https://www.relayrun.net/) · [Inicio rápido](docs/es/README.md) · [Habilidades para IA](skills/README.md)

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

[Proponer funciones](https://github.com/relayrun/gitguard/discussions/categories/ideas) · [Preguntas y respuestas](https://github.com/relayrun/gitguard/discussions/categories/q-a) · [Informar de un problema](https://github.com/relayrun/gitguard/issues/new/choose) · [Contribuir (inglés)](docs/CONTRIBUTING.md)

## 1. Conoce Git Guard en 40 segundos

https://github.com/user-attachments/assets/24058217-bf03-4f7d-a4e4-333f86bd868c

[Descargar el vídeo en español · MP4 · 40 s](https://raw.githubusercontent.com/relayrun/gitguard/main/assets/videos/RelayRun-GitGuard-Intro-es-v12.mp4)

## 2. La IA prepara; las personas deciden

**Colabora con la IA de forma eficiente y mantén la seguridad del repositorio bajo control humano.**

**Git Guard es un proyecto de código abierto de [RelayRun](https://www.relayrun.net/) para colaborar con Git.** Ofrece manuales de configuración para personas, habilidades reutilizables para IA, plantillas y ejemplos de despliegue. Ayuda a desarrolladores individuales y equipos a limitar las operaciones de riesgo de la IA y reservar la revisión y la fusión finales a las personas.

> [!NOTE]
> **Una persona da la instrucción → la IA actúa dentro de lo autorizado → una persona revisa el resultado.**

Está dirigido a quienes usan repositorios Git e IA para modificar código o documentación. **OneDev y GitHub son ejemplos de configuración, no las únicas plataformas admitidas por el planteamiento.** Los mismos principios pueden adaptarse a otros gestores Git, comprobando sus capacidades y los resultados reales.

## 3. ¿Por qué Git Guard?

La IA puede cambiar código rápidamente, pero también sobrescribir el historial con un push forzado, borrar una rama o modificar la principal sin revisión. Si dispone de permisos de administración, podría cambiar las propias reglas de protección.

Decir «no hagas eso» en una instrucción no basta. Los controles se apoyan en **permisos del servidor, vías de acceso y copias independientes**. La IA realiza el trabajo autorizado; las personas conservan las decisiones importantes y los medios de recuperación.

## 4. ¿Cómo se protege el repositorio?

| Medida | Resultado buscado |
| --- | --- |
| Proteger la rama principal | La IA puede subir ramas de trabajo autorizadas, pero no hacer push directo a main, reescribir su historial mediante push forzado ni borrar ramas protegidas. |
| Crear, revisar y fusionar desde la web por una persona | La IA prepara rama, título y descripción. Una persona crea la solicitud en OneDev/GitHub, revisa los cambios y realiza la fusión. |
| Limitar vías para eludir la revisión | El ejemplo de OneDev autogestionado bloquea la API REST en el proxy inverso y cierra el acceso directo al servidor y otras rutas alternativas. |
| Separar contribución y administración | La identidad cotidiana de la IA no tiene permisos de fusión final, cambios en las protecciones ni gestión de copias; tampoco utiliza la sesión administrativa de una persona. |
| Conservar copias independientes | Copias en otro equipo o NAS, puntos históricos de recuperación protegidos y comprobaciones de integridad. Compilación y arranque son opcionales según el proyecto. |

> [!WARNING]
> **Límites esenciales:** restringir los push directos o forzados de la IA a main y las fusiones autónomas; cerrar REST y otras rutas que permitan eludir la revisión, dejando la revisión y fusión finales a las personas.

Son objetivos de configuración y aceptación, no pruebas de que los controles ya estén activos. Consulta las [versiones y limitaciones de OneDev](docs/es/onedev.md#sources-and-limits) y las reglas propias de la plataforma en la [guía de GitHub](docs/es/github.md).

## 5. La IA puede ayudar con la configuración

Puedes seguir el manual o entregar el manual y la habilidad correspondiente a un asistente. **Se recomienda Computer Use con la interfaz visible:** observa las acciones, concede los permisos necesarios y escribe personalmente las credenciales sensibles. Al terminar, cierra la sesión administrativa temporal y devuelve la IA a su identidad cotidiana restringida.

| Entorno | Punto de partida |
| --- | --- |
| OneDev autogestionado | [Manual](docs/es/onedev.md) · [Habilidad de configuración y aceptación (inglés)](skills/gitguard-onedev-safety/SKILL.md) |
| GitHub | [Guía de GitHub](docs/es/github.md) |
| Otros gestores Git | Adaptar el [flujo común](docs/es/workflow.md) y la [matriz de aceptación](docs/es/security-acceptance.md) a sus permisos e interfaces. |

La preparación inicial tiene cuatro partes: definir repositorio, rama principal e identidades separadas; configurar; comprobar operaciones permitidas y rechazadas en un repositorio de prueba aislado y autorizado; organizar las [copias y la recuperación](docs/es/backup-and-recovery.md). No hay que repetirla en cada cambio. Revisa lo afectado cuando cambien permisos, reglas o entorno.

### Revisar contenido sensible antes del commit

Pide a la IA que siga la [guía de revisión del contenido público](docs/es/public-content-review.md): definir alcance de publicación y modo del comprobador, y revisar por separado archivos de trabajo, bytes preparados e historial saliente. El auxiliar señala posibles claves, rutas de máquinas, direcciones privadas y problemas similares; resuelve y vuelve a revisar los hallazgos antes de un commit o push autorizado. No borra ni sustituye contenido ni detecta toda información privada; imágenes y vídeos requieren revisión humana. Guarda las listas de secretos/cuentas propias de la organización en configuración privada fuera de los repositorios. La [habilidad de colaboración (inglés)](skills/gitguard-workflow/SKILL.md) incluye los requisitos operativos.

## 6. Cuatro pasos cotidianos

Usa la [habilidad de colaboración (inglés)](skills/gitguard-workflow/SKILL.md) y el procedimiento Git del proyecto.

| Paso | Lo que dices o haces | Lo que hace la IA |
| --- | --- | --- |
| 1. Commit local | «Ejecuta el paso 1 según Git.md». | Lee el procedimiento, revisa los cambios y crea el commit local. Todavía no sube nada. |
| 2. Push y preparación | «Ejecuta el paso 2 según Git.md». | Sube la rama autorizada y prepara título, descripción y resultados de las comprobaciones. |
| 3. Revisión y fusión humanas | Crea la solicitud en la web; comprueba ramas de origen y destino, título, descripción, diferencias y controles; después confirma la fusión. | Explica y ayuda. Una persona realiza la fusión final. |
| 4. Limpieza posterior | «Ya he fusionado. Comprueba el resultado y realiza la limpieza». | Verifica el contenido realmente integrado, sincroniza main de forma segura y elimina solo las ramas confirmadas como terminadas. |

`Git.md` representa el documento real del proyecto; su nombre puede variar. Tú decides cuándo hacer commit, push y fusión. [Flujo completo](docs/es/workflow.md)

## 7. Recursos disponibles

- [Inicio rápido y siete manuales en español](docs/es/README.md) · [Cobertura de los ocho idiomas](docs/README.md).
- [Dos habilidades para IA](skills/README.md): colaboración diaria y configuración/aceptación de OneDev.
- [Plantillas](templates/README.md) para entregas, descripciones y registros de comprobación.
- [Ejemplos de despliegue](examples/onedev/README.md) y [herramientas de comprobación y empaquetado](scripts/README.md).
- [Integración de vídeos e idiomas](docs/es/animation-and-language.md).

Habilidades, plantillas, ejemplos de despliegue y herramientas de comprobación siguen siendo recursos compartidos en inglés.

## 8. Preguntas frecuentes y alcance

### ¿Debo configurar todo de nuevo con cada cambio?

No. Sigue los cuatro pasos diarios y revisa las opciones afectadas si cambian las identidades, los permisos o el entorno.

### ¿Puede utilizarlo una sola persona?

Sí, separando los roles humano/IA y la sesión temporal de configuración del uso diario. Si las reglas de la plataforma exigen otra persona revisora, ese requisito sigue vigente.

### ¿Instalar una habilidad protege automáticamente el repositorio?

No. Las habilidades orientan a la IA. Las restricciones efectivas requieren configurar el servidor y [verificar los permisos](docs/es/security-acceptance.md).

### ¿Qué idiomas están disponibles?

Hay presentación, inicio rápido, los siete manuales detallados y vídeo correspondiente en los ocho idiomas. Consulta la [cobertura](docs/README.md). Las traducciones son borradores para revisión; no se afirma una revisión editorial por hablantes nativos.

Adapta los documentos, habilidades y ejemplos a tu entorno. Una comprobación documental no es una aceptación de seguridad real; una versión local no equivale a una publicación. [Créditos de sonido](assets/videos/README.md) · [Revisión del contenido público](docs/es/public-content-review.md) · [Repositorio](https://github.com/relayrun/gitguard)

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
