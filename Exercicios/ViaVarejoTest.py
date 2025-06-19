vetor1 = ["1111-1", "1111-2", "1111-3"]
vetor = ["2222-1", "2222-2"]

for produto in vetor:
    if produto != produto+1:
        print('este é o caminho')

    if int(produto[-1]) == len(vetor1):
        print(produto)
