import re 
from hashlib import sha256
from models import Users

class CreateUser:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    @property    
    def is_authenticated(self):
        if not self.valid_password() or not self.valid_username():
            return False
        
        #Criptografia
        password = sha256(self.password.encode()).hexdigest()
        print(password)
        user = Users(self.username, password)
        user.create()
            
        return True
      
    def valid_password(self):
        print(f'teste de dento do valid password: {self.password}')
        if not self.password:
            return False
        
        elif len(self.password) < 6:
            self.message = self.messages_error('A senha deve ter no mínimo 6 caracteres.')
            return False, self.message
            
        elif not re.search('[0-9]', self.password):
            return False
        
        elif not re.search('[A-Z]', self.password):
            return False
            
        elif not re.search('[a-z]', self.password):
            return False
        
        elif re.search(r'\s', self.password):
            return False #, "A senha não pode conter espaços em branco."
            
        return True
            
    def valid_username(self):
        if not self.username:
            return False
        
        if len(self.username) < 0:
            return False 
                
        elif len(self.username) > 10:
            return False
            
        return True

    def messages_error(self, msg):
        messages = []
        messages.append(msg)
        return messages