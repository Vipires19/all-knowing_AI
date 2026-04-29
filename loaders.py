import os
from time import sleep
import streamlit as st
from langchain_community.document_loaders import (WebBaseLoader,
                                                  YoutubeLoader, 
                                                  CSVLoader, 
                                                  PyPDFLoader, 
                                                  TextLoader,
                                                  UnstructuredExcelLoader)
from youtube_transcript_api import YouTubeTranscriptApi

from fake_useragent import UserAgent

def carrega_site(url):
    documento = ''
    for i in range(5):
        try:
            os.environ['USER_AGENT'] = UserAgent().random
            loader = WebBaseLoader(url, raise_for_status=True)
            lista_documentos = loader.load()
            documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
            break
        except:
            print(f'Erro ao carregar o site {i+1}')
            sleep(3)
    if documento == '':
        st.error('Não foi possível carregar o site')
        st.stop()
    return documento

def carrega_youtube(video_id):
    try:
        # valida se existe transcript
        YouTubeTranscriptApi.list_transcripts(video_id)

        loader = YoutubeLoader(
            video_id,
            add_video_info=False,
            language=['pt', 'en']  # fallback inteligente
        )

        lista_documentos = loader.load()

        if not lista_documentos:
            raise ValueError("Sem conteúdo no vídeo")

        documento = '\n\n'.join([doc.page_content for doc in lista_documentos])

        if not documento.strip():
            raise ValueError("Transcript vazio")

        return documento

    except Exception as e:
        st.error(f"Erro ao carregar vídeo: {str(e)}")
        st.stop()

def carrega_csv(caminho):
    loader = CSVLoader(caminho)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento

def carrega_xlsx(caminho):
    loader = UnstructuredExcelLoader(caminho)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento

def carrega_pdf(caminho):
    loader = PyPDFLoader(caminho)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento

def carrega_txt(caminho):
    loader = TextLoader(caminho)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento
