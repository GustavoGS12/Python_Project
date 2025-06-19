from csv import writer
from csv import reader
from random import randint


def adicionar_livro():

    with open('Livros.csv', 'w') as arquivo:
        escritor_csv = writer(arquivo)
        continuar = None
        escritor_csv.writerow(['Código', 'Título', 'Autor', 'Páginas'])
        while continuar != 'S':
            codigo = randint(1, 1000)
            livro = input('Qual o título?')
            autor = input('Qual o autor?')
            paginas = input('Quantas páginas?')
            escritor_csv.writerow([codigo, livro, autor, paginas])
            continuar = input('Deseja continuar? S/N').upper()


def excluir_livro():
    pass


def mostrar_lista():
    pass
