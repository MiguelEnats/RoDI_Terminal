import rodi

from time import sleep

from colorama import init, Fore, Style

init(autoreset=True)

robot = rodi.RoDI()

def sensores():

	sensor = robot.sense()
	estado1 = sensor[0]
	estado2 = sensor[1]
	enemy = robot.see()
	return estado1, estado2, enemy

class modos(object):


	def seguidor(self):
		
		estado1, estado2, enemy = sensores()
		print Fore.BLUE + Style.BRIGHT + "RoDI seguira la linea negra hasta que le digas que se detenga"
		if estado1 > 100 and estado2 > 100:
			robot.move_backward()
			estado1, estado2, enemy = sensores()
		elif estado1 < 100 and estado2 > 100:
			robot.move_right()
			estado1, estado2, enemy = sensores()
		elif estado1 > 100 and estado2 < 100:
			robot.move_left()
			estado1, estado2, enemy = sensores()
		elif estado1 < 100 and estado2 > 100:
			robot.move_forward()
			estado1, estado2, enemy = sensores()

	def sumo(self):
		
		estado1, estado2, enemy = sensores()
		print Fore.BLUE + Style.BRIGHT + "RoDI luchara hasta que le digas que se detenga"
		if estado1 < 100 and estado2 < 100:
			if enemy == 1:
				robot.move_backward()
				sleep(0.5)
				robot.move_forward()
				estado1, estado2, enemy = sensores()
			elif enemy < 20:
				robot.move_forward()
				estado1, estado2, enemy = sensores()
			else:
				robot.move_right()
				estado1, estado2, enemy = sensores()
		elif estado1 > 100 and estado2 < 100:
			robot.move_right()
			estado1, estado2, enemy = sensores()
		elif estado1 < 100 and estado2 > 100:
			robot.move_left()
			estado1, estado2, enemy = sensores()
		else:
			robot.move_right()
			estado1, estado2, enemy = sensores()
			
	def callejera(self):

		estado1, estado2, enemy = sensores()
		print Fore.BLUE + Style.BRIGHT + "RoDI luchara hasta que le digas que se detenga"
		if enemy < 20:
			robot.move_forward()
			estado1, estado2, enemy = sensores()
		elif enemy == 1:
			robot.move_backward()
			sleep(0.5)
			robot.move_forward()
			estado1, estado2, enemy = sensores()
		else:
			robot.move_right()
			estado1, estado2, enemy = sensores()