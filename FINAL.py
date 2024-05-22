class Livros:                                  # Aqui creie uma class pra os livros e defini seus atributos, para uma melhor organização do codigo ultilizei do Def pra definir funçoes ao logo do codigo
    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor

    def __str__(self):
        return f"Livro: {self.nome}, Autor: {self.autor}, Codigo: {self.codigo}"
    
  

class Biblioteca: # na biblioteca é ondo tudo acontece, nesta parte defini as funções e adicionei cada livro alem de comprimir tudo em uma classe só que é a biblioteca
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def busca_livro_codigo(self, codigo):
        for livro in self.livros:
            if livro.codigo == codigo:
                return livro
        return None
    
    def busca_livro_nome(self, nome):
        for livro in self.livros:
            if livro.nome.lower() == nome.lower():
                return livro
        return None
    
    def busca_livro_autor(self, autor):
        for livro in self.livros:
            if livro.autor.lower() == autor.lower():
                return livro
        return None

biblioteca = Biblioteca()
biblioteca.adicionar_livro(Livros(1, "A Revolução dos Bichos", "George Orwell"))
biblioteca.adicionar_livro(Livros(2, "A Menina que Roubava Livros", "Markus Zusak"))
biblioteca.adicionar_livro(Livros(3, "Neuromancer", "William Gibson"))
biblioteca.adicionar_livro(Livros(4, "O Sol é para Todos", "Harper Lee"))

def busca_livro(biblioteca, criterio, valor):  # Utilizando de uma variavel chamada critério creie a função de busca, onde apartir de uma 
    if criterio == "codigo":                    # Das 3 informações(codigo, autor ou nome) consigo extrair o livro requerido
        return biblioteca.busca_livro_codigo(valor)
    elif criterio == "nome":
        return biblioteca.busca_livro_nome(valor)
    elif criterio == "autor":
        return biblioteca.busca_livro_autor(valor)
    else:
        return None
    
def interface(): #
    print("Bem-vindo à Biblioteca!")
    print("Escolha o critério de busca: ")
    print("1. Código")
    print("2. Nome")
    print("3. Autor")

    escolha = input("Digite o número do critério de busca:")

    if escolha == "1":
        valor = int(input("Digite o código do livro: "))
        criterio = "codigo"
    elif escolha == "2":
        valor = input("Digite o nome do livro: ")
        criterio = "nome"
    elif escolha == "3":
        valor = input("Digite o nome do autor: ")
        criterio = "autor"
    else:
        print("Critério inválido")
        return

    livro = busca_livro(biblioteca, criterio, valor)
    if livro:
        print(f"Livro encontrado: {livro}")
    else:
        print("Livro não encontrado.")

interface()
