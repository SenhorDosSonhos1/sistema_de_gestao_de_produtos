import re 
from hashlib import sha256
from models import Users

class CreateUser:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    #Verifica se os campos estão validos e cria se for True
    @property    
    def is_authenticated(self):
        if not self.valid_password() or not self.valid_username():
            return False
        
        #Criptografia
        password = sha256(self.password.encode()).hexdigest()
        user = Users(self.username, password)
        user.create()
            
        return True
      
    def valid_password(self):
        if not self.password:
            self.message = self.messages_error('O campo senha não pode está vazio.')
            return False
        
        elif len(self.password) < 6:
            self.message = self.messages_error('A senha deve ter no mínimo 6 caracteres.')
            return False 
            
        elif not re.search('[0-9]', self.password):
            self.message = self.messages_error('A senha deve conter pelo menos um numero inteiro.')
            return False
        
        elif not re.search('[A-Z]', self.password):
            self.message = self.messages_error('A senha deve conter pelo menos uma letra maiuscula.')
            return False
            
        elif not re.search('[a-z]', self.password):
            self.message = self.messages_error('A senha deve conter pelo menos uma letra minuscula.')
            return False
        
        elif re.search(r'\s', self.password):
            self.message = self.messages_error('A senha não pode conter espaços em branco.')
            return False
            
        return True
            
    def valid_username(self):
        if not self.username:
            self.message = self.messages_error('O campo usuário não pode está vazio.')
            return False
        
        if len(self.username) < 3 and len(self.username) > 10:
            self.message = self.messages_error('O campo deve ter no mínimo 3 caracteres e no máximo 10 caracteres.')
            return False 
            
        return True

#Lançamento das mensagens de error
    def messages_error(self, msg):
        return msg