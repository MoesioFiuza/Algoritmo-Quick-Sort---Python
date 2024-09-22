import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def atualizar_grafico(frame, dados, cores):
    plt.cla()
    plt.bar(range(len(dados)), dados, color=cores)

def particionar(dados, inicio, fim, atualizar_grafico_func):
    pivo = dados[fim]
    i = inicio - 1
    cores = ['maroon'] * len(dados)

    for j in range(inicio, fim):
        if dados[j] < pivo:
            i += 1
            dados[i], dados[j] = dados[j], dados[i]
            cores[i], cores[j] = 'purple', 'purple'
            yield dados, cores 
            cores[i], cores[j] = 'maroon', 'maroon'

    dados[i + 1], dados[fim] = dados[fim], dados[i + 1]
    yield dados, ['maroon'] * len(dados)  

def quick_sort(dados, inicio, fim, atualizar_grafico_func):
    if inicio < fim:
        pi = particionar(dados, inicio, fim, atualizar_grafico_func)
        for frame in pi:
            yield frame
        yield from quick_sort(dados, inicio, pi - 1, atualizar_grafico_func)
        yield from quick_sort(dados, pi + 1, fim, atualizar_grafico_func)

def visualizar_quick_sort(dados):
    fig, ax = plt.subplots()
    ax.set_title("Visualização Quick Sort")

    def update(frame):
        dados, cores = frame
        atualizar_grafico(dados, cores)

    ani = animation.FuncAnimation(fig, update, frames=quick_sort(dados, 0, len(dados) - 1, atualizar_grafico), interval=50)
    plt.show()

if __name__ == "__main__":
    np.random.seed(0)
    dados = np.random.randint(0, 100, 100)
    visualizar_quick_sort(dados)
