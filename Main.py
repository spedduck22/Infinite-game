while True:
    import pygame
    from anthropic import Anthropic
    API_KEY = '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'
    ai = Anthropic(api_key=API_KEY)
    item1 = input("Input 1: ")
    item2 = input("\nInput 2: ")

    response = ai.messages.create(max_tokens=100,messages=[
        {
            "role":"user",
            "content": (f"use {item1} and {item2} to make a new item and the only thing that you should reply with is the item, and can you make the item a real thing that relates to the combination with no description and max of 3 words and an emoji that describes the output. Generate the emoji before the word")
        }
    ], model="claude-3-5-sonnet-latest")
    print("\n", response.content[0].text, "\n")
