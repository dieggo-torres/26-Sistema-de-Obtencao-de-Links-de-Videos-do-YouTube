# Importa o arquivo rotina.py
from rotina import esperar_elementos

# Biblioteca os
import os

# Importações da biblioteca selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Biblioteca urllib
import urllib

# Biblioteca time
import time

# Método da biblioteca python-dotenv
from dotenv import load_dotenv

# Biblioteca pandas
import pandas as pd

# Carrega as variáveis do arquivo .env
load_dotenv()

# Cria uma instância do Google Chrome
navegador = webdriver.Chrome()

# Recuperação e formatação da palavra-chave
palavra_chave = urllib.parse.quote(os.getenv('PALAVRA_CHAVE'))

# Define um parâmetro na URL do YouTube para fazer a busca
navegador.get(f'https://youtube.com/results?search_query={palavra_chave}')

# Espera 5s para que a página carregue os resultados da busca
time.sleep(5)

# Executa um script do JavaScript para rolar a página
for i in range(10):
    scroll = 5000 * i
    navegador.execute_script(f'window.scroll(0, {scroll});')

    # Aguarda 2s antes da próxima rolagem
    time.sleep(2)

# Obtém os links dos vídeos
videos = navegador.find_elements(
    By.CSS_SELECTOR,
    os.getenv('SELETOR_CSS_LINK_VIDEO')
)

# Obtém os títulos dos vídeos
titulos = navegador.find_elements(
    By.CSS_SELECTOR,
    os.getenv('SELETOR_CSS_TITULO_VIDEO')
)

# Espera pelo menos 50 elementos aparecerem
esperar_elementos(videos)

# Dicionário para armazenar as informações dos vídeos
videos_info = {}

# Percorre a lista de vídeos
for i, video in enumerate(videos):
    if video.get_attribute('href') and i < len(titulos):
        # Obtém as informações do vídeo
        link_video = video.get_attribute('href')
        titulo_video = titulos[i].text

        if titulo_video not in videos_info:
            # Cria uma nova entrada no dicionário
            videos_info[i] = [titulo_video, link_video]
        else:
            pass
else:
    pass

# Cria um dataframe a partir do dicionário
df_videos_info = pd.DataFrame.from_dict(videos_info, orient='index')

# Renomeia as colunas especificadas
df_videos_info.rename(columns={0: 'Título', 1: 'Link'}, inplace=True)

# Exporta o arquivo em formato .xlsx
df_videos_info.to_csv(
    'link-videos-yt.csv',
    sep=',',
    encoding='utf-8'
)
