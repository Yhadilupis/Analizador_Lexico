import tkinter as tk
from ply.lex import LexError
from analizador_lex import lexer

def analizar():
    data = text_input.get("1.0", tk.END)
    print(data)
    lexer.input(data)
    output.delete("1.0", tk.END)

    try:
        while True:
            tok = lexer.token()
            if not tok:
                break
            output.insert(tk.END, f"Token: {tok.type}, Lexema: {tok.value}\n")
    except LexError as e:
        output.insert(tk.END, f"Error: {e}\n")

root = tk.Tk()
root.title("Analizador Léxico")

#área de texto para la entrada
text_input = tk.Text(root, height=10, width=50, bg="lightgray", fg="black")
text_input.pack()

analyze_button = tk.Button(root, text="Analizar", command=analizar)
analyze_button.pack()

#mostrar la salida y los errores
output = tk.Text(root, height=10, width=50, bg="black", fg="white")
output.pack()

root.mainloop()