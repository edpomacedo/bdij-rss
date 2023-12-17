# bdij-rss

![doi:10.5281/zenodo.10397801](https://zenodo.org/badge/DOI/10.5281/zenodo.10397801.svg)

Ferramenta para compilação de notícias dos Tribunais que as publicam RSS.

## Estrutura

- `./main.py`: Rotina para extração de notícias de XMLs de RSS Feeds.

## Pré-requisitos

Utiliza as bibliotecas `beautifulsoup4`, `nltk` e `feedparser`.

## Instalação

```bash
git clone https://github.com/edpomacedo/bdij-rss.git
cd bdij-rss
python -m venv venv
.\venv\Scripts\activate
pip install beautifulsoup4 nltk feedparser
```

## Uso

1. Execute o comando `python main.py`.

As palavras mais recorrentes em uma notícia se tornarão um subdiretório dentro de `./feeds`.

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas alterações (`git commit -am 'Adicione uma nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Crie um novo Pull Request

## Licença

Copyright 2023 EDPO AUGUSTO FERREIRA MACEDO

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contato

[Base de Dados de Institutos Jurídicos](https://github.com/bdij)