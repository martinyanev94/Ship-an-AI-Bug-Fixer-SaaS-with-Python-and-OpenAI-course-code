result = client.chat.completions.create(

    model=ft_id,

    messages=[

        {

            "role": "user",

            "content": "KeyError session user_id in Flask route ->",

        }

    ],

    max_tokens=60,

    temperature=0.2,

)

print(result.choices[0].message.content)
