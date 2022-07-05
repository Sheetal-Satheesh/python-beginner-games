# This is a sample Python script.
from storys_madlibs import thirst_crow as tc, the_fox_nd_the_grapes as fg
import random
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   choose_story = random.choice([tc, fg])
   choose_story.madlib()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
