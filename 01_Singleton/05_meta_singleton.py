癤?
'''
Created on 2019. 3. 19.

@author: TY
'''

class MetaSingleton(type):
    _instances = {}
    def __call__(cls,*args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    '''
        __call__ 硫붿냼?쒕뒗 ?대? 議댁옱?섎뒗 ?대옒?ㅼ쓽 媛앹껜瑜??앹꽦?좊븣 ?몄텧?섎뒗 ?뚯씠?ъ쓽 ?뱀닔 硫붿냼?쒕떎. 
        Logger()???대옒?ㅺ? ?앹꽦?섎㈃  MetaSingleton 硫뷀??대옒?ㅼ쓽 __call__ 硫붿냼?쒓? ?ㅽ뻾 ?쒕떎. 
    '''
    
class Logger(metaclass=MetaSingleton):
    '''
            ?꾨Т 濡쒖쭅???놁?留?硫뷀? ?대옒?ㅼ쓽 __call__ 硫붿냼?쒓? 癒쇱? ?ㅽ뻾 ?쒕떎.
    '''
    pass

logger1 = Logger()
logger2 = Logger()

print(logger1,logger2)
