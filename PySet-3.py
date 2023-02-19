*1*
def maxi(a,b,c):
    l = [a,b,c]
    print(max(a,b,c))

#*2*
def rev(s):
    l = []
    for i in s:
        l.append(i)
    a = l[::-1]
    revers = ''.join(a) 
    print(revers)
    
#*3*
def palindrome(s):
    if s == s[::-1]:
        print ("is a palindrome")
    else:
        print("is not a palindrome")

#*4*
def wrapping():
    def bold_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<b>{result}</b>"
        return wrapper

    def italic_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<i>{result}</i>"
        return wrapper

    def underline_decorator(func):
        def wrapper(*args,**kwargs):
            result = func(*args, **kwargs)
            return f"<u>{result}<u>"
        return wrapper

    def mono_decorator(func):
        def wrapper(*args,**kwargs):
            result = func(*args, **kwargs)
            return f"<'''>{result}<'''>"
        return wrapper

    @bold_decorator
    @italic_decorator
    @underline_decorator
    @mono_decorator
    def my_text(s):
        return s

    print(my_text("SOS"));

#wrapping()

#*5*
def add(a,b):
    print(a+b) 

def subtract(a,b):
    print(a-b) 

def mmultiply(a,b):
    print(a*b) 

def divide(a,b):
    print(a/b) 

def main():
    a = int(input("Enter a number"))
    b = int(input("Enter a number"))
    while True:
        print('''Press 
        1.Add
        @.subtract
        3.Multiply
        4.Devide''')
        ch = int(input("enter your choice"))

        if ch == 1:
            add(a,b)
        elif ch == 2 :
            subtract(a,b)
        elif ch == 3 :
            mmultiply(a,b)
        elif ch == 4:
            divide(a,b)
        else:
            break
        
#*6*
def snowy():
    print("Use boots")
def rainy():
    print("Use Gumboots")
def sunny():
    print("Use Sneakers")
def main2()
    while True:
        s = input("How is the weather ![sunny , snowy  , rainy]")
        if s == "sunny" or "Sunny":
            sunny()
        elif s == "snowy" or "Snowy":
            snowy()
        elif s == "rainy" or "Rainy":
            rainy()
        else:
            break

