# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import openai
import config

def chatGPTModel(question):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": question},
        ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    print(result)

if __name__ == '__main__':
    # print_hi('PyCharm')
    str = "YES"
    while True:
        str = input("Enter your question(enter:N or NO to quit):")
        if str.upper() == "NO" or str.upper() == "N":
            break
        print("--------------------------the answer----------------------------")
        chatGPTModel(str)
        print("--------------------------the answer----------------------------")

