from docassemble.base.functions import get_config
import requests

def eligibility(name, **kwargs):
  endpoint= get_config("exitpage") + "/api/v1/eligibility"
  r = requests.get(endpoint, params={"name": name, "args": kwargs})
  if r.status_code == 200:
    try:
      r_json = r.json()
      if r_json:
        return r_json.get("data")
    except:
      return None
  return None
