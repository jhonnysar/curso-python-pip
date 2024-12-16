import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return[1,2,3,4,5]

@app.get('/contact',response_class=HTMLResponse)
def get_list():
    return '''
        <h1>Hola soy una paginita en este libro owo</h1>
        <p>Y yo soy su parrafito uwu </p>
    '''

def run():
    store.get_Categories()

if __name__ == '__main__':
    run() 