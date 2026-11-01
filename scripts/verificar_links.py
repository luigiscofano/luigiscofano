"""Confere arquivos e âncoras dos links Markdown locais usados neste perfil."""

from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit


RAIZ = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\s]+)\)")
CABECALHO = re.compile(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$")


def linhas_documentais(texto):
    """Ignora exemplos cercados por crases ou tils, preservando a numeração."""
    cerca = None
    for numero, linha in enumerate(texto.splitlines(), start=1):
        marcador = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", linha)
        if marcador:
            delimitador, restante = marcador.groups()
            if cerca is None:
                cerca = delimitador
            elif (delimitador[0] == cerca[0]
                  and len(delimitador) >= len(cerca) and not restante.strip()):
                cerca = None
            continue
        if cerca is None:
            yield numero, linha


def ancoras(texto):
    """Gera identificadores para os títulos ATX simples usados nos READMEs."""
    encontrados = set()
    for _, linha in linhas_documentais(texto):
        titulo = CABECALHO.match(linha)
        if not titulo:
            continue
        nome = re.sub(r"[*`_]", "", titulo.group(1)).lower()
        base = "".join(
            caractere for caractere in nome
            if caractere.isspace() or caractere in "-_"
            or unicodedata.category(caractere)[0] in "LNM"
        ).replace(" ", "-")
        identificador, repeticao = base, 0
        while identificador in encontrados:
            repeticao += 1
            identificador = f"{base}-{repeticao}"
        encontrados.add(identificador)
    return encontrados


def verificar(raiz):
    arquivos = sorted({
        *raiz.glob("*.md"),
        *(raiz / "docs").rglob("*.md"),
        *(raiz / "scripts").rglob("*.md"),
    })
    textos = {arquivo: arquivo.read_text(encoding="utf-8") for arquivo in arquivos}
    ids = {arquivo: ancoras(texto) for arquivo, texto in textos.items()}
    erros, conferidos = [], 0
    for arquivo, texto in textos.items():
        for numero, linha in linhas_documentais(texto):
            # O perfil usa links inline; URLs externas não precisam de rede.
            for link in LINK.finditer(linha):
                endereco = link.group(1)
                url = urlsplit(endereco)
                if url.scheme or url.netloc:
                    continue
                conferidos += 1
                caminho = unquote(url.path)
                destino = (arquivo.parent / caminho).resolve() if caminho else arquivo
                problema = None
                if not destino.is_relative_to(raiz):
                    problema = "caminho fora do repositório"
                elif not destino.exists():
                    problema = "arquivo ou pasta inexistente"
                elif url.fragment and destino.suffix.lower() == ".md":
                    if destino not in ids:
                        ids[destino] = ancoras(destino.read_text(encoding="utf-8"))
                    if unquote(url.fragment) not in ids[destino]:
                        problema = "âncora inexistente"
                if problema:
                    erros.append(f"{arquivo.relative_to(raiz)}:{numero}: {problema}: {endereco}")
    return len(arquivos), conferidos, erros


def main():
    arquivos, links, erros = verificar(RAIZ)
    for erro in erros:
        print(erro, file=sys.stderr)
    if erros:
        print(f"FALHA: {len(erros)} problema(s) em {links} links locais.", file=sys.stderr)
        return 1
    print(f"OK: {links} links locais em {arquivos} arquivos Markdown.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
