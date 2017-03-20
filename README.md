# flickr-images-downloader

A simple Python script to download images with a particular tag from Flickr using its API sorted by interestingness.

### Usage

Obtain the Flick Public Key and Flickr Secret Key from Flickr after signing up.

Past it in the file in the `FLICKR_PUBLIC` and `FLICKR_SECRET` variables resp.

### How to Run 
	$ python get.py

Images will be downloaded and stored with the name `<PhotoID>.jpg`

### Logs

After downloading the images the logs will be stored in the file `data`.

Every line of file `data` contains information about a single image -
	PhotoID Tags OwnerID UserName
Tags are space separated