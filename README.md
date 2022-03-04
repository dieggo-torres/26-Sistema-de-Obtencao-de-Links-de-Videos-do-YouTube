# [Profissional] Sistema de Obtenção de Links de Vídeos do YouTube

Neste projeto, criei um sistema que abre uma página do [Youtube](https://www.youtube.com/) usando uma URL personalizada para poder obter links de vídeos que correspondem aos resultados da busca.

Dado que o YouTube só carrega mais vídeos se rolarmos a página, precisei usar JavaScript para executar tal comando.

## Utilidade

Este projeto pode ser útil se você quiser, por exemplo, obter links de vídeos relacionados a uma palavra-chave nos quais você poderia fazer anúncios.

Ao fim de sua execução, o programa cria um arquivo CSV para organizar as informações obtidas. Carreguei o CSV que obtive para este repositório para que você possa ver a solução que este programa proporciona.

## Bibliotecas Usadas

Usei para este projeto as bibliotecas a seguir:

- os
- urllib
- time
- selenium
- dotenv
- pandas

## Arquivo .env

Crie seu próprio arquivo .env para listar as variáveis de ambiente da aplicação. Note que usei as seguintes variáveis:

- PALAVRA_CHAVE
- SELETOR_CSS_LINK_VIDEO
- SELETOR_CSS_TITULO_VIDEO
