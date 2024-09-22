import matplotlib.pyplot as plt
import numpy as np

def atualizar_grafico(dados, cores):
    plt.cla()
    plt.bar(range(len(dados)), dados, color=cores)
    plt.pause(0.001)

def particionar(dados, inicio, fim, atualizar_grafico_func):
    pivo = dados[fim]
    i = inicio - 1
    cores = ['maroon'] * len(dados)

    for j in range(inicio, fim):
        if dados[j] < pivo:
            i += 1
            dados[i], dados[j] = dados[j], dados[i]
            cores[i], cores[j] = 'purple', 'purple'
            atualizar_grafico_func(dados, cores)  
            cores[i], cores[j] = 'maroon', 'maroon'

    dados[i + 1], dados[fim] = dados[fim], dados[i + 1]
    atualizar_grafico_func(dados, ['maroon'] * len(dados))
    return i + 1

def quick_sort(dados, inicio, fim, atualizar_grafico_func):
    if inicio < fim:
        pi = particionar(dados, inicio, fim, atualizar_grafico_func)
        quick_sort(dados, inicio, pi - 1, atualizar_grafico_func)
        quick_sort(dados, pi + 1, fim, atualizar_grafico_func)

def visualizar_quick_sort(dados):
    plt.figure()
    plt.title("Visualização Quick Sort")
    plt.bar(range(len(dados)), dados, color='maroon')
    plt.pause(1)

    quick_sort(dados, 0, len(dados) - 1, atualizar_grafico)
    plt.show()

if __name__ == "__main__":
    np.random.seed(0)
    dados = np.random.randint(0, 70, 70)
    visualizar_quick_sort(dados)
