while True:
    from anthropic import Anthropic
    API_KEY = 'My_API_Key_Here'

    ai = Anthropic(api_key=API_KEY)
    item1 = input("Input 1: ")
    item2 = input("Input 2: ")

    response = ai.messages.create(max_tokens=100,messages=[
        {
            "role":"user",
            "content": (f"use {item1} and {item2} to make a new item and the only thing that you should reply with is the item, and can you make the item a real thing that relates to the combination with no description.")
        }
    ], model="claude-3-5-sonnet-latest")
    print(response.content[0].text)
