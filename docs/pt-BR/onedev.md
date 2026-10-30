# Configuração do OneDev: permissões da IA e revisão humana

[English](../en/onedev.md) · [简体中文](../zh-CN/onedev.md) · [日本語](../ja/onedev.md) · [Deutsch](../de/onedev.md) · [Français](../fr/onedev.md) · [Español](../es/onedev.md) · [Português (Brasil)](onedev.md) · [Русский](../ru/onedev.md)

[Página inicial Git Guard](../../README.pt-BR.md) · [Início rápido](README.md)

Este guia do **RelayRun Git Guard** explica como separar permissões humanas e da IA, proteger main, restringir caminhos que contornam a revisão e manter cópias recuperáveis independentes no OneDev auto-hospedado. A IA faz commits e envia branches dentro da autorização; uma pessoa cria a solicitação, revisa e executa o merge final na interface web.

**Git Guard atende pessoas e equipes com repositórios Git, não apenas usuários do OneDev.** OneDev e GitHub são exemplos de configuração. Outras plataformas de gestão Git podem seguir os [princípios comuns de colaboração e proteção](workflow.md), verificando ajustes e resultados conforme suas capacidades. Este capítulo demonstra OneDev; o [guia GitHub](github.md) traz outro exemplo. OneDev é plataforma de terceiros, não produto RelayRun.

Rascunho de revisão 0.1. Referência de interface e diagnóstico: **OneDev 14.1.0**. É um exemplo versionado, não recomendação de instalar uma versão antiga sem conferir suporte atual. [Fluxo](workflow.md) · [Validação de segurança](security-acceptance.md) · [Alternativa GitHub](github.md)

**Nesta página:** [Configuração com IA](#visible-ai-assisted-setup) · [Implantação](#1-select-a-deployment-boundary) · [Identidades](#2-establish-separate-identities) · [Proteção de branches](#3-initialize-and-protect-the-target-branch) · [Merge humano](#4-set-pr-defaults-without-confusing-responsibilities) · [Entrada REST](#5-optional-rest-ingress-restriction) · [Armadilhas comuns](#6-two-common-pitfalls) · [Validação e recuperação](#7-acceptance-and-recovery) · [Fontes](#sources-and-limits)

Antes de commit ou envio autorizado, siga o guia para [configurar e executar a verificação](public-content-review.md#configure-the-public-content-check) e [interpretar e tratar ocorrências](public-content-review.md#interpret-results-and-handle-findings).

<a id="visible-ai-assisted-setup"></a>

## Configuração visível com auxílio da IA

Você pode configurar manualmente ou pedir à IA que siga este guia e a habilidade de configuração numa interface Computer Use visível. Primeiro identifique projeto exato, ator, configurações a mudar e reversão. A pessoa aprova esse escopo e pode observar; não se presume acesso administrativo oculto ou permanente.

Para controles administrativos, use uma sessão temporária supervisionada destinada àquelas mudanças. A pessoa digita credenciais sensíveis sem colocá-las em chat, capturas ou arquivos do repositório. Não reutilize sessão administrativa para contornar uma ação diária negada. Ao terminar, confira os ajustes, execute a validação delimitada apropriada, encerre a sessão elevada e retorne à identidade diária restrita. Se a interface disponível não conseguir executar uma etapa, informe e deixe-a para a pessoa; não alegue um clique que não aconteceu.

Observar a tela ajuda a explicar a configuração; permissões impostas e seus testes fornecem proteção.

<a id="1-select-a-deployment-boundary"></a>

## 1. Escolher uma fronteira de implantação

Prefira computador, servidor ou NAS independente com arquitetura e suporte a contêineres compatíveis com a versão OneDev escolhida. Mantenha servidor, runtime de contêineres, armazenamento, backups e credenciais administrativas fora do alcance da identidade IA de desenvolvimento. Uso no mesmo host requer permissões explícitas de sistema/arquivos; Docker sozinho não cria a separação.

Use o guia oficial e o [exemplo parametrizado](../../examples/onedev/README.md). Antes de iniciar, escolha versões/digests de imagens com suporte, local independente de dados, entrada TLS e método de recuperação. O exemplo expõe apenas um gateway de loopback, omite o socket Docker e desabilita mapeamentos diretos HTTP/SSH no host. É configuração inicial, não instalação de produção testada. Builds em contêineres podem exigir executor projetado separadamente.

<a id="2-establish-separate-identities"></a>

## 2. Estabelecer identidades separadas

| Onde inspecionar | O que fazer | Verificar |
| --- | --- | --- |
| Administration → Users / Groups | Separar revisor/administrador humano, colaborador IA e identidade de backup somente leitura | Participações e credenciais reais, incluindo acesso herdado |
| Administration → Roles | Examinar permissões de código, gestão de projetos e outras da função | O nome não basta; IA não deve possuir/administrar projetos nem mudar proteção |
| Project → Settings → Authorizations → Users / Groups | Conceder apenas escopo necessário; examinar pais | Backup lê somente o repositório previsto; direitos IA correspondem ao modelo declarado |
| Project → Settings → General | Inspecionar projeto pai e função padrão efetiva | Nenhum acesso anônimo/padrão nem propriedade herdada involuntários |

A opção “Manage Pull Requests” desativada na função Code Writer de referência trata de gestão/operações em lote; não comprova que um code writer nunca possa fazer o merge final. Teste essa autoridade separadamente após aprovação humana válida. Não exponha sessão web humana nem token administrativo à identidade IA diária. A sessão supervisionada e delimitada acima é temporária e não deve permanecer para o Git cotidiano.

<a id="3-initialize-and-protect-the-target-branch"></a>

## 3. Inicializar e proteger a branch de destino

Inicialize a branch protegida prevista no fluxo de configuração controlado pela pessoa antes de habilitar regra que impeça sua criação. Não desligue rotineiramente a proteção para a IA inicializá-la ou repará-la.

Abra **Project → Settings → Code → Branch Protection**. Na interface de referência, selecione a branch protegida, geralmente `main`, e os sujeitos previstos; a referência usa `anyone`. Leia a ordem: nesta versão, regras locais vêm antes das regras do pai e vale a primeira correspondência. Uma regra filha pode ocultar uma regra superior mais rígida; inspecione o comportamento efetivo.

| Opção | Raciocínio necessário |
| --- | --- |
| Prevent forced push | Ativar na branch protegida; testar recusa real de reescrita não autorizada num repositório descartável |
| Prevent deletion | Proteger a branch; excluir o repositório é permissão diferente |
| Prevent creation | Decidir após inicialização; não substitui proteção de atualização/revisão |
| Required reviewers | Selecionar revisor humano independente na interface; conferir expressão e conta resultantes |
| Required builds / signatures | Escolher conforme projeto, com verificações que realmente executem e chaves de assinatura confiáveis |
| File/tag protection | Definir somente escopo necessário; regras de branch não comprovam proteção de tags ou releases |

A referência anterior não exigia revisor inicialmente; depois foram acrescentadas exigências. Bloquear force-push **não bloqueia** push direto comum em fast-forward. Teste esse caminho explicitamente. Um revisor nomeado que também envia a PR pode ser tratado de modo diferente na referência; separar humanos e IA é essencial. Não apresente a configuração como garantia de merge exclusivamente humano antes do teste próprio dessa capacidade.

Salve mudanças deliberadas somente dentro de sua autorização. Releia valores e identidades correspondentes; capturas mostram configuração, não imposição efetiva.

<a id="4-set-pr-defaults-without-confusing-responsibilities"></a>

## 4. Ajustar padrões da PR sem confundir responsabilidades

Abra **Project → Settings → Pull Requests**. Confira se cada campo é local ou herdado.

- **Default merge strategy:** a referência usa Squash. Um padrão não proíbe outras estratégias.
- **Default assignee:** responsabilidade pelo trabalho, não revisor obrigatório.
- **Delete source branch after merge:** limpeza opcional, também dependente da permissão do ator. Nunca conclua que todas as branches antigas devem ser removidas.
- Antes da entrega, examine sempre origem, destino, diff, título e verificações. A pessoa revisa e faz o merge; a IA não clica em merge nem habilita auto-merge.

Após squash, confira a alteração integrada em relação ao histórico real do destino. IDs de commit diferentes, sozinhos, não indicam perda de conteúdo. Siga o fluxo comum para sincronização segura e limpeza delimitada.

<a id="daily-human-request-creation"></a>

### Criação diária de solicitações pela pessoa

Depois que a IA envia a branch autorizada e propõe título/descrição, a pessoa abre a página de pull requests, cria nova solicitação, confere origem/destino, insere o texto e envia. Leia diff e resultados reais de testes/revisões antes de confirmar pessoalmente o merge. Veja a [passagem completa](workflow.md). Se o criador também é revisor obrigatório, confira as regras de aprovação da versão; use outro humano autorizado quando necessário, em vez de enfraquecer a proteção.

<a id="5-optional-rest-ingress-restriction"></a>

## 5. Restrição opcional da entrada REST

Uma implantação própria pode negar o namespace REST no gateway e permitir os caminhos web/Git necessários. O [exemplo de gateway](../../examples/onedev/README.md) descreve esse modelo. Ele pode desativar integrações; escolha-o somente se adequado ao serviço.

Inspecione todas as rotas: porta direta do backend, SSH, hostname alternativo, IPv6, túneis, sessões web autenticadas, tarefas de servidor e administração de contêiner/host. Bloquear um endpoint do proxy não comprova bloqueio dos demais caminhos. Inclua normalização de caminhos, variações de caixa/codificação, operações Git reais e WebSockets necessários na validação. Falhas de rede não são evidência de negação de permissão.

<a id="6-two-common-pitfalls"></a>

## 6. Duas armadilhas comuns

<a id="pr-source-branch-is-not-suggested"></a>

### A branch de origem não é sugerida para a PR

Na referência 14.1.0, as sugestões consideram o e-mail do autor do último commit e os endereços verificados do usuário conectado. Examine autor e usuário pretendidos. Adicione somente endereço controlado por esse usuário em Email Addresses e conclua a verificação normal. Comportamento de administrador não significa que usuários comuns possam dispensá-la.

Reabra a criação da PR e confira origem/destino. Escolher a branch manualmente também é válido. Isso corrige uma sugestão; não faz merge automático nem concede aprovação. Não mude identidade global Git nem reescreva histórico só para obter a sugestão. Origem escolhida explicitamente tem prioridade.

<a id="a-ready-pr-remains-marked-work-in-progress"></a>

### Uma PR pronta continua marcada como trabalho em andamento

A referência trata título iniciado por `wip` ou `[wip]`, sem distinguir maiúsculas, como trabalho em andamento e bloqueia merge. Isso **não** proíbe títulos iniciados por qualquer letra inglesa. Afeta o título da PR, que pode ter sido derivado de mensagem de commit ou branch.

Remova o marcador apenas quando o trabalho estiver realmente pronto. Revisões, verificações e merge final humano continuam necessários; bloqueio WIP não prova fronteira de permissão de merge. Verifique a regra na versão implantada.

<a id="7-acceptance-and-recovery"></a>

## 7. Validação e recuperação

Use a [matriz compartilhada](security-acceptance.md) e o [modelo de evidências](../../templates/security-acceptance.csv). Comece com inventário somente leitura; obtenha autorização apropriada antes de testes de recusa em repositório descartável. Registre ator, versão, caminhos, controle, estado antes/depois e motivo real da recusa. Falha inexplicada ou teste ausente é “não verificado”.

Mantenha versões independentes recuperáveis dos repositórios **e** dados/configuração do serviço conforme o [guia de backup](backup-and-recovery.md). Um clone atualizado não é backup completo do OneDev. Compilação e inicialização são opcionais e não validam todo banco ou anexo do servidor.

<a id="sources-and-limits"></a>

## Fontes e limites

- [Instalação oficial em contêiner](https://docs.onedev.io/installation-guide/run-as-docker-container) e [configuração de proxy reverso](https://docs.onedev.io/administration-guide/reverse-proxy-setup).
- [Seleção de branch de origem versionada](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/web/page/project/pullrequests/create/NewPullRequestPage.java).
- [Condições WIP e merge versionadas](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/PullRequest.java).
- [Proteção de branch versionada](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/support/code/BranchProtection.java) e [verificações de push](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/git/hook/GitPreReceiveCallback.java).

O tutorial combina observações da interface e revisão de fontes vinculadas à versão. Escrevê-lo não instala OneDev nem certifica outro servidor, função, modelo NAS, proxy ou versão.

**A seguir:** confira permissões configuradas com a [matriz](security-acceptance.md) e siga o [fluxo de quatro etapas e limpeza](workflow.md). Volte à [visão geral Git Guard](../../README.pt-BR.md) para a apresentação do produto.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
