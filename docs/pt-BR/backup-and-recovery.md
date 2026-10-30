# Backup independente e recuperação

[English](../en/backup-and-recovery.md) · [简体中文](../zh-CN/backup-and-recovery.md) · [日本語](../ja/backup-and-recovery.md) · [Deutsch](../de/backup-and-recovery.md) · [Français](../fr/backup-and-recovery.md) · [Español](../es/backup-and-recovery.md) · [Português (Brasil)](backup-and-recovery.md) · [Русский](../ru/backup-and-recovery.md)

[Página inicial Git Guard](../../README.pt-BR.md) · [Início rápido](README.md)

Rascunho básico 0.1 — 2026-10-28.

Permissões e cópias recuperáveis tratam falhas diferentes. A base é sincronização automática para um dispositivo independente, verificações de integridade e pontos históricos protegidos. **Compilação e inicialização do aplicativo são opcionais**: escolha testes manuais, disparo separado ou automação adicional conforme o projeto.

<a id="personal-and-company-schedules"></a>

## Agendamento pessoal e empresarial

Uma pessoa pode ligar periodicamente um notebook secundário e deixar o gatilho configurado sincronizar os dados. Especifique se o gatilho é inicialização do sistema ou login; uma tarefa de login não executa antes de esse usuário entrar. Uma empresa pode usar um dispositivo independente disponível com agenda diária, tratamento de execuções perdidas, tentativas de rede limitadas, controle de concorrência e falhas visíveis.

São escolhas de implementação, não funções entregues pelo guia. Sua leitura não instala script nem tarefa agendada. Não dê à identidade IA de desenvolvimento autoridade para excluir todas as versões de recuperação nem administrar o dispositivo de backup.

<a id="define-what-the-copy-covers"></a>

## Definir a cobertura da cópia

Uma cópia de trabalho de main não é um backup completo do servidor. Declare cobertura de branches/histórico, trabalho apenas local ou sem commit, fontes/documentos, dependências necessárias, recursos de execução, configuração externa e projetos privados. Guarde segredos num processo de recuperação protegido adequadamente, nunca em exemplos públicos ou arquivo comum destinado a compartilhamento.

Dados do repositório e metadados da hospedagem Git são diferentes. Uma restauração completa auto-hospedada também pode exigir banco consistente, contas/permissões, issues/PRs, anexos, configuração e armazenamento. Teste recuperação do serviço separadamente da compilação do código.

Um espelho atualizado pode reproduzir exclusões. Mantenha pontos independentes e proteja a última versão conhecida como boa. Escolha retenção conforme a necessidade real; não apague cópias antigas automaticamente só porque uma transferência nova informou sucesso.

<a id="baseline-checks"></a>

## Verificações básicas

1. Confirme origem, revisão/escopo previsto, destino, identidade e espaço disponível. Preserve dados alheios.
2. Sincronize sem sobrescrever cópia alterada/divergente nem enviar mudanças de volta. Verifique igualdade exata com a revisão obtida pretendida; uma branch local adiantada pode parecer já atualizada.
3. Capture o escopo declarado de forma consistente, com identificador único de recuperação. Registre regras de inclusão/exclusão e arquivos obrigatórios.
4. Confira manifesto e hashes relevantes de fontes/arquivos/pacotes. Abrir um ZIP, contar arquivos ou calcular somente seu hash não prova que os fontes necessários foram incluídos. Falhas obrigatórias devem reprovar o resultado.
5. Guarde resultados duráveis e restaure periodicamente em destino separado e vazio. Identifique integridade e restauração separadamente; até que uma restauração ocorra, ela não está verificada.

<a id="optional-compilation-and-startup"></a>

## Compilação e inicialização opcionais

Se escolhidas, compile a cópia restaurada usando as ferramentas realmente compatíveis e um procedimento de build limpo. Registre configuração, cobertura, projetos não carregados/excluídos e dependências. Um diretório de restauração vazio não prova build limpo se o próprio pacote inclui saídas em cache. Não deixe arquivos não declarados da máquina original esconderem omissões.

Uma lição histórica útil: um backup pode incluir arquivos de projeto e omitir fontes necessários de fornecedores; compilar a cópia restaurada pode revelar essa falta. Mas compilar, por si só, não valida todos os documentos, recursos de execução, bancos de hospedagem ou caminhos da aplicação.

Opcionalmente, inicie o aplicativo restaurado e teste funções básicas em ambiente apropriado, evitando efeitos na produção. Para documentação ou conteúdo estático, escolha testes relevantes de links/conteúdo/site em vez de impor um compilador sem relação com o projeto.

Registre build/inicialização como **não selecionado**, **não verificado**, **aprovado** ou **reprovado**, conforme aplicável. Uma verificação opcional não selecionada não reprova o backup básico; uma transferência concluída também não deve ser chamada de validada por compilação.

<a id="if-validation-fails"></a>

## Se a validação falhar

Determine se a falha é omissão do backup, requisito do ambiente ou defeito do aplicativo. Corrija regras de inclusão ou ambiente declarado, crie novo ponto, restaure e repita verificações afetadas. Preserve a versão boa anterior e o registro da falha. Não sobrescreva evidências de falha silenciosamente nem declare um backup antigo reparado sem revalidá-lo.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
