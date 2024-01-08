list_question = [
    {'질문': '1 번째 문제의 질문', '점수': '10'},
    {'질문': '2 번째 문제의 질문', '점수': '8'},
    {'질문': '3 번째 문제의 질문', '점수': '9'},
    {'질문': '4 번째 문제의 질문', '점수': '7'},
    {'질문': '5 번째 문제의 질문', '점수': '6'},
]

list_answer = [
    {'답안': '첫 번째 문제의 첫 번째 답안'},
    {'답안': '첫 번째 문제의 두 번째 답안'},

]

final_output = ""

html_template = """
<div>문제{index} : {question} / 점수 : {score}</div>
<div>답안 :
1) {answer1}
2) {answer2}
3) {answer3}
4) {answer4}
</div>
"""


for i in range(len(list_question)):
    final_output += html_template.format(
        index=i+1,
        question=list_question[i]['질문'],
        score=list_question[i]['점수'],
        answer1=list_answer[i*4]['답안'],
        answer2=list_answer[i*4+1]['답안'],
        answer3=list_answer[i*4+2]['답안'],
        answer4=list_answer[i*4+3]['답안']
    )
    
    


print(final_output)