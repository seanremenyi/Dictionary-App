import requests
import json

class Definition():
    def __init__(self, word):
        self.word = word

    def get_definition(self):
        with open("definitions.json", 'r') as f:
            files = f.read()
            fileloads = json.loads(files)
            try:
                self.definitions = fileloads[self.word]
            except:
                self.api_call()
                self.add_to_json()
                self.get_definition()


    def api_call(self):
            listof = []
            json_string = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{self.word}")
            jsons = json.loads(json_string.text)
            definitions_list = jsons[0]["meanings"][0]["definitions"]
            for definition in definitions_list:
                    listof.append(definition["definition"])
            self.definitions = listof[:]

    def add_to_json(self):
        with open("definitions.json", "r") as f:
            dictionary = f.read()
            dictionaryjson = json.loads(dictionary)
            dictionaryjson[self.word] = self.definitions
        with open("definitions.json", "w") as f:
            json_string = json.dumps(dictionaryjson)
            f.write(json_string)


def main():
    while True:
        user_input = input("What word do you want to look up: ")
        if user_input == 'quit':
            break
        new = Definition(user_input)
        new.get_definition()
        print("************")
        print(new.word, new.definitions)
        

main()