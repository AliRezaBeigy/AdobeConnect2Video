import os

class Struct(object): pass

def execute_ffmpeg(command):
    os.system(f'ffmpeg {command}')

def isMethod(message, cdata):
    return message is not None and \
            hasattr(message, 'Method') and \
            message.Method is not None and \
            hasattr(message.Method, 'cdata') and \
            message.Method.cdata == cdata

def isString(message, cdata):
    return message is not None and \
            hasattr(message, 'String') and \
            message.String is not None and \
            hasattr(message.String, 'cdata') and \
            message.String.cdata == cdata
