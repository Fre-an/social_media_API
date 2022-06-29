from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify(password_attempt, hashed_password):
    return pwd_context.verify(password_attempt, hashed_password)