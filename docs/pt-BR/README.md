# Git Guard — Início rápido

[English](../en/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Español](../es/README.md) · [Português (Brasil)](README.md) · [Русский](../ru/README.md)

[Página inicial Git Guard](../../README.pt-BR.md)

Apresentação, início rápido, os sete manuais detalhados e vídeo estão disponíveis em português. OneDev e GitHub são exemplos; os princípios podem ser adaptados a outros gerenciadores Git. Esta tradução é uma versão para revisão, não uma aceitação de segurança real.

Antes de commit ou envio autorizado, siga o guia para [configurar e executar a verificação](public-content-review.md#configure-the-public-content-check) e [interpretar e tratar ocorrências](public-content-review.md#interpret-results-and-handle-findings).

## A IA pode ajudar a configurar

Siga o manual ou entregue o manual e a skill adequada a um assistente. **Prefira Computer Use com interface visível:** acompanhe as ações, conceda somente as permissões necessárias e digite pessoalmente as credenciais sensíveis. Ao terminar, encerre a sessão administrativa temporária e devolva à IA sua identidade cotidiana restrita.

| Ambiente | Por onde começar |
| --- | --- |
| OneDev auto-hospedado | [Manual](onedev.md) · [Skill de configuração e aceitação (inglês)](../../skills/gitguard-onedev-safety/SKILL.md) |
| GitHub | [Guia do GitHub](github.md) |
| Outros gerenciadores Git | Adaptar o [fluxo compartilhado](workflow.md) e a [matriz de aceitação](security-acceptance.md) às permissões e interfaces disponíveis. |

A preparação inicial tem quatro partes: definir repositório, branch principal e identidades separadas; configurar os controles; testar ações permitidas e recusadas em um repositório isolado e autorizado; organizar [backups e recuperação](backup-and-recovery.md). Não é preciso repetir tudo em cada alteração. Reavalie as partes afetadas quando permissões, regras ou ambiente mudarem.

## Quatro passos no dia a dia

Use a [skill de colaboração (inglês)](../../skills/gitguard-workflow/SKILL.md) com o fluxo Git do seu projeto.

| Passo | O que você diz ou faz | O que a IA faz |
| --- | --- | --- |
| 1. Commit local | “Execute o passo 1 conforme Git.md.” | Lê o fluxo, confere as alterações e cria o commit local. Nada é enviado ainda. |
| 2. Push e preparação | “Execute o passo 2 conforme Git.md.” | Envia a branch autorizada e prepara título, descrição e resultados das verificações. |
| 3. Revisão e merge humanos | Crie o pedido na web; confira branches de origem e destino, título, descrição, diferenças e verificações; depois confirme o merge. | Explica e ajuda. Uma pessoa realiza o merge final. |
| 4. Limpeza após o merge | “Já fiz o merge. Confira o resultado e faça a limpeza.” | Verifica o conteúdo realmente integrado, sincroniza main com segurança e remove apenas branches confirmadas como concluídas. |

`Git.md` representa o documento real do projeto; o nome pode variar. Você decide quando fazer commit, push e merge. [Fluxo completo](workflow.md)

## Segurança e recuperação

Uma configuração existente não comprova sua eficácia. Testes de recusa exigem um repositório descartável e autorização específica; marque caminhos não testados como não verificados. Mantenha sincronização independente e versões históricas protegidas. Compilar do zero e iniciar o programa são verificações opcionais, escolhidas conforme o projeto.

No exemplo OneDev, o e-mail verificado do autor pode afetar a sugestão da branch de origem, sem executar um merge. Prefixos WIP no título podem bloquear a integração na versão de referência; isso não proíbe títulos comuns que começam com letras.

## Guias detalhados

- [Fluxo diário](workflow.md)
- [Configuração OneDev](onedev.md)
- [Correspondência GitHub](github.md)
- [Validação de segurança](security-acceptance.md)
- [Backup e recuperação](backup-and-recovery.md)
- [Revisão de conteúdo público](public-content-review.md)
- [Animação e idiomas](animation-and-language.md)
- [Skills](../../skills/README.md) · [Templates](../../templates/README.md)

Habilidades, modelos, exemplos de implantação e ferramentas de verificação continuam como recursos compartilhados em inglês.

A IA prepara as alterações; uma pessoa revisa e realiza a integração final.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
