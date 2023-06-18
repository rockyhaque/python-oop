#function is a first class object

def double_decker():
    print('Starting the double decker')
    def inner_fun():
        print('Inside the inner')
        return 2000
    return inner_fun

# print(double_decker())
# print(double_decker()())

def do_something(work):
    print('Work started')
    # print(work)
    work()
    print('Work ended')

# do_something(33)
# do_something('heii')

def coding():
    print('Python programming')

# do_something(coding)
def sleeping():
    print('sleeping and dreaming in python')

do_something(sleeping)
