import speech_recognition as sr
import pyttsx3
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import wikipedia
import os
#import PyAudio
audio = sr.Recognizer()
maquina = pyttsx3.init()
os.environ['SPOTIPY_CLIENT_ID'] = '5c416155fed34c9cbbf19f7ce9ebe464'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'c88431b0e25d4396905f86bcb5a5c354'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://example.com/callback'

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))


def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'lica' in comando:
                comando = comando.replace('lica', '')
                maquina.runAndWait()
    except:
        print('Microfone não funfa')
        maquina.say('Nao entendi')

    return comando


def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = sp.search(musica, 1, 0, "track")
        nome_artista = resultado['tracks']['items'][0]['artists'][0]['name']
        nome_musica = resultado['tracks']['items'][0]['name']
        track_uri = resultado['tracks']['items'][0]['uri']
        maquina.say(f'Tocando {nome_musica} de {nome_artista}')
        maquina.runAndWait()
        sp.start_playback(uris=[track_uri])


comando_voz_usuario()