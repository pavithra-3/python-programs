#decision making
#if condition
if True:
    print('hai')

if False:
    print('hai')

if bool(0):
    print('bye')

if bool(0) or bool(1):
    print('bye')
    
#if condition    
n=input("enter:")
if n:
    print('data is present')
    
#if-else condition
n=input("enter:")
if n:
    print('data is present')
else:
    print('data is not present')

#nested if-else condition
if True:
    print('main if')
    if True:
        print('nested if')
    else:
        print('nested else')
else:
    print('main else')

if True:
    print('main if')
    if True:
        print('nested if')
    else:
        print('nested else')
else:
    print('main else')

#elif condition
if True:
    print('A')
elif True:
    print('B')
elif True:
    print('C')
else:
    print(False)

if False:
    print('A')
elif True:
    print('B')
elif True:
    print('C')
else:
    print(False)

#even or odd
n=int(input("enter:"))
if n%2==0:
    print("even number")
else:
    print("odd number")

#vowel or not
n=input("enter a char:")
if n in 'aeiouAEIOU':
    print("vowel")
else:
    print("not vowel")
    
