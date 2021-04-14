# goals of assignment
# goal 1: should be able to prompt with a random default message if no match
# goal 2: have some patterns that just match on keywords, don't capture
# goal 3: have one or more that uses SOME captured information
# goal 4: have one or more that uses TWO pieces of captured information

# Test Phrases:
# Greetings Eliza!
# My name is Lou
# I was hurt after falling down some stairs
# I love cake.
# My parents are quite rude sometimes.
# My brother just had his first child!
# I am sad because I fell in front of everyone.
# School is like capitalism.
# School is why I have no time.
# exit

# real conversation example:
# luisestevez@Luiss-MacBook-Air src % python3 assignment2.py
# Hello, I am ELIZA.
# > Hello Eliza my name is Lou.
# Welcome. How are you doing? Can I help you with anything?
# > my brothers are mean
# How is your relationship with your brothers?
# > they are alright
# Does that evoke any strong emotions?
# > sometimes
# I'm not sure I follow. Could you clarify
# > Sometimes my parents favor them
# Anything else about your parents that comes to mind?
# > school is like capitalism.
# What makes you think school is like capitalism?
# > exit
# Goodbye!

import re
import random

# knowledge, data, and models
default_model = [
    'Very interesting.',
    'I\'m not sure I follow. Could you clarify?',
    'Go on.',
    'What does that suggest to you?',
    'Does that evoke any strong emotions?'
]
conversation_model = {

    # matching 1 subgroup
    r'\b(hello|hi|greetings|hey)\b': [
        'Greetings. How are you doing today?',
        'Welcome. How are you doing? Can I help you with anything?',
        'Hello! How are you doing?'
        ],
    r'\bname\b': [
        'This is anonymous, don\'t worry about names.'
    ],
    r'\bi was (.*)': [
        'Why does the fact that you were {match1} come to mind now?',
        'Were you really?'
    ],
    r'\bi love (.*)\b': [
        'What about {match1} do you love the most?',
        'What doy you love about {match1}'
    ],
    r'\bmy (mom|mother|dad|father|parents)\b': [
        'Tell me more about your {match1}.',
        'Anything else about your {match1} that comes to mind?',
        'Have your parents had a strong influence on you?'
    ],
    r'\bmy (brothers?|sisters?|siblings?)\b': [
        'Do your siblings have a significant impact on you?',
        'How is your relationship with your {match1}?'
    ],
    r'\bi am (depressed|sad|happy|angry|mad)\b': [
        'Did you come to me because you are {match1}?',
        'Did something happen recently to make you feel {match1}?'
    ],
    # matching 2 subgroups
    r'\b(.*) is like (.*)\b': [
        'Why do you believe {match1} and {match2} are alike?',
        'What resemblance do you see between {match1} and {match2}?',
        'What makes you think {match1} is like {match2}?'
    ],
    r'(.*) is why i (.*)': [
        'Why do you believe {match1} is responsible for {match2}?',
        'Can you elaborate on that connection?'
    ]
}

# main function
def discuss(user_in):
    match = None
    subg1 = ""
    subg2 = ""
    response = ""

    for pattern in conversation_model.keys():
        if match == None:
            match = re.search(pattern, user_in)
            if match != None:
                response = random.choice(conversation_model[pattern])

    if match != None:
        if len(match.groups()) > 0:
            subg1 = match.group(1)
        if len(match.groups()) > 1:
            subg2 = match.group(2)
        print(response.format(match1 = subg1, match2 = subg2))
    else:
        print(random.choice(default_model))


# main loop

done = False
print("Hello, I am ELIZA.")

while not done:
    user_input = input("> ")
    if user_input.lower() == 'exit':
        print('Goodbye!')
        done = True
    else:
        discuss(user_input.lower())


