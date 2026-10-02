summary = client.chat.completions.create(

    model="gpt-3.5-turbo",

    messages=[

        {

            "role": "user",

            "content": "KeyError session user_id in Flask route ->",

        }

    ],

    max_tokens=80,

    temperature=0.2,

)

print(summary.choices[0].message.content)
