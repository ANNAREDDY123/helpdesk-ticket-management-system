from fastapi import HTTPException
from jose import jwt, JWTError

SECRET_KEY = "helpdesk_secret_key"
ALGORITHM = "HS256"


def verify_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
