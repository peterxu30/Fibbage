import random
import os
from questions import Questions

class Player:
	def __init__(self, name):
		self.name = name
		self.score = 0

	# Returns player name
	def get_name():
		return self.name

	# Returns player's current score
	def get_score():
		return self.score

	# Add a point to player score
	def get_point(self, points=1):
		self.score += points

class Game:

	# List of questions
	questions = Questions #{1: [Question, Answer]}
	
	# Question Number
	q_n = 1

	def __init__(self):
		self.initialized = False
		self.question_number = 1 #tells functions which question currently on
		self.number_of_questions = len(self.questions) 
		self.players = {} #player object = {1: player object, ...}
		self.lies = {} #{1: lie, 2: lie} keys are player numbers, lies are strings. Changes every question
		self.answers = {} #{1: answer, 2: answer...} key = player number, answer = string. Changes every question


	# PLAYER RELATED METHODS -------------------------------

	# Adds a player to the current game
	def add_player(self, name):
		self.players[len(self.players)+1] = Player(name)

	# Returns a player
	def get_player(self, player_num):
		return self.players[player_num]

	# Returns a player's name
	def player_name(self, player_num):
		return self.get_player(player_num).get_name()

	# Returns a player's score
	def player_score(self, player_num):
		return self.get_player(player_num).get_score()

	# Return's the current question
	def current_question(self):
		return self.questions[self.question_number]


	# GAMEPLAY RELATED METHODS -------------------------------

	def submit_lie(self, player_num, lie):
		self.lies[0] = self.get_real_answer()
		self.lies[player_num] = lie

	def scramble_lies(self):
		#lies = [self.lies[i] for i in self.lies]
		random.shuffle(self.lies)
		for i in range(len(self.lies)):
			print('%s. %s'%(i+1, self.lies[i]))

	def submit_answer(self, player_num, answer):
		lies_list = [self.lies[i] for i in self.lies]
		if answer in lies_list:
			self.answers[player_num] = answer
		else:
			print('Not a valid answer, try again!')
			return self.submit_answer(player_num, input('Answer: '))

	def get_real_answer(self):
		return self.questions[self.question_number][1]

	def check_answer(self, player_num):
		real_answer = self.get_real_answer()
		player = self.get_player(player_num)
		if self.answers[player_num] == real_answer:
			player.get_point()
			return '%s is correct!'%player.name
		else:
			return '%s is incorrect!'%player.name

	def score_check(self):
		for player in self.players:
			print(self.player_name(player), ': ', self.player_score(player))


	# GAME PHASE RELATED METHODS -------------------------------

	def initialization_phase(self):
		os.system('cls')
		if not self.initialized:
			input('Welcome to Fibbage - The Ultimate Trivia Game!')
			print('\n')
			number_players = eval(input('How many players? '))
			for i in range(number_players):
				self.add_player(input('\nWhat is your name? '))
			print('\n')
			self.initialized = True
		os.system('cls')

	def end_phase(self):
		self.question_number += 1
		if self.question_number > len(self.questions):
			print('Game Over!')
			scores = [[self.player_name(player), self.player_score(player)] for player in self.players]
			scores = sorted(scores, key = lambda x: x[1])
			winner = scores[0]
			print('%s wins with %s points!'%(winner[0], winner[1]))
			self.question_number = 1
			self.initialized = False
			self.players = {}
		self.lies = {}
		self.answers = {}
		input('\nPress anything to continue.')
		#resets game

	def play_phase(self):
		self.initialization_phase()

		
		for player in self.players:
			print('Question %s \n'%self.question_number)
			print(self.current_question()[0])
			print('\nEnter your lies!\n')
			self.submit_lie(player, input('%s\'s lie: '%self.player_name(player)))
			os.system('cls') 
		
		for player in self.players:
			print('\nThe question is:\n %s'%self.current_question()[0])
			print('Your choices are:\n')
			self.scramble_lies()
			print('\nSubmit your answers!')
			print('\n%s\'s turn'%self.player_name(player))
			self.submit_answer(player, input('Answer: '))
			os.system('cls')

		print('Let\'s see how you did!\n')
		for player in self.players:
			print(self.check_answer(player))
		print('\n')
		self.score_check()
		#input('Press anything to continue')

		self.end_phase()

# MAIN METHOD -------------------------------

game = Game()

while 1:
	game.play_phase()


	


