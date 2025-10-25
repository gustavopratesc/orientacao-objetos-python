# Médico e Paciente:
# Faça uma associação onde o Médico tem vários pacientes e pode consultar informações de cada um, como nome e histórico médico.

class Paciente:
    contagem_paciente = 0
    def __init__(self, nome: str) -> None:
        self.nome = nome
        Paciente.contagem_paciente += 1
        self.id_fila = Paciente.contagem_paciente
        
    def paciente_formatado(self) -> str:
        return f'Paciente: {self.nome} | Fila {self.id_fila}'
    

class Medico:
    def __init__(self, nome, area):
        self.nome = nome
        self.area = area
        self.pacientes = []

    def adicionar_paciente(self, paciente: Paciente) -> None:
        self.pacientes.append(paciente)

    def mostrar_relatorio(self) -> None:
        print(f'-- Medico: {self.nome} | Área: {self.area}')
        print('Pacientes')
        for p in self.pacientes:
            print(p.paciente_formatado())



gustavo = Medico('Gustavo', 'Pediatra')

ana = Paciente('Ana')
joao = Paciente('João')
maria = Paciente('Maria')

gustavo.adicionar_paciente(ana)
gustavo.adicionar_paciente(joao)
gustavo.adicionar_paciente(maria)

gustavo.mostrar_relatorio()