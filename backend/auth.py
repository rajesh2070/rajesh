import jwt
import bcrypt
from datetime import datetime, timedelta

# Secret key for JWT encoding/decoding
SECRET_KEY = 'your_secret_key'

# Function to hash a password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# Function to verify a password
def verify_password(hashed_password, password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Function to create a JWT token
def create_token(user_id):
    expiration = datetime.utcnow() + timedelta(days=30)
    token = jwt.encode({'user_id': user_id, 'exp': expiration}, SECRET_KEY, algorithm='HS256')
    return token

# Function to decode a JWT token
def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Example usage
if __name__ == '__main__':
    user = 'rajesh'
    password = 'test123d$'

    # Hashing the user's password
    hashed_password = hash_password(password)
    print(f'Hashed Password for {user}: {hashed_password}')

    # Creating a JWT token
    token = create_token(user)
    print(f'Token for {user}: {token}')