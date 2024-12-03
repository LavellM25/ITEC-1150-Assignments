""" M. Bock 9/19/2019  This program asks for a number of students, and a number
of quizzes that each student must take. Then it collects their quiz scores into a list and
provides an average for each student. A list of lists and overall average is also provided. """

# this re-write of quiz avg. saves student scores in a list of lists
# could this help simplify programs with nested loops?


def main():
    try:
        num_students, num_quizzes = inputs()
        list_of_lists, overall_average = processing(num_students, num_quizzes)
        final_outputs(num_students, num_quizzes, list_of_lists, overall_average)
        restart = input('Would you like to start over? Enter y or n: ')
        if restart == 'y':
            main()
        else:
            print('Thanks for using the program')
    except Exception as err:
        print(err)


def inputs():  # collect info needed from user
    print('How many students are taking quizzes?')
    num_students = get_pos_int()
    print('How many quizzes will each one take?')
    num_quizzes = get_pos_int()
    return num_students, num_quizzes


def get_pos_int():  # ensures "int-able" input over 0
    pos_int = input('\tEnter a positive whole number: ')
    while pos_int.isnumeric() is False or pos_int == '0':
        pos_int = input('\tPlease enter a whole number, greater than 0: ')
    pos_int = int(pos_int)
    return pos_int


def processing(num_students, num_quizzes):
    overall_total = 0  # initialize three group-level variables
    overall_average = 0.0
    list_of_lists = []  # empty list
    for student in range(num_students):
        student_score_list = []  # empty list
        print(f'Quiz info for student #{student + 1}: ')
        for quiz in range(num_quizzes):
            print(f'\tScore for quiz #{quiz + 1}:')
            quiz_score = get_pos_int()  # call function to get valid, individual quiz score
            student_score_list.append(quiz_score)  # build a list to save student quiz scores
            # print(student_score_list) # turn on during development to watch code in action
        student_total = sum(student_score_list)
        student_average = student_total / num_quizzes  # calculate student avg. when all quizzes recorded
        loop_outputs(student_total, student_average, student, student_score_list)
        # save group-level data
        overall_total += student_total  # add student total quiz points to group total quiz points
        list_of_lists.append(student_score_list)  # add each student's list of scores to a list of lists
        # print(list_of_lists)  # turn on during development to watch code in action
    overall_average = overall_total / num_students / num_quizzes
    return list_of_lists, overall_average


def loop_outputs(student_total, student_average, student, student_score_list):
    print(f'\tQuiz score list for student #{student + 1}: {student_score_list} ')
    print(f'\tTotal points = {student_total}')
    print(f'\tQuiz Average = {student_average :<0.2f}')


def final_outputs(num_students, num_quizzes, list_of_lists, overall_average):
    print(f'Overall results for {num_students} students & {num_quizzes} quizzes ')
    print('Here is the list of score lists: ', list_of_lists)
    print(f'Group average = {overall_average:<0.2f}')
    for score_set in range(len(list_of_lists)):
        print(f'Student #{score_set + 1} scores: {list_of_lists[score_set]}')


main()
