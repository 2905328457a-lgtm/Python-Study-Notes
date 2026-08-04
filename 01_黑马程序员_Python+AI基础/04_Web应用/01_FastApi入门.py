from fastapi import FastAPI

# 创建FastApi实例
app = FastAPI()

# 定义Api接口
@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/users")
def users():
    return [
        {"name": "张三"},
        {"name": "李四"},
        {"name": "王五"}
    ]

# 启动服务 ——> uvicorn 01_FastApi入门:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)