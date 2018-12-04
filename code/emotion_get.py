import http.client, urllib.request, urllib.parse, urllib.error
import capture_img as cap_img
import json

find_text = ['anger', 'happiness', 'neutral', 'sadness']

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '0a35f9f9b2984576b501cc35a7dd750c',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
})


class get_emotion:
    def __init__(self, route):
        self.route = route

    def get_emotion_pic(self, pic_num): #get emotion from image
        body = open(self.route + str(pic_num) + '.jpg', 'rb').read()
        conn = http.client.HTTPSConnection('eastasia.api.cognitive.microsoft.com')
        res = conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        response = conn.getresponse()
        data = json.loads(response.read().decode('utf-8'))
        
        point_arr = []
        
        for i in find_text:
            if(len(data) != 0):
                point_arr.append(data[0]['faceAttributes']['emotion'][i])
            else:
                print('cannot get emotion from : {}.jpg'.format(pic_num))
                break
            
        conn.close()
        return point_arr

class main:
    def __init__(self):
        get_image_info = cap_img.main("./video/emotion_test.mp4").return_value()
        
        for i in range(0, get_image_info[0]):
            print(get_emotion(get_image_info[1]).get_emotion_pic(i))

if __name__ == "__main__":
    main()