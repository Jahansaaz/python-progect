Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def EX1_5 (x):
...      if x<1:
...          print("infant")
...      if x>1 and x<13:
...          print("child")
...      if x>=13 and x<20:
...          print("teenager")
...      if x>=20:
...          print("adult")
...      '''
...      (int)->str
...      this function receive your age then return the stage of life.
...      example:
...      >>>EX1_5(0.5)
...      infant
...      '''
... 
...      
