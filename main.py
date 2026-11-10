# ==============================================================================
# SIMULADOR DE PLANTA DE PRODUCCIÓN
# ==============================================================================

def simular_jornada(nombre, capacidad, estado, horas_jornada, piezas_acum, horas_acum):
    """Simula el trabajo de una máquina individual durante una jornada."""
    if estado == "Operativa":
        produccion_jornada = capacidad * horas_jornada
        piezas_acum += produccion_jornada
        horas_acum += horas_jornada
        print(f"  [+] [{nombre}] Operó {horas_jornada}h -> Producidas en jornada: {produccion_jornada} piezas.")
    else:
        print(f"  [!] [{nombre}] NO pudo operar en esta jornada por estar en estado: '{estado}'.")
    return piezas_acum, horas_acum, estado


def ejecutar_simulacion_completa():
    continuar_simulacion = "s"

    while continuar_simulacion.lower() == "s":
        print("==========================================================")
        print("    INICIO DE LA SIMULACIÓN - 5 JORNADAS DE PRODUCCIÓN")
        print("==========================================================\n")

        # --- CONFIGURACIÓN INICIAL DE EQUIPOS ---
        print("[CONFIGURACIÓN] Inicializando equipos de la planta...")
        
        # Máquina 1
        nombre_m1 = "Cortadora CNC"
        cap_m1 = 50
        estado_m1 = "Operativa"
        piezas_m1 = 0
        horas_m1 = 0

        # Máquina 2
        nombre_m2 = "Ensambladora Automática"
        cap_m2 = 30
        estado_m2 = "Operativa"
        piezas_m2 = 0
        horas_m2 = 0

        # Máquina 3
        nombre_m3 = "Empaquetadora Industrial"
        cap_m3 = 40
        estado_m3 = "Operativa"
        piezas_m3 = 0
        horas_m3 = 0

        print(f"  -> {nombre_m1} ({cap_m1} pzs/h)")
        print(f"  -> {nombre_m2} ({cap_m2} pzs/h)")
        print(f"  -> {nombre_m3} ({cap_m3} pzs/h)\n")

        # --- JORNADA 1 (4 horas de producción normal) ---
        print("----------------------------------------------------------")
        print(" [JORNADA 1] Inicio de operaciones regulares (4 horas)")
        print("----------------------------------------------------------")
        piezas_m1, horas_m1, estado_m1 = simular_jornada(nombre_m1, cap_m1, estado_m1, 4, piezas_m1, horas_m1)
        piezas_m2, horas_m2, estado_m2 = simular_jornada(nombre_m2, cap_m2, estado_m2, 4, piezas_m2, horas_m2)
        piezas_m3, horas_m3, estado_m3 = simular_jornada(nombre_m3, cap_m3, estado_m3, 4, piezas_m3, horas_m3)

        # --- JORNADA 2 (3 horas de producción y reporte de falla) ---
        print("\n----------------------------------------------------------")
        print(" [JORNADA 2] Operación continua (3 horas) e incidencia")
        print("----------------------------------------------------------")
        piezas_m1, horas_m1, estado_m1 = simular_jornada(nombre_m1, cap_m1, estado_m1, 3, piezas_m1, horas_m1)
        piezas_m2, horas_m2, estado_m2 = simular_jornada(nombre_m2, cap_m2, estado_m2, 3, piezas_m2, horas_m2)
        piezas_m3, horas_m3, estado_m3 = simular_jornada(nombre_m3, cap_m3, estado_m3, 3, piezas_m3, horas_m3)
        print(f" ⚠️ [INCIDENCIA] {nombre_m1} reporta sobrecalentamiento y pasa a estado: 'Averiada'.")
        estado_m1 = "Averiada"

        # --- JORNADA 3 (2 horas con máquina averiada / detenida) ---
        print("\n----------------------------------------------------------")
        print(" [JORNADA 3] Operación con equipo detenido (2 horas)")
        print("----------------------------------------------------------")
        piezas_m1, horas_m1, estado_m1 = simular_jornada(nombre_m1, cap_m1, estado_m1, 2, piezas_m1, horas_m1)
        piezas_m2, horas_m2, estado_m2 = simular_jornada(nombre_m2, cap_m2, estado_m2, 2, piezas_m2, horas_m2)
        piezas_m3, horas_m3, estado_m3 = simular_jornada(nombre_m3, cap_m3, estado_m3, 2, piezas_m3, horas_m3)

        # --- JORNADA 4 (Mantenimiento y 4 horas post-reparación) ---
        print("\n----------------------------------------------------------")
        print(" [JORNADA 4] Mantenimiento correctivo y reanudación (4 horas)")
        print("----------------------------------------------------------")
        print(f" 🔧 [MANTENIMIENTO] Se repara {nombre_m1}. Estado restaurado a: 'Operativa'.")
        estado_m1 = "Operativa"
        piezas_m1, horas_m1, estado_m1 = simular_jornada(nombre_m1, cap_m1, estado_m1, 4, piezas_m1, horas_m1)
        piezas_m2, horas_m2, estado_m2 = simular_jornada(nombre_m2, cap_m2, estado_m2, 4, piezas_m2, horas_m2)
        piezas_m3, horas_m3, estado_m3 = simular_jornada(nombre_m3, cap_m3, estado_m3, 4, piezas_m3, horas_m3)

        # --- JORNADA 5 (3 horas finales de cierre de producción) ---
        print("\n----------------------------------------------------------")
        print(" [JORNADA 5] Cierre de ciclo y turno final (3 horas)")
        print("----------------------------------------------------------")
        piezas_m1, horas_m1, estado_m1 = simular_jornada(nombre_m1, cap_m1, estado_m1, 3, piezas_m1, horas_m1)
        piezas_m2, horas_m2, estado_m2 = simular_jornada(nombre_m2, cap_m2, estado_m2, 3, piezas_m2, horas_m2)
        piezas_m3, horas_m3, estado_m3 = simular_jornada(nombre_m3, cap_m3, estado_m3, 3, piezas_m3, horas_m3)

        # --- CONSOLIDACIÓN Y REPORTE FINAL ---
        total_planta = piezas_m1 + piezas_m2 + piezas_m3

        print("\n" + "=" * 65)
        print("   REPORTE GENERAL CONSOLIDADO - LAS 5 JORNADAS DE PLANTA")
        print("=" * 65)
        print(f" • {nombre_m1:<25} | Horas Totales: {horas_m1}h | Piezas: {piezas_m1} | Estado: {estado_m1}")
        print(f" • {nombre_m2:<25} | Horas Totales: {horas_m2}h | Piezas: {piezas_m2} | Estado: {estado_m2}")
        print(f" • {nombre_m3:<25} | Horas Totales: {horas_m3}h | Piezas: {piezas_m3} | Estado: {estado_m3}")
        print("-" * 65)
        print(f" TOTAL GENERAL DE LA PLANTA (5 Jornadas): {total_planta} piezas.")
        print("=" * 65)

        # Preguntar si desea reiniciar
        print("\n" + "~" * 65)
        continuar_simulacion = input("¿Desea volver a ejecutar todo el ciclo de 5 jornadas? (s/n): ")
        print("~" * 65 + "\n")

    print("¡Simulación finalizada con éxito. Hasta luego!")


if __name__ == "__main__":
    ejecutar_simulacion_completa()