# Fluxo diário de trabalho com Git

[English](../en/workflow.md) · [简体中文](../zh-CN/workflow.md) · [日本語](../ja/workflow.md) · [Deutsch](../de/workflow.md) · [Français](../fr/workflow.md) · [Español](../es/workflow.md) · [Português (Brasil)](workflow.md) · [Русский](../ru/workflow.md)

[Página inicial Git Guard](../../README.pt-BR.md) · [Início rápido](README.md)

Rascunho básico 0.1 — 2026-10-28.

<a id="read-and-scope-the-work"></a>

## Ler as instruções e delimitar o trabalho

Identifique exatamente projeto, diretório local, branch, remoto, visibilidade e autorização atual. Leia a entrada de instruções do agente, o plano vigente e os procedimentos relevantes. Preserve alterações alheias à tarefa, preparadas ou não. Editar, fazer commit, enviar por push, criar uma PR, publicar uma versão e implantar um site são ações distintas; mantenha as autorizações realmente concedidas sem tratar um plano geral como permissão para todas elas.

<a id="step-1--record-the-local-change"></a>

## Etapa 1 — registrar a alteração local

Revise a lista de arquivos alterados e as diferenças. Execute verificações adequadas à mudança. Para material público, conclua a [revisão de publicação](public-content-review.md) **antes do commit**, mesmo que ele fique inicialmente local. Prepare apenas os arquivos previstos e faça o commit local autorizado. Confira sua identificação, seu conteúdo e as alterações restantes na árvore de trabalho.

Um commit local não envia o trabalho. Não inicialize outro repositório, adicione remoto, altere proteções nem crie tarefa de backup implicitamente durante uma edição comum. Não descarte alterações alheias para obter um estado limpo.

<a id="step-2--share-the-branch-and-prepare-the-pr"></a>

## Etapa 2 — compartilhar a branch e preparar a PR

Dentro da autorização atual, verifique o destino remoto e toda a diferença da branch em relação ao alvo real. Inclua commits anteriores ainda não integrados na análise de escopo, não apenas o último. Confira novamente o limite do conteúdo público antes de qualquer envio.

Envie a branch de trabalho autorizada sem forçar. No exemplo padrão da página inicial e da animação, prepare origem/destino corretos, sugestão de título e descrição e resultados reais de validação para a pessoa criar a solicitação na interface web. Não descreva um formulário preparado como uma PR já criada.

Quem adota o método pode autorizar separadamente a IA a criar ou atualizar a PR correspondente. Só então realize a ação e confirme sua existência e estado reais. Essa variante não concede autoridade de merge final. Uma branch enviada ou PR em rascunho num repositório público já expõe seu conteúdo; ele não fica privado até o merge.

Se uma política ou permissão bloquear a ação, informe a recusa real. Não contorne usando sessão administrativa, outro token, porta direta do servidor, acesso a contêiner ou outra interface. Resolver um conflito de conteúdo não amplia silenciosamente a ação permitida.

<a id="human-final-review-and-merge"></a>

## Revisão e merge finais pela pessoa

No exemplo padrão, abra a página de solicitações do repositório no OneDev/GitHub, inicie uma nova solicitação, confira origem e destino sugeridos, preencha título e descrição e envie. Se já existir uma solicitação criada sob autorização separada, examine-a sem duplicar. Sugestões de branches padrão não equivalem a aprovação.

A pessoa revisa toda a diferença, evidências de teste, destino e resultado pretendido, e então faz o merge final. Neste fluxo, a IA não clica em merge, não chama API/CLI de merge nem ativa merge automático em nome da pessoa.

Revisão obrigatória e autoridade exclusiva de merge humano são controles diferentes. Uma revisão aprovada ainda pode deixar a identidade IA capaz de integrar. Valide ambos antes de descrever o fluxo como tecnicamente imposto. Proteja também credenciais administrativas e sessões web existentes, além da conta do bot.

<a id="after-the-human-confirms-merge"></a>

## Depois que a pessoa confirmar o merge

1. Verifique o merge real no servidor e seu destino. Uma instrução para preparar a PR não é uma confirmação de merge.
2. Busque as referências e compare a alteração revisada com o resultado integrado. Squash/rebase podem alterar IDs de commits; quando o destino avançou, compare a base adequada e o diff resultante em vez de exigir árvores completas idênticas. Para squash sobre a mesma base, árvores finais equivalentes são evidência útil.
3. Antes da limpeza, procure trabalho sem commit, commits não publicados, outras árvores de trabalho e o procedimento de recuperação/retenção aplicável. Não crie backup não solicitado nem sobrescreva trabalho apenas local para forçar alinhamento.
4. Avance a branch protegida local por fast-forward quando a relação com o remoto permitir. Pare e explique divergências em vez de apagá-las com reset.
5. Remova somente a branch de trabalho comprovadamente concluída, dentro da autorização de limpeza. Se o servidor já a excluiu, elimine a referência de rastreamento obsoleta sem recriá-la. Um squash pode não satisfazer um teste de exclusão baseado apenas em ancestralidade; confira conteúdo e evidências do trabalho preservado antes de uma alternativa autorizada.
6. Informe o estado real das branches/árvores de trabalho, qualquer trabalho mantido e problemas pendentes. Limpeza local não equivale a implantação nem publicação de versão.

<a id="keep-the-rules-portable"></a>

## Manter as regras adaptáveis

O proprietário define convenções de nomes e revisão. OneDev e GitHub têm controles e modelos de contas diferentes; a sequência compartilhada permanece. Use a [validação de segurança](security-acceptance.md) para separar política pretendida de limites verificados, e a [correspondência GitHub](github.md) para as diferenças resumidas da plataforma.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
