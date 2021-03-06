# Wasd2Play


![](https://github.com/viktor02/wasd2play/raw/master/img/hello.png)

Open any stream in your favorite player!

### Install
#### From pip
`pip install wasd2play`

#### Manually
`python setup.py install`


### Requirements
`pip install -r requirements.txt`

### Features
* Open live wasd.tv streams

  Ex: `wasd.tv/thedrzj -p vlc`

  Desc: Open live stream THEDRZJ in vlc player

* Open  archived streams 

  Ex: `wasd2play wasd.tv/thedrzj --list`
  
  Ex: `wasd2play wasd.tv/thedrzj --select 2`
  
  or just `wasd2play wasd.tv/thedrzj --last`
  
* Download stream
  
  Ex: `wasd2play thedrzj -d` 
  
  Download stream


### Help
```
usage: wasd2play [options] url

Open any stream in your favorite player!

positional arguments:
  url                   stream url

optional arguments:
  -h, --help            show this help message and exit
  -p YOUR_PLAYER, --player YOUR_PLAYER
                        Point your player
  -l, --last            Open last stream
  -s SELECTED, --select SELECTED
                        Select stream
  -ls [PAGE], --list [PAGE]
                        Show recent streams page by page
  -d, --download        Download stream with ffmpeg

Have a good time!
```