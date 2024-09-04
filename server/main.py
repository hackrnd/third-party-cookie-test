from fastapi import FastAPI, HTTPException, Response, Cookie
from fastapi.responses import JSONResponse
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://urban-meme-g4w9qvrgv7wcw94x-3000.app.github.dev"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In a real-world scenario, you'd want to use a secure database
# This is just for demonstration purposes
users = {
    "alice": "pass",
    "bob": "pass"
}

@app.get("/login")
async def login(username: str, password: str, response: Response):
    if username in users and users[username] == password:
        response.set_cookie(key="username", value=username, httponly=True, samesite="none", secure=True)
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@app.get("/user")
async def get_user(username: Optional[str] = Cookie(None)):
    if username:
        return JSONResponse(content={"username": username})
    else:
        raise HTTPException(status_code=401, detail="Not authenticated")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)