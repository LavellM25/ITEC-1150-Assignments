"""
Author: Lavell McGrone
Date: 2024-09-19
Description: Calculate and display letter grade for student given their score on the quiz
"""

# Prompt the user for quiz score input
score = input('Enter quiz score: ')

# Make sure user inputs a integer and not a decimal value or word/phrase
if '.' in score:
    print("Error: Please enter a whole number, not a decimal or float.")
elif not score.isdigit():
    print("Error: Please enter a valid integer, not words or special characters.")
else:
    score = int(score)

# Ensure user enters input is within the valid range (0-100)
    if score > 100:
        print("Input Error: Score cannot be higher than 100.")
    elif score < 0:
        print("Input Error: Score cannot be less than 0.")
    else:
        if score >= 90:
            print('Letter grade = A')
            print("Perfect")
        elif score >= 80:
            print('Letter grade = B')
            print("Excellent, you rocked it, keep it up")
        elif score >= 70:
            print('Letter grade = C')
            print("Great, but there are some improvements need to made. Keep practicing")
        elif score >= 60:
            print('Letter grade = D')
            print("You may need more practice then most, we suggest you coming to instructor's office hours")
        else:
            '''
            Erik:
                I think you're the first one I've looked at tonight that realized this could be an else instead of an 
                elif score < 60
            '''
            print('Letter grade = F')
            print("Reflect on areas that you missed. Practice more and go to office hours")
