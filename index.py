import os

def bootstrap():
    print('Fumiko: Первый запуск.')
    f = open('.index_bootstrap', 'w')
    f.write('')
    f.close()
    os.system('/usr/local/bin/python -m pip install -r requirements.txt')
    import FumikoBot

def start():
    print('Fumiko: Запуск.')
    import FumikoBot

if '.index_bootstrap' in os.listdir('.'):
    start()
else:
    bootstrap()
