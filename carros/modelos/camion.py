from . carro import Carro

class  Camion(Carro):
    def __init__(self, placa, marca, modelo, pais_procedencia, capacidad_carga):
        super().__init__(placa, marca, modelo, pais_procedencia)

        self.capacidad_carga = capacidad_carga

    def  cargar_mercancia(self):
        print('La mercancia se esta cargando...')

    def  descargar_mercancia(self):
        print('La mercancia se esta descargando...')

        