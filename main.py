import os
import feedparser
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tag import pos_tag
from bs4 import BeautifulSoup

def extrair_palavra_chave(texto):
    # Remover tags HTML usando BeautifulSoup
    soup = BeautifulSoup(texto, 'html.parser')
    texto_limpo = soup.get_text()

    # Tokenização e remoção de stop words
    tokens = word_tokenize(texto_limpo.lower())
    stop_words = set(stopwords.words("portuguese"))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]

    # Identificação da frequência das palavras
    frequencia = FreqDist(tokens)

    # Escolha da palavra mais frequente que não seja um determinante (DT) ou preposição (IN)
    palavra_chave = max(frequencia, key=lambda x: frequencia[x] if pos_tag([x])[0][1] not in ['DT', 'IN'] else 0)

    return palavra_chave

def limpar_html_para_markdown(texto_html):
    # Remover tags HTML usando BeautifulSoup
    soup = BeautifulSoup(texto_html, 'html.parser')
    texto_limpo = soup.get_text()
    return texto_limpo

def salvar_noticia_como_markdown(titulo, link, descricao, pubdate, content, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"---\n")
        arquivo.write(f"title: \"{titulo}\"\n")
        arquivo.write(f"link: \"{link}\"\n")
        arquivo.write(f"description: \"{descricao}\"\n")
        arquivo.write(f"pubdate: \"{pubdate}\"\n")
        arquivo.write(f"---\n\n")
        arquivo.write(f"## Conteúdo\n\n{content}\n")

def categorizar_noticias(feed_url, pasta_destino):
    # Verificar se a pasta de destino existe, caso contrário, criá-la
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Realizar a coleta de notícias
    feed = feedparser.parse(feed_url)

    # Iterar sobre as entradas do feed
    for i, entry in enumerate(feed.entries):
        titulo = entry.title
        link = entry.link
        descricao = entry.description
        pubdate = entry.published
        content = limpar_html_para_markdown(entry.content[0].value) if 'content' in entry else ""

        # Extrair a palavra-chave do texto da notícia
        palavra_chave = extrair_palavra_chave(descricao)

        # Criar o caminho da subpasta com base na palavra-chave
        subpasta = os.path.join(pasta_destino, palavra_chave)

        # Verificar se a subpasta existe, caso contrário, criá-la
        if not os.path.exists(subpasta):
            os.makedirs(subpasta)

        # Criar o caminho do arquivo com base no título da notícia
        caminho_arquivo = os.path.join(subpasta, f'noticia_{i + 1}.md')

        # Salvar a notícia no formato Markdown
        salvar_noticia_como_markdown(titulo, link, descricao, pubdate, content, caminho_arquivo)

if __name__ == "__main__":
    feed_url = "https://res.stj.jus.br/hrestp-c-portalp/RSS.xml"
    pasta_destino = "./feeds"

    categorizar_noticias(feed_url, pasta_destino)
