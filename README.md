[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=mirosjm/MSF-Practica3)

# Modelado de Sistemas Fisiológicos. Práctica 3: Sistema cardiovascular [Jacobo21212669]

## Autor
Miroslava Jacobo Mendoza

Ingeniería Biomédica, Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana. Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: l21212669@tectijuana.edu.mx

## Objetivos general
Analizar el comportamiento dinámico del sistema cardiovascular utilizando el modelo Windkessel de cuatro elementos, con el propósito de comprender la influencia de los parámetros hemodinámicos clave —impedancia característica, distensibilidad arterial, resistencia periférica e inercia arterial— en la presión y el flujo sanguíneo, así como diseñar estrategias de control que permitan evaluar la estabilidad y respuesta del sistema ante distintas condiciones fisiológicas.


## Actividades
1. Calcular analíticamente la función de transferencia del sistema.
2. Determinar el error en estado estacionario y la estabilidad del sistema en lazo abierto.
3. Construir el diagrama de bloques.
4. Diseñar el controlador con Simulink utilizando el bloque PID Controller y la herramienta Tune para sintonizar los valores óptimos para cada una de las ganancias kP, kI y kD.
5. Ilustrar el cambio de la presión sobre la distensibilidad arterial [Pp(t)] en respuesta a la presión arterial de entrada Pa(t). Utilice la función de entrada Uniform Random Number con la siguiente configuración: min = -0.2 V, max = 1 V, seed = 106, Sample time = 0.5.
6. Determinar la respuesta a la función en el intervalo t∈[0,15] (segundos), en Python, Simulink y Multisim en lazo abierto y en lazo cerrado con el controlador.
7. Elaborar el diagrama biológico del sistema con BioRender.com
8. Discutir los resultados obtenidos en la experimentación in silico y elaborar el reporte de la práctiva.


## Docente
Dr. Paul A. Valle

Posgrado en Ciencias de la Ingeniería [PCI] y Departamento de Ingeniería Eléctrica y Electrónica [DIEE], Tecnológico Nacional de México/IT Tijuana. Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: paul.valle@tectijuana.edu.mx
