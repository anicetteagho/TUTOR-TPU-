# SYCAM-PUB V217 — Device Attachment

Rattachement à la demande (Termux / 127.0.0.1).

```js
SycamV217.openDevice()
await SycamV217.discoverLocal()
await SycamV217.attach('http://127.0.0.1:8765')
SycamV217.detach()
```

Backend exemple : `backend/termux-local-api-example.py`
