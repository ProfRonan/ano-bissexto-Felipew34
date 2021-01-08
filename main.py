"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    a = int(input("Ano:"))
    if a%4==0 and a%100!=0:
      print(f"O ano [a] é bissexto.")
    elif a%400==0:
      print(f"O ano [a] é bissexto.")
    else:
      print(f"O ano [a] não é bissexto.")      
            

if __name__ == '__main__':
    main()
