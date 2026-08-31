class Motorista:

    def __init__(self, nome, cpf, cnh, categoria_cnh):
        self.nome = nome
        self.cpf = cpf
        self.cnh = cnh
        self.categoria_cnh = categoria_cnh
        self.ativo = True


    def inativar(self):
        if not self.ativo:
            return("Motorista já está inativo.")
    
        self.ativo = False
        return("Motorista inativo com sucesso")


    def ativar(self):
        if self.ativo:
            return "Motorista já está ativo."

        self.ativo = True
        return "Motorista ativado com sucesso."
