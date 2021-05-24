import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))
stop_words.add(".")
print(stopwords.words('english'))

# compare words distribution
# caption_file_oscar = "/raid/tongtong/haoran/image_caption/ms_image_caption/Oscar/oscar/datasets/Flickr30k/model_0060000/test_flickr_caption.json"
caption_file_oscar = "/raid/tongtong/haoran/image_caption/ms_image_caption/Oscar/oscar/image_captioning/coco_captioning_base_scst/checkpoint-15-66405/pred.model_0060000.test_haoran.beam5.max20.odlabels_coco_format.json"
caption_file_nt2 = "/raid/tongtong/haoran/image_caption/Image-Caption-Event-Detection/neuraltalk2/neuraltalk2/vis/vis.json"

oscar_captions = []
nt2_captions = []

oscar_words = dict()
nt2_words = dict()

# step 1 find overlapping ids
with open(caption_file_oscar,'r') as oscar_file,open(caption_file_nt2,'r') as nt2_file:
    oscar_captions = json.load(oscar_file)
    nt2_captions = json.load(nt2_file)

print(oscar_captions[0])
print(nt2_captions[0])

def incr_1(dic,key):
    if key in dic:
       dic[key] += 1
    else:
       dic[key] = 1

for caption in oscar_captions:
    for word in word_tokenize(caption['caption']):
        if word not in stop_words:
            incr_1(oscar_words,word)

for caption in nt2_captions:
    for word in word_tokenize(caption['caption']):
        if word not in stop_words:
            incr_1(nt2_words,word)


print(len(oscar_words))
print(len(nt2_captions))


# step 2 count word frequency for each
