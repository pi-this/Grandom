import time

class grandom:
    def value(allow_negative=True):
        guti_string = str(time.time())
        guti_int = int(guti_string[-1:11:-1]) # pulls the last 5 digits from the guti_string and reverses them
        # then converts to int value

        # The guti int formula creates a simulation of a random number
        gutiif = round(time.time()*guti_int/2)
        
        if int(str(gutiif)[0]) > 5 and allow_negative:
            return gutiif*-1
        
        return gutiif
    
    def unit(allow_negative=True):
        if allow_negative:
            value = int(str(grandom.value(allow_negative=True))[0:2:1])
            if str(value)[0] == "-":
                return value
            else:
                return int(str(value)[1])
        else:
            return int(str(grandom.value())[1])
        
    def letter(upper=False): # should be between 10 and 99
        # meaning 89 options
        # I want 97-122
        option_value = int(str(grandom.value(allow_negative=False))[0:2])
        ascii_value = ( (25/89) * (option_value-10) ) + 97
        # ^ formula for converting a 10-99 range of the option_value
        # to the 97-122 range for the lower case letters of the ascii_value range
        if upper:
            return chr(round(ascii_value)).upper()
        return chr(round(ascii_value))

    
    def word():
        letter1 = grandom.letter()
        letter2 = grandom.letter()
        letter3 = grandom.letter()
        if letter1 in "aeiou":
            vowel = letter1
            constant1 = letter2
            constant2 = letter3
            
        elif letter2 in "aeiou":
            vowel = letter2
            constant1 = letter1
            constant2 = letter3
        elif letter3 in "aeiou":
            vowel = letter3
            constant1 = letter1
            constant2 = letter2
        else:
            return "No vowels."
        
        # this runs if there is a vowel
        # the vowel is put in the middle
        return constant1+vowel+constant2
    
    def coin_flip(output=str):
        """
        The grandom.coin_flip() function will flip a coin into "heads" or "tails", but because I want
        to allow for further customization later on I want to by default have a string output, but allow for
        an integer output aswell. I will create a parameter for this function called 'output'.
        """
        
        # to generate a coin flip I will use the grandom.value() % 2 to return an odd or even value (1 or 0)
        if output == int:
            return grandom.value() % 2
        if output == float:
            return float(grandom.value() % 2)
        if output == str:
            return "heads" if not grandom.value() % 2 else "tails"
        if output == bool:
            return True if not grandom.value() % 2 else False
    
    
    def grange(start=0, end=10):
        result = 0
        for i in range(start, end):
            result += grandom.coin_flip(output=int)
            
        return result+start # this is to allow a range of 3-5 or another example would be 5-10 or even -3 to 2. Instead of limiting 0-N, the code now allows N-N
    
    def die(sides=6):
        
        return grandom.grange(1,sides+1) # add 1 to that way it includes 6
        # as neat as this is... It is nothing at all 'random'. It is so rigged.
        # I ran it maybe 30 times and it only rolled 1 once.
    def dice(count=1, sides=6):
        
        rolls = []
        
        for amount in range(count):
            rolls.append(grandom.die(sides=sides))
        return rolls
        
        
        """
        here is what I am going to do...
        
        
        I need to do a grandom.range(0,10)
        Which will choose a random number between 0 and 10
        To do this I should use one of these functions:
        
        grandom.unit()
        or
        grandom.value()
        
        There are multiple ways I can reach this problem, but my first idea is to do this...
        I will use grandom.unit() and see if the value is odd or even. Example:
        if grandom.value() % 2 == 0:
            return "even"  
        else:
            return "odd"
            
        The classic "odd" or "even" logic combined with the grandom.value() function will
        create a random generation between the values of 0 and 1. (odd or even.)
        
        Now here is my next thought. Knowing that I am able to do this I should translate thoese values into 1 and 0.
        return grandom.value() % 2 # This way I am able to create a result of either 1 or 0 without even using the if statement
        Ok. I have a random 1 or 0 value, but how do I turn this into a ranged value of 0 through 10 or anything else to replace the number ten?
        Lets start with this thought. I initially had the idea of creating a 0 and 1 similar to a coin flip due to the idea of adding each randomly generated
        0 or 1 to create our desired output. I'll later explain after I create a new function: coin_flip()
        """
        
        """
        Now that I have grandom.grange I can do the next challenge. Which is... grandom.list(["green", "blue", "yellow", "red"])
        I am aware that in creating a function called list I am using a built in function, but right now I don't care because it will always be called as grandom.list and NOT list.
        I may change the name later.
        """
        
    def list(items):
        # I am going to pick a random number using the new grandom.grange() function
        # then I am going to return the index value of the list from that grandom.grange() function
        
        # start=0 because all lists start with 0
        # end=len(items)-1 because I need the end to be at the end of the list. The end of the list isn't the length of it because len starts with 1, while index starts with 0
        value = grandom.grange(start=0, end=len(items)-1)
        
        return items[value]
        
            


        
    
#     def dice(count=1, sides=6):
#         try:
#             if sides % grandom.unit() == 0:
#                 return 1
#             else:
#                 return sides % grandom.unit() == 0
#         except:
#             return 1
        
"""
This is a random project.
I would like this to become a Python 3 module called Grandom

The objective of the Grandom module is to add a new perspective and muliple options to random
This will replace the random module with other opprotunities.

I plan on having a function that randomly generates words from randomly generated letters
Randomly generated words can be turned into randomly generated sentences

The idea here is that this module will created random sentences by running a grandom command

Question:
If I have say 1 vowel and 1 letter how might I randomly move thoes letters to make a word

Another question:
what if I added 3 letters. 1 vowel and 2 constanints?
"""

#print(grandom.value())
#print(grandom.unit())
# print(grandom.dice())
#print(grandom.word())
if __name__ == "__main__":
    #print(grandom.grange(start=1, end=5))
    #print(grandom.list(["red", "green", "blue"]))
    for i in range(20):
        print(grandom.unit())

"""
Find the pattern and create the word.

• Consonant Digraphs: ch, sh, th, ph, wh, ck, ng.
• Vowel Digraphs (Diphthongs): ea, ee, ai, oo, ou, oi, ay

• Vowels: [a, e, i, o, u]
• Vowel Blends: [ee, ea, ai, oo, ou, ay, ie]
• Single Consonants: [b, c, d, f, g, h, j, k, l, m, n, p, r, s, t, v, w, z]
• Start Clusters: [st, bl, cl, fl, pr, tr, br, cr, fr, gr, ch, sh, th, wh]
• End Clusters: [nt, nd, st, ck, mp, nk, lt, ld, ch, sh, th, ng]

• CV (e.g., go, me)
• CVC (e.g., pad, tin)
• StartCluster + Vowel + Coda (e.g., stop, thin)
• Onset + VowelBlend + EndCluster (e.g., paint, reach)


"""


"""
functions now available:
grandom.value(allow_negative=True) # returns a 'random' value assosiated with time (may be negative or positive)
grandom.unit(allow_negative=True) # returns a 'random' value between -9 and +9, unless allow_negative == False
grandom.letter(upper=False) # returns a 'random' letter from the 26 letters of the english alphabet. (by default the letters are lowercase)
grandom.word() # returns a 'random' 3 letter word with 1 vowel. (this function is still a word in progress)
grandom.coin_flip(output=str) # returns a 'random' string ("heads" or "tails"), unless the output parameter is set to a differet type. bool: True or False, int: 1 or 0, float: 1.0 or 0
grandom.grange(start=0,end=10) # returns a 'random' integer value between the start integer and the end integer. These values may be any integer. (negative or positive.)
grandom.list(items) # returns a 'random' value from the given list. This function is the first function without an input default.

Next function to make:
grandom.dice(count=2, sides=6)
# next I want to make a dice function that returns a tuple: return dice1, dice2

My idea on how this will be done is to use the grandom.grange function that set a variable to a random value from 1-sides: grandom.grange(1,sides)
One die is easy, it would mean I simply roll it one time

I do a for amount in range(count): and for every time the loop is done I add another grandom.grange to the loop

Next step after this: Custom sides. Some dice are unique in the sense that they start with 0, or maybe skip 3. Or even have a message or picture on the die.
Next after this do a deck of playing cards...
"""