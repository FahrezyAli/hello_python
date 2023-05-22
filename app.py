def have_fun():
    for i in range(5):
        print(i)

class Reptile:
    def __init__(self, length):
        self.length = length

class Snake(Reptile):
    def slither(self):
        print("I'm a snake 🐍")

def main():
    hello, hola = 'Hello Python!', 'Hola Python!'

    print(hello)
    
    my_tuple = ('a', 'b')
    
    my_list = [1,2,3]
    
    my_dict = {
    'key': 'value'
    }

    map(lambda x: x * 2, my_list)

    have_fun()

    python = Snake(15)

    python.slither()
    
if __name__ == "__main__":
    main()
