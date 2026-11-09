# funciones para mostrar reportes y paneles en pantalla

def mostrar_panel_estado(jornada, materia, horas, estado):
    print("\n" + "="*30)
    print("  PANEL DE CONTROL - JORNADA", jornada)
    print("="*30)
    print("materia prima disponible:", materia)
    print("horas restantes del turno:", horas)
    print("estado de la planta:", estado)
    print("="*30)

def calcular_indicadores(producidas, buenas):
    if producidas == 0:
        eficiencia = 0
    else:
        eficiencia = (buenas / producidas) * 100
    return round(eficiencia, 2)