From flask import Flask

app=Flask()

@app.route("/<var>")
def home(var=None):
  return "Hlw bro" +str(var)
  
  
  if __name__=="__name__":
  app.run()
