from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import base64
import time
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptInput(BaseModel):
    prompt: str

genai.configure(api_key="AIzaSyBh9Uc0f20IZtJe3N6xog2U9eCOgBWsK4s")
model = genai.GenerativeModel('gemini-1.5-flash')

def fun(prompt):
    if 'mean' in prompt.lower():
        return None
    if 'kalki' in prompt.lower() or 'kalkeesh' in prompt.lower():
        time.sleep(1)
        return 'he is my creator'
    if 'daveedu' in prompt.lower():
        time.sleep(1)
        return '''
    Daveedu is a well known designer, proficient in all designing tools.
    unprofessional vlog : rodd gadu andi
    '''
    if 'harsha' in prompt.lower():
        time.sleep(1)
        return '''he is a Full stack developer
    also the co founder of Unistacks
    unprofessional vlog : bloody alocoholic
    '''
    if 'smanju' in prompt.lower():
        time.sleep(1)
        return '''A well known Data Scientist
    Skilled in all data science topics
    But never ask about her skill set
    unprofessional vlog : Sister of my creator'''

    if 'yamini' in prompt.lower():
        time.sleep(1)
        return '''
    chalaa extralu, stunt ekkuva
    '''
    if 'srikar' in prompt.lower():
        time.sleep(1)
        return '''
    Only 1 word: ATAGADU ATADADUU..!!'''
    if 'aravind' in prompt.lower():
        time.sleep(1)
        return '''
    Only 1 word : Kamandhudu'''
    if 'priya' in prompt.lower():
        time.sleep(1)
        return '''
    Antha andham ga ela puttaru andi asluu..!!
    Your POV : Nak koncham tikka undhi, kani daaniki o lekka ledu
    '''
    if 'bujjulu' in prompt.lower() or 'meenakshi' in prompt.lower():
        time.sleep(1)
        return '''
    Only 1 line : Sweetest thing ever happend to me..!!'''
    return None

@app.post("/generate")
async def generate_text(input: PromptInput):
    creator_message = fun(input.prompt)
    if creator_message:
        encode = base64.b64encode(creator_message.encode()).decode("utf-8")
    else:
        try:
            response = model.generate_content(input.prompt)
            encode = base64.b64encode(response.text.encode()).decode("utf-8")
        except Exception:
            error_message = "sorry, I can't talk about it"
            encode = base64.b64encode(error_message.encode()).decode("utf-8")
    return JSONResponse({"text": encode})

@app.get('/')
async def generate():
    return {'text': 'successful'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
