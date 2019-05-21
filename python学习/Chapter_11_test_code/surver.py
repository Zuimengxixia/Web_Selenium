class AnonymousSurvey():
    '''手机匿名调查问卷的答案'''
    def __init__(self,question):
        '''存储一个问题，并为存储答案做准备'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''显示调查问卷'''
        print(self.question)

    def store_response(self,new_responses):
        '''存储单份调查答卷'''
        self.responses.append(new_responses)

    def show_results(self):
        '''显示手机到的所有答卷'''
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)