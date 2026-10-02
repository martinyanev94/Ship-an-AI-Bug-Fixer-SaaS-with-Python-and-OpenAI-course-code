# client already constructed at module level (L01 pattern)

    response = client.chat.completions.create(

        model=model_engine,

        messages=conversation_history

    )

    bot_reply = response.choices[0].message.content

    conversation_history.append(

        {"role": "assistant", "content": bot_reply}

    )

    return bot_reply
