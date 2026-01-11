# modules , comments and pip in chapter 1
# using pip install (module name) we can install modules and packages 


import pyjokes # importing a module
print ("printing jokes .....")
joke = pyjokes.get_joke() # using a function from the module
print(joke)


"""
# comments in python
1. single line comment - use #
2. multi line comment - use ''' or 
"""

import pyttsx3
engine = pyttsx3.init()
engine.say('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.
''')
engine.runAndWait()