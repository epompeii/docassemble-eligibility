from docassemble.base.functions import get_config
import requests

def get_variable(variable):
  endpoint= get_config("exitpage") + "/api/v1/variables/"
  r = requests.get(endpoint, params={"variable": variable})
  if r.status_code == 200:
    try:
      r_json = r.json()
      if r_json:
        return r_json.get("data")
    except:
      return None
  return None
