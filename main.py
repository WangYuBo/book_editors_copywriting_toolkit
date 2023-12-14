# 服务器端，用来接收和处理前端发来的信息

import uvicorn 
from fastapi import FastAPI,Request
from fastapi.responses import StreamingResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from generate_bot import GenerateBot

app = FastAPI()

myBot = GenerateBot()


# 注意：访问目录给出如下相对路径directory="W3/hard_work/templates"，服务器才能找到index.html，否则若directory="templates"，则服务器认为templates与W3是平级目录；
templates = Jinja2Templates(directory="W3/hard_work/templates")
app.mount("/static", 
          StaticFiles(directory="W3/hard_work/static"), 
          name="static")

class Prompt(BaseModel):
    prompt: str

# 监听前端页面访问服务器根目录，返回index.html
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    #print(request.headers)
    return templates.TemplateResponse("index.html", {"request": request})



# 访问'/generate_bot'，服务器获取用户发来的书名即prompt，调用GenerateBot类的genBook()方法，获取该书的小红书文案
@app.post("/api/generate")
async def generate_bot(data: Prompt):
    #print('test....')   
    stream = myBot.genBook(data.prompt)
    
    return StreamingResponse(stream)
   


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)