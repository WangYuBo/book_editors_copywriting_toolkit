# 导入相关的库
import uvicorn # uvicorn库是做什么用的？起服务器的，似乎可以直接调用run()方法来起一个服务；里面的uvicorn.Server是什么作用？
from fastapi import  FastAPI, Request,Form
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


# 用相对路径，复用W2中get_book_info.py中的DouBanBookUtil类
from ...W2.get_book_info import DouBanBookUtil

# 引入小红书文案生成方法generate
from ...W2.generate_xsh import generate


# 创建一个FastAPI实例
app = FastAPI()
print("实例化 FastAPI")

# 创建一个数据模型，用于接收和发送数据
class Item(BaseModel):
    id: int
    name: str

# 创建一个路由，接收get请求，请求路径为服务器根路由
@app.get("/",response_class=HTMLResponse)
def root():
    print("接收到get访问请求，进入服务端根路由")
    return "Hello World!This is a FastAPI project."


# 创建一个路由，接收post请求，请求路径为/api/get
@app.post("/api/get",response_class=HTMLResponse)
def get(request: Request):
    print("接收到post请求，进入服务端根路由")
    return "Hello World!This is a FastAPI project."

# 创建一个路由，接收get请求，请求路径为/api/get
@app.get("/api/get",response_class=HTMLResponse)
def get(request: Request):
    return "Hello! This is route /api/get from get()."


# 创建一个"/name/lilei"的路由，接收get请求，访问这个路由时，调用getName()方法
@app.get("/name/lilei",response_class=HTMLResponse)
def getName():
    print("接收到访问lilei请求，进入服务端/name/lilei")
    return "Hello, lilei!"




# 创建一个"/index"的路由，访问这个路由时，调用getIndex()方法，访问index.html
@app.get("/index",response_class=HTMLResponse)
def getIndex():
    print("访问/index的路由，调用getIndex()方法，访问index.html")
    return "Hello, lilei!"



# 创建一个路由，接收POST请求，请求路径为/items；异步；
@app.post("/items/")
async def create_item(item: Item):
    # 返回接收到的数据，item.name应为图书名字
    print("接收到POST请求,图书名字为"+item.name)
    # 根据书名调用豆瓣读书API，找到该书目的摘要
    #summary = DouBanBookUtil().get_book_summary_by_name(item.name)
    
    # 调用智谱AI api接口，根据书名生成小红书文案

    return {"name":  item.name}


if __name__ == "__main__":
    print("启动服务")
    uvicorn.run(app, host="127.0.0.1", port=1234)
    