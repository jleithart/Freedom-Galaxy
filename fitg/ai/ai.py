import rpyc
from fitg.backend import service
import json
from pprint import pprint
import time

class AI:
	'''
	This class will construct an AI object that will connect to 
	the server and act as a client in the game.

	'''

	def __init__(self, connection_options=None):
		# Eventually get the config options and use them to
		# connect to the server.

		# self.response will be the object that stores the backend response
		# received from a given call to the backend
		self.client = rpyc.connect("localhost", 55889, service.ClientService)
		self.response = None
		self.connection_options = connection_options

	def start_game(self):
		# Eventually get the config options and use them to define the game

		game_list = self.client.root.list_games()
		print("Listing all games")
		pprint(glist)

		# Adding validate_only=True to any call will only validate if 
		# it's possible.
		# You need to catch an IntegrityError when calling this since 
		# name is unique
		self.response = self.client.root.start_game(name="test", 
											   player="bob")
		print("Starting game test with player bob")
		pprint(response)

	def run(self):	
		# COUP : C
		# DIPLOMACY : D
		# ASSASSINATION: A
		# STOP REBELLION: R
		# GAIN CHARACTERS: G

		environ_list # = all environs in this scenario

		#when it's our turn
		while(run):
			reactionMove = False
			if(ourTurn):
				stack_list = selt.client.root.get_state(#g = et our stacks
				character_stack_list # = get our character stack list

				enemy_stack_list # = get their stacks that we can see
				#if any planet is in rebellion
				# is this an ID or an object?
				if planet_in_rebellion:
					# this is NOT for combat 
					self.client.root.move(character_stack, game_id, "stack");
										  game_name="test", 
										  planet_in_rebellion.location)
					# switching the for below into a function
					MoveStrongestUnits(planet_in_rebellion.id)
					for enemy_stack in enemy_stack_list:
						if(enemy_stack.stack_detection() && enemy_stack.location == planet_in_rebellion.location):
							# don't know what my options are
							# probably no options because we want 
							# all the characters to be available for missions
							self.client.root.combat(combined_stack, enemy_stack)
					self.client.root.assign_mission("R", character_stack)
				else:
					#operations (movement/combat)
					for enemy_stack in enemy_stack_list:
						#check to see if any of them are detected
						if(enemy_stack.stack_detection()):
							#send the strongest units
							MoveStrongestUnits(enemy_stack.environ_id)
							for stack in stack_list:
								#tell them to move even if we can't
								#leaders for the future
								self.client.root.move(stack,
													  game_name='test', 
													  enemy_stack.location)
							# need to combine the stacks for combat
							# combined_stack is the stack at the location 
							# we're moving to.
							# need to add options (leaders)
							self.client.root.combat(combined_stack,
													enemy_stack)
						else:
							for stack in stack_list:
								if random() < 0.20:
									for environ in environ_list:
										if random() < 0.50:
											self.client.root.move(
														stack,
														game_name="test",
														environ)

					#search (combat)
					# TBD

					#missions
					for character_stack in character_stack_list:
						tmp = random() % 4;
						if tmp == 0:
							# Diplomacy
							self.client.root.assign_mission("D",
															character_stack)
						elif tmp == 1:
							# coup
							self.client.root.assign_mission("C",
															character_stack)
						elif tmp == 2:
							#assassination
							self.client.root.assign_mission("A",
															character_stack)
						else:
							#gain character
							self.client.root.assign_mission("G",
															character_stack)
				ourTurn = False
			else:
				#reactionary move?

				# get all enemies (even the non-detected ones) sorted
				# list please
				enemy_stack_list 
				
				# get all stacks of military units -- sorted list please
				stack_list 
				for enemy_stack in enemy_stack_list:
					for stack in stack_list:
						if stack.location != enemy_stack.location 
											 and not reactionMove:
							unit = stack.units.pop()
							self.client.root.move(unit,
												  game_name="test",
												  enemy_stack.location)
							reactionMove = True
						if enemy_stack.location == stack.location:
							#do we search and therefore fight?
							if random() < 0.50:
								Search(stack, enemy_stack)
				#is someone detected in the environ we are in? do we want 
				# to search?
				#reaction move
			
			# Don't want to poll the system, so sleep for 10 seconds
			# because the backend won't put us to sleep.
			time.sleep(10)

def MoveStrongestUnits(environid):
	environ = self.client.root.get_state(gameid, "environ", environid)
	stack_list # = get all stacks
	num_units = 0 #want to make sure that we don't send too many units over
	new_location_stack #need a new location stack to append to
	#
	while(num_units < environ.size):
		best_attack = 0 # want to start with 0
		best_unit # the unit that has the best attack after each iteration
		best_stack # the stack that contains the best unit
		for stack in stack_list:
			for unit in stack:
				if best_attack < unit.environ_combat && unit.mobile:
					best_attack = unit.environ_combat
					best_unit = unit
					best_stack = stack
		if best_attack != 0:
			moving_stack = self.client.root.split_stack(session, best_stack.id, best_unit.id, False)
			self.client.root.move(session, moving_stack, environ.id)
			if(num_units == 0):
				new_location_stack = moving_stack
			else:
				self.client.root.merge_stack(session, moving_stack, new_location_stack)

		num_units += 1


if __name__ == '__main__':
	ai = AI()
	exit_value = AI.run()