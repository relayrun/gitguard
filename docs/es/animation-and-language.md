# Integración de animación e idiomas

[English](../en/animation-and-language.md) · [简体中文](../zh-CN/animation-and-language.md) · [日本語](../ja/animation-and-language.md) · [Deutsch](../de/animation-and-language.md) · [Français](../fr/animation-and-language.md) · [Español](animation-and-language.md) · [Português (Brasil)](../pt-BR/animation-and-language.md) · [Русский](../ru/animation-and-language.md)

[Portada Git Guard](../../README.es.md) · [Inicio rápido](README.md)

La breve presentación sigue este orden: marca, riesgos del repositorio, límites de permisos comprobados, configuración visible asistida por IA y cuatro relevos diarios. Ilustra el método sin certificar un servidor real. El flujo escrito es la referencia; Git.md en un diálogo de ejemplo designa el archivo real de procedimiento del proyecto que lo adopta.

<a id="homepage-placement-and-language"></a>

## Ubicación e idioma en la portada

Coloca la presentación de 40 segundos justo después de la lista de idiomas del README y antes de la introducción principal y del ejemplo de cuatro pasos. El título inglés es «Git Guard in 40 seconds» y el chino «40 秒了解 Git Guard». Es una visión general del producto, no el tutorial completo de configuración.

Usa el idioma del README elegido. El README inglés predeterminado enlaza su MP4; chino simplificado y japonés enlazan los suyos. No añadas otro selector de idioma para el vídeo. Cambiar el README también selecciona su vídeo. Alemán, francés, español, portugués brasileño y ruso usan igualmente sus películas terminadas. Este paquete local contiene las ocho parejas README/vídeo.

<a id="delivery-and-playback"></a>

## Entrega y reproducción

- Distribuye solo MP4. Conserva las portadas PNG como recursos reutilizables, no como GIF animados. Las composiciones editables, recursos compartidos y traducciones permanecen en el entorno de producción; se distribuyen solo las exportaciones elegidas.
- Cada README de GitHub muestra el vídeo de su idioma mediante una URL de adjunto en un párrafo independiente y conserva debajo un enlace de descarga directa del MP4. Las notas de los recursos enumeran los MP4 incluidos y los adjuntos por idioma. Otros lectores Markdown pueden mostrar solo un enlace.
- Un README no puede ejecutar JavaScript personalizado ni elegir vídeos según el idioma del navegador o la IP. Las portadas enlazadas abren archivos; las etiquetas HTML video ordinarias se filtran. Sustituye adjuntos solo con autorización para publicar, verifica la reproducción real y actualiza juntos el README y la tabla. GitHub controla el reproductor; no se garantizan inicio automático, bucle ni conservación del último fotograma.
- En un sitio web, resuelve el idioma mediante URL explícita, elección manual guardada, preferencias de contenido compatibles del navegador y, finalmente, inglés como alternativa. Selecciona el vídeo disponible correspondiente a ese mismo idioma. No hace falta un menú de vídeo separado. Identifica claramente una alternativa en inglés y no etiquetes chino simplificado como traducción a chino tradicional.
- La reproducción web empieza silenciada. Activa efectos solo tras un clic explícito; conserva controles de pausa/silencio, portada/reproducción manual alternativa y atención a movimiento reducido. La reproducción normal termina en el último fotograma, con repetición y bucle opcional. Sin JavaScript, conserva enlaces MP4 normales.
- Las ocho exportaciones actuales duran 40 segundos, con breves efectos de acción y sin música de fondo. Conserva toda la animación final de marca seguida de la tarjeta estática; no añadas el inicio al final.
- Usa nombres previsibles como RelayRun-GitGuard-Intro-en-v12.mp4 y sus equivalentes zh-CN, ja, de, fr, es, pt-BR y ru. Consulta [recursos de vídeo y créditos sonoros](../../assets/videos/README.md).

<a id="before-adding-media-to-a-release"></a>

## Antes de incluir medios en una publicación

Inspecciona fotogramas exportados, texto, metadatos y derechos. Verifica duración completa de vídeo/audio, decodificación, tamaño medido y enlaces de idiomas. La reproducción real en navegador es distinta de comprobar archivos; los controles numéricos de audio no sustituyen la escucha. Los avisos de binarios/tamaño del escáner requieren revisión manual acotada; no los suprimas globalmente.

Distribuye solo las exportaciones seleccionadas y créditos necesarios. Fuentes editables, pruebas privadas, grabaciones sin procesar y planes internos no pertenecen al paquete público. Una vista local aproxima la presentación y no certifica el renderizado en GitHub. Subir adjuntos públicos, integrar el sitio y desplegar son acciones separadas.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
