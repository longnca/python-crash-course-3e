from survey import AnonymousSurvey

# Define a question and make a survey
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the question and store the responses to the question
language_survey.show_question()
print(f"Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# show the survey results
print("\nThank you to everyone who participate in the survey.")
language_survey.show_results()