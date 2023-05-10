# -*- coding: utf-8 -*-

# 사회기술-차례대로 순서를 지켜요

import os, sys
import re
import csv
import random
from datetime import datetime
import time

# sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')

sys.path.append('/home/pi/Pibo_Play/')
from data.p_conversation_manage import ConversationManage, WordManage, NLP
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech
import data.behavior.behavior_list as behavior

from openpibo.device import Device

cm = ConversationManage()
wm = WordManage()
nlp = NLP()
audio = TextToSpeech()
   
device = Device()

class Mus():
    
    def __init__(self): 
        self.user_name = '찬익'
        self.score = []
        self.turns = []
        self.reject = []
        
        self.Positive = ['pos', '좋아', '좋은', '좋았', '좋다', '재미있', '재미 있', '재밌', '재밌어']
        self.Negative = ['neg', '별로', '아니', '안 해', '안해', '안 할래', '안 하', '싫어', '싫', '재미없', '재미 없']
        self.Neutral = ['neu', '글쎄', '몰라', '모르', '몰라', '몰랐', '보통']  
        
    
    def bt(self):
        # data = device.get_system()
        while True:
            data = device.send_cmd(device.code_list['SYSTEM']).split(':')[1].split('-')
            result = data[3] if data[3] else "No signal"

            if result == "on":
                print(result)
                # os.system('python3 /home/pi/button_test.py')
                time.sleep(1)
            else:
                continue
                
        
    def mus_8(self):
        pibo = cm.tts(bhv="do_suggestion_S", string=f"곡식 주머니 옮기기 놀이를 해보자!")
             
        
        while True:
            answer = cm.responses_proc(re_bhv="do_waiting_A", re_q=f"준비가 되면 준비 됐다고 말해줘~")
            
            if answer[0][0] == "done" or answer[0][0] == "yes":
                pibo = cm.tts(bhv="do_joy_A", string=f"좋았어. 놀이 방법을 알려줄께!")
                time.sleep(1)                
                pibo = cm.tts(bhv="do_explain_B", string=f"곡식을 넣은 양말은 개미가 열심히 일 해서 마련한 식량이야. 곡식 주머니를 조심히 떨어트리지 않고 머리나 어깨에 얹고 운반해보자!")

                pibo = cm.tts(bhv="do_question_S", string=f"어렵지 않지? 준비 됐으면 시작하자고 말해줘~")
                break
            
            if answer[0][0] == "no":
                pibo = cm.tts(bhv="do_suggestion_S", string=f"그럼 다른 놀이 하자! {wm.word(self.user_name, 0)}가 다시 내 머리를 쓰다듬어주면 돼!")
                sys.exit(0)
                
            else:
                continue
        
        while True:
            answer = cm.responses_proc(re_bhv="do_waiting_A", re_q=f"준비 됐으면 시작하자고 말해줘~")
            
            if answer[0][0] == "done" or answer[0][0] == "yes":
                pibo = cm.tts(bhv="do_explain_A", string=f"좋았어! 먼저 곡식주머니를 만들어보자. 양말에 곡식을 넣은 다음 발목을 묶어줘.")
                time.sleep(1)
                pibo = cm.tts(bhv="do_explain_B", string=f"그 다음은 어디까지 곡식주머니를 옮길지 목표점을 정해보자. 다 했으면 다 했다고 말해줘.")

                break
            else:
                continue
            
        while True:
            answer = cm.responses_proc(re_bhv="do_waiting_A", re_q=f"다 했으면 다 했다고 말해줘.")


            if answer[0][0] == "done" or answer[0][0] == "yes":
                pibo = cm.tts(bhv="do_suggestion_S", string=f"잘했어! 이젠 공을 머리에 얹고 목표점까지 움직여보자~ 다 왔으면 다 왔어 라고 말해줘.")
          
                break
            else:
                continue                         
        


if __name__ == "__main__":
    
    mus = Mus()
    mus.mus_8()