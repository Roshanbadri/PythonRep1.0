import json
from flask import Flask
app = Flask(__name__)

jstr = {'BuildNumber':'345', 'Variant':'10L', 'RegionalCode':'IND'}
json_string = json.dumps(jstr)
print type(json_string)
@app.route('/flask')
def hello_flask():
  
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return json_string

if __name__ == '__main__':
   app.run(port=5000,debug=True)