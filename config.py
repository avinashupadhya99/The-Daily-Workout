import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '7lBy4UYclr2khl/ViOPO1WbFKTSllV/TCwnf3R+AjBg='