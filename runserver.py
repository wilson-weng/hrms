# -*- encoding: utf8 -*-

from core import app
from hrms import controller

app.config['DEBUG_TB_HOSTS'] = '127.0.0.1'
app.config['DEBUG_TB_PROFILER_ENABLED'] = True
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
