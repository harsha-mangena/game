import bcrypt
import re

class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    @classmethod
    def create_user(cls, **kwargs):
        hashed_password = bcrypt.hashpw(kwargs['password'].encode('utf-8'), bcrypt.gensalt())
        kwargs['password'] = hashed_password

        return cls(**kwargs)
    
    @staticmethod
    def validate(username, password, retyped_password):
        # Validate username
        if not re.match("^[a-zA-Z0-9_]+$", username):
            raise ValueError("Username must contain only alphanumeric characters and underscores.")
        
        min_length = 8
        if len(password) < min_length:
            raise ValueError(f"Password must be at least {min_length} characters long.")
        
        # Validate password
        if password != retyped_password:
            raise ValueError("Both passwords should be same.")
        
        # Password should contain at least one digit, one uppercase letter,
        # one lowercase letter, and one special character
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
            raise ValueError("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        
        return True

