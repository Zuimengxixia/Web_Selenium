from Chapter_11_test_code.surver import AnonymousSurvey

#定义一个问题，并创建一个表示调查的 AnonymousSurvey
question = "What language did you first learn to speak?"
my_suevery = AnonymousSurvey(question)

#显示问题并存储答案
my_suevery.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break

    my_suevery.store_response(response)

#显示调查结果
print("\nThank you to evertone who participated in the survey!")
my_suevery.show_results()