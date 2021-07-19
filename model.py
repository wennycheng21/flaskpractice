import requests
 
def getImageUrlFrom(query):
    giphy_request_link = "https://api.giphy.com/v1/gifs/search?api_key=gFTrLlmuLVD68qG76B5SBZBa4AHxFR0O&q=dog&limit=25&offset=0&rating=g&lang=en"
    response = requests.get(giphy_request_link).json()
    return response["data"][0]["images"]["fixed_height"]["url"]
def getBeyonceImage(beyonce):
    giphy_request = "https://api.giphy.com/v1/gifs/search?api_key=gFTrLlmuLVD68qG76B5SBZBa4AHxFR0O&q=beyonce&limit=25&offset=0&rating=g&lang=en"
    res = requests.get(giphy_request).json()
    return res["data"][0]["images"]["fixed_height"]["url"]