import tkinter as tk
from analizador_lex import Lexer


class LexerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico")

        self.texto_entrada = tk.Text(
            root, height=10, width=50, bg="lightgray", fg="black")
        self.texto_entrada.pack(pady=10)

        self.boton_analizar = tk.Button(
            root, text="Analizar", command=self.analizar_codigo)
        self.boton_analizar.pack(pady=5)

        self.resultados_texto = tk.Text(
            root, height=17, width=50, bg="black", fg="white")
        self.resultados_texto.pack(pady=10)

    def analizar_codigo(self):
        codigo = self.texto_entrada.get("1.0", tk.END)
        if not codigo:
            self.resultados_texto.delete(1.0, tk.END)
            self.resultados_texto.insert(
                tk.END, "Error: El código está vacío.")
            return

        lexer = Lexer(codigo)
        resultados = []

        while True:
            try:
                token = lexer.obtener_siguiente_token()
                if token.tipo == "LEXEMA_NO_RECONOCIDO":
                    resultados.append(
                        f"Error: Lexema no reconocido - '{token.valor}'")
                else:
                    resultados.append(str(token))
                if token.tipo == "FIN":
                    break
            except Exception as e:
                # resultados.append(f"Error: {e}")
                break

        self.resultados_texto.delete(1.0, tk.END)
        self.resultados_texto.insert(tk.END, "\n".join(resultados))


if __name__ == "__main__":
    root = tk.Tk()
    app = LexerApp(root)
    root.mainloop()
