"""
Lets learn about variables and types. 

A variable is a way to store something. You can think of it as a pickle jar.
The jar can hold 1 pickle, 2 pickles, 1000 pickles, or you could put a muffin in it (why though).

Lets see an example
"""

#A variable named jar and its storing the number 3.
Jar = 3

"""
A type is what type of variable do you have. Is it a number? Is it a letter? Is it a sentence?

Here are some basic types and what they mean. You will learn more as time goes on but these
are the basic ones you should know now:
    int: Short for integer. Its a whole number with no decimal place. ints can't have a decimal.

    float: Short for floating point number. This is a number with a decimal. Can be also be a whole number.

    str: Short for String. This is a sentance.

From the example earlier, you can see that jar is a int since its a whole number.
Now lets make Jar a float.
"""

#The variable Jar being set to 3.5.
Jar = 3.5

"""
When creating a float, you need to remember to add a decimal to the number. If you want to create a whole
number as a float, you do the following
"""

#The variable Jar being set to 3 but still being a float.
Jar = 3.0

"""
Now lets make Jar a string.
"""

#The variable Jar being set to "Jar!".
Jar = "Jar!"

"""
When creating a string, you need to put "" around what you want your string to be.

Now its your turn, You set Jar to something.
"""

#Letting you choose what Jar says now.
Jar = "INSERT HERE"

"""
So now lets do something with are jar. Why not print what you stored in Jar.

Remember from lesson1 on how to print and how we would type in print what we wanted?
Now lets put in our Jar.
"""

#This will print what you set Jar equal to earlier
print(Jar)

"""
Go to command prompt and run "python lesson2.py" and see what happens
"""

"""
Notice how the computer remembered what you typed into Jar and later it printed it when you asked.
This is why variables are useful. You can store something away for a while until you need it later.
"""

"""
You may wonder how do I know what type something is?

Well python is nice enough to give you a function to do so: type().

Lets print out what type Jar is.
"""

#Saves the type of jar to a new variable called JarsType
JarsType = type(Jar)
#Prints JarsType
print(JarsType)

"""
The last thing in this lesson is how do I convert one type to another?

Well python also is nice enough to give you functions to do this as well.

The int(), float(), and str() functions will convert whatever is inside of them to the respective type.

This will only work though if you format them correctly for convertion.

Example:
    str() is the nicest out of all of them and will convert all ints and floats to strings
        str(3) will give you a string set to "3"
        str(3.5) will give you a string set to "3.5"

    float() will convert all ints to floats and correctly formatted strings to floats
        float(3) will give you a float set to 3.0
        float("3") will give you a float set to 3.0
        float("3.5") will give you a float set to 3.5
        float("Pickle") will give you an error
        The string must be a number to be able to conver to a float

    int() will convert all floats and correctly formatted strings to ints
        int(3.5) will give you a int set to 3
            All floats will round down to a whole number
        int(3.99999) will give you a int set to 3
        int("3") will give you a int set to 3
            int() will only accept whole numbers. If you give int() a decimal, it will give you an error
        int("3.5") will give you an error
        int("Pickle") will give you an error
"""

"""
Things you should be able to answer after this lesson:
    What is a variable?
    What is a type?
    What is a int?
    What is a float?
    what is a string?
    How do I create an int, float, and string?
    How do I know what type a variable is?
    How do I convert a type?
"""


"""
Extra!

You can call a function inside a function. 

Example:
    print(type(Jar))

This will print the type of Jar without needing to save it previously,
"""
