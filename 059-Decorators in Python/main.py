# #Without parameters
# def greet(fx):
#     def mfx():
#         print("Good morning")
#         fx()
#         print("Thanks for using this Function")
#     return mfx

# # @greet
# def hello():    print("Hello World")


# # hello()
# greet(hello)()



#With Parameters
def greet(fx):
    def mfx(*args,**kwargs):
        print("Good morning")
        fx(*args,**kwargs)
        print("Thanks for using this Function")
    return mfx



def add(a,b):
    print(a+b)

greet(add)(1,2)


