import bottle
import model

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')