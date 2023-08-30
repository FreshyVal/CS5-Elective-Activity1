
class ChatBot:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.properties = {
            "hair_color": "black",
            "eye_color": "brown",
            "height": 165,
            "weight": 55,
            "favorite_color": "blue",
            "favorite_food": "pizza",
            "favorite_movie": "The Shawshank Redemption",
            "favorite_book": "The Lord of the Rings",
            "favorite_animal": "dog",
            "favorite_place": "the beach"
        }

    def get_property(self, property_name):
        return self.properties[property_name]

    def set_property(self, property_name, value):
        self.properties[property_name] = value

    def talk(self):
        user_input = input("What would you like to talk about? ")
        response = ""
        if user_input in self.properties:
            response = "My {} is {}.".format(user_input, self.get_property(user_input))
        else:
            response = "I'm not sure what you mean by that."
        return response


def main():
    chatbot = ChatBot("CS5 Bot", 22, "male")

    while True:
        print(chatbot.talk())


if __name__ == "__main__":
    main()