# Especificación de validación de seguridad

[English](../en/security-acceptance.md) · [简体中文](../zh-CN/security-acceptance.md) · [日本語](../ja/security-acceptance.md) · [Deutsch](../de/security-acceptance.md) · [Français](../fr/security-acceptance.md) · [Español](security-acceptance.md) · [Português (Brasil)](../pt-BR/security-acceptance.md) · [Русский](../ru/security-acceptance.md)

[Portada Git Guard](../../README.es.md) · [Inicio rápido](README.md)

Borrador base 0.1 — 2026-10-28.

Esta especificación es común al manual humano y a futuras habilidades. Es un plan de pruebas, no un informe de instalación aprobada. La guía detallada de OneDev y la correspondencia breve de GitHub deben remitir aquí sin definir criterios incompatibles.

<a id="inspect-first"></a>

## Inspeccionar primero

Registra plataforma/versión, visibilidad, ramas protegidas, identidades, roles, permisos de tokens/aplicaciones, reglas heredadas, orden/aplicación y excepciones de bypass. Inspecciona las rutas pertinentes de Git/SSH/HTTPS, web, API, CI/integración, proxy y host/almacenamiento. Comprueba si la IA también puede usar sesiones web o credenciales humanas existentes.

En instalaciones propias, inspecciona acceso al host, contenedores, directorios de datos y puertos alternativos. Un servidor/NAS independiente solo crea un límite útil cuando la IA no puede administrarlo. Un proxy inverso controla las solicitudes que lo atraviesan; no protege una ruta alternativa expuesta ni el almacenamiento subyacente. Las plataformas alojadas necesitan controles propios de cuentas/aplicaciones; no se puede asumir que el patrón de proxy propio sea trasladable.

<a id="test-only-in-the-authorized-environment"></a>

## Probar solo en el entorno autorizado

Usa un repositorio o instancia desechable autorizado por separado, con reglas representativas e identidades distintas. Confirma que los datos de prueba son recuperables y qué operaciones deben permitirse. Realiza pruebas negativas únicamente sobre esos objetos desechables, con contenido inocuo y conservando evidencias. Este documento no autoriza borrar repositorios de producción, reescribir historia real ni cambiar roles activos.

<a id="acceptance-matrix"></a>

## Matriz de validación

| Capacidad/ruta | Resultado esperado para la identidad IA restringida | Evidencia necesaria |
| --- | --- | --- |
| Leer y preparar una rama de trabajo permitida | Permitido dentro del alcance | Control positivo que alcanza el servicio previsto con la identidad prevista |
| Subir commits nuevos ordinarios directamente a main protegida | Denegado por la política prevista | Rechazo real y referencia protegida sin cambios |
| Forzar la reescritura de historial protegido | Denegado | Rechazo de permiso e historial sin cambios |
| Borrar rama/referencia protegida | Denegado | Rechazo real y referencia todavía presente |
| Borrar repositorio/proyecto | Denegado | Proyecto desechable presente y cuenta sin capacidad efectiva de borrado |
| Aprobar en nombre de la persona exigida | Denegado | Identidades de revisión y registro de autorización |
| Ejecutar la integración final, incluso tras aprobar las revisiones | Denegado según la política de integración exclusivamente humana | Resultado real de permisos; una PR sin aprobar no es prueba suficiente |
| Activar/usar integración automática o una integración equivalente | Denegado a la IA en este flujo | Ruta API/web/aplicación y actor real registrados |
| Cambiar roles, protecciones, listas de bypass o controles de seguridad | Denegado | Configuración antes/después y rechazo |
| Usar otra credencial, sesión, endpoint o ruta CI | Sin autoridad involuntaria | Inventario y prueba acotada de cada ruta pertinente; las desconocidas quedan sin verificar |
| Modificar host/contenedor/almacenamiento del repositorio | Sin acceso administrativo o destructivo | Evidencia del límite de sistema/almacenamiento, no solo una casilla de aplicación |
| Borrar/sobrescribir todos los puntos de recuperación | Denegado a la identidad de desarrollo | Conservación independiente y separación de administración de copias |
| La persona revisa y ejecuta la integración prevista | Permitido según la política de revisión | Control positivo con la identidad humana real |

Revisa creación de ramas/etiquetas, borrado de etiquetas y excepciones de ramas cuando afecten a la política. No bloquees accidentalmente toda preparación mientras afirmas haber separado responsabilidades.

<a id="record-each-result"></a>

## Registrar cada resultado

Para cada fila conserva identidad de prueba, identidad del software/configuración, origen/destino, operación y ruta, resultado esperado, resultado real/motivo, estado de objetos antes/después, hora y ubicación de evidencias. Oculta credenciales y datos privados ajenos antes de compartirlas.

Usa **aprobado**, **fallido** o **no verificado**, con explicación. Tiempo de espera agotado, fallo de acceso, conflicto, petición inválida, marcador WIP, servidor caído, captura o interruptor activado no prueban que el permiso previsto rechazara la acción. Un control positivo ayuda a distinguir la restricción efectiva de una prueba mal configurada.

Si un límite obligatorio falla o queda sin verificar, señala la carencia explícitamente. Explica qué operaciones están realmente bloqueadas, sin afirmar que se eliminó cualquier error posible de la IA. Repite las pruebas afectadas tras cambios de roles, proxy, reglas, versión o integraciones; conserva evidencias anteriores con su alcance original.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
