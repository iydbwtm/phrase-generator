import random

starterwords = ["Hi,", "Hello,"]
questions = ["what are you doing? ", "how are you? ", "where are you? "]
aboutmyself = ["driving right neow.", "swimming right neow.", "on a walk right neow.", "skydiving right neow."]
ending = ["Good luck, write back soon!", "Bye!", "Best Wishes!"]

def generatephrase():
    starterword = random.choice(starterwords)
    question = random.choice(questions)
    aboutme = random.choice(aboutmyself)
    end = random.choice(ending)
    phrase = f"{starterword} {question}I'm currently {aboutme} {end}"
    return phrase

print(generatephrase())