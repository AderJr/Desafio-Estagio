# Para resolver esse probelma eu usei de um princípio matemático envolvendo logaritmos. O princípio basicamente mostra que qualquer número logaritmizado a uma base 10
#  resultará em um valor aproximado (acontece quando não múltiplo de 10, onde nesses casos deve-se arredondar o resultado para baixo e somar 1) ou exato da quantidade
#   de digitos/algarismos que aquele número possui. Segue a linha de raciocínio por partes...

# Primeiramente eu adicionei a biblioteca matemática para poder usar os logaritmos;
import math

# Depois crio uma função de tudo;
def achar_digitos_Fibonacci():
    # Aqui adiciono algumas variáveis de inicialização, como...
    
    # Variável bool para o laço de repetição posterior;
    verdadeiro = False
    
    # Dois números de entrada para realizar as somas necessários para Fibonacci e o atual e atribuí a todos o valor 1 (x-1 + x-2 = x);
    numI = 1
    numF = 1
    numAtual = 1
    
    # Essa será a variável de contagem do índice ou posição de Fibonnaci (2 por que já temos o numI e numF representando as duas primeiras casas);
    indFibonacci = 2
    
    # E essa é a variável de controle do número de digitos requisitado;
    numDigitsMin = 1000
    
    # Aqui que a mágica começa :);
    while not verdadeiro:
        # Primeiro eu coloquei um sisteminha simples de atualização das casas anteriores e coloquei a fórmula para achar o valor atual;
        numI = numF
        numF = numAtual
        numAtual = numI + numF
        
        # Essa será a contagem do índice, irá parar quando achar o número requisitado;
        indFibonacci = indFibonacci + 1
        
        # Aqui temos a aplicação das funções matemáticas de arredondamento e logaritmo de base 10 com o número atual. A soma de 1 para casos de não múltiplos de 10;
        numDigits = math.floor(math.log(numAtual, 10) + 1)
        
        # Condicional que verifica se atingimos o número esperado, caso achado só trocamos o nosso valor booleando para sair do laço de repetição;
        if numDigits >= numDigitsMin:
            verdadeiro = True

    # Aqui, eu apenas atribui uma formatação de String a uma variável para mostrar um print mais bonitinho;
    resultado = f'''
    Número buscado: {numAtual}
    Número de dígitos: {numDigits}
    Índice de Fibonacci: {indFibonacci}'''
    print(resultado)

# E, por último mas não menos importante, eu executei a função para mostrar o código;
achar_digitos_Fibonacci()

# Como consideração final, digo que gostei muito do desafio e espero ter muitos outros junto a vocês ;)
