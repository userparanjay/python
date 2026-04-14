from fastapi import HTTPException ,Request
from fastapi.responses import JSONResponse 

async def global_exception_handler(request: Request, exc: Exception): 
    print(exc,request.url,"error11")
    return JSONResponse( 
        status_code=500, 
        content={"message": "Something went wrong"} )

