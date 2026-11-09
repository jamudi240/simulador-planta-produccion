# modulo de funciones de apoyo y calculos generales

def calcular_costo_total(costo_mantenimiento, costo_operativo_extra=0.0):
    # calcula la sumatoria de gastos de la jornada
    total = costo_mantenimiento + costo_operativo_extra
    return round(total, 2)

def formatear_dinero(monto):
    # devuelve el valor con formato de dolar estandar
    return f"${monto:.1f}"

def validar_entrada_numerica(mensaje, valor_por_defecto=50):
    # funcion auxiliar para pedir numeros de forma segura sin que el programa se rompa
    try:
        resultado = int(input(mensaje))
        return resultado
    except:
        print("entrada no valida. usando valor por defecto:", valor_por_defecto)
        return valor_por_defecto

# prueba rapida del modulo
if __name__ == "__main__":
    print("probando funciones generales...")
    gasto_ejemplo = calcular_costo_total(150.0, 0.0)
    print("gasto total calculado:", formatear_dinero(gasto_ejemplo))