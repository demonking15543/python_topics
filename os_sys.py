import sys, os
def displayhook(value):
    if value:
        sys.stdout.write("Sys is printing...\n")
        print(os.getcwd())
    return

displayhook(5)

a = 5
print(type(5))
print(type(str(a)))
a = "one"
print(bool(a))