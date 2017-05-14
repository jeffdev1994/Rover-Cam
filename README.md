# Rover-Cam

webapp to see what the puppy is doing

intended to be run off raspberry pi 3 with webcam attached

## Getting Started

### From Root of `webapp`:

* pip install -r requirements.txt

* create ssl files
```
openssl genrsa 1024 > host.key
chmod 400 host.key
openssl req -new -x509 -nodes -sha1 -days 365 -key host.key -out host.crt
```

* Create config.py
```python
import uuid

class Config:
    def __init__(self):
        self.password = ""
        self.users = {}
        self.secretKey = ""
        self.cameraURL = ""

config = Config()
```

* ./webServer.py
