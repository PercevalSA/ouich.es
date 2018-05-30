# ouich.es

Simple python script to download quotes (text + audio) from http://ouich.es

## Quick Start

```bash
pip3 install bs4 json requests wget
python3 download.py
```

## output

* `sounds.json` : list all text quotes as in [kaamelott soundboard](https://github.com/2ec0b4/kaamelott-soundboard/blob/master/sounds/sounds.json)
* `*.mp3` : all audio quotes downloaded