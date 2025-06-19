import smtplib
import email.message
import pygame
import sys
from time import sleep


def enviar_email():

    corpo_email = f"""
                    <p> Ola Ben 10 </p>
                    <p> Lindo </p>
                    <p> Teste do codigo </p> """
    msg = email.message.Message()
    msg['Subject'] = "Email automatico"
    msg['From'] = "testeg.dev@outlook.com"
    msg['TO'] = "rh470723@gmail.com"
    password = 'gu521478029'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.outlook.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado com sucesso')
    pass


def notificacao():
    pygame.init()
    titulo = 'Confira o email'
    texto = 'Por favor, entre no email'
    x, y = 600, 500
    bg_color, text_color = (255, 0, 0), (229, 235, 52)
    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption(titulo)
    font = pygame.font.Font('freesansbold.ttf', 42)
    msg = font.render(texto, True, text_color)
    msg_rect = msg.get_rect()
    msg_rect.center = (x // 2, y // 2)
    while True:
        screen.fill(bg_color)
        screen.blit(msg, msg_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
    pass

#enviar_email()

#sleep(1800)

notificacao()
