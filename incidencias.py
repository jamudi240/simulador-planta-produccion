# modulo de incidencias hecho por el integrante 4
import random

def evaluar_incidencia_jornada():
    # probabilidad sencilla de que ocurra un evento (30% de probabilidad)
    numero = random.randint(1, 10)
    
    if numero <= 3:
        print("\natencion! ocurrio una incidencia en la planta.")
        print("1. falla electrica corta")
        print("2. falta de material en linea")
        opcion = input("elija como resolver (1 o 2): ")
        
        if opcion == "1":
            print("se reiniciaron los equipos. perdida ligera de tiempo.")
            return "falla_electrica", 1
        else:
            print("se solicito material de emergencia. reduccion de ritmo.")
            return "falta_material", 2
    else:
        print("\njornada sin incidencias reportadas.")
        return "ninguna", 0
    # prueba rapida del modulo
if __name__ == "__main__":
    print("probando incidencias...")
    evaluar_incidencia_jornada()