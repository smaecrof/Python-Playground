# Author: Spencer Mae-Croft
# Date: 08/31/2020

from survey import AnonymousSurvey

# Define a question and make a survey 
question = "What was the first programming language you learned?"
my_survey = AnonymousSurvey(question)

#Show the question and store the responses to the question
my_survey.show_question()

print("Enter 'q' to exit the application")

while True:
    response = input("Language: ")

    if response.lower() == 'q':
        break

    my_survey.store_response(response)


# Show the survey results
my_survey.show_results() 


