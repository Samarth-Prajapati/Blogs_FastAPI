from passlib.context import CryptContext
from schemas import User

pwd_cxt = CryptContext(schemes = ['bcrypt'], deprecated = 'auto')

class Hash():
    def bcrypt(password:str):
        return pwd_cxt.hash(password)
    
    def verify(hased_pass, plain_pass):
        return pwd_cxt.verify(plain_pass, hased_pass)