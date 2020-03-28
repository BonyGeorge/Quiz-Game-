import requests as rq
import json as js
import random as rand
import html as ht

url = "https://opentdb.com/api.php?amount=1&category=21&difficulty=easy&type=boolean"
end = ""

while end != 'quit':
    r = rq.get(url)

    if r.status_code != 200:
        end = input("Sorry, there is an error.")

    else:
        valid_answer = False
        data = js.loads(r.text)
        answer_num = 1
        quest = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct = data['results'][0]['correct_answer']
        answers.append(correct)
        rand.shuffle(answers)

        print(ht.unescape(quest) + '\n')

        for answer in answers:
            print(str(answer_num) + '- ' + ht.unescape(answer))
            answer_num += 1
        while not valid_answer:
            user_ans = input("\n Type Number of answer.")
            try:
                user_ans = int(user_ans)
                if user_ans > len(answers) or user_ans < 0:
                    print("Invalid answer")
                else:
                    valid_answer = True
            except:
                print("Invalid answer")

        user_ans = answers[int(user_ans) - 1]

        if user_ans == correct:
            print("\n Congratulations!! " + ht.unescape(answer))
        else:
            print("\n Sorry, the answer is " + ht.unescape(answer))

            end = input("Enter quit to exist or press enter to try again").lower()
print("\n Thanks For Playing")
