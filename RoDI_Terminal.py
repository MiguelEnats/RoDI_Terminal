import os

import rodi

from time import sleep

from colorama import init, Fore, Style

init(autoreset=True)

robot = rodi.RoDI()

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

class action():

	accion=''

	def comienzo():

		print "---------Este es un Test de RoDI, elije la accion que desea realizar.---------"

		print '''
1-Adelante
2-Atras
3-Izquierda
4-Derecha
5-Medir la distancia de un objeto que hay delante. (distancia o medir)
6-Autonomo. Recorrer sin chocar. Por 1 min. (auto)
7-Saber si hay luz, o esta oscuro alrededor del RoDI. (luz)
8-Producir un sonido. (sonido)
9-Sonar un musica predeterminada (Star Wars). (musica)
10-Encender Led. (encender)
11-Apagar Led. (apagar)
12-Encender Led de forma aleatoria. (aleatorio)
13-Parpadear (Titilar) el Led. (parpadear)
'''
		print '''
Instruccion:
Escribe la/s accion/es que desea realizar o el numero de la accion(y ayuda para especificaciones)
limpiar, borrar, clear - para limpiar la pantalla
Salir - salir
'''
	comienzo()

	def ayuda():

		print '''Ayuda:
------Para las primeras 4 acciones, indicar el tiempo en segundos a realizar la accion. Presionar 0 (cero) para elegir otra accion		
------Para la opcion (5, 6, 7, 8, 9) NO es necesario indicar un tiempo, solo basta con teclear la opcion.
------Accion (8). Por defecto reproducira solo un pitido.
------Accion (10). Mantendra encendido el Led si no se le indica que se apague
------Accion (11). Se refiere a que el Led podra encenderse de cualquier color de forma aleatoria.
------Accion (12). El Led se encendera y apagara cada medio segundo.'''

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
				print Fore.BLUE + Style.BRIGHT + "RoDI retrosedera por %s segundos" %tiempo
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
				print Fore.BLUE + Style.BRIGHT + "RoDI girara a la derecga por %s segundos" %tiempo
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
			if dis > 10:
				robot.move_forward()
				dis = robot.see()
			elif dis < 10:
				robot.move_stop()
				robot.move_backward()
				sleep(1)
				robot.move_left()
				sleep(0.5)
				dis = robot.see()
				s+=1
			elif s >= 20:
				print Fore.RED + Style.BRIGHT + 'RoDI/autonomo>', Fore.BLUE + Style.BRIGHT + "RoDI esta quieto"
				robot.move_stop()
				break		
			

	def luz():

		l = robot.light()
		print Fore.RED + Style.BRIGHT + "RoDI/luz>", Fore.BLUE + Style.BRIGHT + "Percibo %d intensidad de luz" %l 
	
	def soni():

		print Fore.RED + Style.BRIGHT + "RoDI/sonido>", Fore.BLUE + Style.BRIGHT + "Reproducir sonido"
		robot.sing(1000, 1000)
		sleep(3)
		print Fore.RED + Style.BRIGHT + "RoDI/sonido>", Fore.BLUE + Style.BRIGHT + "Fin del sonido"

	def musica():
		#hay que probar
		print Fore.RED + Style.BRIGHT + "RoDI/musica>", Fore.BLUE + Style.BRIGHT + "Reproducir musica"
		robot.sing(988, 500)
		robot.sing(1319, 1000)
		robot.sing(1568, 250)
		robot.sing(1480, 250)
		robot.sing(1319, 1000)
		robot.sing(1976, 500)
		robot.sing(1760, 1250)
		robot.sing(1480, 1000)
		robot.sing(988, 500)
		robot.sing(1319, 1000)
		robot.sing(1568, 250)
		robot.sing(1480, 250)
		robot.sing(1175, 1000)
		robot.sing(1319, 500)
		robot.sing(988, 1000)
		sleep(1)
		robot.sing(988, 500)
		robot.sing(1319, 1000)
		robot.sing(1568, 250)
		robot.sing(1480, 250)
		robot.sing(1319, 1000)
		robot.sing(1976, 500)
		robot.sing(2349, 1000)
		robot.sing(2217, 500)
		robot.sing(2093, 1000)
		robot.sing(1760, 500)
		robot.sing(2093, 1000)
		robot.sing(1976, 250)
		robot.sing(1866, 250)
		robot.sing(1568, 500)
		robot.sing(1319, 1000)
		sleep(2)
		print Fore.RED + Style.BRIGHT + "RoDI/musica>" + Fore.BLUE + Style.BRIGHT + "Fin de la muscia"

	def prender():

		print Fore.RED + Style.BRIGHT + "RoDI/encender>", Fore.BLUE + Style.BRIGHT + "Led encendido"
		robot.led(1)

	def apagar():

		print Fore.RED + Style.BRIGHT + "RoDI/encender>", Fore.BLUE + Style.BRIGHT + "Led apagado"
		robot.led(0)

	def aleatorio():

		print Fore.RED + Style.BRIGHT + "RoDI/aleatorio>", Fore.BLUE + Style.BRIGHT + "El Led se volvio loco..."
		for i in range (256):
			rojo, verde, azul = wheel(i)
			robot.pixel(rojo, verde, azul)
			sleep(0.005)
		robot.pixel(0,0,0)
		print Fore.RED + Style.BRIGHT + "RoDI/aleatorio>", Fore.BLUE + Style.BRIGHT + "El Led ya se calmo"

	def titilar():
		print Fore.RED + Style.BRIGHT + "RoDI/parpadear>", Fore.BLUE + Style.BRIGHT + "El Led esta parpadeando"
		for i in range(10):
			robot.light(1)
			sleep(0.5)
			robot.light(0)
			sleep(0.5)
		print Fore.RED + Style.BRIGHT + "RoDI/parpadear>", Fore.BLUE + Style.BRIGHT + "El Led dejo de parpadear"

	while True:

		accion = raw_input(Fore.RED + Style.BRIGHT+"RoDI>")
		accion = accion.lower()
		if accion in ('clear', 'limpiar', 'borrar', 'cls', '0'):
			os.system('clear')
			comienzo()
		elif accion == 'ayuda':
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
		elif accion in ('9', 'musica', 'nueve'):
			musica()
		elif accion in ('10', 'encender', 'diez'):
			prender()
		elif accion in ('11', 'apagar', 'once'):
			apagar()
		elif accion in ('12', 'aleatorio', 'doce'):
			aleatorio()
		elif accion in ('13', 'parpadear', 'trece'):
			titilar()
		elif accion == 'salir':
			break
			exit