import json
import random

import telegram
import telebot

dados = {1: ['Would You Ever',
             'Would_You_Ever.jpg',
             'https://open.spotify.com/track/57p8CBvPOxrvyCbn6ttl5r?si=a5c664c550e54916',
             'https://www.youtube.com/watch?v=r-SurvChGFk'],
         2: ['Castle of Glass',
             'Castle_of_Glass.jpg',
             'https://open.spotify.com/track/1r1fPuhj9H4VdXr7OK6FL5?si=f813e6ec2b5149ad',
             'https://www.youtube.com/watch?v=ScNNfyq3d_w']}

key = random.randint(0, (len(dados)-1))
print(key)


class TelegramBot:

    def __init__(self):
        token = '5523685150:AAGrNtrSqGV1wWZeVxdQiLxCB0kcbVDaAcE'
        self.url_base = f"t.me/Song_of_day_bot{token}/"

    def music(self):
        pass


class Musica:
    def __init__(self):
        self.nome = dados[key][0]
        self.foto = dados[key][1]
        self.linkA = dados[key][2]
        self.linkB = dados[key][3]
