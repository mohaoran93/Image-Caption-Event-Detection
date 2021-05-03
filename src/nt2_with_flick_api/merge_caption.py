# merge caption and flickr api result
import json

flickr_res = "flickr_api/flickr_api_result.json"
caption_res = "neuraltalk2/vis/vis.json"

flickr_json, caption_json = [],[]

with open(flickr_res,'r') as f1,open(caption_res) as f2:
    flickr_json = json.load(f1)
    caption_json = json.load(f2)

caption_dic = {}
for each in caption_json:
    filename = each['file_name'].strip().split("/")[-1]
    caption_dic[filename] = each['caption']

merged_json = []

for each in flickr_json:
    each['caption'] = caption_dic[each['local_img_name']]

print(flickr_json)  
