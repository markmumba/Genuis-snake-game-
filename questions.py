from mathgenerator import mathgen
import  random





class Maths:
    def __init__(self):
        self. generate_questions()

    def generate_questions(self):
        x  = [23,10,26,50,7,110,62,40]
        lst = []
        
        for _ in range(100):
            for i in x:
                question= mathgen.genById(i)
                lst.append(question)
        return lst 

    def get_random_question(self):
        lst=self.generate_questions()
        random_question = random.choice(lst)
        return random_question

    def check_answer(self,answer):
        if self.get_random_question()[1] == answer:
            self.get_random_question()[0]
        else:
            quit()
        
            


            

maths =Maths()

while True:
    print("Answer the following Maths question")
    question = maths.get_random_question()
    print(question)
    answer = str(input())
    x = maths.check_answer(answer)






