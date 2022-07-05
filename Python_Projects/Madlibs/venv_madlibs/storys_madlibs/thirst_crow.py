#Madlibs Which allows people to fillout the blanks with their word of choice
# Can be implemented using String Concatenation
def madlib():
    print("______________________")
    print("Story: No Pain No Gain")
    story()
    print("_______________________")

    adj1 = input("Adjective: ")
    verb1 = input("Verb: ")
    season = input("Season: ")
    article = input("Article: ")
    pronoun = input("Pronoun: ")
    verb2 = input("Verb: ")
    verb3 = input("Verb: ")
    verb4 = input("Verb: ")

    madlibs = f"Once a {adj1} crow was {verb1} hither and thither in search of water. It was {season} season. It was so hot and it has not rainded for days. After searching for so long. {article} crow found a jar with water at the bottom. {pronoun} tried his level best to sip the water but could not succeed He saw some pebble {verb2} nearby. He {verb3} the pebbles with his beak and {verb4} into the pot one by one. The level of water started rising. Finally, the crow was able to quench his thirst by drinking the water and flew away."
    print(madlibs)

def story():
    print("Once a _____ crow was _____ hither and thither in search of water. It was _____ season. It was so hot and it has not rainded for days. After searching for so long. _____ crow found a jar with water at the bottom. _____ tried his level best to sip the water but could not succeed. He saw some pebble ______ nearby. He ____ the pebbles with his beak and ____ into the pot one by one. The level of water started rising. Finally, the crow was able to quench his thirst by drinking the water and flew away.")