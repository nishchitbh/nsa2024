from fastapi import status, HTTPException, Depends, APIRouter

route = APIRouter(tags=['Main Page'])

@route.get("/", status_code=status.HTTP_200_OK)
def main():
    return {"hi": "hello"}

