from flask import flask

app=Flask(_name_)

@app.route("/")
def hello():
  """Return a friendly HTTP greeting.

  Returns:
     A string with the words 'hello word!'.

     """
  return "hello word!"

if __name__ =="__cc__":

  app.run(host="127.0.0.1",port=8080,debug=True)
     
