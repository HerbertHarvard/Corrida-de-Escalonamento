import tkinter as tk
from PIL import Image, ImageTk
import random

class Processo:
    def __init__(self, nome, tempo_execucao, prioridade, imagem):
        self.nome = nome
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade
        self.imagem = imagem
        self.progresso = 0

def iniciar_interface():
    root = tk.Tk()
    root.title("Corrida de Processos - Of Monsters and Men")
    root.geometry("900x600")

    imagem_fundo = Image.open("dirtypaws.png")
    imagem_fundo = imagem_fundo.resize((900, 600))
    imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

    label_fundo = tk.Label(root, image=imagem_fundo)
    label_fundo.image = imagem_fundo
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

    titulo = tk.Label(root, text="Corrida de Processos", font=("Arial", 20, "bold"), bg="white")
    titulo.pack(pady=10)

    escolha_label = tk.Label(root, text="Escolha a política de escalonamento:", font=("Arial", 12), bg="white")
    escolha_label.pack()

    escolha_var = tk.StringVar(value="Round Robin")
    fifo_radio = tk.Radiobutton(root, text="FIFO", variable=escolha_var, value="FIFO", bg="white")
    fifo_radio.pack()
    rr_radio = tk.Radiobutton(root, text="Round Robin", variable=escolha_var, value="Round Robin", bg="white")
    rr_radio.pack()

    quantum_label = tk.Label(root, text="Defina o Quantum (Round Robin):", font=("Arial", 12), bg="white")
    quantum_label.pack()
    quantum_entry = tk.Entry(root, font=("Arial", 12))
    quantum_entry.pack()

    botao_iniciar = tk.Button(root, text="Iniciar Corrida", font=("Arial", 14),
                              command=lambda: iniciar_corrida(root, escolha_var.get(), quantum_entry))
    botao_iniciar.pack(pady=10)

    botao_limpar = tk.Button(root, text="Limpar Corrida", font=("Arial", 14),
                             command=lambda: limpar_corrida(root))
    botao_limpar.pack(pady=10)

    root.mainloop()

def limpar_corrida(root):
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame) or isinstance(widget, tk.Label) or isinstance(widget, tk.Scale):
            widget.destroy()

def iniciar_corrida(root, escolha, quantum_entry):
    limpar_corrida(root)
    
    quantum = int(quantum_entry.get()) if quantum_entry.get().isdigit() else 2

    processos = [
        Processo("King and Lionheart", random.randint(3, 7), random.randint(1, 10), "king.png"),
        Processo("Dirty Paws", random.randint(3, 7), random.randint(1, 10), "dirty.png"),
        Processo("Mountain Sound", random.randint(3, 7), random.randint(1, 10), "mountain.png")
    ]

    frame_processos = tk.Frame(root, bg="white")
    frame_processos.pack()

    barras = []
    for processo in processos:
        img = Image.open(processo.imagem)
        img = img.resize((120, 120))
        img = ImageTk.PhotoImage(img)

        processo_frame = tk.Frame(frame_processos, bg="white")
        processo_frame.pack(side="top", padx=10, pady=5)

        label_img = tk.Label(processo_frame, image=img, bg="white")
        label_img.image = img
        label_img.pack()

        label_nome = tk.Label(processo_frame, text=processo.nome, font=("Arial", 12), bg="white")
        label_nome.pack()

        barra = tk.Scale(processo_frame, from_=0, to=100, orient="horizontal", length=300, bg="white")
        barra.pack()
        barras.append((barra, processo))

    def atualizar_corrida():
        terminou = True
        for barra, processo in barras:
            if processo.progresso < 100:
                processo.progresso += random.randint(5, 15)
                processo.progresso = min(processo.progresso, 100)
                barra.set(processo.progresso)
                terminou = False
        
        if terminou:
            vencedor = min(processos, key=lambda p: p.tempo_execucao) if escolha == "Round Robin" else processos[0]
            resultado_label.config(text=f"O vencedor é {vencedor.nome}!")
        else:
            root.after(500, atualizar_corrida)

    resultado_label = tk.Label(root, text="Corrida em andamento...", font=("Arial", 14), bg="white")
    resultado_label.pack()

    atualizar_corrida()

if __name__ == "__main__":
    iniciar_interface()