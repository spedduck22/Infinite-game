item1 = input("\nInput 1: ")
while True:
    from anthropic import Anthropic
    API_KEY = ''
    ai = Anthropic(api_key=API_KEY)
    item2 = input("\nInput 2: ")

    response = ai.messages.create(max_tokens=100,messages=[
        {
            "role":"user",
            "content": (f"use {item1} and {item2} to make a new item and the only thing that you should reply with is the item, and can you make the item a real thing that relates to the combination with no description and max of 2 words and an emoji that describes the output. Generate the emoji before the word, you can also use 2 emojies but don't everytime. Don't say the same thing across multiple messages of the same session.")
        }
    ], model="claude-3-5-sonnet-latest")
    print("\n","New input 1: ", response.content[0].text)
    item1 == response.content[0].text
