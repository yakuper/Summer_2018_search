
class Institute(object):
    def __init__(self, name, boxes):
        self.name = name
        self.boxes = boxes

    def regen_boxes(self): #  removes the opened box from the coice of boxes
        pass



class Agent(object):
    def __init__(self, name, boxes):
        self.name = name
        self.boxes = boxes
        self.choices = []

    def gen_utilities(self):
        for box in self.boxes:
            p = box[1] #  p is the probablity
            r = box[2] #  r is the reward in the box
            c = 5 ###  To Do: generate c with code
            reservation_price = (p * r - c) / p
            self.choices.append((box[0],reservation_price))
        self.choices = dict(self.choices)

    def choose_box(self):
        return max(self.choices, key =self.choices.get)









e1 = Environment('first_experiment')
e1.reward(100)
e1.set_box(5)
print(e1.box)
a1 = Agent('Adam', e1.box)
a1.gen_utilities()
print(a1.choices)
Choice = a1.choose_box()
print(Choice)