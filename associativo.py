import tkinter as tk
from tkinter import ttk
from collections import defaultdict, deque

# Função para inicializar a cache
def inicializar_cache(num_conjuntos, num_blocos_por_conjunto):
    cache = defaultdict(lambda: deque(maxlen=num_blocos_por_conjunto))
    return cache

# Função para imprimir o estado atual da cache
def imprimir_cache(cache):
    cache_str = ""
    for conjunto, blocos in cache.items():
        cache_str += f"Conjunto {conjunto}:\n"
        for indice, valor in enumerate(blocos):
            lru = "(LRU)" if indice == 0 else ""
            cache_str += f"    Linha {indice}: {valor} {lru}\n"
    return cache_str

# Função para o mapeamento associativo por conjunto com política LRU
def mapeamento_associativo_conjunto_lru(pos_memoria, num_conjuntos, num_blocos_por_conjunto):
    cache = inicializar_cache(num_conjuntos, num_blocos_por_conjunto)
    output_str = imprimir_cache(cache) + "\n"

    hits = 0
    misses = 0

    for posicao in pos_memoria:
        conjunto = posicao % num_conjuntos
        if posicao in cache[conjunto]:
            hits += 1
            cache[conjunto].remove(posicao)
            cache[conjunto].append(posicao)  # Move o bloco para o final da fila (mais recentemente usado)
            output_str += f"Hit: Posição de memória {posicao} encontrada no conjunto {conjunto}\n"
        else:
            misses += 1
            if len(cache[conjunto]) == num_blocos_por_conjunto:
                cache[conjunto].popleft()  # Remove o bloco mais antigo do conjunto
            cache[conjunto].append(posicao)
            output_str += f"Miss: Posição de memória {posicao} não encontrada no conjunto {conjunto}\n"
        output_str += imprimir_cache(cache) + "\n"

    total_acessos = len(pos_memoria)
    output_str += "\nResumo:\n"
    output_str += f"Total de posições de memórias acessadas: {total_acessos}\n"
    output_str += f"Total de hits: {hits}\n"
    output_str += f"Total de misses: {misses}\n"
    taxa_cache_hit = (hits / total_acessos) * 100 if total_acessos > 0 else 0
    output_str += f"Taxa de cache hit: {taxa_cache_hit:.2f}%\n"

    return output_str

# Função para iniciar o mapeamento a partir da interface gráfica
def iniciar_mapeamento():
    try:
        pos_memoria = list(map(int, entry_pos_memoria.get().split()))
        num_conjuntos = int(entry_num_conjuntos.get())
        num_blocos_por_conjunto = int(entry_num_blocos_por_conjunto.get())
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, mapeamento_associativo_conjunto_lru(pos_memoria, num_conjuntos, num_blocos_por_conjunto))
    except ValueError:
        output_text.insert(tk.END, "Erro: Por favor, insira números inteiros válidos.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Simulador de Memória Cache Por Mapeamento Associativo por conjunto")

# Estilo
style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0")
style.configure("TButton", background="#007bff", foreground="white", font=('Helvetica', 12, 'bold'))
style.map("TButton", background=[('active', '#0056b3')])
style.configure("Red.TLabel", foreground="red")
style.configure("Green.TLabel", foreground="green")

# Frames
frame_input = ttk.Frame(root, padding="20")
frame_input.grid(row=0, column=0, sticky="nsew")

frame_output = ttk.Frame(root, padding="20")
frame_output.grid(row=1, column=0, sticky="nsew")

# Labels e Entradas
label_pos_memoria = ttk.Label(frame_input, text="Posições de Memória (separadas por espaços):")
label_pos_memoria.grid(row=0, column=0, padx=10, pady=5)

entry_pos_memoria = ttk.Entry(frame_input, width=50)
entry_pos_memoria.grid(row=0, column=1, padx=10, pady=5)

label_num_conjuntos = ttk.Label(frame_input, text="Número de Conjuntos:")
label_num_conjuntos.grid(row=1, column=0, padx=10, pady=5)

entry_num_conjuntos = ttk.Entry(frame_input)
entry_num_conjuntos.grid(row=1, column=1, padx=10, pady=5)

label_num_blocos_por_conjunto = ttk.Label(frame_input, text="Número de Blocos por Conjunto:")
label_num_blocos_por_conjunto.grid(row=2, column=0, padx=10, pady=5)

entry_num_blocos_por_conjunto = ttk.Entry(frame_input)
entry_num_blocos_por_conjunto.grid(row=2, column=1, padx=10, pady=5)

# Botão para iniciar o mapeamento
button_iniciar = ttk.Button(frame_input, text="Iniciar Mapeamento", command=iniciar_mapeamento)
button_iniciar.grid(row=3, columnspan=2, pady=10)

# Texto de saída
output_text = tk.Text(frame_output, width=80, height=20, wrap="word", font=('Helvetica', 10))
output_text.grid(row=0, column=0, padx=10, pady=5)

# Scrollbar para o texto de saída
scrollbar = ttk.Scrollbar(frame_output, orient="vertical", command=output_text.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
output_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
