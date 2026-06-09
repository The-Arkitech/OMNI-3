import os
import sys
import socket
import threading
import time
import sqlite3
import ssl
import json
import paho.mqtt.client as mqtt
from datetime import datetime

class _109485736:
    def __init__(self):
        self._948572104 = "0.0.0.0"
        self._284751930 = "0.0.0.0"
        self._748392015 = 0
        self._483920157 = [0]
        self._194857302 = "000000000.db"
        self._583920147 = True
        self._384752910 = False
        self._847592014()

    def _847592014(self):
        with sqlite3.connect(self._194857302) as c:
            c.execute("""
                CREATE TABLE IF NOT EXISTS _573920148 (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ts TEXT,
                    st TEXT,
                    comp TEXT,
                    msg TEXT
                )
            """)
            c.commit()

    def _294857103(self, st, comp, msg):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with sqlite3.connect(self._194857302) as c:
            c.execute("INSERT INTO _573920148 (ts, st, comp, msg) VALUES (?, ?, ?, ?)", (ts, st, comp, msg))
            c.commit()

class _394857201:
    def __init__(self, ctx):
        self._109485736 = ctx

    def _739201485(self):
        while self._109485736._583920147 and not self._109485736._384752910:
            for p in self._109485736._483920157:
                if self._109485736._384752910: break
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                r = s.connect_ex((self._109485736._948572104, p))
                if r == 0:
                    self._109485736._294857103("000000000", "000000000", f"000000000 {p}")
                s.close()
            time.sleep(5)

class _849302157:
    def __init__(self, ctx):
        self._109485736 = ctx

    def _928475103(self, payload):
        try:
            d = json.loads(payload)
            if d.get("sig") == "000000000":
                self._483920148()
        except Exception:
            pass

    def _483920148(self):
        self._109485736._384752910 = True
        self._109485736._583920147 = False
        self._109485736._294857103("000000000", "000000000", "000000000")
        try:
            if os.path.exists(self._109485736._194857302):
                os.remove(self._109485736._194857302)
        except Exception:
            pass
        sys.exit(0)

class _583920154:
    def __init__(self, ctx, exe):
        self._109485736 = ctx
        self._849302157 = exe
        self._194857203 = mqtt.Client()
        self._194857203.on_message = self._384751920

    def _384751920(self, c, u, m):
        p = m.payload.decode()
        self._109485736._294857103("000000000", "000000000", f"000000000: {m.topic}")
        self._849302157._928475103(p)

    def _847592013(self):
        try:
            self._194857203.tls_set(cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2)
            self._194857203.connect(self._109485736._284751930, self._109485736._748392015, 60)
            self._194857203.subscribe("000000000")
            self._194857203.loop_start()
        except Exception as e:
            self._109485736._294857103("000000000", "000000000", str(e))

class OMNI3:
    def __init__(self):
        self._294857201 = _109485736()
        self._847592015 = _394857201(self._294857201)
        self._483920154 = _849302157(self._294857201)
        self._194857304 = _583920154(self._294857201, self._483920154)

    def run(self):
        self._294857201._294857103("000000000", "000000000", "000000000")
        self._194857304._847592013()
        
        t = threading.Thread(target=self._847592015._739201485)
        t.daemon = True
        t.start()

        try:
            while not self._294857201._384752910:
                time.sleep(1)
        except KeyboardInterrupt:
            self._294857201._583920147 = False
            sys.exit(0)

if __name__ == "__main__":
    app = OMNI3()
    app.run()
