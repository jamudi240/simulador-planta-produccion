# modulo de produccion hecho por el integrante 3

def verificar_viabilidad(materia_prima, horas_disponibles, consumo_por_unidad=1):
    # verifica si hay recursos suficientes para trabajar
    if materia_prima <= 0:
        print("alerta: no hay materia prima para iniciar")
        return False
    if horas_disponibles <= 0:
        print("alerta: no hay horas disponibles en el turno")
        return False
    return True

def simular_produccion_jornada(planificada, materia_disponible, horas_disponibles):
    # regla basica: cada unidad usa 1 de materia prima y 0.007 horas
    unidades_posibles = min(planificada, materia_disponible)
    
    # horas reales usadas
    horas_usadas = unidades_posibles * 0.007
    if horas_usadas > horas_disponibles:
        horas_usadas = horas_disponibles
        unidades_posibles = int(horas_usadas / 0.007)
        
    # margen simple de unidades defectuosas
    buenas = int(unidades_posibles * 0.95)
    materia_consumida = unidades_posibles
    
    return unidades_posibles, buenas, materia_consumida, round(horas_usadas, 2)
# prueba rapida del modulo
if __name__ == "__main__":
    print("probando produccion...")
    producidas, buenas, gastado, tiempo = simular_produccion_jornada(60, 100, 8)
    print("producidas:", producidas)
    print("buenas:", buenas)
    print("materia gastada:", gastado)
    print("tiempo usado:", tiempo)