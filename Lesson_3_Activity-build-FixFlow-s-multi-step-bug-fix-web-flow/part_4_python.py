    fix_resp = client.chat.completions.create(

        model='gpt-3.5-turbo',

        messages=fix_messages,

        max_tokens=500

    )

    explain_resp = client.chat.completions.create(

        model='gpt-3.5-turbo',

        messages=explain_messages,

        max_tokens=500

    )

    fixed_code = fix_resp.choices[0].message.content

    explanation = explain_resp.choices[0].message.content

    return render_template(

        'index.html',

        fixed_code=fixed_code,

        explanation=explanation

    )
