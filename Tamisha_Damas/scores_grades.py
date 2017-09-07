# Create a function that generates ten scores between 60 and 100. Display the grade for the score.
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

#define the function
import random

def grades(g):
    print "Scores and Grades"
    for x in range(0,g):
        score = random.randint(60, 101)
        if score >= 60 and score <= 69:
            print "Score: {}; Your grade is D".format(score)
        elif score >= 70 and score <= 79:
            print "Score: {}; Your grade is C".format(score)
        elif score >= 80 and score <= 89:
            print "Score: {}; Your grade is B".format(score)
        elif score >= 90 and score <= 100:
            print "Score: {}; Your grade is A".format(score)
    print "End of the program, Bye!"
grades(10)
