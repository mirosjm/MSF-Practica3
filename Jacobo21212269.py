"""
Práctica 3: Sistema cardiovascular

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Miroslava Jacobo Mendoza
Número de control: 21212669
Correo institucional: l21212669@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Instalar librerias en consola
#!pip install control
#!pip install slycot

# Librerías para cálculo numérico y generación de gráficas
import numpy as np
import math 
import matplotlib.pyplot as plt
import control


# Datos de la simulación
x0,t0,tend,dt,w,h = 0,0,10,1E-3,10,5
N = round((tend-t0)/dt) + 1
t = np.linspace(t0,tend,N)

u = np.sin(2*math.pi*95/60*t) + 0.8

def cardio(Z,C,R,L):
    num = [L*R, R*Z]
    den = [C*L*R*Z,L*R+L*Z,R*Z]
    sys = control.tf(num,den)
    return sys

#individuo hipotenso
Z = 0.02
C = 0.25
R = 0.6
L = 0.005

sysHipo = cardio(Z, C, R, L)
print('Individuo hipotenso')
print(sysHipo)

#individuo nomotenso
Z = 0.033
C = 1.5
R = 0.95
L = 0.01

sysN = cardio(Z, C, R, L)
print('Individuo nomotenso')
print(sysN)

#individuo hipertenso
Z = 0.05
C = 2.5
R = 1.4
L = 0.02

sysHiper = cardio(Z, C, R, L)
print('Individuo hipertenso')
print(sysHiper)


# Componentes del controlador
def controlador(kI):
    Cr = 10E-6
    Re = 1/(kI*Cr); print('Re = ', Re)
    
    numPID = [1]
    denPID = [Re*Cr,0]
    PID = control.tf(numPID,denPID)
    print(PID)
    return PID
    
    
# Sistema de control en lazo cerrado hipotenso
PID = controlador(103.32809)
X = control.series(PID,sysHipo)
sysPIDHipo = control.feedback(X,1, sign= -1)
print(sysPIDHipo)

# Sistema de control en lazo cerrado hipertenso
PID = controlador(495.72)
X = control.series(PID,sysHiper)
sysPIDHiper = control.feedback(X,1, sign= -1)
print(sysPIDHiper)


# Respuesta del sistema en lazo abierto y en lazo cerrado
morado =[68/255, 23/255, 82/255]
rosa =[255/255, 116/255, 139/255]
naranja =[255/255, 101/255, 0/255]
verde =[228/255, 241/255, 172/255]


#Grafica lazo abierto
fig1 = plt.figure();
_,Pp = control.forced_response(sysHipo,t,u,x0)
plt.plot(t,Pp,"-", color = rosa, label = "Pp(t): Hipotenso")

_,Pp = control.forced_response(sysN,t,u,x0)
plt.plot(t,Pp,"-", color = morado, label = "Pp(t): Nomotenso")

_,Pp = control.forced_response(sysHiper,t,u,x0)
plt.plot(t,Pp,":", color = naranja, label = "Pp(t): Hipertenso")

#_,VPID = ctrl.forced_response(sysPID,t,u1,x0)
#plt.plot(t,VPID,":", linewidth = 3, color = verde, label = "VID(t)")

plt.xlim(0,10); plt.xticks(np.arange(0,11,1.0))
plt.ylim(-0.5,2); plt.yticks(np.arange(-0.5,2.5,0.5))
plt.xlabel("t [s]", fontsize = 11)
plt.ylabel("Pp(t) [v]", fontsize = 11)
plt.legend(bbox_to_anchor = (0.5,-0.3), loc= "center", ncol=3,
           fontsize = 8, frameon = False)
plt.show()
fig1.savefig("Lazo_abierto.pdf",bbox_inches = "tight")


#Grafica control hipotenso

fig2 = plt.figure();
_,Pp = control.forced_response(sysHipo,t,u,x0)
plt.plot(t,Pp,"-", color = rosa, label = "Pp(t): Hipotenso")

_,Pp = control.forced_response(sysN,t,u,x0)
plt.plot(t,Pp,"-", color = morado, label = "Pp(t): Nomotenso")

#_,Pp = control.forced_response(sysHiper,t,u,x0)
#plt.plot(t,Pp,":", color = naranja, label = "Pp(t): Hipertenso")

_,VPID = control.forced_response(sysPIDHipo,t,u,x0)
plt.plot(t,VPID,":", linewidth = 3, color = verde, label = "Pp(t): Controlador")

plt.xlim(0,10); plt.xticks(np.arange(0,11,1.0))
plt.ylim(-0.5,2); plt.yticks(np.arange(-0.5,2.5,0.5))
plt.xlabel("t [s]", fontsize = 11)
plt.ylabel("Pp(t) [v]", fontsize = 11)
plt.legend(bbox_to_anchor = (0.5,-0.3), loc= "center", ncol=3,
           fontsize = 8, frameon = False)
plt.show()
fig2.savefig("Lazo_cerrado_hipotenso.pdf",bbox_inches = "tight")

#Grafica control hipertenso

fig3 = plt.figure();
#_,Pp = control.forced_response(sysHipo,t,u,x0)
#plt.plot(t,Pp,"-", color = rosa, label = "Pp(t): Hipotenso")

_,Pp = control.forced_response(sysN,t,u,x0)
plt.plot(t,Pp,"-", color = morado, label = "Pp(t): Nomotenso")

_,Pp = control.forced_response(sysHiper,t,u,x0)
plt.plot(t,Pp,"-", color = naranja, label = "Pp(t): Hipertenso")

_,VPID = control.forced_response(sysPIDHiper,t,u,x0)
plt.plot(t,VPID,":", linewidth = 3, color = verde, label = "Pp(t): Controlador")

plt.xlim(0,10); plt.xticks(np.arange(0,11,1.0))
plt.ylim(-0.5,2); plt.yticks(np.arange(-0.5,2.5,0.5))
plt.xlabel("t [s]", fontsize = 11)
plt.ylabel("Pp(t) [v]", fontsize = 11)
plt.legend(bbox_to_anchor = (0.5,-0.3), loc= "center", ncol=3,
           fontsize = 8, frameon = False)
plt.show()
fig3.savefig("Lazo_cerrado_hipertenso.pdf",bbox_inches = "tight")