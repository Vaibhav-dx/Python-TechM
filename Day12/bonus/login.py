def login(username: str,password:str)->bool:
    users={
        'vaibhav':'1234',
        'tanmay':'5678'
    }
    return users.get(username)==password
print(login('vaibhav','123'))
print(login('tanmay','5678'))