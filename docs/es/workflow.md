# Flujo de trabajo diario con Git

[English](../en/workflow.md) · [简体中文](../zh-CN/workflow.md) · [日本語](../ja/workflow.md) · [Deutsch](../de/workflow.md) · [Français](../fr/workflow.md) · [Español](workflow.md) · [Português (Brasil)](../pt-BR/workflow.md) · [Русский](../ru/workflow.md)

[Portada Git Guard](../../README.es.md) · [Inicio rápido](README.md)

Borrador base 0.1 — 2026-10-28.

<a id="read-and-scope-the-work"></a>

## Leer las instrucciones y delimitar el trabajo

Identifica el proyecto exacto, directorio local, rama, remoto, visibilidad y autorización vigente. Lee las instrucciones de entrada del agente, el plan actual y los procedimientos pertinentes. Conserva los cambios ajenos a la tarea, preparados o no. Editar, crear commits, hacer push, crear una PR, publicar una versión y desplegar un sitio son acciones distintas; respeta las autorizaciones ya concedidas sin interpretar un plan general como permiso para todas ellas.

<a id="step-1--record-the-local-change"></a>

## Paso 1 — registrar el cambio local

Revisa los archivos modificados y sus diferencias. Ejecuta comprobaciones adecuadas al cambio. Para material público, completa la [revisión de publicación](public-content-review.md) **antes del commit**, aunque vaya a permanecer local al principio. Añade al área de preparación solo los archivos previstos y crea el commit local autorizado. Comprueba su identificador, contenido y los cambios que siguen en el árbol de trabajo.

Un commit local no sube el trabajo. No inicialices otro repositorio, añadas un remoto, cambies protecciones ni crees tareas de copia de seguridad de forma implícita durante una edición normal. No descartes cambios ajenos para obtener un estado limpio.

<a id="step-2--share-the-branch-and-prepare-the-pr"></a>

## Paso 2 — compartir la rama y preparar la PR

Dentro de la autorización vigente, verifica el destino remoto y toda la diferencia de la rama frente al destino real. Incluye los commits anteriores de la rama todavía no integrados, no solo el último. Revisa de nuevo el límite entre contenido público y privado antes de subir nada.

Haz push de la rama de trabajo autorizada sin forzar. En el ejemplo habitual de la portada y la animación, prepara origen/destino correctos, propuesta de título y descripción y resultados reales de validación para que la persona cree la solicitud en la interfaz web. No presentes un formulario preparado como una PR ya creada.

Quien adopte el método puede autorizar por separado a la IA a crear o actualizar la PR correspondiente. Solo entonces realiza esa acción y verifica su existencia y estado reales. Esta variante no concede autoridad para la integración final. Una rama subida o una PR en borrador en un repositorio público ya expone su contenido; no permanece privada hasta integrarse.

Si una política o permiso bloquea la acción, informa del rechazo real. No lo eludas mediante una sesión de administrador, otro token, un puerto directo del servidor, acceso al contenedor u otra interfaz. Resolver un conflicto de contenido no amplía implícitamente la acción permitida.

<a id="human-final-review-and-merge"></a>

## Revisión e integración finales por una persona

En el ejemplo habitual, abre la página de solicitudes del repositorio en OneDev/GitHub, inicia una nueva, verifica las ramas sugeridas, introduce título y descripción y envíala. Si ya existe una solicitud mediante un flujo autorizado por separado, examínala sin duplicarla. Las sugerencias de ramas predeterminadas no son una aprobación.

La persona revisa toda la diferencia, pruebas de validación, destino y resultado previsto, y después realiza la integración final. En este flujo la IA no pulsa merge, no invoca una API/CLI de integración ni activa la integración automática en nombre de la persona.

La revisión obligatoria y la autoridad exclusiva de integración humana son controles separados. Una revisión aprobada puede seguir permitiendo que la identidad IA integre. Verifica ambos antes de describir el flujo como técnicamente impuesto. Protege las credenciales administrativas y las sesiones web existentes, además de la cuenta del bot.

<a id="after-the-human-confirms-merge"></a>

## Después de que la persona confirme la integración

1. Verifica la integración real en el servidor y su destino. Una orden de preparar una PR no confirma que se haya integrado.
2. Obtén las referencias y compara el cambio revisado con el resultado integrado. Squash/rebase pueden cambiar los identificadores de commits; si el destino avanzó, compara la base adecuada y el diff resultante en lugar de exigir árboles completos idénticos. En un squash con la misma base, árboles finales equivalentes aportan evidencia útil.
3. Antes de limpiar, comprueba trabajo sin commit, commits no publicados, otros árboles de trabajo y los acuerdos de recuperación/conservación aplicables. No crees copias no solicitadas ni sobrescribas trabajo exclusivamente local para forzar la alineación.
4. Avanza la rama protegida local por fast-forward cuando su relación con el remoto lo permita. Ante una divergencia, detente y explícala en vez de borrarla con un reset.
5. Elimina solo la rama de trabajo verificada como terminada, dentro de la autorización de limpieza. Si el servidor ya la eliminó, depura su referencia de seguimiento obsoleta sin recrearla. Un squash puede no superar una comprobación de borrado basada solo en ascendencia; verifica contenido y trabajo conservado antes de una alternativa autorizada.
6. Informa del estado real de ramas y árboles de trabajo y de cualquier trabajo conservado o problema pendiente. La limpieza local no equivale a desplegar ni publicar una versión.

<a id="keep-the-rules-portable"></a>

## Mantener las reglas adaptables

El propietario define las convenciones de nombres y revisión. OneDev y GitHub tienen controles y modelos de cuentas distintos; la secuencia compartida es la misma. Usa la [validación de seguridad](security-acceptance.md) para distinguir la política deseada de los límites comprobados, y la [guía GitHub](github.md) para las diferencias resumidas de esa plataforma.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
