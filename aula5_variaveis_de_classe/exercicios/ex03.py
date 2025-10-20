class ConfigSistema:
    tema = 'Claro'
    
    def mudar_tema(self, novo_tema):
        ConfigSistema.tema = novo_tema


obj1 = ConfigSistema()
obj2 = ConfigSistema()

obj1.mudar_tema('escuro')

print(obj1.tema)
print(obj2.tema)

