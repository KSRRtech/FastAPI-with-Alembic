name= 'sai'
print('hello', name)


def method1(text):
    print (text)


method1("how are you?")

def method2(text):
    notes = [{"name":"jay", "id":1},{"name":"john","id":2},{"name":"blr", "id":3}]

    for note in notes:
        if note["id"] == 2:
            print ("found blr"+text +" "+note["name"])


method2("hello")
   