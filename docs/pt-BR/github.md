# GitHub: correspondência resumida de recursos

[English](../en/github.md) · [简体中文](../zh-CN/github.md) · [日本語](../ja/github.md) · [Deutsch](../de/github.md) · [Français](../fr/github.md) · [Español](../es/github.md) · [Português (Brasil)](github.md) · [Русский](../ru/github.md)

[Página inicial Git Guard](../../README.pt-BR.md) · [Início rápido](README.md)

Rascunho básico 0.1 — conferido com a documentação GitHub vinculada em 2026-10-28.

OneDev continua sendo o principal exemplo detalhado do Git Guard. GitHub é o exemplo secundário: use o mesmo [fluxo diário](workflow.md), a mesma [validação de segurança](security-acceptance.md) e as mesmas [orientações de backup](backup-and-recovery.md). Este capítulo relaciona capacidades, não configurações atuais de um repositório específico.

| Requisito compartilhado | Correspondência no GitHub |
| --- | --- |
| Preparação e commit locais | Trabalho Git local comum; nenhum envio remoto nesta etapa |
| Colaboração remota autorizada | Enviar uma branch de trabalho e preparar o texto; no exemplo padrão a pessoa cria a PR na web |
| Revisão obrigatória e main protegida | Configurar proteção/rulesets de branch e exigências de revisão adequadas |
| Restringir force-push e exclusão de referências protegidas | Manter desativadas as permissões correspondentes e examinar exceções |
| Merge final humano | Separar identidade/credenciais IA da autoridade humana; revisão obrigatória sozinha não reserva o direito de merge |
| Após o merge humano | Verificar o resultado, sincronizar main local com segurança e limpar somente a branch confirmada como concluída |

O GitHub documenta branches protegidas e rulesets de branches/tags para repositórios públicos nos planos Free; a disponibilidade para privados depende do plano. Não deduza que todos os recursos avançados ou push rulesets estão incluídos apenas pela disponibilidade para repositórios públicos. [Branches protegidas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) · [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).

Revisões aprovadas obrigatórias não estabelecem, por si só, quem pode executar o merge depois. Exceções administrativas de proteção clássica, atores permitidos, listas de bypass, permissões de aplicativos e credenciais humanas acessíveis também importam. As restrições de push documentadas para repositórios de organizações compatíveis são um controle a avaliar junto da obrigatoriedade de PR; teste a identidade real antes de afirmar exclusividade humana. O proprietário deve manter controle separado da administração, exclusão do repositório e alteração de regras.

No exemplo padrão, a pessoa segue a criação de pull request: verifica base (destino) e compare (origem), preenche título/descrição, envia, revisa diferenças e verificações e faz pessoalmente o merge. Aprovações independentes exigidas continuam valendo; criar uma PR não a aprova. O [fluxo compartilhado](workflow.md) descreve a variante de criação por IA autorizada separadamente.

O GitHub também oferece merge automático; este fluxo deixa a execução final com a pessoa. Não o habilite como conveniência incidental. Não suponha que um token permita escrita em branches de trabalho mas proíba todos os merges apenas por ter o rótulo de restrito.

O exemplo de proxy reverso do OneDev auto-hospedado não se transforma em um proxy diante do GitHub. Relacione o objetivo de proteção às identidades, regras, permissões de aplicativos e caminhos de acesso verificados próprios do GitHub.

Antes da adoção, examine plano real da conta, visibilidade, regras ativas e exceções, e aplique a matriz comum em ambiente descartável autorizado. A redação deste capítulo não alterou configurações nem realizou testes negativos de segurança.


<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
