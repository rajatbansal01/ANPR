from fastapi import FastAPI
import uvicorn
from fastapi import UploadFile,File
from functions import *
from PIL import Image
from io import BytesIO

def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get('/welcome')
def get_name(name:str):
    return {'Welcome in AI world': f'{name}'}

@app.post('/predict')
async def reg_number(file: UploadFile =File(...)):
    content = await file.read()
    nparr = np.fromstring(content, np.uint8)
    number, image = find_num(nparr)
    return {'vehicle number':f'{number}'}

if __name__=="__main__":
    uvicorn.run(app,port=8000,host='127.0.0.1')
