# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import openai

def print_hi(name):
    openai.api_key = "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"

    # list models
    models = openai.Model.list()

    # print the first model's id
    print(models.data[0].id)

    # create a completion
    completion = openai.Completion.create(model="ada", prompt="Hello world")

    # print the completion
    print(completion.choices[0].text)


def chatGPTModel(question):
    openai.api_key = "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"

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
    while str.upper() != "NO" and str.upper() != "N":
        str = input("Enter your question(enter:N or NO to quit):")
        print("--------------------------the answer----------------------------")
        chatGPTModel(str)
        print("--------------------------the answer----------------------------")

