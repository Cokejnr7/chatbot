import openai
from decouple import config

openai.api_key = config('OPENAI_SECRET_KEY')


def trial():
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": "You are a helpful assistant."
        }, {
            "role": "user",
            "content": "Who won the world series in 2020?"
        }, {
            "role":
            "assistant",
            "content":
            "The Los Angeles Dodgers won the World Series in 2020."
        }, {
            "role": "user",
            "content": "Where was it played?"
        }])


def gpt3_completion(prompt,
                    engine='text-davinci-002',
                    temp=0.7,
                    top_p=1.0,
                    tokens=400,
                    freq_pen=0.0,
                    pres_pen=0.0,
                    stop=['<<END>>']):
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    response = openai.Completion.create(engine=engine,
                                        prompt=prompt,
                                        temperature=temp,
                                        max_tokens=tokens,
                                        top_p=top_p,
                                        frequency_penalty=freq_pen,
                                        presence_penalty=pres_pen,
                                        stop=stop)

    text = response['choices'][0]['text'].strip()
    return text
