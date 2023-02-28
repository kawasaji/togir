"""
  _              _      
 | |            (_)     
 | |_ ___   __ _ _ _ __ 
 | __/ _ \ / _` | | '__|
 | || (_) | (_| | | |   
  \__\___/ \__, |_|_|   
            __/ |       
           |___/        
        
    by @kawasaji
    https://github.com/kawasaji/togir

"""

from Package.main import *

print("started?")

if __name__ == '__main__':
    from handler.main_handler import dp

    executor.start_polling(dp, skip_updates=True)
