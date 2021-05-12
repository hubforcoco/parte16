from modelos.rectangulo import Rectangulo
from modelos.triangulo import Triangulo
from modelos.circulo import Circulo

def main():
    figuras = []

    rectangulo_rojo = Rectangulo('rojo', 'negro', 10, 5)
    circulo_verde = Circulo('verde', 'negro', 5)
    triangulo_negro = Triangulo('negro', 'gris', 7, 10)

    figuras.append(rectangulo_rojo)
    figuras.append(circulo_verde)
    figuras.append(triangulo_negro)

    print()

    print('El area de las figuras:')

    print()


    for f in figuras:
        f.dibujar()
        area = f.area()
        print(f'El área es igual a {area} u^2')

        print()

    print()

    # Demostración de la sobreescritura de métodos:
    print('Demostración de la sobreescritura de métodos:')
    print()

    print(rectangulo_rojo)

    print()

    print(circulo_verde)

    print()

    print(triangulo_negro)



if __name__ == '__main__':
    main()