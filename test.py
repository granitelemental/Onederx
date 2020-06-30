import time
from db import Data

data = Data()


while True:
    print(data.current_time())

    print(data.check_if_time())

    print(data.get_active())

    time.sleep(1)