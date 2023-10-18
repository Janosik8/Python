import random
import string


class generator:

    @classmethod
    def generator_hasla(cls, length):
        characters = list(string.ascii_letters + string.digits + string.punctuation)
        random.shuffle(characters)
        password = []

        for i in range(0, length):
            password.append(random.choice(characters))

        random.shuffle(password)

        password = "".join(password)

        return password


obj = generator
print(obj.generator_hasla(15))
