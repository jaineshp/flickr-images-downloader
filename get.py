from flickrapi import FlickrAPI
from pprint import pprint
from os import system as runCommand

FLICKR_PUBLIC = ''
FLICKR_SECRET = ''	

flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format = 'parsed-json')

tag = raw_input("Please enter the tag : ")
number = raw_input("Number of photos to download : ")
response = flickr.photos.search(tags = tag, per_page = number * 4, extras='url_o', privacy_filter = 1)
photos = response['photos']
l = photos['photo']
ids_list = []
for dictionary in l:
	ids_list.append(dictionary['id'])

done = 0

op_file = open('data', 'w')

for id in ids_list:
	if done == number:
		break
	try:
		response = flickr.photos.getInfo(photo_id = id, format = 'parsed-json')
		photo_details = response['photo']
		owner_id = response['photo']['owner']['nsid']
		username = response['photo']['owner']['username']
		list_tags = photo_details['tags']['tag']
		purl = photo_details['urls']['url'][0]['_content']
		all_tags = []
		for d in list_tags:
			all_tags.append(str(d['raw']))
		all_tags = ' '.join(all_tags)
		response = flickr.photos.getSizes(photo_id = id, format = 'parsed-json')
		src = {}
		for i in response['sizes']['size']:
			src[i['label']] = i['source']
		if 'Original' in src:
			runCommand('wget {0} -O {1}.jpg'.format(src['Original'], id))
		else:
			for i in src:
				runCommand('wget {0} -O {1}.jpg'.format(src[i], id))
				break
		op_file.write(str(id) + ' ' + all_tags + ' ' + owner_id + ' ' + username + '\n')
		done += 1
	except:
		pass
op_file.close()
