import random
import math
grades = ['D','C','B','A','A']
def grades_and_scores():
	print("Scores and Grades")
	for i in range(10):
		score = random.randint(0,40)
		print("Score: {}; Your grade is {}".format(score+60, grades[int(score/10)]))
	print("End of the program. Bye!")
	
grades_and_scores()