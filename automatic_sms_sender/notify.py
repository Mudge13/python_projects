import requests

requests.post("https://ntfy.sh/mihir_topic",
              data="OOGA BOOGA BOO BOO !!!".encode(encoding='utf-8'))
