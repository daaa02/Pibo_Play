# -*- coding: utf-8 -*-

# 사회기술-큰 소리로 이야기 하거나 통화하지 않아요

import os, sys
import re
import csv
import random
from datetime import datetime
import time
import json

# sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')

sys.path.append('/home/pi/Pibo_Play/')
from data.p_conversation_manage import ConversationManage, WordManage, NLP
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech
import data.behavior.behavior_list as behavior
from data.spread import google_spread_sheet

cm = ConversationManage()
wm = WordManage()
nlp = NLP()
audio = TextToSpeech()
gss = google_spread_sheet()

folder = "/home/pi/UserData"
filename = os.path.basename(__file__).strip('.py')
today = datetime.now().strftime('%m%d_%H%M')
csv_conversation = open(f'{folder}/{today}_{filename}.csv', 'a', newline='', encoding = 'utf-8')
csv_preference = open(f'{folder}/aa.csv', 'a', newline='', encoding = 'utf-8')
cwc = csv.writer(csv_conversation)
cwp = csv.writer(csv_preference)
crc = csv.reader(csv_conversation, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"')


class Com():
    
    def __init__(self): 
        with open('/home/pi/name_config.json', 'r') as f:
            config = json.load(f)        
            self.user_name = config['user_name'] 
        self.aa = ''
        self.score = []
        self.turns = []
        self.reject = []
        
        self.Positive = ['pos', '좋아', '좋은', '좋았', '좋다', '재미있', '재미 있', '재밌', '재밌어']
        self.Negative = ['neg', '별로', '아니', '안 해', '안해', '안 할래', '안 하', '싫어', '싫', '재미없', '재미 없']
        self.Neutral = ['neu', '글쎄', '몰라', '모르', '몰라', '몰랐', '보통']  
                
        
    def com_5(self):
        
        pibo = cm.tts(bhv="do_suggestion_S", string=f"날으는 택배 놀이를 해보자!")
        
        time.sleep(1)
        pibo = cm.tts(bhv="do_explain_A", string=f"이번 놀이는 공 훌라후프, 종이와 그림도구, 가위, 테이프가 필요해!") 
        time.sleep(1)
        pibo = cm.tts(bhv="do_waiting_A", string=f"훌라후프가 없으면 이불이나 수건으로 동그라미 모양을 만들어도 좋아. 준비가 되면 준비 됐어 라고 말해줘~")
        cwc.writerow(['pibo', pibo])        
        
        while True:
            answer = cm.responses_proc(re_bhv="do_waiting_A", re_q=f"준비가 되면 준비 됐다고 말해줘~")
            cwc.writerow(['user', answer[0][1], answer[1]])
            self.reject.append(answer[1])
            
            if answer[0][0] == "done" or answer[0][0] == "yes" or answer[0][0] == "next":
                pibo = cm.tts(bhv="do_joy_A", string=f"좋았어. 놀이 방법을 알려줄께!")
                time.sleep(1)
                pibo = cm.tts(bhv="do_explain_B", string=f"종이에 과일을 그리고 오린 다음에 공에 붙이면 과일 택배가 완성돼. 과일 택배는 손으로 굴려서 훌라후프 동그라미 모양 안에 넣을거야.")
                cwc.writerow(['pibo', pibo])                
                pibo = cm.tts(bhv="do_question_S", string=f"할 수 있지? 할 수 있으면 할 수 있다고 말해줘~")
                break
            
            if answer[0][0] == "no":
                pibo = cm.tts(bhv="do_suggestion_S", string=f"그럼 다른 놀이 하자! {wm.word(self.user_name, 0)}가 다시 내 머리를 쓰다듬어주면 돼!")
                self.score = [0.0, 0.0, 0.0, -0.25]
                cwp.writerow([today, filename, self.score[0], self.score[1], self.score[2],self.score[3]])       
                sys.exit(0)
                
            else:
                continue
        
        while True:
            answer = cm.responses_proc(re_bhv="do_waiting_A", re_q=f"할 수 있으면 할 수 있다고 말해줘~")
            cwc.writerow(['user', answer[0][1], answer[1]])
            self.reject.append(answer[1])
            
            if answer[0][0] == "done" or answer[0][0] == "yes" or answer[0][0] == "next":
                pibo = cm.tts(bhv="do_explain_A", string=f"과일택배를 빠르게 동그라미 안으로 배달해보자! 준비가 되면 시작하자고 말해줘~")
                cwc.writerow(['pibo', pibo])
                break
            else:
                continue
            
        while True:
            answer = cm.responses_proc(re_bhv="do_waiting_A", re_q=f"준비가 되면 시작하자고 말해줘~")
            cwc.writerow(['user', answer[0][1], answer[1]])
            self.reject.append(answer[1])

            if answer[0][0] == "done" or answer[0][0] == "yes" or answer[0][0] == "next":
                pibo = cm.tts(bhv="do_joy_B", string=f"그래애! 시작하자")
                time.sleep(1)
                pibo = cm.tts(bhv="do_suggestion_L", string=f"{wm.word(self.user_name, 0)}가 좋아하는 과일을 그려보자! 다 그렸으면 다 그렸다고 말해줘~")  
                cwc.writerow(['pibo', pibo])                
                break
            else:
                continue                         
        
        while True:
            answer = cm.responses_proc(re_bhv="do_waiting_B", re_q=f"과일을 다 그렸으면 다 그렸다고 말해줘~")
            cwc.writerow(['user', answer[0][1], answer[1]])
            self.reject.append(answer[1])
            
            if answer[0][0] == "done" or answer[0][0] == "yes" or answer[0][0] == "next":
                pibo = cm.tts(bhv="do_joy_B", string=f"우와아~! 정말 맛있어 보이는 걸?")
                time.sleep(1)                
                pibo = cm.tts(bhv="do_suggestion_L", string=f"이제 그림을 오려서 공에 붙이면 과일 택배 완성이야. 다 붙이면 다 붙였어 라고 말해줘~")
                cwc.writerow(['pibo', pibo])                
                break
            else:
                continue
            
        while True:    
            time.sleep(1)
            audio.audio_play(filename="/home/pi/Pibo_Play/data/behavior/audio/sound_dancing.mp3", volume=-1800, background=True)
            answer = cm.responses_proc(re_bhv="do_waiting_A", re_q=f"다 붙이면 다 붙였어 라고 말해줘~")
            cwc.writerow(['user', answer[0][1], answer[1]])
            self.reject.append(answer[1])

            if answer[0][0] == "done" or answer[0][0] == "yes" or answer[0][0] == "next":
                cwc.writerow(['user', answer[0][1], answer[1]])
                self.reject.append(answer[1])
                
                audio.stop()
                pibo = cm.tts(bhv="do_suggestion_S", string=f"좋아. 이제 공을 손으로 굴려서 동그라미 안으로 과일 택배를 배달해 보자!")
                cwc.writerow(['pibo', pibo])
                text_to_speech(text="준비이~~~~ 시이작!")
                audio.audio_play(filename="/home/pi/Pibo_Play/data/behavior/audio/sound_dancing.mp3", volume=-1800, background=True)
                pibo = cm.tts(bhv="do_question_S", string=f"다 옮겼으면 다 옮겼어 라고 말해줘~")                
                break
            else:
                continue
        
        while True:       
            answer = cm.responses_proc(re_bhv="do_waiting_A", re_q=f"다 옮겼으면 다 옮겼어 라고 말해줘~")
            cwc.writerow(['user', answer[0][1], answer[1]])
            self.reject.append(answer[1])

            if answer[0][0] == "done" or answer[0][0] == "yes" or answer[0][0] == "next":
                pibo = cm.tts(bhv="do_compliment_S", string=f"우와아~ 정말 빠르게 배달했는걸? 멋지다아~")
                pibo = cm.tts(bhv="do_compliment_L", string=f"과일 택배를 열심히 배달했어. 고생했어!")
                break
            else:
                continue            
        
        while True:          
            pibo = cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}는 어떤 과일을 좋아하고, 어떤 과일을 싫어해?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"어떤 과일을 좋아하고, 어떤 과일을 싫어해?")
            cwc.writerow(['pibo', pibo])
            cwc.writerow(['user', answer[0][1], answer[1]])
            self.reject.append(answer[1])
            
            pibo = cm.tts(bhv="do_question_S", string=f"정말? 왜?")
            answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"그렇구나. 파이보는 상큼한 향이 나는 과일이 좋아. {wm.word(self.user_name, 0)}는 좋아하는 향기가 있어?")
            cwc.writerow(['pibo', pibo])
            cwc.writerow(['user', answer[0][1], answer[1]])
            self.reject.append(answer[1])
            
            pibo = cm.tts(bhv="do_question_S", string=f"생각만 해도 기분이 좋다~")
            break                    
            
            
        pibo = cm.tts(bhv="do_stop", string=f"{wm.word(self.user_name, 0)}가 열심히 놀이를 했으니, 오늘은 술술 스탬프를 찍어줄께.")
        behavior.do_stamp()
        time.sleep(1)
        
        pibo = cm.tts(bhv="do_suggestion_S", string=f"사진을 찍어 줄게! 과일 택배를 들고 브이해봐!")
        behavior.do_photo()
        
        
        # 3. 피드백 수집
        time.sleep(1)                   
        pibo = cm.tts(bhv='do_question_S', string="파이보랑 노는 거 재미있었어? 재밌었는지, 별로였는지 얘기해줄래?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"파이보랑 노는 거 재미있었어?")        

        if len(answer[0][1]) != 0:
            for i in range(len(self.Negative)):
                if self.Negative[i] in answer[0][1]:
                    self.aa = 'negative'          
            for j in range(len(self.Positive)):
                if self.Positive[j] in answer[0][1]:
                    self.aa = 'positive'                
            if len(self.aa) == 0: 
                self.aa = 'else'
              
        if self.aa == "negative":
            cm.tts(bhv="do_joy_A", string=f"파이보는 {wm.word(self.user_name, 0)}랑 놀아서 재미있었어!")
            self.score = [-0.5, 0.0, 0.0, 0.0]
        
        if self.aa == "positive":
            cm.tts(bhv="do_joy_A", string=f"나도야! 다음에 또 재미있는 놀이 알려줄게.")
            self.score = [0.5, 0.0, 0.0, 0.0]
            
        if self.aa != "negative" and self.aa != "positive": # if answer[0][0] == "neutral":
            cm.tts(bhv="do_joy_A", string=f"{wm.word(self.user_name, 0)}랑 노는 건 정말 재미있어.")
            self.score = [-0.25, 0.0, 0.0, 0.0]
        
        cwp.writerow([today, filename, self.score[0], self.score[1], self.score[2],self.score[3]])

        # 종료 인사
        pibo = cm.tts(bhv="do_joy_A", string=f"나랑 놀아줘서 고마워~")

        # 4. Paradise framework 기록
        turns = sum((self.reject[i] + 1) * 2 for i in range(len(self.reject)))  
        reject = sum(self.reject) 
        
        cwc.writerow(['Turns', turns])
        cwc.writerow(['Rejections', reject])
        cwc.writerow(['Misrecognitions', ])

        cwc.writerow(['%Turns', ])
        cwc.writerow(['%Rejections', ])
        cwc.writerow(['%Misrecognitions', ])

        # 5. 활동 완료 기록
        today_end = datetime.now().strftime('%m%d_%H%M')        
        gss.write_sheet(name=self.user_name, today=f'end_{today_end}', activities=filename)

if __name__ == "__main__":
    
    com = Com()
    com.com_5()