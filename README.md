# Simulador de Planta de Produccion

Proyecto modular desarrollado para la simulacion y control de procesos en una planta industrial, cumpliendo con los criterios de programacion estructurada y buenas practicas de desarrollo.

## Estructura del Proyecto
El sistema esta dividido en los siguientes modulos independientes:
- **`main.py`**: Archivo principal que coordina el flujo de las jornadas y la ejecucion general.
- **`config.py`**: Contiene las constantes, estados de las maquinas y la funcion de configuracion inicial.
- **`produccion.py`**: Modulo encargado de verificar la viabilidad y simular la produccion diaria de unidades.
- **`incidencias.py`**: Simula eventos aleatorios y contingencias en la linea de trabajo.
- **`mantenimiento.py`**: Controla el acumulado de horas de las maquinas y registra el mantenimiento preventivo.
- **`reportes.py`**: Gestiona la visualizacion del panel de control y el cálculo de eficiencia.
- **`funciones.py`**: Agrupa funciones auxiliares para calculos y validaciones seguras.

## Requisitos
- Python 3.x instalado en el equipo.

## Como Ejecutar el Simulador
1. Clona o descarga este repositorio.
2. Abre tu terminal en la carpeta principal del proyecto.
3. Ejecuta el siguiente comando:
   ```bash
   python main.py