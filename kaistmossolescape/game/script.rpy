﻿

#################################################################3333
# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
screen set_name(title, init_name):
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5 yalign 0.5
        vbox:
            spacing 20
            text title xalign 0.5
            input default init_name xalign 0.5

define config.gl2 = True

image Jihyeon = Live2D("Resources/Hiyori", base=.6, loop=True)

image Natori = Live2D("Resources/natori_pro_t06", base=.6, loop=True)

define config.gl2 = True
image Hiyori = Live2D("Resources/Hiyori", base=.6, loop=True)   #짝꿍. 5번녀.. 
image Hitomi = Live2D("Resources/Epsilon", base=.6, loop=True)  #일본인 여자. 4번녀 
image Natori = Live2D("Resources/natori_pro_t06", base=.6, loop=True) # 남자 주인공. 
image Kaistian = Live2D("Resources/230203 vtuber_1", base=.6, loop=True)    #카이녀, 2번녀  INTP 

define j = Character("지현",color="#e38634")

define n = Character("나경",color="#f7e200")

define h = Character("히토미",color="#f73bbe")

define sy = Character("시연",color="#2b69e5")

define sg = Character("슬기",color="#870821")

# 이미지, 동영상 저장하기  
image bg1 :
    "images/N1_bg.jpeg"
    zoom 0.73
image bg2 :
    "images/Room113_bg.jpeg"
    zoom 0.88
image gpt:
    "images/gpt_chat.png"
image blog:
    "images/howtotalktowoman.png"

image bg_dorm:
    "images/bg_dorm.jpg"
    zoom 1.4
image bg_113computer:
    "images/bg_113computer.jpg"
    zoom 1.5
image bg_room113_whole:
    "images/bg_room113_whole.jpg"
    zoom 1.5
image bg_holala:
    "images/bg_holala.jpg"
    zoom 1.5
image bg_kaimaru:
    "images/bg_kaimaru.jpg"
    zoom 1.5
image bg_taepungso:
    "images/bg_taepungso.jpg"
    zoom 1.5
image bg_117:
    "images/bg_117.jpg"


image gptvideo =Movie(play="images/gptvideo.webm",size=(1120,620),loop=False,xalign=0.5,yalign=0.1)
image kakaotalkVideo1 =Movie(play="images/video_kakaotalk1.webm",size=(900,400),loop=False,xalign=0.5,yalign=0.1)
image kakaotalkVideo2 =Movie(play="images/video_kakaotalk2.webm",size=(900,400),loop=False,xalign=0.5,yalign=0.1)
image everytimeVideo=Movie(play="images/video_everytime.webm",size=(1000,500),loop=False,xalign=0.5,yalign=0.1)




# 여기에서부터 게임이 시작합니다.
label start:
    scene bg1
    with fade

    $ name = renpy.call_screen("set_name",title=" 이름을 입력해주세요. ", init_name="이름 입력칸")
    $ school = renpy.call_screen("set_name",title=" 학교를 입력해주세요. ", init_name="학교 입력칸")
    $ p = Character( name , color="#28abf1")

    play music "PerituneMaterial_Sakuya.mp3"

    show Natori mtn_01 exp_03 with dissolve
    
    "대망의 몰입 캠프 날!!!"
    
    "두근두근 카이생의 모쏠 탈출기 시작합니다."

    
    stop music

    jump scene2

    return

label scene2:
    scene bg2
    with fade

    "저기 멀리에서 짝이 보인다. 여자인듯 하다."
    p "짝꿍이 여자네...\n"
    p "초등학교 이후로 여자랑 말을 해본 적이 없는데..."
    p "말은 어떻게 건네야 하지?"

menu :
    "행동을 결정하시오"
    "gpt에게 물어보기":
        jump .gpt    
    "구글링하기":
        jump .google
    

label .gpt:
    show gptvideo
    p "gpt야 도와줘!!" 
    p "역시 gpt는 신이야."
    hide gptvideo with dissolve
    jump scene2_2

label .google:
    show blog at top
    p "구글은 알겠지?"
    p "구글은 신이야"
    hide blog     
    jump scene2_2


label scene2_2:
    with fade
    show Jihyeon m03 m04
    with dissolve

    play music "audio/japanese-corporate-99139.mp3"
    
    "그 때 어떤 귀여운 여자가 앞에 다가온다. 나의 짝꿍이다."
    "사람이 이렇게나 귀여울 수 있구나."
    "심장이 미친 듯이 요동친다"    
    j "안녕~ 너가 태윤이구나! 한 주 동안 잘 부탁해~"
    
    menu: 
        "초반부터 너무 잘해주면 별로겠지?":
            stop music
            p "너가 직접 코딩해보고 판단해!왜 부탁을 해\n 나는 너가 줏대 있는 인간이었으면 좋겟어."
            jump scene2_3_1    
        "최대한 친절하게 대하자!":
            p "그..그래 나..도 잘 부탁해~"
            jump scene2_3_2
            # 말풍선 띄우고, toast로 호감도 하락. 


label scene2_3_1:
    with fade
    j "미친놈인가...쟤랑은 말 섞으면 안되겠다."
    jump scene3

label scene2_3_2:
    with fade
    j "그래ㅋㅋ 나는 이화여대에서 왔는데 너는 어디서 왔어?"
    p "나는 [school]에서 왔어. 이번주 잘해보자"
    stop music
    "여자랑 대화 하는 거 할만하네 후훗. 역시 나야"
    jump scene3





label scene3:
    with fade
    scene bg_room113_whole

    "여학생들이 하나 둘 도착하기 시작했다. 나는 조용히 관찰했다."
    "카이스트 여학생이 멋쩍게 머리를 쳐다보며 소리내어 인사했다."

    show Kaistian
    sy "안녕하세요, 제 이름은 시연입니다. 앞으로 한 주 동안 잘 부탁드려요."
    "그녀는 몹시 츤데레 같은 성격을 가진 것처럼 보였다."
    "다소 냉담하고 거만스러워 보였지만, \n 가끔씩 보여주는 부끄러움이 그녀를 더욱 매력적으로 보이게 했다."
    hide Kaistian with dissolve

    "일본에서 온 유학생, 히토미가 소개를 시작했다."
    show Hitomi m_01 
    with dissolve
    h "콘니치와, 와세다 대학교에서 왔습니다.\n 한국어가 아직 서툴러서 잘 못하더라도 이해해 주세요." 
    "그녀의 말투는 약간 어색했지만, \n그것이 오히려 그녀의 매력을 더욱 부각시켰다."
    hide Hitomi
    
    "이렇게 첫 분반 회의가 시작되었다."    
    "그들과 함께 하는 동안 어떤 일들이 일어날지는 아직 아무도 모른다."    
    "다만 가슴 뛰는 일이 생기길 간절히 바랄 뿐이다."


label scene4:   # 첫날, 강의실 안. 
    
    label scene4_1:
        with fade 
        scene bg_113computer
        
        show Hiyori m04
        j "Recycler View가 너무 어려워.. 너는 이거 다 이해했어?"

        menu:
            "당연하지...너 여태껏 컴공 다니면서 뭐햇어 너 학점 1점대야?":
                jump .scene4_1_a
            #결과: 일주일동안 토라져서 말안하기( 오늘 저녁 같이 못먹음)
            "내가 천천히 설명 해줄게. 리사이클러 뷰는 어쩌구 저쩌구~":
                jump .scene4_1_b
            
        label .scene4_1_a:
            j "나 사실 학점 1.27이야. 학고 받고 집에서 쫓겨나서 몰입캠프 온거야."
            j "비록 사실이라도 말을 그딴식으로 하는 사람이랑 나는 일주일동안 같이 못 지낼 거 같아."
            j "넌 탈락이야!"
            hide Hiyori
            jump end1

        label .scene4_1_b:            
            "개발이 익숙했던 [name]. 1분만에 화면에 연락처 탭을 구현한다."            
            j " 오빠는 정말 똑똑해! \n 세상에 앨런 튜링이랑 오빠만 남는다고 해도 나는 오빠를 택할거야."

            hide Hiyori
            jump scene4_2


    label scene4_2:
        "리사이클러 뷰를 수정 하던 중 디테일이 부족하다는 생각을 한다."
        "실제 번호를 사용하면 디테일이 살지 않을까라는 생각을 한다."
        menu:
            "연락처를 물어본다":
                jump scene4_3_1
            "아..아..니야 아직은 일러. 그녀와 조금 더 친해진 후 연락처를 물어봐야겠어.":
                # 그렇게 첫날이 끝나고 기숙사로 혼자돌아갔다. 
                # 다음날로 이동
                jump scene6
    

    label scene4_3_1:
        show Hiyori m01 m07 m06

        p "여기 연락처 탭 부분에 너 전화번호 좀 써주라."        
        j "지금 내 번호 따는거야? 내 번호 비싼데ㅋㅋ"
        j "그래도 오빠니까 특별히 줄게. 연락 자주하자"
        "방금 그녀가 나한테 연락을 자주하자고 했다...\n심장이 마구 요동친다..이게 사랑인가?"
        #심장 튀어나오는 병맛 애니메이션 있으면 좋을듯.
        jump scene5

    
label scene5:   #새벽 2시, 기숙사. 
    with fade 
    scene bg_dorm  
        
    p "나랑 만나는 게 행운이라고 했어. 그녀도 나와 같은 마음인 걸까?"
    $ renpy.movie_cutscene("images/video_everytime.webm", delay=None, loops=0, stop_music=True)
    p "그녀도 나에게 관심이 있는 것 같아.\n 한 번 연락을 해봐야겠다."

    menu:
        "오늘 정신 없었을 텐데 수고 많았어. 내일 보자.":
            jump scene5_1_a

        "너를 처음 본 순간 나는 심장이 멎는 줄 알았어… \n 천사가 인간으로 태어났으면 너와 같은 얼굴이었을 거라 확신해 나랑 사귈래?":
            jump scene5_1_b

        "아냐.. 아직 일러.. (아무것도 보내지 않는다)":
            jump scene6

label scene5_1_a:
    $ renpy.movie_cutscene("images/video_kakaotalk1.webm", delay=None, loops=0, stop_music=True)
    p "그녀와 조금 더 가까워진 기분이 드는 걸 "
    p "내일은 그녀에게 조금더 적극적으로 다가가봐야지 "

    
label scene5_1_b:
    $ renpy.movie_cutscene("images/video_kakaotalk2.webm", delay=None, loops=0, stop_music=True)
    p "그러자 그녀에게서 연락이 왔다."
    p "설레는 마음으로 카톡창을 열자.."
    show Jihyeon m07 m08 m09
    j "너무 당황스러워!\n 다시는 개인적인 일로 연락하지마!"
    jump end2
 
        
    


label scene6:
    # 술자리 회식
    scene bg_holala

    p "벌써 주말이잖아. 첫 주가 어떻게 지나갔는지 모르겠네."

    j "뭐야~  여기는 몇반이에요? 3반? 나는 2반 나경이야! 뭐야~ 여기 잘생긴 오빠는 이름이 뭐야?"
    menu:
        "나.. 말하는 거야? 나는 xx대학에서 온 xx이야.":
            d " 카이스트에도 이런 인재가 있었구나 담엔 밥 같이 먹어요"
        "저는 xx입니다만, 초면인데 왜. 반말 하시죠? ":
            d " 죄송합니다…제가 무례했네여"
            "갑자기 분위기가 싸해지고, 정적이 흘렀다.."

    label scene6_1:
        "뭐야 뭐야 그러지 말고 술게임이나 해요~"
        "술게임을 하며 분위기가 달아오르고, 다시 시끄러워졌다."
        show Hitomi m05
        "히토미 술 너무 많이 마신 거 아니야?"
        
        menu:
            "나서서 술을 대신 마신다.":
                jump scene6_1_a
            "자기 문제는 자기가 알아서 해야지. 그냥 넘긴다.":
                jump scene7

    label scene6_1_a:
        h "헤에- 오나짱 스고이데스네~ \n 구해줘서 고맙다구.."
        h "오니짱 처럼 든든한 사람은 처음 보는 것 같은데에 "
        h "이따 오니짱이랑 태평소 같이 가도 되는 걸까나.."
        menu:
            p "피곤한데.. 그냥 집에 갈까?"
            "아니야. 국밥 먹고 가자. ":
                jump scene7
            "미안. 국밥은 너혼자 먹고.":
                jump scene8


label scene7:
    # 태평소 국밥
    scene bg_taepungso


label scene8:
    # 카이마루 
    p "어제 너무 많이 마셨나?\n 속이 너무 안좋은 걸."
    p "해장이나 해야겠다"
    scene bg_kaimaru




label end1:
    "그렇게 나는 일주일간 그녀와 아무 말도 할 수 없었고, \n 몰입캠프 전체에  인신공격남으로 소문나게 되어 \n 괴로운 한달을 보내야 했다..."
label end2:
    "그렇게 나는 일주일간 그녀와 아무 말도 할 수 없었고, \n 몰입캠프 전체에  급발진남으로 소문나게 되어 \n 괴로운 한달을 보내야 했다..."