import os, sys
from threading import Thread
from multiprocessing.pool import ThreadPool
from concurrent import futures
from openpibo.device import Device

sys.path.append('/home/pi/Pibo_Play/data')
from data.speech_to_text import speech_to_text

device = Device()

import time


# timelimit = time.time() + 10 

# while time.time() < timelimit:
#     speech_to_text()
#     # print("hh")
    # time.sleep(1)


# def button():
#     touch_count = 0
#     while time.time() < timelimit:
#         data = device.send_cmd(device.code_list['SYSTEM']).split(':')[1].split('-')
#         result = data[1] if data[1] else "No signal"
        
#         if result == "touch":
#             touch_count += 1
#             print("touch:", touch_count)
            
#             if touch_count % 2 == 0:
#                 device.eye_on(255,245,80)
#                 print("ㅂㅂ")
#                 raise Exception("탈출") 
            
#         else:
#             continue
    

# result = []

# t1 = Thread(target=button, args=(), daemon=False)
# t1.start()
# while True:
#     try:
#         # a = speech_to_text()
#         t2 = Thread(target=speech_to_text, args=(), daemon=True)
#         t2.start()
#     except Exception as e:
#         print("TOUCH~!", e)
#         break
# # print(a)




# # try:
# #     # t2 = Thread(target=speech_to_text, args=(), daemon=True)
# #     # t2.start()
# #     a = speech_to_text()
# #     print(a)
# #     # with futures.ThreadPoolExecutor() as executor:
# #     #     future = executor.submit(speech_to_text)
# #     #     return_value = future.result()
# #     #     print("result:", return_value)
    
# # except Exception as e:        
# #         print("AA")
# #         print(e)
        

# # while True:
# #     try:
# #         # # # speech_to_text()        
# #         t2 = Thread(target=speech_to_text, args=(), daemon=True)
# #         t2.start()
# #         break
        
# #         # pool = ThreadPool(processes=2)
# #         # async_result = pool.apply_async(speech_to_text, ())
# #         # return_val = async_result.get()
# #         # break
        
# #         with futures.ThreadPoolExecutor() as executor:
# #             future = executor.submit(speech_to_text)
# #             return_value = future.result()
# #             print("result:", return_value)
# #             break
        
    
# #     except Exception as e:        
# #         print("AA")
# #         print(e)
# #         break

# #     break