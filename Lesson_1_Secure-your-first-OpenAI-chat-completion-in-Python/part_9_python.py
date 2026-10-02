buggy_code = "def average(total, count):\n    return total / count"

prompt = (

    "Explain the bug and propose a fix for this Python code:\n"

    f"{buggy_code}"

)

response = client.chat.completions.create(

    model="gpt-3.5-turbo",

    messages=[{"role": "user", "content": prompt}],

    max_tokens=120,

    n=1,

    temperature=0.2,

)
