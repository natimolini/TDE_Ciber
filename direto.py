import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para inicializar a cache
def inicializar_cache(tamanho_cache):
    cache = {i: -1 for i in range(tamanho_cache)}
    return cache

# Função para imprimir o estado atual da cache
def imprimir_cache(cache, tree):
    for i in tree.get_children():
        tree.delete(i)
    for posicao_cache, posicao_memoria in cache.items():
        tree.insert('', 'end', values=(posicao_cache, posicao_memoria))

# Função para o mapeamento direto
def mapeamento_direto(tamanho_cache, pos_memoria, output_text, tree):
    cache = inicializar_cache(tamanho_cache)
    imprimir_cache(cache, tree)

    hits = 0
    misses = 0

    for posicao in pos_memoria:
        posicao_cache = posicao % tamanho_cache
        if cache[posicao_cache] == posicao:
            hits += 1
            output_text.insert(tk.END, f"Hit: Posição de memória {posicao} encontrada na posição de cache {posicao_cache}\n", 'hit')
        else:
            misses += 1
            output_text.insert(tk.END, f"Miss: Posição de memória {posicao} não encontrada na posição de cache {posicao_cache}\n", 'miss')
            cache[posicao_cache] = posicao
        imprimir_cache(cache, tree)

    total_acessos = len(pos_memoria)
    output_text.insert(tk.END, f"\nResumo:\n", 'summary')
    output_text.insert(tk.END, f"Total de posições de memórias acessadas: {total_acessos}\n", 'summary')
    output_text.insert(tk.END, f"Total de hits: {hits}\n", 'summary')
    output_text.insert(tk.END, f"Total de misses: {misses}\n", 'summary')
    taxa_cache_hit = (hits / total_acessos) * 100 if total_acessos > 0 else 0
    output_text.insert(tk.END, f"Taxa de cache hit: {taxa_cache_hit:.2f}%\n", 'summary')

# Função para iniciar o mapeamento a partir da interface gráfica
def iniciar_mapeamento():
    try:
        tamanho_cache = int(entry_tamanho_cache.get())
        pos_memoria = list(map(int, entry_pos_memoria.get().split()))
        output_text.delete("1.0", tk.END)
        mapeamento_direto(tamanho_cache, pos_memoria, output_text, tree)
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Entrada inválida! Certifique-se de digitar números inteiros.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Simulador de Memória Cache Por Mapeamento Direto")

# Definindo estilo
style = ttk.Style()
style.configure("TFrame", padding="10")
style.configure("TButton", padding="5", relief="raised")
style.configure("TLabel", padding="5", background="lightgrey")
style.configure("Treeview.Heading", background="grey", foreground="black", font=('Helvetica', 10, 'bold'))
style.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white", font=('Helvetica', 10))
style.map("Treeview", background=[('selected', 'lightblue')], foreground=[('selected', 'black')])

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_titulo = ttk.Label(frame, text="Simulador de Memória Cache Por Mapeamento Direto", font=('Helvetica', 14, 'bold'))
label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 10))

label_tamanho_cache = ttk.Label(frame, text="Tamanho da Cache:")
label_tamanho_cache.grid(row=1, column=0, sticky=tk.W, pady=5)

entry_tamanho_cache = ttk.Entry(frame)
entry_tamanho_cache.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

label_pos_memoria = ttk.Label(frame, text="Posições de Memória (separadas por espaços):")
label_pos_memoria.grid(row=2, column=0, sticky=tk.W, pady=5)

entry_pos_memoria = ttk.Entry(frame)
entry_pos_memoria.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

button_iniciar = ttk.Button(frame, text="Iniciar Mapeamento", command=iniciar_mapeamento)
button_iniciar.grid(row=3, column=0, columnspan=2, pady=10)

output_text = tk.Text(frame, width=50, height=10, wrap='word', background='white', foreground='black', font=('Helvetica', 10))
output_text.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)

# Configuração da tabela
tree = ttk.Treeview(frame, columns=('Posição Cache', 'Posição Memória'), show='headings')
tree.heading('Posição Cache', text='Posição Cache')
tree.heading('Posição Memória', text='Posição Memória')
tree.column('Posição Cache', width=150)
tree.column('Posição Memória', width=150)
tree.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)

# Configurando tags de texto
output_text.tag_configure('hit', foreground='green')
output_text.tag_configure('miss', foreground='red')
output_text.tag_configure('summary', background='white', foreground='black')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()


