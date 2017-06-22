import os

import rodi

import musicas

import creacion

robot = rodi.RoDI()

musica = musicas.music()

#dj = creacion.DJ() en proceso

from time import sleep

from colorama import init, Fore, Style

init(autoreset=True)


os.system('clear')

def wheel(wheel_pos):

    wheel_pos = 255 - wheel_pos
    if wheel_pos < 85:
        return (255 - wheel_pos * 3, 0, wheel_pos * 3)
    if wheel_pos < 170:
        wheel_pos -= 85
        return (0, wheel_pos * 3, 255 - wheel_pos * 3)
    wheel_pos -= 170
    return (wheel_pos * 3, 255 - wheel_pos * 3, 0)

def comienzo():

	print Fore.RED + Style.BRIGHT +"--------------------------------Terminal de RoDI--------------------------------"

	print Fore.RED + Style.BRIGHT +'''
1-''','''Adelante''',Fore.RED + Style.BRIGHT +'''
2-''','''Atras''',Fore.RED + Style.BRIGHT +'''
3-''','''Izquierda''',Fore.RED + Style.BRIGHT +'''
4-''','''Derecha''',Fore.RED + Style.BRIGHT +'''
5-''','''Medir la distancia de un objeto que hay delante. (distancia)''',Fore.RED + Style.BRIGHT +'''
6-''','''Autonomo. RoDI libre. (auto)''',Fore.RED + Style.BRIGHT +'''
7-''','''Saber si hay luz, o esta oscuro alrededor del RoDI. (luz)''',Fore.RED + Style.BRIGHT +'''
8-''','''Producir un sonido. (sonido)''',Fore.RED + Style.BRIGHT +'''
9-''','''Bibioteca de Canciones. (biblioteca)''',Fore.RED + Style.BRIGHT +'''
10-''','''Encender Led. (encender)''',Fore.RED + Style.BRIGHT +'''
11-''','''Apagar Led. (apagar)''',Fore.RED + Style.BRIGHT +'''
12-''','''Encender Led de forma aleatoria. (aleatorio)''',Fore.RED + Style.BRIGHT +'''
13-''','''Parpadear (Titilar) el Led. (parpadear)
'''
	print  Fore.RED + Style.BRIGHT +'''
Instruccion:''','''
Escribe la/s accion/es que desea realizar o el numero de la accion(y ayuda para especificaciones)
limpiar, borrar, clear - para limpiar la pantalla
Salir - salir
'''
comienzo()

def ayuda():

	print '''Ayuda:
------Para las primeras 4 acciones, indicar el tiempo en segundos a realizar la accion. Presionar 0 (cero) para elegir otra accion		
------Para la opcion (5, 6, 7, 8, 10, 11 y 12, 13) NO es necesario indicar un tiempo, solo basta con teclear la opcion.
------Accion (8). Por defecto reproducira solo un pitido.
------Accion (10). Mantendra encendido el Led si no se le indica que se apague
------Accion (12). Se refiere a que el Led podra encenderse de cualquier color de forma aleatoria.
------Accion (13). El Led se encendera y apagara cada medio segundo.'''

def adelante():

	while True:
		tiempo = input(Fore.RED + Style.BRIGHT + 'RoDI/adelante>')
		if tiempo < 0:
			print Fore.GREEN + Style.BRIGHT + "Error: No se permite numeros negativos. Intentalo de nuevo."
		elif tiempo > 0:
			print Fore.BLUE + Style.BRIGHT + "RoDI avanzara por %s segundos" %tiempo
			robot.move_forward()
			sleep(tiempo)
			robot.move_stop()
			print Fore.BLUE + Style.BRIGHT + "RoDI se detuvo"
		else:
			break

def atras():

	while True:
		tiempo = input(Fore.RED + Style.BRIGHT + 'RoDI/atras>')
		if tiempo < 0:
			print Fore.GREEN + Style.BRIGHT + "Error: No se permite numeros negativos. Intentalo de nuevo."
		elif tiempo > 0:
			print Fore.BLUE + Style.BRIGHT + "RoDI retrocedera por %s segundos" %tiempo
			robot.move_backward()
			sleep(tiempo)
			robot.move_stop()
			print Fore.BLUE + Style.BRIGHT + "RoDI se detuvo"
		else:
			break
def izquierda():
		
	while True:
		tiempo = input(Fore.RED + Style.BRIGHT + 'RoDI/izquierda>')
		if tiempo < 0:
			print Fore.GREEN + Style.BRIGHT + "Error: No se permite numeros negativos. Intentalo de nuevo."
		elif tiempo > 0:
			print Fore.BLUE + Style.BRIGHT + "RoDI girara a la izquierda por %s segundos" %tiempo
			robot.move_left()
			sleep(tiempo)
			robot.move_stop()
			print Fore.BLUE + Style.BRIGHT + "RoDI se detuvo"
		else:
			break

def derecha():

	while True:
		tiempo = input(Fore.RED + Style.BRIGHT + 'RoDI/derecha>')
		if tiempo < 0:
			print Fore.GREEN + Style.BRIGHT + "Error: No se permite numeros negativos. Intentalo de nuevo."
		elif tiempo > 0:
			print Fore.BLUE + Style.BRIGHT + "RoDI girara a la derecha por %s segundos" %tiempo
			robot.move_right()
			sleep(tiempo)
			robot.move_stop()
			print Fore.BLUE + Style.BRIGHT + "RoDI se detuvo"
		else:
			break

def mirar():

	dis = robot.see()
	print Fore.RED + Style.BRIGHT + "RoDI/medir>", Fore.BLUE + Style.BRIGHT + "Veo un objeto a %d cm" %dis 

def auto():

	s = 1
	print Fore.RED + Style.BRIGHT + 'RoDI/autonomo>', Fore.BLUE + Style.BRIGHT + "RoDI es libre"
	while True:
		dis = robot.see()
		if dis < 10:
			robot.move_stop()
			robot.move_backward()
			sleep(0.5)
			robot.move_left()
			sleep(0.5)
			dis = robot.see()
			s+=1
		elif s >= 6:
			print Fore.RED + Style.BRIGHT + 'RoDI/autonomo>', Fore.BLUE + Style.BRIGHT + "RoDI esta quieto"
			robot.move_stop()
			break
		elif dis > 10:
			robot.move_forward()
			dis = robot.see()
				
			

def luz():

	l = robot.light()
	print Fore.RED + Style.BRIGHT + "RoDI/luz>", Fore.BLUE + Style.BRIGHT + "Percibo %d intensidad de luz" %l 

def soni():

	print Fore.RED + Style.BRIGHT + "RoDI/sonido>", Fore.BLUE + Style.BRIGHT + "Reproduciendo sonido"
	robot.sing(1000, 1000)
	sleep(1)
	print Fore.RED + Style.BRIGHT + "RoDI/sonido>", Fore.BLUE + Style.BRIGHT + "Fin del sonido"

def biblioteca():

	os.system('clear')
		
	print Fore.GREEN + Style.BRIGHT +"BIBIOTECA DE CANCIONES"
	print'''Aqui puedes elegir la cancion que desea escuchar:
1-Harry Potter (harry)
2-Star Wars (star)
3-Escribe tu propia cancion (en proceso)
-----Estamos agregando mas canciones para que disfrutes mas de tu RoDI
'''		
	while True:
		opcion = raw_input(Fore.RED + Style.BRIGHT + "RoDI/musica>")
		if opcion in ('1', 'harry', 'uno'):
			print Fore.RED + Style.BRIGHT + "RoDI/musica>" + Fore.BLUE + Style.BRIGHT + "Reproduciendo Harry Potter"
			musica.harry()
			print Fore.RED + Style.BRIGHT + "RoDI/musica>" + Fore.BLUE + Style.BRIGHT + "Fin de Harry Potter"
		elif opcion in ('2', 'star', 'dos'):
			print Fore.RED + Style.BRIGHT + "RoDI/musica>" + Fore.BLUE + Style.BRIGHT + "Reproduciendo Star Wars"
			musica.Star_Wars()
			print Fore.RED + Style.BRIGHT + "RoDI/musica>" + Fore.BLUE + Style.BRIGHT + "Fin de Star Wars"
		#elif opcion in ('3', 'hazlo', 'tres'): esto esta en proceso
			#dj.inicio()
		elif opcion in ('1', '2', '3', 'harry', 'star', 'hazlo', 'uno', 'dos', 'tres'):
			print Fore.GREEN + Style.BRIGHT + "Error: Solo introduce las opciones permitidas. Intentalo de nuevo"
		elif opcion == '0':
			os.system('clear')
			comienzo()
			break
		else:
			print Fore.BLUE + Style.BRIGHT + "Presiona el numero de la opcion, o la palabra entre parentesis, y 0 (cero) para regresar atras"

def prender():

	print Fore.RED + Style.BRIGHT + "RoDI/encender>", Fore.BLUE + Style.BRIGHT + "Led encendido"
	robot.led(1)

def apagar():

	print Fore.RED + Style.BRIGHT + "RoDI/apagar>", Fore.BLUE + Style.BRIGHT + "Led apagado"
	robot.led(0)

def aleatorio():

	print Fore.RED + Style.BRIGHT + "RoDI/aleatorio>", Fore.BLUE + Style.BRIGHT + "El Led se volvio loco..."
	for j in range (2):
		for i in range (256):
			rojo, verde, azul = wheel(i)
			robot.pixel(rojo, verde, azul)
			sleep(0.005)
		robot.pixel(0,0,0)
	robot.pixel(0,0,0)
	print Fore.RED + Style.BRIGHT + "RoDI/aleatorio>", Fore.BLUE + Style.BRIGHT + "El Led ya se calmo"

def titilar():
	
	print Fore.RED + Style.BRIGHT + "RoDI/parpadear>", Fore.BLUE + Style.BRIGHT + "El Led esta parpadeando"
	for i in range(5):
		robot.led(1)
		sleep(0.5)
		robot.led(0)
		sleep(0.5)
	print Fore.RED + Style.BRIGHT + "RoDI/parpadear>", Fore.BLUE + Style.BRIGHT + "El Led dejo de parpadear"

def facil():
	
	os.system('clear')
	print Fore.GREEN + Style.BRIGHT + "Trucos"
	print '''Estos son algunos trucos que se pueden realizar:
1-Cuadrado
2-Circulo
3-Triangulo
'''
	while True:
		accion = raw_input(Fore.RED + Style.BRIGHT + "RoDI/figuras>")
		accion = accion.lower()
		if accion in ('1', 'cuadrado', 'uno'):
			print Fore.RED + Style.BRIGHT + "RoDI/figuras>" + Fore.BLUE + Style.BRIGHT + "RoDI esta haciendo un cuadrado" 
			for i in range(3):
				robot.move_forward()
				sleep(2)
				robot.move_right()
				sleep(0.25)
			robot.move_stop()
			print Fore.RED + Style.BRIGHT + "RoDI/figuras>" + Fore.BLUE + Style.BRIGHT + "RoDI hizo un cuadrado"
		elif accion in ('2', 'circulo', 'dos'):
			print Fore.RED + Style.BRIGHT + "RoDI/figuras>" + Fore.BLUE + Style.BRIGHT + "RoDI esta haciendo un circulo"
			for i in range(23):
				robot.move_forward()
				sleep(0.3)
				robot.move_right()
				sleep(0.1)
			robot.move_stop()
			print Fore.RED + Style.BRIGHT + "RoDI/figuras>" + Fore.BLUE + Style.BRIGHT + "RoDI hizo un circulo"
		elif accion in ('3', 'triangulo', 'tres'):
			print Fore.RED + Style.BRIGHT + "RoDI/figuras>" + Fore.BLUE + Style.BRIGHT + "RoDI esta haciendo un triangulo"
			for i in range(2):
				robot.move_right()
				sleep(0.25)
				for i in range(2):
					robot.move_forward()
					sleep(2)
					robot.move_right()
					sleep(0.5)	
			robot.move_stop()
			print Fore.RED + Style.BRIGHT + "RoDI/figuras>" + Fore.BLUE + Style.BRIGHT + "RoDI hizo un triangulo"
		elif not accion in ('1', '2', '3', 'cuadrado', 'circulo', 'triangulo', 'uno', 'dos', 'tres'):
			os.system('clear')
			comienzo()
			break

while True:

	accion = raw_input(Fore.RED + Style.BRIGHT+"RoDI>")
	accion = accion.lower()
	if accion in ('clear', 'limpiar', 'borrar', 'cls', '0'):
		os.system('clear')
		comienzo()
	elif accion in('ayuda', 'help', 'no se', 'nose'):
		ayuda()
	elif accion in ('1', 'adelante', 'uno'):
		adelante()
	elif accion in ('2', 'atras', 'dos'):
		atras()
	elif accion in ('3', 'izquierda', 'tres'):
		izquierda()
	elif accion in ('4', 'derecha', 'cuatro'):
		derecha()
	elif accion in ('5', 'cinco', 'distancia'):
		mirar()
	elif accion in ('6', 'auto', 'seis'):
		auto()
	elif accion in ('7', 'luz', 'siete'):
		luz()
	elif accion in ('8', 'sonido', 'ocho'):
		soni()
	elif accion in ('9', 'biblioteca', 'nueve'):
		biblioteca()
	elif accion in ('10', 'encender', 'diez'):
		prender()
	elif accion in ('11', 'apagar', 'once'):
		apagar()
	elif accion in ('12', 'aleatorio', 'doce'):
		aleatorio()
	elif accion in ('13', 'parpadear', 'trece'):
		titilar()
	elif accion in ('truco', 'secreto', 'oculto'):
		facil()
	elif accion in ('guerrero', 'modo_sumo', 'espartanos', 'auauau'):
		sumo()
	elif accion == 'salir':
		break
		exit