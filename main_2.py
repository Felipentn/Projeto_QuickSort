import threading
import time
import os 

def troca(a, b):
    temp = a
    a = b
    b = temp

def particao(vet, inicio, fim):
    pivo = vet[fim]  # Seleciona o último elemento como pivô
    i = inicio - 1  # Inicializa um contador

    # Percorre o vetor da posição 'inicio' até a posição 'fim - 1'
    for j in range(inicio, fim):
        if vet[j] < pivo:  # Se o elemento atual for menor que o pivô
            i += 1  # Incrementa o contador
            troca(vet[i], vet[j])  # Troca os elementos nas posições 'i' e 'j'

    troca(vet[i + 1], vet[fim])  # Coloca o pivô na posição correta
    return i + 1  # Retorna a posição do pivô

def quicksort(vet, inicio, fim):
    if inicio < fim:  # Verifica se ainda há elementos para ordenar
        pivo = particao(vet, inicio, fim)

        # Cria uma nova thread para ordenar a primeira metade do vetor (antes do pivô)
        args1 = (vet, inicio, pivo - 1)
        thread1 = threading.Thread(target=quicksort, args=args1)
        thread1.start()

        # Cria uma nova thread para ordenar a segunda metade do vetor (após o pivô)
        args2 = (vet, pivo + 1, fim)
        thread2 = threading.Thread(target=quicksort, args=args2)
        thread2.start()

        thread1.join()  # Aguarda a conclusão da thread 1
        thread2.join()  # Aguarda a conclusão da thread 2

def ler_arquivo_txt(path):
    # Mapeia os caminhos dos arquivos com base em chaves
    nome_arquivo = {
        'path_1000' : f'{os.getcwd()}\\BaseTesteNumerosAleatorios\\1000NumerosAleatorios.txt',
        'path_10000' : f'{os.getcwd()}\\BaseTesteNumerosAleatorios\\10000NumerosAleatorios.txt',
        'path_100000' : f'{os.getcwd()}\\BaseTesteNumerosAleatorios\\100000NumerosAleatorios.txt'
    }
    
    with open(nome_arquivo[path], 'r') as arquivo:
        conteudo = arquivo.read()  # Lê o conteúdo do arquivo
    
    lista = conteudo.split(",")  # Divide o conteúdo em uma lista de números
    return lista

if __name__ == '__main__':
    vet = ler_arquivo_txt('path_1000')  # Lê o arquivo '100000NumerosAleatorios.txt'
    tam = len(vet)  # Obtém o comprimento do vetor

    start = time.time()  # Armazena o tempo de início da execução

    quicksort(vet, 0, tam - 1)  # Chama a função de ordenação Quicksort

    end = time.time()  # Armazena o tempo de término da execução

    delta = end - start  # Calcula o tempo de execução

    print("O vetor ordenado:")
    for i in range(tam):
        print(vet[i])  # Imprime os elementos ordenados do vetor

    print("Tempo de execução: {} segundos".format(delta))
