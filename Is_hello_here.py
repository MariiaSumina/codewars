def validate_hello(greetings):

    #solution one
    #greetings = greetings.lower()
    #if "hello" in greetings:
       # ans = True
    #elif "ciao" in greetings:
        #ans = True
    #elif "salut" in greetings:
        #ans = True
    #elif "hallo" in greetings:
        #ans = True
    #elif "hola" in greetings:
        #ans = True
    #elif "ahoj" in greetings:
        #ans = True
    #elif "czesc" in greetings:
        #ans = True
    #else:
        #ans = False
    #return ans

   #solution two
   g = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for s in g:
        if s in greetings.lower():
            return True
    return False