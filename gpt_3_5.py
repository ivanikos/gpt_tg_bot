
import openai
import os


openai.api_key = os.environ['OPENAI_API_KEY']

def gpt_try(prompt):
    try:
        completion = openai.chat.completions.create(
              model="gpt-3.5-turbo",
              messages=[
                {"role": "user", "content": f"{prompt}"}
              ]
            )
        return [completion.choices[0].message.content, prompt]
    except Exception as exc:
        return [str(exc), "warning"]

# answer = gpt_try(prompt)
#
# print(answer)









