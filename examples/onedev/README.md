# OneDev deployment reference

This is an **unexecuted reference configuration**, not a production deployment or a security certificate. See the [OneDev tutorial](../../docs/en/onedev.md) and [acceptance specification](../../docs/en/security-acceptance.md).

## Intended topology

Human-controlled TLS ingress → loopback gateway → internal OneDev HTTP service. Use a separate host/server or supported NAS where practical. The AI contributor has restricted repository access, not server or container administration.

[Compose example](compose.example.yaml) requires an explicitly chosen OneDev image, Nginx image and independent absolute data location. It publishes the gateway on loopback only. Add a properly configured trusted HTTPS ingress before remote use. Do not expose the backend or Docker socket as a convenience.

[Gateway configuration](nginx.conf) demonstrates optional REST-namespace denial while forwarding web/Git and upgrade requests. This can break REST integrations and is deliberately not a default recommendation for every installation. The example does not configure SSH, a build executor, a certificate, a domain, database consistency, resource limits or retention.

## Adapt, inspect, then validate

1. Check current official support, CPU architecture, NAS container support and resources. Pin approved images; do not treat the tutorial's historical UI version as the latest safe version.
2. Resolve the three required variables through your local deployment environment. Keep credentials out of Compose and the public package.
3. Use the container runtime's configuration validation and Nginx syntax test before starting. A syntax check does not prove network isolation.
4. Verify ingress HTTPS, server URL, web sign-in, required WebSockets and legitimate Git read/feature-branch operations.
5. In a separately authorized disposable repository, test main direct push, force-push, deletion, reviewer/merger authority and proxy denial. Include case/encoding/normalization variants and all alternate ports/hosts/IPv6 paths.
6. Verify independent protected recovery points for service data as well as repositories. A clone does not back up users, database state and attachments.

The raw backend has no host port mapping in this example. Users who can control Docker or the host can still reach or alter the service; this is why account/host separation matters. A process listening on the same host may reach loopback; loopback alone does not constrain a privileged AI.

Official references: [container installation](https://docs.onedev.io/installation-guide/run-as-docker-container), [reverse proxy](https://docs.onedev.io/administration-guide/reverse-proxy-setup). The Docker socket shown in some installation examples is intentionally omitted here; Docker-based job execution needs a separate design and is not asserted functional.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
