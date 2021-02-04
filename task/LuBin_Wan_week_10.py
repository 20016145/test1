import random
class Dice():
	def __init__ (self,sides):
		self.sides=sides
	def roll_dice(self):
		return random.randint(1, 6)

class DiceSet():
	def __init__ (self,diceamount,dice_sides):
		self._dice_list = []
		self._dice_amount = _dice_amount
		self._dice_slides = dice_sides

		for i in range(self._dice_amount):
			self._dice_list.append(Dice(self._dice_sides))

	def roll_set(self):
		numbers_thrown = []
		for dice in self ._dice_list:
			numbers_thrown.append(dice.roll_dice())
			return numbers_thrown

	def dice_rooller(sides, num_of_dice, num_of_rolls):
		dice_set = DiceSet(num_ofdice, sides)
		result_throws = []
		for roll in range(num_of_rolls):
			current_roll = dice_set.roll_set()
			result_throws.append(current_roll)
			print(roll,  roll+1, ":", current_roll)
			return result_throws



