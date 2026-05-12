from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import StreamingResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx, os, json

app = FastAPI()
security = HTTPBearer()
API_KEY = os.getenv('API_KEY', '')
OLLAMA_URL = 'http://localhost:11434'

def verify_key(creds: HTTPAuthorizationCredentials = Depends(security)):
    if creds.credentials != API_KEY:
        raise HTTPException(status_code=401, detail='Invalid API key')
    return creds.credentials

@app.post('/v1/chat/completions')
async def chat(request: Request, key: str = Depends(verify_key)):
    body = await request.json()
    async def stream():
        async with httpx.AsyncClient(timeout=300) as client:
            async with client.stream('POST', f'{OLLAMA_URL}/api/chat',
                                     json=body) as resp:
                async for chunk in resp.aiter_bytes():
                    yield chunk
    return StreamingResponse(stream(), media_type='application/x-ndjson')

@app.get('/health')
async def health(): return {'status': 'ok'}
