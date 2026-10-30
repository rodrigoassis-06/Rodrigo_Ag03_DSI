
TOTAL_ENTREVISTADOS = 10

def main():
    print("=" * 10)
    print("  PESQUISA DE SATISFAÇÃO DE ATENDIMENTO - EMPRESA TUDOWEB  ")
    print("=" * 10)
    print(f"Total de participantes a serem entrevistados: {TOTAL_ENTREVISTADOS}\n")

    # Contadores de respostas
    total_excelente = 0
    total_bom = 0
    total_ruim = 0

    # Estrutura de repetição FOR para coletar os dados de cada entrevistado
    for i in range(1, TOTAL_ENTREVISTADOS + 1):
        print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
        
        # Coleta do nome e idade
        nome = input("Digite o nome: ").strip()
        
        while True:
            try:
                idade = int(input("Digite a idade: "))
                if idade > 0:
                    break
                print("Por favor, digite uma idade válida (maior que 0).")
            except ValueError:
                print("Valor inválido. Digite um número inteiro para a idade.")

        # Coleta e validação da opinião
        print("Opções de avaliação:")
        print("  1 - EXCELENTE")
        print("  2 - BOM")
        print("  3 - RUIM")

        while True:
            opiniao = input("Informe sua opinião (1, 2 ou 3): ").strip()
            
            # Estrutura de decisão para verificar e contabilizar a opinião
            if opiniao == "1":
                total_excelente += 1
                break
            elif opiniao == "2":
                total_bom += 1
                break
            elif opiniao == "3":
                total_ruim += 1
                break
            else:
                print("Opção inválida! Digite apenas 1 para EXCELENTE, 2 para BOM ou 3 para RUIM.")

    # Exibição dos resultados finais solicitados na atividade
    print("\n" + "=" * 10)
    print("             RESULTADO FINAL DA PESQUISA                   ")
    print("=" * 10)
    print(f"a) Quantidade de respostas 'EXCELENTE': {total_excelente}")
    print(f"b) Quantidade de respostas 'RUIM':      {total_ruim}")
    print(f"   Quantidade de respostas 'BOM':       {total_bom}")
    print(f"   Total de entrevistados:              {TOTAL_ENTREVISTADOS}")
    print("=" * 10)

if __name__ == "__main__":
    main()

