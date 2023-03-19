import openai
import os


# openai.organization = "org-XNE0GNeBY8RQag2cQRbHzDzu"
# openai.api_key = os.environ['OPENAI_API_KEY']
# openai.api_key = "k-XMlFMU2MrnIfBa9lmfFoT3BlbkFJ4yzcdR8BO03CmsaEhMxV"

# openai.Model.list()

# prompt = "Придумай идею для телеграм бота, чтобы приносил прибыль. "


# prompt = "праонализируй новости с какого-нибудь новостного сайта за сегодняшний день, приведи самую свежую новость" \
#          " , приведи ссылку на эту новость и ссылку на фото относящееся к этой новости" # НЕ работает


prompt = "Придумай шутку на тему IT"


def gpt_try(prompt):
    print(prompt)

    try:

        completion = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[
                {"role": "user", "content": f"{prompt}"}
              ]
            )
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content
    except Exception as exc:
        return str(exc)

# answer = gpt_try(prompt)
#
# print(answer)









