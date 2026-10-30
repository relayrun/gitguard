# Copias independientes y recuperación

[English](../en/backup-and-recovery.md) · [简体中文](../zh-CN/backup-and-recovery.md) · [日本語](../ja/backup-and-recovery.md) · [Deutsch](../de/backup-and-recovery.md) · [Français](../fr/backup-and-recovery.md) · [Español](backup-and-recovery.md) · [Português (Brasil)](../pt-BR/backup-and-recovery.md) · [Русский](../ru/backup-and-recovery.md)

[Portada Git Guard](../../README.es.md) · [Inicio rápido](README.md)

Borrador base 0.1 — 2026-10-28.

Los permisos y las copias recuperables atienden fallos diferentes. La base es sincronizar automáticamente a un dispositivo independiente, comprobar la integridad y proteger puntos históricos de recuperación. **Compilar y arrancar la aplicación es opcional**: elige comprobaciones manuales, un disparador separado o automatización adicional según el proyecto.

<a id="personal-and-company-schedules"></a>

## Programación personal y empresarial

Una persona puede encender periódicamente un portátil secundario y dejar que el disparador configurado sincronice los datos. Indica si se activa al arrancar el sistema o al iniciar sesión; una tarea ligada al inicio de sesión no se ejecuta antes de que ese usuario acceda. Una empresa puede usar un dispositivo independiente disponible con programación diaria, gestión de ejecuciones omitidas, reintentos de red limitados, control de concurrencia y fallos visibles.

Son decisiones de implementación, no funciones entregadas por esta guía. Leerla no instala scripts ni tareas programadas. No concedas a la identidad IA de desarrollo autoridad para borrar todas las versiones recuperables ni administrar el dispositivo de respaldo.

<a id="define-what-the-copy-covers"></a>

## Definir la cobertura de la copia

Una copia de trabajo de main no es un respaldo completo del servidor. Especifica cobertura de ramas/historial, trabajo exclusivamente local o sin commit, código/documentos, dependencias necesarias, recursos de ejecución, configuración externa y proyectos privados. Conserva los secretos en un procedimiento de recuperación debidamente protegido, nunca en ejemplos públicos ni archivos corrientes destinados a compartirse.

Los datos del repositorio y los metadatos de alojamiento Git son distintos. La recuperación completa de un servicio propio puede requerir también base de datos consistente, cuentas/permisos, incidencias/PR, adjuntos, configuración y almacenamiento. Prueba la restauración del servicio aparte de la compilación.

Un espejo actualizado puede reproducir eliminaciones. Mantén puntos independientes y protege la última versión conocida como válida. Ajusta la retención a la necesidad real; no borres automáticamente copias antiguas solo porque una nueva transferencia indique éxito.

<a id="baseline-checks"></a>

## Comprobaciones básicas

1. Confirma origen, revisión/alcance previsto, destino, identidad y espacio disponible. Conserva datos ajenos.
2. Sincroniza sin sobrescribir una copia modificada/divergente ni devolver cambios al origen. Verifica igualdad exacta con la revisión obtenida prevista; una rama local adelantada podría aparentar estar ya actualizada.
3. Captura coherentemente el alcance declarado con un identificador único del punto de recuperación. Registra reglas de inclusión/exclusión y archivos obligatorios.
4. Comprueba manifiesto y hashes pertinentes de código, archivos y archivos comprimidos. Abrir un ZIP, contar archivos o calcular solo su hash no prueba que incluya los fuentes requeridos. Los fallos obligatorios deben hacer fallar el resultado.
5. Guarda resultados duraderos y restaura periódicamente en un destino separado y vacío. Distingue integridad de restauración; hasta restaurar, esta última no está verificada.

<a id="optional-compilation-and-startup"></a>

## Compilación y arranque opcionales

Si se eligen, compila la copia restaurada con la cadena de herramientas realmente compatible y un procedimiento limpio. Registra configuración, cobertura, proyectos no cargados/excluidos y dependencias. Un directorio de restauración vacío no demuestra compilación limpia si el propio archivo incluye salidas en caché. No permitas que archivos no declarados de la máquina de desarrollo original oculten omisiones.

Una lección histórica útil es que un respaldo puede incluir archivos de proyecto pero omitir código fuente de un proveedor necesario; compilar la copia restaurada puede revelar el hueco. Aun así, compilar no valida todos los documentos, recursos de ejecución, bases del alojamiento o rutas de la aplicación.

Opcionalmente, inicia la aplicación restaurada y comprueba funciones básicas en un entorno de prueba adecuado, evitando efectos en producción. Para proyectos de documentación o contenido estático, elige comprobaciones pertinentes de enlaces/contenido/sitio en vez de imponer un compilador ajeno.

Registra compilación/arranque como **no seleccionado**, **no verificado**, **aprobado** o **fallido**, según proceda. No seleccionar una prueba opcional no hace fallar el respaldo básico; terminar una transferencia tampoco permite etiquetarla como validada por compilación.

<a id="if-validation-fails"></a>

## Si falla la validación

Determina si el fallo es una omisión del respaldo, un requisito de entorno o un defecto de aplicación. Corrige las inclusiones o el entorno declarado, crea otro punto, restaura y repite las comprobaciones afectadas. Conserva la copia buena anterior y el registro fallido. No sobrescribas evidencias fallidas en silencio ni declares reparado un respaldo antiguo sin revalidarlo.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
