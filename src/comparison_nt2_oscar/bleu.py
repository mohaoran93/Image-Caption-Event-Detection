from bleu import *

import json

caption_result_path = "/home/neuraltalk2/vis/vis.json"
caption_gt_paht = "/raid/tongtong/haoran/image_caption/dataset/flickr30k_images/results.csv"
# 1000092795.jpg| 0| Two young guys with shaggy hair look at their hands while hanging out in the yard .

image_ids_1 = set()
image_ids_2 = set()


cr = {} # caption result
ct = {} # capption ground truth

with open(caption_result_path,'r') as f1:
    for each in json.load(f1):
        id = each["file_name"].split("/")[-1].replace(".jpg","")
        cr[id] = [each["caption"]]
        image_ids_1.add(id)

with open(caption_gt_paht,'r') as f2:
    for each_line in f2.readlines()[1:]:
        # image_name| comment_number| comment
        # 1000092795.jpg| 0| Two young guys with shaggy hair look at their hands while hanging out in the yard .
        try:
            id,_,caption = each_line.split("|")
        except:
            continue
        id = id.strip().replace(".jpg","")
        caption = caption.strip().replace(" .","")
        image_ids_2.add(id)
        if id in ct.keys():
            ct[id].append(caption)
        else:
            ct[id] = [caption]

over_lapping_ids = image_ids_1 & image_ids_2
with open("overlapping_ids.list","w") as f:
    for id in over_lapping_ids:
        f.write(id+"\n")

cr2 = {}
ct2 = {}
for id in over_lapping_ids:
    cr2[id] = cr[id]
    ct2[id] = ct[id]

# delete ct,cr
print cr2,ct2

bleu = Bleu()
res = bleu.compute_score(ct2,cr2)
print res[0]
