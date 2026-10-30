# Especificação de validação de segurança

[English](../en/security-acceptance.md) · [简体中文](../zh-CN/security-acceptance.md) · [日本語](../ja/security-acceptance.md) · [Deutsch](../de/security-acceptance.md) · [Français](../fr/security-acceptance.md) · [Español](../es/security-acceptance.md) · [Português (Brasil)](security-acceptance.md) · [Русский](../ru/security-acceptance.md)

[Página inicial Git Guard](../../README.pt-BR.md) · [Início rápido](README.md)

Rascunho básico 0.1 — 2026-10-28.

Esta especificação é compartilhada pelo manual humano e futuras habilidades. É um plano de testes, não um relatório de instalação aprovada. O guia detalhado do OneDev e o resumo GitHub devem apontar para cá sem criar critérios contraditórios.

<a id="inspect-first"></a>

## Inspecionar primeiro

Registre plataforma/versão, visibilidade, branches protegidas, identidades, funções, permissões de tokens/aplicativos, regras herdadas, ordem/aplicação e exceções de bypass. Examine caminhos relevantes de Git/SSH/HTTPS, web, API, CI/integração, proxy e host/armazenamento. Confira se uma sessão web ou credencial humana existente também é utilizável pela IA.

Na hospedagem própria, examine acesso a host, contêineres, diretórios de dados e portas alternativas. Um servidor/NAS independente só cria uma fronteira útil se a IA não puder administrá-lo. Um proxy reverso controla solicitações que passam por ele; não protege outro caminho exposto nem o armazenamento abaixo dele. Plataformas hospedadas precisam de controles próprios de contas/aplicativos, sem presumir que se possa copiar o padrão de proxy local.

<a id="test-only-in-the-authorized-environment"></a>

## Testar somente no ambiente autorizado

Use repositório ou instância descartável com autorização separada, regras representativas e identidades distintas. Confirme dados de teste recuperáveis e operações que devem ser permitidas. Faça testes negativos somente nesses objetos descartáveis, com conteúdo inofensivo, e retenha evidências. Este documento não autoriza excluir repositórios de produção, reescrever histórico real nem alterar funções em uso.

<a id="acceptance-matrix"></a>

## Matriz de validação

| Capacidade/caminho | Resultado esperado para a identidade IA restrita | Evidência necessária |
| --- | --- | --- |
| Ler e preparar uma branch de trabalho permitida | Permitido no escopo | Controle positivo alcança o serviço pretendido com a identidade pretendida |
| Enviar commits comuns diretamente para main protegida | Negado pela política pretendida | Recusa real e referência protegida inalterada |
| Reescrever histórico protegido por force-push | Negado | Recusa de permissão e histórico inalterado |
| Excluir branch/referência protegida | Negado | Recusa real e referência ainda presente |
| Excluir repositório/projeto | Negado | Projeto descartável preservado; conta sem capacidade efetiva de exclusão |
| Aprovar em nome da pessoa exigida | Negado | Identidades de revisão e registro de autorização |
| Executar merge final, inclusive após aprovação | Negado sob a política de merge exclusivamente humano | Resultado real de permissão; uma PR não aprovada, sozinha, é teste insuficiente |
| Ativar/usar merge automático ou integração equivalente | Negado à IA neste fluxo | Caminho API/web/aplicativo e ator real registrados |
| Alterar funções, proteção, bypass ou verificações de segurança | Negado | Configuração antes/depois e recusa |
| Usar outra credencial, sessão, endpoint ou caminho CI | Sem autoridade involuntária | Inventário e teste delimitado por caminho relevante; caminhos desconhecidos seguem não verificados |
| Modificar host/contêiner/armazenamento do repositório | Sem acesso administrativo ou destrutivo | Evidência de fronteira do sistema/armazenamento, não apenas uma opção do aplicativo |
| Excluir/sobrescrever todos os pontos de recuperação | Negado à identidade de desenvolvimento | Retenção independente e separação da administração do backup |
| Pessoa revisa e executa o merge previsto | Permitido pela política de revisão | Controle positivo com a identidade humana real |

Examine criação de branches/tags, exclusão de tags e exceções por branch quando afetarem a política. Não bloqueie sem querer toda preparação enquanto declara sucesso na separação de responsabilidades.

<a id="record-each-result"></a>

## Registrar cada resultado

Para cada linha, retenha identidade de teste, identificação do software/configuração, origem/destino, operação e caminho, resultado esperado, resultado real/motivo, estado antes/depois, horário e localização da evidência. Remova credenciais e dados privados alheios antes de compartilhar.

Use **aprovado**, **reprovado** ou **não verificado**, com explicação. Timeout, falha de login, conflito, solicitação inválida, marcador WIP, servidor indisponível, captura de tela ou opção habilitada não provam que a permissão pretendida recusou a ação. Um controle positivo ajuda a separar aplicação da regra de um teste mal configurado.

Se um limite obrigatório falhar ou não for verificado, declare a lacuna. Diga quais operações estão realmente bloqueadas, sem alegar eliminar todo erro possível da IA. Repita testes afetados após mudanças em função, proxy, regra, versão ou integração; mantenha evidências anteriores com seu escopo original.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
