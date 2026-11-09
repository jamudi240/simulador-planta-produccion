# configuraciones principales de la planta

# estados de las maquinas
estable = "operativa"
alta = "advertencia"
critico = "detenida"

# valores base para la simulacion
max_horas_turno = 8
materia_prima_inicial = 100
costo_mantenimiento_base = 150.0
limite_horas_mantenimiento = 30

def obtener_configuracion_inicial():
    # funcion para retornar los parametros base de la planta
    return {
        "materia_inicial": materia_prima_inicial,
        "horas_turno": max_horas_turno,
        "costo_mant": costo_mantenimiento_base,
        "limite_horas": limite_horas_mantenimiento
    }

# prueba rapida del modulo con formato visible
if __name__ == "__main__":
    print("\n" + "="*40)
    print("    CONFIGURACION INICIAL DE LA PLANTA")
    print("="*40)
    config = obtener_configuracion_inicial()
    print("- materia prima inicial:", config["materia_inicial"])
    print("- horas por turno:", config["horas_turno"])
    print("- costo de mantenimiento: $", config["costo_mant"])
    print("- limite de horas para mantenimiento:", config["limite_horas"])
    print("="*40 + "\n")