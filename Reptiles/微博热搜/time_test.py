import time

time = (time.strftime("%Y{y}%m{m}%d{d}%H{h}%M{min}", time.localtime())).format(y='年', m='月', d='日', h='时', min='分')