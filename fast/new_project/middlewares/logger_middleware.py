from fastapi import Request
async def logger_middleware(req:Request,next):
    print("REQUEST",req.method,req.url,req)
    
    res=await next(req)

    print("RESPONSE",res.status_code,res)
    return res


