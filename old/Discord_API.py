'''
Created on Oct 14, 2017

@author: Tyler-OC
'''
import requests

class Discord:
    #url = "https://discordapp.com/api/webhooks/368691847595556864/aR9kQ8VtEy3hz5kWT-ZSx52jNUxrFH6_FD8r4ZwyaipZQPSmxxZhMTBeB2S_mHBKU-iH"
    url = "https://discordapp.com/api/webhooks/369319043540451328/XGUTj23m-f2Vn1fItR5oCKbIIqcJ9kNl-VxB9MxzU3OzyxgAJHjukc_YW0gQQVjl5lkW"
    data = {"content" : "",
            "username" : "",
            "avatar_url" : "",
            "tts" : "",
            "file" : "",
            "embeds" : ""}
    
    def sendMessage(self, content, username = None, avatar_url = None, tts = None, file = None, embeds = None):
        data = self.data
        data["content"] = content
        data["username"] = username
        data["avatar_url"] = avatar_url
        data["tts"] = tts
        data["file"] = file
        data["embeds"] = embeds
        
        request = requests.post(self.url, data)
        print(request)