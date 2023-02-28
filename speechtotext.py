import requests

endpoint = "https://eastus.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=ja-JP&format=detailed"
headers = {
    "Content-Type" : "audio/wav",
    "Ocp-Apim-Subscription-Key": "a8b8864f9c6942679dc6e34369234cd8",
}
response = requests.post(endpoint, headers=headers, data=open("伊豆の踊り子.wav", "rb"))
print(response.text)