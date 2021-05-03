import flickrapi
import json
import requests
import os
import imghdr

api_key = "8eb125a29103001fd80205c899619704"
api_secret = "0456e2f367e5933d"
img_url_500px_format = "https://live.staticflickr.com/{server_id}/{id}_{secret}.jpg"

save_img_path = "./temp_imgs/"

if not os.path.exists(save_img_path):
    os.makedirs(save_img_path)


flickr = flickrapi.FlickrAPI(api_key, api_secret,format='parsed-json')
recent_photos = flickr.photos.getRecent()['photos']['photo']


res_all = []
for photo in recent_photos:
    try:
        print(photo)
        server_id,id,secret,title = photo['server'],photo['id'],photo['secret'],photo['title']
        
        try:
           loc = flickr.photos.geo.getLocation(photo_id = id)
           latitude = loc['photo']['location']['latitude']
           longitude = loc['photo']['location']['longitude']
        except Exception as e:
           loc = None
           latitude = None
           longitude = None
	
        try:
           tags = flickr.tags.getListPhoto(photo_id=id)
           tags = [e['_content'] for e in tags['photo']['tags']['tag']]
        except:
           tags = []

        print("loc: ",loc)
        print("tags: ",tags)
        img_url = img_url_500px_format.format(server_id=server_id,id=id,secret=secret)
        print(img_url)
        img_content = requests.get(img_url, allow_redirects=True).content
        img_name = server_id+"_"+id+'.jpg'
        open(save_img_path+img_name, 'wb').write(img_content)
        file_type = imghdr.what(save_img_path+img_name)        
        if file_type != "jpeg":
           os.remove(save_img_path+img_name)
           if os.path.exists(save_img_path+img_name):
               print("remove file failed")
           continue
        # print("file_type:",file_type)
        res = {}
        res['imag_id'] = id
        res['loc'] = loc
        res['latitude'] = latitude
        res['longitude'] = longitude
        res['tags'] = tags
        res['url'] = img_url
        res['title'] = photo['title']
        res['local_img_name'] = img_name
        res_all.append(res)
    except Exception as e:
        print(e)
        continue

with open('flickr_api_result.json', 'w') as outfile:
    json.dump(res_all, outfile)
