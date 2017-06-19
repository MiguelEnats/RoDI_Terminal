'''
Los colores disponibles para las constantes Back y Fore son los siguientes: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE.
Los estilos son DIM, NORMAL, BRIGHT
'''
import os
os.system('clear')
import rodi
from time import sleep
from colorama import init, Fore, Style
init(autoreset=True)
robot = rodi.RoDI()
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
9-Sonar un musica predeterminada (Star War). (musica)
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
		while True:
			dis = robot.see()
			if dis > 10:
				robot.move_forward()
				dis = robot.see()
			if dis < 10:
				robot.move_stop()
				robot.move_backward()
				sleep(1)
				robot.move_left()
				sleep(1)
				dis = robot.see()
			s = raw_input(Fore.RED + Style.BRIGHT + 'RoDI/autonomo>'+ Fore.BLUE + Style.BRIGHT + "Presiona cualquier tecla para detenerme: ")
			if s != '':
				print Fore.RED + Style.BRIGHT + 'RoDI/autonomo>', Fore.BLUE + Style.BRIGHT + "RoDI esta quieto"
				robot.move_stop()
				break		
			

	def luz():
		l = robot.light()
		print Fore.RED + Style.BRIGHT + "RoDI/luz>", Fore.BLUE + Style.BRIGHT + "Siento %d" %dis 
	
	def soni():
		print Fore.RED + Style.BRIGHT + "RoDI/sonido>", Fore.BLUE + Style.BRIGHT + "Reproducir sonido"
		robot.sing(33, 1000)
		sleep(3)
		print Fore.RED + Style.BRIGHT + "RoDI/sonido>", Fore.BLUE + Style.BRIGHT + "Fin del sonido"

	def musica():
		print Fore.RED + Style.BRIGHT + "RoDI/musica>", Fore.BLUE + Style.BRIGHT + "Reproducir musica"
		robot.sing(1000, 1000)
		sleep(1)
		print Fore.GREEN + Style.BRIGHT + "En trabajo para mejorar el sonido"
		print Fore.RED + Style.BRIGHT + "RoDI/musica>", Fore.BLUE + Style.BRIGHT + "Fin de la muscia"

	def prender():
		print Fore.RED + Style.BRIGHT + "RoDI/encender>", Fore.BLUE + Style.BRIGHT + "Led encendido"
		robot.led(1)

	def apagar():
		print Fore.RED + Style.BRIGHT + "RoDI/encender>", Fore.BLUE + Style.BRIGHT + "Led apagado"
		robot.led(0)

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
		elif accion == 'salir':
			break
			exit