from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
# import google.generativeai as genai
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class PromptInput(BaseModel):
#     prompt: str

# genai.configure(api_key="AIzaSyBh9Uc0f20IZtJe3N6xog2U9eCOgBWsK4s")
# model = genai.GenerativeModel('gemini-1.5-flash')

# @app.post("/generate")
# async def generate_text(input: PromptInput):
#     response = model.generate_content(input.prompt)
#     encode = base64.b64encode(response.text.encode()).decode("utf-8")  
#     return JSONResponse({"text": encode})

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get('/')
async def generate():
    return {'text': 'successful'}