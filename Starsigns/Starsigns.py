# starsigns
# tool to understand and momorize starsigns
# startsigns class is subclass from classes modalities and elements
# next step:


# method ask zodiac month, element and modality
# 3 object attributes: answered right (def 0) & wrong (def 0) and learnfactor (def 0) sigmoid learn factor (def 0.5)
# method ask: changed answered right or wrong and edit LF: +1 wenn richtig, -1 wenn falsch, simgoid learn factor: SLF= =1/(1+EXP(-LF))

# done
# recall only 2 signs
# ask how many to recall 
# recall 5 times
# ask how often recall

class Element():
    ''' element class '''
    def __init__(self,name="",aspect=""):
        '''initialze name and aspect attributes'''
        self.name = name
        self.aspect = aspect

    def get_descriptive_name(self):
        '''return a neatly formatted name and desctiption'''
        if self.aspect != "":
            long_name = "Element " + self.name + " represents " + self.aspect
            return long_name
        else:
            long_name = "Element " + self.name
            return long_name         

    def set_aspect(self,aspect):
        ''' set the the aspect of the element'''
        self.aspect = aspect

    def set_name(self,name):
        ''' set the the name of the element'''
        self.name = name

fire = Element("fire")
fire.set_aspect("action & creativity")

water = Element("water")
water.set_aspect("emotions")

air = Element("air","intellect")
earth = Element ("earth","substance & practicality")

elementsList = [fire,water,air,earth]
for i in elementsList:
    print(i.get_descriptive_name())
    


class Modality():
    ''' class modality '''
    def __init__(self,name="",power=""):
        '''initialze name and power attributes'''
        self.name = name
        self.power = power

    def get_descriptive_name(self):
        '''return a neatly formatted name and desctiption'''
        if self.power != "":
            long_name = "The " + self.name + " modality marks the power of " + self.power
            return long_name
        else:
            long_name = self.name + " modality" 
            return long_name.capitalize()         

    def set_power(self,power):
        ''' set the the power of the modality'''
        self.power = power

    def set_name(self,name):
        ''' set the the name of the modality'''
        self.name = name


cardinal = Modality("cardinal")
cardinal.set_power("initiation")

fixed = Modality("fixed")
fixed.set_power("sustaining")

mutable = Modality("mutable","change")


ModalityList = [cardinal,fixed,mutable]
for i in ModalityList:
    print(i.get_descriptive_name())

class Starsign ():
    '''class starsign with classes Element & Modality as attributes'''
    def __init__(self,name = "",month=""):
        '''initialze name and aspect attributes'''
        self.name = name
        self.month = month
        self.modality = Modality()
        self.element = Element()   

    def get_descriptive_name(self):
            '''return a neatly formatted name and desctiption'''
            if self.modality.name != "" and self.element.name != "":
                long_name = "The starsign " + self.name + " is born in " + self.month + "\nIt's root power is " + self.modality.name + " " + self.element.name
                return long_name
            else:
                long_name = "The starsign " + self.name + " is born in " + self.month
                return long_name
    
    def set_element(self,element):
        '''set the element of a starsign'''
        self.element = element

    def set_modality(self,modality):
        '''set the modality of a starsign'''
        self.modality = modality 
""" 
    def recall_month(self,rounds=5, recall=3):
        ''' recall month of starsign '''
"""
    
aries = Starsign("Aries","april")
print (aries.get_descriptive_name())
aries.set_modality(cardinal)
aries.set_element(fire)
print (aries.get_descriptive_name())
print(aries.modality.power)
print(aries.element.aspect)


taurus = Starsign("Taurus","May")
taurus.set_modality(fixed)
taurus.set_element(earth)
print (taurus.get_descriptive_name())
print(taurus.modality.power)
print(taurus.element.aspect)

gemini = Starsign("Gemini","June")
gemini.set_modality(mutable)
gemini.set_element(air)
print (gemini.get_descriptive_name())
print(gemini.modality.power)
print(gemini.element.aspect)

cancer = Starsign("Cancer","July")
cancer.set_modality(cardinal)
cancer.set_element(water)

leo = Starsign("Leo","August")
leo.set_modality(fixed)
leo.set_element(fire)

virgo = Starsign("Virgo","September")
virgo.set_modality(mutable)
virgo.set_element(earth)

libra = Starsign("Libra","October")
libra.set_modality(cardinal)
libra.set_element(air)

scorpio = Starsign("Scorpio","November")
scorpio.set_modality(fixed)
scorpio.set_element(water)

sagittarius = Starsign("Sagittarius","December")
sagittarius.set_modality(mutable)
sagittarius.set_element(fire)

capricorn = Starsign("Capricorn","January")
capricorn.set_modality(cardinal)
capricorn.set_element(earth)

aquarius = Starsign("Aquarius","February")
aquarius.set_modality(fixed)
aquarius.set_element(air)

pisces = Starsign("Pisces","March")
pisces.set_modality(mutable)
pisces.set_element(water)

StarsignList = [aries,taurus,gemini,cancer,leo,virgo,libra,scorpio,sagittarius,capricorn,aquarius,pisces]
print (len(StarsignList))
for i in StarsignList:
    print(i.get_descriptive_name())
    print(i.modality.get_descriptive_name())
    print(i.element.get_descriptive_name())
    print()


# 

# Recall month of Starsign
import random as rn

# ask how many starsigns to recall 
entered = False
while entered == False:
    try:
        recall = int(input("Recall how many Starsigns? \n1-12: "))
    except ValueError:
        print ("Error: wrong input")
        continue
    except : #catches ctrl-C error
        print ("No!")
        continue
    if  not (1 <= recall <= 12):
        print ("Error: the value is not within permitted range (1-12)")
    else: 
        entered = True

# ask how many rounds of recalling 
entered = False
while entered == False:
    try:
        rounds = int(input("Recall month of Starsign how often?  \n1-10: "))
    except ValueError:
        print ("Error: wrong input")
        continue
    except : #catches ctrl-C error
        print ("No!")
        continue
    if  not (1 <= rounds <= 10):
        print ("Error: the value is not within permitted range (1-10)")
    else: 
        entered = True


for r in range(rounds):
    i = rn.randint(0,recall-1) # recall how many starsigns
    print ("When is the birthday of " + StarsignList[i].name + " ?")
    print (StarsignList[i].month)
    ans = input().lower()
    ans = ans[0:3]
    if ans == StarsignList[i].month[0:3]:
        print ("Yes, it's " + StarsignList[i].month)
    else:
        print ("No, it's " + StarsignList[i].month)


# recall elements and modality
"""

# Recall element of Starsign
import random as rn
i = rn.randint(0,11)
print ("What is the element of " + StarsignList[i].name + " ?")
print (StarsignList[i].element.name)
ans = input().lower()
ans = ans[0:3]
if ans == StarsignList[i].element.name[0:3]:
    print ("Yes, it's " + StarsignList[i].element.name)
else:
    print ("No, it's " + StarsignList[i].element.name)

# Recall modality of Starsign
import random as rn
i = rn.randint(0,11)
print ("What is the modality of " + StarsignList[i].name + " ?")
print (StarsignList[i].modality.name)
ans = input().lower()
ans = ans[0:3]
if ans == StarsignList[i].modality.name[0:3]:
    print ("Yes, it's " + StarsignList[i].modality.name)
else:
    print ("No, it's " + StarsignList[i].modality.name)
    
   
"""