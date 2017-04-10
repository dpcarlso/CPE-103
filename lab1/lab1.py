# Drew Carlson
# Lab 1
# CPE103



#* Section 1 (Git)

# persnickety



#* Section 2 (Data Definitions)

#* 1) # a Fahrenheit Temperature is a number representing the temperature in Fahrenheit (English units)
      # a Celsius Temperature is a number represeting the temperature in Celsius (SI units)

#* 2) # a Price is a number representing the price of something in cents

#* 3)
# a Name is a string representing the name of an item
# a Price is a number representing the price of the item
# A PriceRecord represents a lists of items at a store
class PriceRecord():
    def __init__(self,name,price):
        self.name = name        # a Name
        self.price = price      # a Price
    def __repr__(self):
        return ("PriceRecord(%r,%r)" % (self.name,self.price))
    def __eq__(self,other):
        return type(other) == PriceRecord and self.name == other.name and self.price == other.price

#* 4)
# a URL is a string that represents the specific address of a website
# a Date is a number that represents the date the URL was visited
# an OpenTab represents the tabs that are open on a web browser
class OpenTab():
    def __init__(self,url,date):
        self.url = url              # a URL
        self.date = date            # a Date
    def __repr__(self):
        return ("OpenTabs(%r,%r)" % (self.url,self.date))
    def __eq__(self,other):
        return type(other) == OpenTab and self.url == other.url and self.date == other.date




#* Section 3 (Signature, Purpose Statements, Headers)

#* 1)

# float float ---> float
# function takes a price and adds the sales tax
def sales(price,tax_per):
    pass

#* 2)

# Database string ---> float
# function accepts the name of an item and returns the price from store's price database
def item_price(database,item_name):
    pass

#* 3)

# Database string ---> float
# function computes median income of a given geographical region using a given database
def get_income(database,region):
    pass

#* 4)

# Database string ---> list
# function takes given geographical region and a database and finds which cities overlap in that region
def city_overlap(database,region):
    pass



#* Section 4 (Test Cases)

#* 1)

# float float float ---> float
# function that takes three numbers and returns the second largest
def second_largest(a,b,c):
    pass
def test_second_largest(self):
    self.assertEqual(second_largest(1,2,3),2)
    self.assertEqual(second_largest(55,11,102),55)

#* 2)

# string --> string
# function accepts a string and returns "True" if string contains a capital letter
def capital_letter(string):
    pass
def test_capital_letter(self):
    self.assertEqual(capital_letter('ABC'),True)
    self.assertEqual(capital_letter('abc'),False)
    self.assertEqual(capital_letter('I once ate a pie'),True)

#* 3)

# string string ---> string
# function returns the "northernmost" of two given states
def northernmost_state(state_1,state_2):
    pass
def test_northernmost(self):
    self.assertEqual(northernmost_state('California','Oregon'),'Oregon')
    self.assertEqual(northernmost_state('Texas','Ohio'),'Ohio')

#* Section 5 (Whole Functions)

#* 1)

# a Length is a float that represents the length of an object

# float ---> float
# function accepts a length in feet and returns a length in meters
def f2m(length):
    given = length                 # a Length
    in_meters = (given * 0.3048)
    return in_meters

#* 2)

# a Pitch is a float representing the frequency of the note in Hertz
# a Duration is a float representing the length of time of the note in seconds
# a MusicalNote represents the sound emitted from an object
class MusicalNote():
    def __init__(self,pitch,duration):
        self.pitch = pitch                # a Pitch
        self.duration = duration          # a Duration
    def __eq__(self,other):
        return type(other) == MusicalNote and self.pitch == other.pitch and self.duration == other.duration
    def __repr__(self):
        return ("MusicalNote(%r,%r)" % (self.pitch,self.duration))

#* 3)

# MusicalNote ---> MusicalNote
# this function accepts a MusicalNote and returns a MusicalNote with double the frequency
def up_one_octave(note):
    new_pitch = (note.pitch * 2)
    new_duration = note.duration
    new_note = MusicalNote(new_pitch,new_duration)
    return new_note


#* 4)

# MusicalNote ---> None
# function mutates note to double frequency and returns None
def up_one_octave_m(note):
    note.pitch = (note.pitch * 2)
    return None


import unittest

class TestCase(unittest.TestCase):
    def test_f2m(self):
        self.assertEqual(f2m(5),1.524)
        self.assertEqual(f2m(1),.3048)
        self.assertEqual(f2m(10),3.048)

    def test_musical_note(self):
        self.assertEqual(MusicalNote(10,10),MusicalNote(10,10))
        self.assertEqual(MusicalNote(.5,1.3),MusicalNote(.5,1.3))

    def test_up_one_octave(self):
        self.assertEqual(up_one_octave(MusicalNote(5,10)),MusicalNote(10,10))
        self.assertEqual(up_one_octave(MusicalNote(12,12)),MusicalNote(24,12))
        self.assertEqual(up_one_octave(MusicalNote(100,2)),MusicalNote(200,2))

    def test_up_one_octave_m(self):                     # Not sure about this
        note = MusicalNote(10,10)
        new = up_one_octave_m(note)
        self.assertEqual(new,None)
        self.assertEqual(note,MusicalNote(20,10))


if __name__ == '__main__':
    unittest.main
