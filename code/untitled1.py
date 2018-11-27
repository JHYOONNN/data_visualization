import http.client, urllib.request, urllib.parse, urllib.error
import capture_img as cap_img

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

for i in range (0, cap_img.capture_video()):
    body = open('./capture/%d.jpg' %i, 'rb').read()
    
    conn = http.client.HTTPSConnection('eastasia.api.cognitive.microsoft.com')
    res = conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        
    response = conn.getresponse()
    data = response.read()
    data = str(data)
    #print(data)
    
    point_arr = []
    if(len(data)>10):
        for i in find_text:
            length_of_point = 0
            point_start = data.find(i) + len(i) + 2
            temp = data[point_start + 1]
            while(temp != ','):
                temp = data[point_start + 1 + length_of_point]
                length_of_point += 1
            
            point = data[point_start:point_start + length_of_point]
            point_arr.append(float(point))
    else:
        for i in range(0,4):
            point_arr.append(0)
    print(point_arr)
conn.close()