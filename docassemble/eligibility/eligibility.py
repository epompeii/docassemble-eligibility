from docassemble.base.functions import get_config
import requests
import json

# Get the Service information from Instant Attorney
# using the `org_slug` and `service_slug`.
def get_service(org_slug, service_slug):
  service_endpoint = (
    get_config("exitpage") + "/api/v1/organizations/"
    + str(org_slug) + "/services/" + str(service_slug)
  )
  r = requests.get(service_endpoint)
  if r.status_code == 200:
    try:
      r_json = r.json()
      if r_json:
        return r_json.get("data")
    except:
      return None

  return None

# Get the Eligibility code from Instant Attorney
# using the `eligibility_id`.
def get_eligibility_code(eligibility_id):
  eligibility_endpoint = (
    get_config("exitpage") + "/api/v1/eligibility/" + str(eligibility_id)
  )
  default_code = "def qualify():\n  return -1"
  r = requests.get(eligibility_endpoint)
  if r.status_code == 200:
    try:
      r_json = r.json()
      if r_json and r_json.get("data") and r_json.get("data").get("code"):
        return r_json.get("data").get("code")
    except:
      return default_code
  
  return default_code

# Get the result of an Eligibility function from Instant Attorney
# using the `name` of the function and its required `args`.
def eligibility(name, **kwargs):
  endpoint= get_config("exitpage") + "/api/v1/eligibility"
  r = requests.get(endpoint, params={"name": name, "args": json.dumps(kwargs)})
  if r.status_code == 200:
    try:
      r_json = r.json()
      if r_json and r_json.get("data") and r_json.get("data").get("value"):
        return r_json.get("data").get("value")
    except:
      return None

  return None
