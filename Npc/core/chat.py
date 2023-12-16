from openai import OpenAI

client = OpenAI()
chat_log = []

def chat(question):
    query_dict = {"role": "user", "content": question}
    chat_log.append(query_dict)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=chat_log
    )

    assistant = completion.choices[0].message.content

    query_dict = {"role": "assistant", "content": assistant}
    chat_log.append(query_dict)

    return assistant