
def main():
    print('1. Login')
    print('2. Resgistre-se')
    opcao =input('Escolha uma opção: ').strip()

    try:
        opcao = int(opcao)
    except Exception as e:
        print(f'Digite uma opção válida! (Numero inteiro)', str(e))

    match opcao:
        case 1:
            ...
        case 2:
            ...