# modulo de mantenimiento hecho por el integrante 4

def registrar_mantenimiento(horas_acumuladas):
    costo_mantenimiento = 0.0
    
    # si las maquinas llevan mas de 30 horas se recomienda revision
    if horas_acumuladas >= 30:
        print("\n--- aviso de mantenimiento ---")
        print("las maquinas superaron las 30 horas de uso.")
        respuesta = input("desea hacer mantenimiento preventivo hoy? (si/no): ")
        
        if respuesta == "si":
            costo_mantenimiento = 150.0
            print("mantenimiento realizado. costo adicionado: $", costo_mantenimiento)
            horas_acumuladas = 0
        else:
            print("mantenimiento pospuesto. cuidado con posibles fallas.")
            
    return horas_acumuladas, costo_mantenimiento

# prueba rapida del modulo
if __name__ == "__main__":
    print("probando mantenimiento...")
    # simulamos que las maquinas tienen 35 horas de uso
    horas_nuevas, costo = registrar_mantenimiento(35)
    print("horas acumuladas restantes:", horas_nuevas)
    print("costo calculado: $", costo)