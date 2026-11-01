# Manutenção dos links do perfil

Depois de alterar títulos, nomes de arquivos ou atalhos de navegação, execute na raiz do repositório:

```sh
python scripts/verificar_links.py
```

**Requisito:** Python 3.10 ou superior. O script usa somente a biblioteca padrão e não acessa a rede. A leitura do perfil no GitHub continua sem depender de Python.

O verificador percorre os arquivos Markdown da raiz, de `docs/` e de `scripts/`. Confere se arquivos e pastas relativos existem, se os caminhos permanecem no repositório e se âncoras apontam para títulos presentes. Exemplos em blocos de código são ignorados. Em caso de problema, mostra arquivo, linha e destino, e termina com código de saída 1; quando tudo passa, termina com 0.

## Escopo

Atende ao formato utilizado neste perfil: links inline sem espaços ou parênteses no destino e títulos ATX simples, iniciados por `#`. Considera Unicode e sufixos de títulos repetidos. Não é um parser completo de Markdown: links por referência, títulos com HTML ou formatação complexa e links escritos dentro de código inline precisam de revisão manual.

URLs externas, inclusive arquivos de outros repositórios, não são verificadas. Uma aprovação confirma os destinos locais reconhecidos pelo script; a disponibilidade dos projetos externos deve ser conferida separadamente.

[Perfil](../README.md) · [English](../README.en.md) · [Índice dos projetos](../docs/PROJETOS.md)
