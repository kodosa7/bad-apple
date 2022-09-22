# bad-apple
video player of the popular clip in terminal with music

## requirements
- python 3.6+
- pygame

## install
- make sure your venv is set
```
pip3 install -r requirements.txt
```

## run
```
python badapple.py
```

## notes
The video/music sync differs on various systems, so please
try to fiddle with the ```time.sleep(n)``` value in the main script,
where 'n' is the delay value. Default value is ```.0858```.
On Windows, the resize command doesn't work - sorry