# Animation and language integration

[English](animation-and-language.md) · [简体中文](../zh-CN/animation-and-language.md) · [日本語](../ja/animation-and-language.md) · [Deutsch](../de/animation-and-language.md) · [Français](../fr/animation-and-language.md) · [Español](../es/animation-and-language.md) · [Português (Brasil)](../pt-BR/animation-and-language.md) · [Русский](../ru/animation-and-language.md)

[Git Guard home](../../README.md) · [Quick start](README.md)

The short product overview follows: brand, repository risks, tested permission boundaries, visible AI-assisted setup, then the four daily handoffs. It illustrates the method rather than certifying a live server. The written workflow remains authoritative; Git.md in a sample conversation means the adopter's actual workflow file.

## Homepage placement and language

Place the 40-second overview immediately after the README language list and before the core introduction and daily four-step example. The English heading is “Git Guard in 40 seconds”; the Chinese heading is “40 秒了解 Git Guard”. This is a product overview, not the full configuration tutorial.

Use the language of the selected README. The default English README links to the English MP4; Simplified Chinese and Japanese each link to their matching MP4. Do not add a second video-language selector. Switching the README language also chooses its video. German, French, Spanish, Brazilian Portuguese and Russian also use their own completed films. All eight README/video pairs are included in this local package.

## Delivery and playback

- Deliver MP4 only. Keep the PNG covers as reusable assets, not animated GIFs. Editable composition, shared artwork and translated text stay in the production workspace; consumers receive selected exports.
- Each GitHub README embeds its matching video using a standalone GitHub attachment URL, with a direct MP4 download link below it. The bundled MP4 files and language-to-attachment mapping are listed in the video asset notes. Other Markdown viewers may show only a link.
- A repository README cannot run custom JavaScript or select videos by browser language or IP. Linked posters navigate to files; ordinary HTML video tags are filtered. Publish replacement attachments only with authorization, verify actual playback, and update the README and mapping together. GitHub controls the player; autoplay, looping and a held final frame are not guaranteed.
- On a website, resolve the page language from explicit language URL, saved manual choice, supported browser-content preferences, then English fallback. Select the matching available video from that same page language. A separate video-language menu is unnecessary. Clearly label an English fallback and do not label Simplified Chinese as a Traditional Chinese translation.
- Website playback starts muted. Enable effects only on an explicit click; retain pause/mute controls, a poster/manual-play fallback and reduced-motion handling. Default playback ends on the final frame, with replay and optional looping. With JavaScript disabled, retain ordinary MP4 links.
- All eight current exports are 40 seconds, with short action effects and no background music. Preserve full closing brand motion followed by the static end card; do not append the opening to the ending.
- Use predictable names such as RelayRun-GitGuard-Intro-en-v12.mp4 and the corresponding zh-CN, ja, de, fr, es, pt-BR and ru names. See the [video assets and sound credits](../../assets/videos/README.md).

## Before adding media to a release

Inspect exported frames, text, metadata and asset rights. Verify complete video/audio duration, decoding, measured size and language links. Actual browser playback is separate from file checks; numeric audio checks do not replace listening review. A content scanner's binary/oversize finding needs scoped manual review; do not suppress those findings globally.

Only ship selected exports and necessary credits. Editable source, private evidence, raw recordings and internal plans do not belong in the public documentation package. A local reading preview approximates presentation and does not certify GitHub rendering. Public attachment upload, website integration and deployment are separate actions.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
