
# def verify_token(token:str):
#     try:
#         base = jwt.decode(token, "secret", algorithms=["HS256"])
#     except:
#         print("token error")


# dependency.py script
import jwt
from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials= Depends(security)):
    """
        Function that is used to validate the token in the case that it requires it
    """
    token = credentials.credentials

    try:
        payload = jwt.decode(token, key='secret', options={"verify_signature": False,
                                                           "verify_aud": False,
                                                           "verify_iss": False})
        print("payload => ", payload)
        return payload
    except:  # catches any exception
        raise HTTPException(
            status_code=401,
            detail="Ivalid Token")