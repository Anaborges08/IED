nomes = []
usuarios = []

while True:
    usuario = {}

    nome = input("Qual o seu nome? ")
    usuario['nome'] = nome
    nomes.append(nome)

    cidade = input("De que cidade você é? ")
    usuario['cidade'] = cidade

    tem_transporte = input("Você tem algum transporte? (sim/não): ").strip().lower()

    if tem_transporte == 'sim':
        tipo = input("Qual o tipo do transporte (ex: carro, moto, bicicleta, ônibus): ")
        modelo = input("Qual o modelo do transporte: ")
        placa = input("Qual a placa do transporte: ")

        usuario['transporte'] = {
            'tipo': tipo,
            'modelo': modelo,
            'placa': placa
        }
    else:
        usuario['transporte'] = None

    usuarios.append(usuario)

    continuar = input("Deseja cadastrar outro usuário? (sim/não): ").strip().lower()
    if continuar == 'não':
        break

print("\nUsuários:")
for usuario in usuarios:
    print([usuario]) 
