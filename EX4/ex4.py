Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''
... Parinaz Jahansaz
... 4012061011
... '''
... C=['a','b','c','d','e','f','h','A','B','D','E','F','H']
... N=[1,2,3,4,5,6,7,8]
... #Line 7 to 27 is the range of data and related errors
... CK=input(please enter horizontal position of knight(a,b,c,d,f,g,h) : ' )
... if CK is not in C:
...     print('Horizontal input is not a letter')
... if CK.alpha( )==false:
...     print('Horizontal input is not a proper letter'')
... NK=input(please enter vertical position of knight(1,2,3,4,5,6,7,8) : ' )
... if NK is not in N:
...     print('Vertical input is not a number')
... if NK.alpha( )==false:
...     print('Vertical input for knight is not a proper number')
... CB=input(please enter horizontal position of bishop(a,b,c,d,f,g,h) : ' )
... if CB is not in C:
...     print('Horizontal input is not a letter')
... if CB.alpha( )==false:
...     print('Horizontal input is not a proper letter'')
... NB=input(please enter vertical position of bishop(1,2,3,4,5,6,7,8) : ' )
... if NB is not in N:
...     print('Vertical input is not a number')
... if NB.alpha( )==false:
...     print('Vertical input for knight is not a proper number')
...    
... if CK==CB and NK==NB:
...     print('They can not be in the same square')
...    
... M1=C.index(CK)
... M1+=1
... if M1>8:
...     M1=M1-8
...    
... M2=C.index(CB)
... M1+=1
... if M2>8:
...     M2=M2-8
   
M2=N.index(NK)
M3+=1
if M3>8:
    M3=M3-8
   
M4=N.index(NB)
M4+=1
if M4>8:
    M4=M4-8
#Lines 52 to 63 will check if Knight can attack bishop
KB1=M2-M1
if KB1<0:
    KB1=KB1*-1
KB2=M4-M3
if KB2<0:
    KB2=KB2*-1
if KB1=2 and KB2=1:
    print(Knight can attack bishop)
if KB1=1 and KB2=2:
    print(Knight can attack bishop)
else:
    print(Neither of them can attack each other)
#Lines 65 to 74 will check if bishop can attack knight
BK1=M2-M1
if BK1<0:
    BK1=BK1*-1
BK2=M4-M3
if BK2<0:
    BK2=BK2*-1
if BK1==BK2:
    print(bishop attack can knight)
else:
