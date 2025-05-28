cadastros = []

while True:
    usuario = {}
    nome = input("Qual o seu nome? ")
    usuario['nome'] = nome

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

    cadastros.append(usuario)

    continuar = input("Deseja cadastrar outro usuário? (sim/não): ").strip().lower()
    if continuar == 'não':
        break

print("\n--- Lista de Cadastros ---")
for i, usuario in enumerate(cadastros, start=1):
    print(f"\nUsuário {i}:")
    print(f"Nome: {usuario['nome']}")
    print(f"Cidade: {usuario['cidade']}")
    if usuario['transporte']:
        print("Transporte:")
        print(f"  Tipo: {usuario['transporte']['tipo']}")
        print(f"  Modelo: {usuario['transporte']['modelo']}")
        print(f"  Placa: {usuario['transporte']['placa']}")
    else:
        print("Transporte: Nenhum")
 