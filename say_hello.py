def say_hello(name, city, state):
    name1 = ' '.join(name)
    city1 = ''.join(city)
    state1 = ''.join(state)
    return f'Hello, {name1}! Welcome to {city1}, {state}!'

say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')