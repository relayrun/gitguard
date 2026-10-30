# Revisión del contenido público

[English](../en/public-content-review.md) · [简体中文](../zh-CN/public-content-review.md) · [日本語](../ja/public-content-review.md) · [Deutsch](../de/public-content-review.md) · [Français](../fr/public-content-review.md) · [Español](public-content-review.md) · [Português (Brasil)](../pt-BR/public-content-review.md) · [Русский](../ru/public-content-review.md)

[Portada Git Guard](../../README.es.md) · [Inicio rápido](README.md)

Borrador de revisión 0.1. Procedimiento reutilizable para proyectos que publican material. [Flujo](workflow.md)

<a id="configure-the-public-content-check"></a>

## Configurar la comprobación del contenido público

1. Identifica el proyecto exacto y los archivos que se publicarán. Mantén registros internos, credenciales, configuración privada del escáner y diagnósticos fuera de ese árbol. Si el directorio de desarrollo contiene material privado, revisa una copia de publicación separada; no borres los originales privados solo para superar un escaneo.
2. Localiza el comprobador en el código de Git Guard o en la instantánea de referencia incluida con la habilidad instalada. Requiere Python 3.9 o posterior y la biblioteca estándar. No se instala solo, inicia servicios ni impone permisos de servidor. Indica el destino con `--root`; el directorio de la habilidad no es el proyecto objetivo.
3. Usa `--profile generic` en un proyecto que adopte el método. Emplea `--profile gitguard` solo para aplicar también las exclusiones de estructura pública/privada de este paquete. El comprobador no tiene una lista personalizada de términos sensibles ni sustitución automática. Para secretos o identificadores propios de la organización, usa un escáner adecuado aparte, con configuración privada fuera del árbol publicado; consulta las [listas privadas](#sensitive-matching-lists-stay-private).
4. Revisa archivos de trabajo, bytes preparados e historial saliente como ámbitos separados. Los siguientes caminos son ejemplos. Sustituye el rango por los commits que realmente saldrán; el comprobador no hace fetch ni push. Sin repositorio Git, empieza por los archivos y revisa índice/historial cuando existan. Un resultado limitado al árbol de trabajo no certifica commits posteriores.

```sh
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic --staged
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic --history origin/main..HEAD
```

<a id="interpret-results-and-handle-findings"></a>

## Interpretar resultados y tratar hallazgos

La salida **0** significa que no hay hallazgos dentro de las reglas implementadas; **1**, que hay hallazgos que revisar; **2**, que la comprobación no terminó. Los informes muestran rutas, categorías y números de línea, no valores secretos coincidentes. El análisis del árbol de trabajo incluye archivos ignorados salvo los metadatos Git: ignorar un archivo no impide copiarlo accidentalmente a una publicación.

Las reglas señalan firmas de claves privadas, ciertos formatos de tokens GitHub, credenciales en URL, rutas de máquinas, direcciones de red privada y ciertos nombres privados/de ejecución, además de enlaces Markdown relativos rotos o que salen del alcance. No detectan todas las contraseñas ni identificadores de cuentas. Los binarios requieren revisión manual; no se inspeccionan archivos mayores de 2.000.000 bytes; el límite es de 3.000 archivos y 200 commits por rango de historial. Examina por partes los ámbitos declarados mayores, sin omitirlos silenciosamente.

Para cada hallazgo registra categoría, ubicación, decisión y nueva comprobación sin reproducir valores sensibles. Corrige la copia pública o las inclusiones, o justifica el resultado benigno/de revisión manual; después repite las comprobaciones de trabajo, índice e historial afectadas. No suprimas globalmente avisos de binarios o tamaño. Una exposición real de credenciales exige sustituirlas y corregir el historial con autorización separada; esta herramienta no repara historia ni borra/sustituye contenido. Un tiempo agotado o un análisis incompleto no es un aprobado.

Para este paquete de Git Guard, use primero `scripts/prepare_release.py` para crear una copia pública con un alcance explícito. Las cachés de desarrollo permanecen en su ubicación original y las exclusiones se registran por separado. La opción `--media-review` lee un registro privado de los PNG/MP4 revisados individualmente con sus SHA-256 exactos. Solo los avisos binarios coincidentes se marcan como revisados y se enumeran aparte; los archivos modificados, secretos, archivos ilegibles y límites de tamaño siguen pendientes. El código 0 puede incluir esas revisiones documentadas, sin certificar automáticamente la privacidad. Consulte las [instrucciones de comprobación y empaquetado](../../scripts/README.md).

<a id="before-a-local-commit"></a>

## Antes de un commit local

Revisa los archivos modificados reales, incluidos los no rastreados. Confirma propiedad y derechos de publicación. Excluye planes privados, rutas de hosts/usuarios, direcciones internas, tokens, claves privadas, credenciales, datos de clientes, capturas/registros sin procesar y código de productos ajenos. Usa nombres y valores genéricos en los ejemplos.

Comprueba enlaces, UTF-8, cobertura lingüística real, avisos de terceros y exactitud de las afirmaciones de finalización. No anuncies como disponible un sitio o despliegue previsto. Mantén las evidencias privadas fuera del árbol publicado.

Inspecciona los bytes preparados por separado: pueden diferir de los archivos de trabajo. Revisa renombrados/borrados, binarios, submódulos y enlaces simbólicos; un documento visible limpio no prueba que un adjunto incrustado sea seguro. Un commit local no autoriza publicar.

<a id="before-a-push"></a>

## Antes de hacer push

Enumera los commits salientes exactos respecto al destino previsto y revisa cada instantánea pertinente, incluidos archivos borrados. Los secretos antiguos siguen en la historia aunque se eliminen después. Revisa etiquetas y otras referencias solo si forman parte del push propuesto; un repositorio nuevo no debe heredar historial privado por accidente.

Si se confirmó contenido sensible, detén la publicación, organiza la sustitución adecuada de credenciales y una corrección aprobada por separado. No fuerces un push ni borres un repositorio silenciosamente para ocultar la historia. Los escáneres son evidencia auxiliar, no una prueba de que se haya eliminado todo lo privado.

<a id="reviewable-release"></a>

## Publicación revisable

Registra destino, visibilidad, archivos cambiados, historial saliente, decisión sobre derechos/licencia, validación y límites pendientes. Confirma la autorización existente para esa acción exacta. Conserva la integración final humana.

Si el repositorio enlaza un sitio oficial, comprueba hostname, certificado HTTPS, marca y página real. Traduce de manera coherente la etiqueta visible en todos los README compatibles, manteniendo el mismo destino canónico. Revisa el campo Website del repositorio durante la publicación autorizada. El manual debe ser útil independientemente del sitio.

<a id="evidence-levels"></a>

## Niveles de evidencia

Distingue inspeccionado, comprobado estáticamente, probado en comportamiento, desplegado y confirmado por el usuario. Una captura de configuración, código de salida del escáner o transferencia correcta no certifican seguridad real ni restauración. Para permisos, usa la [especificación de validación](security-acceptance.md).

<a id="sensitive-matching-lists-stay-private"></a>

## Las listas sensibles de coincidencias permanecen privadas

Publica solo lógica reutilizable y datos de prueba inventados. Los secretos reales, identificadores de cuentas y listas de coincidencias/sustituciones específicas deben quedar fuera de fuentes, paquetes de habilidades, descargas, capturas e historia Git saliente. Una regla que contiene un valor privado exacto también es sensible; ponerla en una configuración no la vuelve publicable. Las reglas de ignorados no sustituyen la revisión de lo preparado y de la historia.

Si usas otro escáner, como Gitleaks, con configuración privada, proporciona el archivo desde una ubicación privada durante la ejecución. No lo copies a un paquete público, no muestres coincidencias ni uses valores reales como argumentos de comandos o datos de prueba. Conserva los diagnósticos en privado y oculta contenido antes de compartirlos.

El comprobador incluido se escribió de nuevo para Git Guard. No carga una lista privada previa ni reconoce específicamente cuentas de trading/clientes, contraseñas arbitrarias o todos los tokens. Sus heurísticas generales complementan un escáner apropiado y la revisión humana; un resultado limpio no garantiza la ausencia de todo secreto. No limpia el historial.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
