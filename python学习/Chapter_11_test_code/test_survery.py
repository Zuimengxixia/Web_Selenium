'''测试 AnonymousSurvey 类'''
import unittest
from Chapter_11_test_code.surver import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''针对 AnonymousSurvey 类的测试'''

    def test_store_single_response(self):
        '''测试单个答案会被妥善的存储'''
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")

        self.assertIn("English",my_survey.responses)

    def test_store_three_responses(self):
        '''测试三个答案是否会被妥善存储'''
        question ="What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response,my_survey.responses)

if __name__ == '__main__':
    unittest.main()