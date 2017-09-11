def say_hello(person):
   if type(person) == type([]):
      for p in person:
         print ("Hello, %s" % p)
   else:
      print("Hello, %s" % person)


