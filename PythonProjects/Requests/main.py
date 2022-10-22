import requests
data_petstore = {
  "id": 250,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "bulochka",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.post("https://petstore.swagger.io/v2/pet", json = data_petstore)
print(response.text)

data_petstore1 = {
  "id": 250,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "hleb",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.put("https://petstore.swagger.io/v2/pet", json = data_petstore1)
print(response.text)

response = requests.get("https://petstore.swagger.io/v2/pet/250")
print(response.text)