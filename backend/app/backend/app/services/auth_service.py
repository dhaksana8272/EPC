from passlib.context import CryptContext
from app.core.database import get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)


def create_user(username: str, email: str, password: str):
    db = get_db()
    cursor = db.cursor()

    password_hash = hash_password(password)

    try:
        cursor.execute(
            "INSERT INTO ecplogin (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, password_hash)
        )
        db.commit()
        return True
    except Exception:
        return False
    finally:
        cursor.close()
        db.close()


def authenticate_user(username: str, password: str):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM ecplogin WHERE username=%s",
        (username,)
    )
    user = cursor.fetchone()

    cursor.close()
    db.close()

    if not user:
        return False

    return verify_password(password, user["password_hash"])