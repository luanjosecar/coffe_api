import jwt
from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials= Depends(security)):
    '''
        Validação do token de entrada
    '''
    token = credentials.credentials

    try:
        payload = jwt.decode(token, key='secret', options={"verify_signature": False,
                                                           "verify_aud": False,
                                                           "verify_iss": False})
        print("token Payload => ", payload)
        return payload
    except: 
        raise HTTPException(
            status_code=401,
            detail="Ivalid Token")