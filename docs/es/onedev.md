# Configurar OneDev: permisos de IA y revisión humana

[English](../en/onedev.md) · [简体中文](../zh-CN/onedev.md) · [日本語](../ja/onedev.md) · [Deutsch](../de/onedev.md) · [Français](../fr/onedev.md) · [Español](onedev.md) · [Português (Brasil)](../pt-BR/onedev.md) · [Русский](../ru/onedev.md)

[Portada Git Guard](../../README.es.md) · [Inicio rápido](README.md)

Esta guía de **RelayRun Git Guard** explica cómo separar permisos humanos y de IA, proteger main, restringir vías que eluden la revisión y mantener copias recuperables independientes en OneDev autoalojado. La IA crea commits y sube ramas de trabajo dentro de la autorización; una persona crea la solicitud, la revisa y realiza la integración final en la web.

**Git Guard se dirige a personas y equipos que usan repositorios Git, no solo a usuarios de OneDev.** OneDev y GitHub son ejemplos de configuración. Otras plataformas de gestión Git pueden seguir los [principios compartidos de colaboración y protección](workflow.md), verificando ajustes y resultados según sus capacidades. Este capítulo muestra OneDev; la [guía GitHub](github.md) ofrece otro ejemplo. OneDev es una plataforma de terceros, no un producto RelayRun.

Borrador de revisión 0.1. Referencia de interfaz y diagnóstico: **OneDev 14.1.0**. Es un ejemplo versionado, no una recomendación de desplegar una versión antigua sin comprobar su soporte actual. [Flujo](workflow.md) · [Validación de seguridad](security-acceptance.md) · [Alternativa GitHub](github.md)

**En esta página:** [Configuración con IA](#visible-ai-assisted-setup) · [Despliegue](#1-select-a-deployment-boundary) · [Identidades](#2-establish-separate-identities) · [Protección de ramas](#3-initialize-and-protect-the-target-branch) · [Integración humana](#4-set-pr-defaults-without-confusing-responsibilities) · [Acceso REST](#5-optional-rest-ingress-restriction) · [Errores frecuentes](#6-two-common-pitfalls) · [Validación y recuperación](#7-acceptance-and-recovery) · [Fuentes](#sources-and-limits)

Antes de un commit o envío autorizado, sigue la guía para [configurar y ejecutar la comprobación](public-content-review.md#configure-the-public-content-check) e [interpretar y tratar los hallazgos](public-content-review.md#interpret-results-and-handle-findings).

<a id="visible-ai-assisted-setup"></a>

## Configuración visible asistida por IA

Puedes configurar manualmente o pedir a la IA que siga esta guía y la habilidad de configuración mediante una interfaz Computer Use visible. Primero identifica proyecto exacto, actor, ajustes que cambiar y reversión. La persona aprueba ese alcance y puede observar; no se presupone una concesión administrativa oculta o permanente.

Para controles administrativos, utiliza una sesión temporal supervisada destinada a esos cambios. La persona introduce credenciales sensibles sin dejarlas en el chat, capturas o archivos del repositorio. No reutilices una sesión de administrador para eludir una acción diaria denegada. Al terminar, comprueba los ajustes, realiza la validación acotada adecuada, cierra la sesión elevada y vuelve a la identidad diaria restringida. Si la interfaz disponible no permite un paso, indícalo y déjalo a la persona; no afirmes haber hecho un clic que no ocurrió.

Observar la pantalla ayuda a explicar la configuración; los permisos impuestos y sus pruebas aportan la protección.

<a id="1-select-a-deployment-boundary"></a>

## 1. Elegir un límite de despliegue

Prefiere un ordenador, servidor o NAS independiente cuya arquitectura y soporte de contenedores coincidan con la versión OneDev elegida. Mantén servidor, motor de contenedores, almacenamiento, copias y credenciales administrativas fuera del alcance de la identidad IA de desarrollo. Compartir host exige permisos explícitos del sistema y archivos; Docker por sí solo no proporciona la separación.

Usa la guía oficial y el [ejemplo parametrizado](../../examples/onedev/README.md). Antes de arrancar, elige versiones/digests de imágenes compatibles, ubicación de datos independiente, entrada TLS y recuperación. El ejemplo expone únicamente una puerta de enlace loopback, omite el socket Docker y desactiva asignaciones HTTP/SSH directas al host. Es una configuración inicial, no una instalación de producción probada. Las compilaciones en contenedores pueden necesitar un ejecutor diseñado por separado.

<a id="2-establish-separate-identities"></a>

## 2. Establecer identidades distintas

| Dónde inspeccionar | Qué hacer | Verificar |
| --- | --- | --- |
| Administration → Users / Groups | Separar revisor/administrador humano, colaborador IA e identidad de respaldo de solo lectura | Membresías y credenciales reales, incluido acceso heredado |
| Administration → Roles | Revisar permisos de código, gestión de proyecto y otros del rol elegido | El nombre no basta; la IA no debe poseer/administrar proyectos ni cambiar protecciones |
| Project → Settings → Authorizations → Users / Groups | Conceder solo el ámbito necesario; revisar padres | La identidad de respaldo lee solo el repositorio previsto; los derechos IA coinciden con el modelo declarado |
| Project → Settings → General | Revisar proyecto padre y rol predeterminado efectivo | Sin acceso anónimo/predeterminado ni propiedad heredada involuntarios |

La opción «Manage Pull Requests» desactivada del rol Code Writer de referencia se refiere a gestión/operaciones masivas; no prueba que ese rol nunca pueda realizar la integración final. Prueba esa autoridad por separado después de una aprobación humana válida. No expongas una sesión web humana ni token administrativo a la identidad IA diaria. La sesión supervisada descrita es temporal y no debe conservarse para el trabajo Git habitual.

<a id="3-initialize-and-protect-the-target-branch"></a>

## 3. Inicializar y proteger la rama destino

Inicializa la rama protegida prevista bajo el flujo de configuración controlado por una persona antes de activar una regla que impida crearla. No desactives rutinariamente la protección para que la IA la inicie o repare.

Abre **Project → Settings → Code → Branch Protection**. En la interfaz de referencia, selecciona la rama protegida, normalmente `main`, y los sujetos previstos; la referencia usa `anyone`. Lee el orden: en esta versión las reglas locales preceden a las del padre y se usa la primera coincidencia. Una regla hija puede ocultar otra superior más estricta; inspecciona el comportamiento efectivo.

| Opción | Criterio necesario |
| --- | --- |
| Prevent forced push | Activar para la rama protegida; verificar en un repositorio desechable el rechazo de una reescritura realmente no autorizada |
| Prevent deletion | Proteger la rama; borrar el repositorio es un permiso distinto |
| Prevent creation | Decidir tras inicializar; no sustituye la protección de actualizaciones/revisión |
| Required reviewers | Seleccionar revisor humano independiente mediante el selector y verificar expresión y cuenta resultantes |
| Required builds / signatures | Elegir según el proyecto, con comprobaciones que realmente se ejecuten y claves de firma fiables |
| File/tag protection | Definir solo el alcance necesario; las reglas de rama no demuestran protección de etiquetas o versiones |

La referencia anterior inicialmente no exigía revisor; después se añadieron requisitos. Bloquear force-push **no bloquea** un push directo normal por fast-forward. Compruébalo explícitamente. El revisor nombrado que también presenta la PR puede recibir un trato distinto en la implementación de referencia; separar identidades humanas y de IA es esencial. No declares integración exclusivamente humana hasta superar su prueba específica.

Guarda un cambio de configuración deliberado solo dentro de su autorización. Vuelve a leer valores e identidades coincidentes; las capturas muestran configuración, no aplicación efectiva.

<a id="4-set-pr-defaults-without-confusing-responsibilities"></a>

## 4. Configurar valores de PR sin confundir responsabilidades

Abre **Project → Settings → Pull Requests**. Comprueba si cada campo es local o heredado.

- **Default merge strategy:** la referencia usa Squash. Un valor predeterminado no prohíbe otras estrategias.
- **Default assignee:** responsable del trabajo, no el revisor obligatorio.
- **Delete source branch after merge:** limpieza opcional que también depende de los permisos del actor. Nunca deduzcas que deben borrarse todas las ramas antiguas.
- Antes del traspaso, revisa siempre origen, destino, diff, título y comprobaciones. La persona revisa e integra; la IA no pulsa merge ni activa auto-merge.

Tras un squash, verifica el cambio integrado frente al historial real del destino. Identificadores distintos por sí solos no significan pérdida de contenido. Sigue el flujo común para sincronización segura y limpieza acotada.

<a id="daily-human-request-creation"></a>

### Creación humana de solicitudes en el uso diario

Después de que la IA suba la rama autorizada y proporcione título/descripción, la persona abre la página de pull requests, crea una solicitud, verifica origen y destino, introduce el texto y envía. Lee el diff y los resultados reales de controles/revisiones antes de confirmar personalmente la integración. Consulta el [traspaso completo](workflow.md). Si quien crea es también revisor obligatorio, verifica las reglas de aprobación de tu versión; recurre a otro humano autorizado cuando se exija, sin debilitar las protecciones.

<a id="5-optional-rest-ingress-restriction"></a>

## 5. Restricción opcional de entrada REST

Un despliegue propio puede denegar el espacio REST en la puerta de enlace permitiendo las rutas web/Git necesarias. El [ejemplo de puerta de enlace](../../examples/onedev/README.md) describe el modelo. Puede desactivar integraciones; elígelo solo si se adapta al servicio.

Inspecciona toda ruta: puerto backend directo, SSH, hostname alternativo, IPv6, túneles, sesiones web autenticadas, tareas del servidor y administración de host/contenedor. Bloquear un endpoint del proxy no prueba que otros caminos estén bloqueados. Incluye rutas normalizadas, variantes de mayúsculas/codificación, operaciones Git reales y WebSockets necesarios en la validación. Los fallos de red no demuestran denegación de permisos.

<a id="6-two-common-pitfalls"></a>

## 6. Dos errores frecuentes

<a id="pr-source-branch-is-not-suggested"></a>

### No se sugiere la rama origen de la PR

En la referencia 14.1.0, las sugerencias consideran el correo del autor del último commit y las direcciones verificadas del usuario conectado. Inspecciona ambos. Añade solo una dirección controlada por ese usuario en Email Addresses y completa la verificación normal. El comportamiento de un administrador no significa que usuarios ordinarios puedan omitirla.

Reabre la creación de PR y comprueba origen y destino. Seleccionar manualmente la rama también es válido. Esto corrige una sugerencia; no integra automáticamente ni otorga aprobación. No cambies la identidad global de Git ni reescribas historia solo para obtener la sugerencia. Un origen seleccionado explícitamente tiene prioridad.

<a id="a-ready-pr-remains-marked-work-in-progress"></a>

### Una PR lista sigue marcada como trabajo en curso

La implementación de referencia trata los títulos que empiezan por `wip` o `[wip]`, sin distinguir mayúsculas, como trabajo en curso y bloquea la integración. **No** prohíbe todo título que comience con una letra inglesa. Afecta al título de la PR, que puede derivarse del mensaje de commit o de la rama.

Retira el marcador solo cuando el trabajo esté realmente listo. Revisiones, controles e integración humana siguen siendo obligatorios; el bloqueo WIP no prueba un límite de permisos de integración. Verifica la regla en la versión desplegada.

<a id="7-acceptance-and-recovery"></a>

## 7. Validación y recuperación

Usa la [matriz común](security-acceptance.md) y la [plantilla de evidencias](../../templates/security-acceptance.csv). Empieza por inventario de solo lectura; obtén autorización adecuada antes de pruebas de rechazo en un repositorio desechable. Registra actor, versión, rutas, control, estado antes/después y motivo real del rechazo. Un fallo inexplicado o una prueba ausente es «no verificado».

Mantén versiones recuperables independientes de repositorios **y** datos/configuración del servicio según la [guía de respaldo](backup-and-recovery.md). Un clon que se actualiza no es una copia completa de OneDev. Compilación y arranque son opcionales y no validan todas las bases o adjuntos del servidor.

<a id="sources-and-limits"></a>

## Fuentes y límites

- [Instalación oficial en contenedor](https://docs.onedev.io/installation-guide/run-as-docker-container) y [configuración de proxy inverso](https://docs.onedev.io/administration-guide/reverse-proxy-setup).
- [Selección de rama origen en la versión de referencia](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/web/page/project/pullrequests/create/NewPullRequestPage.java).
- [Condiciones WIP e integración versionadas](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/PullRequest.java).
- [Protección de ramas versionada](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/support/code/BranchProtection.java) y [controles de push](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/git/hook/GitPreReceiveCallback.java).

El tutorial combina observaciones de interfaz y revisión de código de una versión concreta. Escribirlo no instala OneDev ni certifica otro servidor, rol, modelo NAS, proxy o versión.

**Siguiente:** verifica los permisos configurados con la [matriz](security-acceptance.md), y sigue el [flujo de cuatro pasos y limpieza](workflow.md). Vuelve a la [presentación Git Guard](../../README.es.md) para conocer el producto.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
