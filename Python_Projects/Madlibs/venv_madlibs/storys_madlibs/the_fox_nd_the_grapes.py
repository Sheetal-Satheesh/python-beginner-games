def madlib():
    print("______________________")
    print("Story:The Fox and the Grapes")
    story()
    print("______________________")

    verb1 = input("Verb: ")
    pronoun = input("Pronoun: ")
    verb2 = input("Verb: ")
    article = input("Article: ")
    verb3 = input("Verb: ")
    verb4 = input("Verb: ")

    madlibs = f"One afternoon a fox was {verb1} through the forest. {pronoun} spotted a bunch of {verb2} over a branch. He thought 'This is exactly what I need to quench my thirst'. Taking a few steps back , {article} fox {verb3} trying to get the grapes. He tried a few times but failed. Finally, the fox give up and proceed to {verb4} away thinking 'The grapes are anyway sour'."
    print(madlibs)

def story():
    print("One afternoon a fox was ______ through the forest. ________ spotted a bunch of _____ over a branch. He thought 'This is exactly what I need to quench my thirst'. Taking a few steps back , _____ fox {verb3} trying to get the grapes. He tried a few times but failed. Finally, the fox give up and proceed to {verb4} away thinking 'The grapes are anyway sour'.")
