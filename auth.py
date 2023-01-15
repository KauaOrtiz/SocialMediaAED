import json

class Signin():
    def __init__(self, username, account):
        self.username = username
        self.account = account
        self.authentication()

    def authentication(self):
        isExist = False
        aux = open('database.json')
        data = json.load(aux)
        for i in data['users']:
            if i["username"]==self.username and i["account"]==self.account:
                print("Conectado")
                isExist = True
                break
        if isExist == False:
            print("Usuário não encontrado, favor realizar login ou tentar novamente")
        aux.close()

class Signup():
    def __init__(self,username,name, account, address, family, friends, someone, customer):
        self.username = username
        self.name = name
        self.account = account
        self.address = address
        self.family = family
        self.friends = friends
        self.someone = someone
        self.customer = customer
        self.authentication()
    
    def authentication(self):
        isExist = False
        aux = open('database.json')
        data = json.load(aux)
        for i in data['users']:
            if i["username"]==self.username:
                print("Nome de usuário existente, tente novamente")
                isExist = True
                aux.close()
                break
        if isExist == False:
            with open("database.json",'r+') as file:
                aux = json.load(file)
                aux["users"].append(self.formatJson())
                file.seek(0)
                json.dump(aux, file, indent = 4)
            print("Cadastro realizado com sucesso!")

    def formatJson(self):
        struct = {
                "username": self.username,
                "name": self.name,
                "account": self.account,
                "address": self.address,
                "family": self.family,
                "friends": self.friends,
                "someone": self.someone,
                "customer": self.customer
                }
        return struct

