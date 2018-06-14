import random as rnd

class Environment(object):
    def __init__(self, name):
        self.name = name         # name of box
        self.box = []            # bundle of boxes

    def reward(self, rewards):
        self.reward = rewards

    def set_box(self, number):   # number of boxes to generate

        for i in range(0, number):
            p = rnd.random()      # p is the probability of successfully getting the reward inside the box
            self.box.append(('box_' + str(1+i), p, self.reward))
        self.number = number

    def create_box_tree(self, name_of_the_file):
        n = self.number
        file = open(name_of_the_file, "w+")
        file.write("nice bro!!!!!!")
        print (n)

    def create_nod(self,a):
        a = 12
        return a



e1 = Environment('first_experiment')
e1.reward(100)
e1.set_box(5)
print(e1.box)
e1.create_box_tree("tree_file.txt")


























