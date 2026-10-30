# Revisão de conteúdo público

[English](../en/public-content-review.md) · [简体中文](../zh-CN/public-content-review.md) · [日本語](../ja/public-content-review.md) · [Deutsch](../de/public-content-review.md) · [Français](../fr/public-content-review.md) · [Español](../es/public-content-review.md) · [Português (Brasil)](public-content-review.md) · [Русский](../ru/public-content-review.md)

[Página inicial Git Guard](../../README.pt-BR.md) · [Início rápido](README.md)

Rascunho de revisão 0.1. Procedimento reutilizável para projetos que publicam material. [Fluxo](workflow.md)

<a id="configure-the-public-content-check"></a>

## Configurar a verificação de conteúdo público

1. Identifique o projeto exato e os arquivos destinados à publicação. Mantenha registros internos, credenciais, configuração privada do scanner e diagnósticos fora dessa árvore. Se o diretório de desenvolvimento tiver material privado, revise uma cópia de publicação separada; não apague os originais privados só para aprovar um scan.
2. Localize o verificador nos fontes do Git Guard ou no snapshot de referência incluído na habilidade instalada. Ele exige Python 3.9 ou superior e a biblioteca padrão. Não se instala, inicia serviço nem impõe permissão de servidor. Defina o alvo explicitamente com `--root`; o diretório da habilidade instalada não é o projeto-alvo.
3. Use `--profile generic` em projetos que adotam o método. Use `--profile gitguard` apenas para aplicar também as exclusões específicas da estrutura pública/privada deste pacote. O verificador não tem lista personalizada de termos sensíveis nem substituição automática. Para segredos ou identificadores específicos da organização, use scanner separado adequado, com configuração privada fora da árvore publicada; veja [listas privadas](#sensitive-matching-lists-stay-private).
4. Revise arquivos de trabalho, bytes preparados e histórico de saída separadamente. Os caminhos abaixo são exemplos. Substitua o intervalo pelos commits realmente destinados ao envio; o verificador não faz fetch nem push. Sem repositório Git, comece pelos arquivos e confira índice/histórico quando existirem. Um resultado apenas da árvore de trabalho não certifica commits futuros.

```sh
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic --staged
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic --history origin/main..HEAD
```

<a id="interpret-results-and-handle-findings"></a>

## Interpretar resultados e tratar ocorrências

Saída **0** significa nenhuma ocorrência nas regras implementadas; **1**, ocorrências a revisar; **2**, verificação incompleta. Os relatórios exibem caminhos, categorias e linhas, não os valores secretos encontrados. O scan da árvore de trabalho inclui arquivos ignorados, exceto metadados Git: ignorar um arquivo não impede sua cópia acidental para uma publicação.

As regras sinalizam assinaturas de chaves privadas, alguns formatos de tokens GitHub, credenciais em URLs, caminhos de máquinas, endereços de rede privada, certos nomes privados/de execução e links Markdown relativos quebrados ou que saem do escopo. Não detectam toda senha ou identificação de conta. Binários exigem revisão manual; arquivos acima de 2.000.000 bytes não são inspecionados; o limite é 3.000 arquivos e 200 commits por intervalo de histórico. Revise escopos declarados maiores em partes, sem omiti-los silenciosamente.

Para cada ocorrência, registre categoria, local, decisão e nova verificação sem reproduzir valores sensíveis. Corrija a cópia pública ou as inclusões, ou justifique o resultado benigno/revisado manualmente; depois verifique novamente os escopos de trabalho, índice e histórico afetados. Não suprima globalmente avisos de binários ou tamanho. Exposição real de credenciais exige substituição e correção do histórico autorizada separadamente; o auxiliar não repara histórico nem apaga/substitui conteúdo. Timeout ou scan incompleto não é aprovação.

Para este pacote Git Guard, use primeiro `scripts/prepare_release.py` para criar uma cópia pública com escopo explícito. Os caches de desenvolvimento permanecem no local original; as exclusões são registradas separadamente. A opção `--media-review` lê um registro privado dos PNG/MP4 revisados individualmente, com seus SHA-256 exatos. Somente os avisos binários correspondentes são marcados como revisados e listados à parte; arquivos alterados, segredos, arquivos ilegíveis e limites de tamanho continuam pendentes. O código 0 pode incluir essas revisões documentadas, sem certificar automaticamente a privacidade. Consulte as [instruções de verificação e empacotamento](../../scripts/README.md).

<a id="before-a-local-commit"></a>

## Antes de um commit local

Revise os arquivos realmente alterados, inclusive não rastreados. Confirme propriedade e direitos de publicação. Remova do escopo público planos privados, caminhos de host/usuário, endereços internos, tokens, chaves privadas, credenciais, dados de clientes, capturas/logs brutos e fontes de produtos alheios. Exemplos usam nomes e valores genéricos.

Confira links, UTF-8, cobertura linguística efetiva, avisos de terceiros e precisão das alegações de conclusão. Site ou implantação planejada não deve ser anunciado como disponível. Evidências privadas ficam fora da árvore de publicação.

Inspecione separadamente os bytes preparados, pois podem diferir dos arquivos de trabalho. Revise renomeações/exclusões, binários, submódulos e links simbólicos; um documento visível limpo não comprova segurança de anexos incorporados. Commit local não autoriza publicação.

<a id="before-a-push"></a>

## Antes de um push

Liste os commits exatos de saída para o destino previsto e examine cada snapshot relevante, inclusive arquivos excluídos. Segredos anteriores permanecem no histórico após remoção posterior. Revise tags e outras referências apenas se fizerem parte do push proposto; um repositório novo não deve herdar histórico privado por acidente.

Se conteúdo sensível foi commitado, interrompa a publicação, providencie substituição apropriada de credenciais e correção aprovada separadamente. Não faça force-push nem exclua repositório silenciosamente para esconder a história. Scanners automáticos dão evidências de apoio, não provam a remoção de todo material privado.

<a id="reviewable-release"></a>

## Publicação que possa ser revisada

Registre destino, visibilidade, arquivos alterados, histórico de saída, decisão sobre direitos/licença, validação e limites restantes. Confirme a autorização existente para aquela ação exata. Preserve o merge final humano.

Se o repositório aponta para site oficial, verifique hostname, certificado HTTPS, marca e página real. Traduza o rótulo visível consistentemente em todos os READMEs, com o mesmo destino canônico. Confira o campo Website do repositório durante a publicação autorizada. O manual deve continuar útil independentemente do site.

<a id="evidence-levels"></a>

## Níveis de evidência

Distinga inspecionado, verificado estaticamente, testado em comportamento, implantado e confirmado pelo usuário. Captura de configuração, status de scanner ou transferência bem-sucedida não certificam segurança real nem restauração. Use a [especificação de validação](security-acceptance.md) para permissões.

<a id="sensitive-matching-lists-stay-private"></a>

## Listas sensíveis de correspondência ficam privadas

Publique apenas lógica reutilizável e dados de teste inventados. Segredos reais, identificadores de contas e listas de correspondência/substituição específicas ficam fora de fontes, pacotes de habilidades, downloads, capturas e histórico Git de saída. Uma regra com um valor privado exato também é sensível; estar em configuração de scanner não a torna publicável. Regras de ignorar não substituem a revisão do índice e do histórico.

Se usar outro scanner, como Gitleaks, com configuração privada, forneça o arquivo de um local privado durante a execução. Não copie para pacote público, não exiba valores encontrados nem use valores reais em argumentos de comando ou dados de teste. Guarde diagnósticos privadamente e remova conteúdo sensível antes de compartilhar.

O verificador incluído foi escrito especificamente para Git Guard. Não carrega lista privada existente nem reconhece especificamente contas de negociação/clientes, senhas arbitrárias ou todo tipo de token. As heurísticas genéricas complementam scanner apropriado e revisão humana; resultado limpo não significa ausência completa de segredos. Ele não limpa histórico.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
