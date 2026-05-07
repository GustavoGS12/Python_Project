import sqlite3
from PIL import Image, ImageDraw, ImageFont
import os
import re
import sys

# Configuração de pastas
diretorio_projeto = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(diretorio_projeto, "cartoes"), exist_ok=True)

# Banco de dados
conn = sqlite3.connect(os.path.join(diretorio_projeto, "clientes.db"))
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL, 
    telefone TEXT NOT NULL
)
""")
conn.commit()

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = (soma * 10 % 11) % 10
        if digito != int(cpf[i]):
            return False
    return True

def input_cancelavel(prompt):
    """Lê a entrada e permite sair do programa se digitar 'sair' ou der Ctrl+C."""
    try:
        entrada = input(prompt).strip()
        if entrada.lower() == 'sair':
            print("\n👋 Encerrando o sistema...")
            conn.close()
            sys.exit()
        return entrada
    except KeyboardInterrupt: # Atalho Ctrl+C
        print("\n\n👋 Interrupção detectada. Saindo...")
        conn.close()
        sys.exit()

def cadastrar_cliente(nome, cpf, telefone):
    cpf_limpo = re.sub(r'\D', '', cpf)
    try:
        cursor.execute(
            "INSERT INTO clientes (nome, cpf, telefone) VALUES (?, ?, ?)",
            (nome, cpf_limpo, telefone)
        )
        conn.commit()
        cliente_id = cursor.lastrowid
        gerar_cartao(nome, cliente_id)
        return True
    except sqlite3.IntegrityError:
        print(f"\n⚠️  Erro: O CPF {cpf} já está cadastrado.")
        return False

def gerar_cartao(nome, cliente_id):
    caminho_imagem = os.path.join(diretorio_projeto, "Cliente de Honra.png")
    if not os.path.exists(caminho_imagem):
        print(f"❌ Erro: Imagem de fundo não encontrada.")
        return

    imagem = Image.open(caminho_imagem).convert("RGB")
    draw = ImageDraw.Draw(imagem)

    try:
        fonte_nome = ImageFont.truetype("arial.ttf", 40)
        fonte_id = ImageFont.truetype("arial.ttf", 25)
    except:
        fonte_nome = ImageFont.load_default()
        fonte_id = ImageFont.load_default()

    draw.text((100, 300), nome.upper(), fill=(212, 175, 55), font=fonte_nome)
    draw.text((110, 345), f"ID: {cliente_id:04d}", fill="lightgray", font=fonte_id)

    nome_arquivo = nome.replace(" ", "_").lower()
    caminho_salvamento = os.path.join(diretorio_projeto, "cartoes", f"cartao_{nome_arquivo}.png")
    imagem.save(caminho_salvamento)
    print(f"✅ Cartão gerado: {nome_arquivo}.png")

# ===== Loop Principal de Cadastro =====
if __name__ == "__main__":
    print("="*40)
    print("SISTEMA CLIENTE DE HONRA LOUVADA")
    print("Digite 'sair' a qualquer momento para encerrar.")
    print("="*40)

    while True:
        print("\n--- Novo Cadastro ---")
        nome = input_cancelavel("Nome completo: ")
        
        while not nome:
            nome = input_cancelavel("O nome é obrigatório: ")

        while True:
            cpf = input_cancelavel("CPF (somente números): ")
            if validar_cpf(cpf):
                break
            
            print("❌ CPF inválido. Tente novamente.")

        telefone = input_cancelavel("Telefone: ")
        
        cadastrar_cliente(nome, cpf, telefone)
        print("-" * 30)