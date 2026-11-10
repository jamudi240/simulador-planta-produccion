# archivo principal del simulador de planta
from config import estable, alta, critico, obtener_configuracion_inicial
from reportes import formatear_dinero, validar_entrada_numerica
from produccion import verificar_viabilidad, simular_produccion_jornada
from incidencias import evaluar_incidencia_jornada
from mantenimiento import registrar_mantenimiento

def main():
    print("bienvenido al simulador de la planta de produccion")
    
    # obtenemos los valores desde el modulo config
    config = obtener_configuracion_inicial()
    materia = config["materia_inicial"]
    horas_acumuladas_maquinas = 0
    
    # simulacion de 3 jornadas de trabajo
    for jornada in range(1, 4):
        horas_disponibles = config["horas_turno"]
        
        print(f"\n--- INICIO JORNADA {jornada} | Materia: {materia} | Horas: {horas_disponibles} ---")
        # pedir plan de produccion al usuario
        try:
            plan = int(input("cuantas unidades desea planificar producir hoy?: "))
        except:
            plan = 50 # valor por defecto si escriben mal
            
        # verificar si se puede producir
        if verificar_viabilidad(materia, horas_disponibles):
            # simular produccion
            producidas, buenas, gastado, tiempo_usado = simular_produccion_jornada(plan, materia, horas_disponibles)
            
            materia = materia - gastado
            horas_disponibles = horas_disponibles - tiempo_usado
            horas_acumuladas_maquinas = horas_acumuladas_maquinas + tiempo_usado
            
            # evaluar incidencias aleatorias
            tipo_incidencia, horas_perdidas = evaluar_incidencia_jornada()
            horas_disponibles = max(0, horas_disponibles - horas_perdidas)
            
            # mantenimiento preventivo
            horas_acumuladas_maquinas, costo_mant = registrar_mantenimiento(horas_acumuladas_maquinas)
            
            # reporte final del dia
            eficiencia = (buenas / producidas) * 100 if producidas > 0 else 0
            print("\nresumen del dia:")
            print("- unidades producidas:", producidas)
            print("- unidades buenas:", buenas)
            print("- eficiencia obtenida:", eficiencia, "%")
            print("- costo de mantenimiento: $", costo_mant)
        else:
            print("no se pudo ejecutar la jornada por falta de recursos.")
            
    print("\nsimulacion finalizada con exito.")

if __name__ == "__main__":
    main()