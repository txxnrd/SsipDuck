﻿# 이 파일에 게임 스크립트를 입력합니다.

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
image Hiyori = Live2D("Resources/Hiyori", base=.6, loop=True)   #짝꿍. 5번녀.. 
image Hitomi = Live2D("Resources/Epsilon", base=.6, loop=True)  #일본인 여자. 4번녀 
image Natori = Live2D("Resources/natori_pro_t06", base=.6, loop=True) # 남자 주인공. 
image Kaistian = Live2D("Resources/230203 vtuber_1", base=.6, loop=True)    #카이녀, 2번녀  INTP 

define j = Character("이화 여대생 ")
define h = Character("와세다 유학생 ")
define k = Character("카이스티안")

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
    zoom 0.88
image bg_113computer:
    "images/bg_113computer.jpg"
    zoom 1.3
image bg_room113_whole:
    "images/bg_room113_whole.jpg"
    zoom 1.5
image bg_everytime:
    "images/bg_everytime.jpg"
image bg_kakaotalk:
    "images/bg_kakaotalk.jpg"
image bg_holala:
    "images/bg_holala.jpg"
    zoom 1.5
image bg_kaimaru:
    "images/bg_kaimaru.jpg"
    zoom 1.5
image bg_117:
    "images/bg_117.jpg"


image gptvideo =Movie(play="images/gptvideo.webm",size=(1120,620),loop=False,xalign=0.5,yalign=0.1)
image kakaotalkVideo1 =Movie(play="images/video_kakaotalk1.webm",size=(800,370),loop=False,xalign=0.5,yalign=0.1)
image kakaotalkVideo2 =Movie(play="images/video_kakaotalk2.webm",size=(800,370),loop=False,xalign=0.5,yalign=0.1)
image everytimeVideo=Movie(play="images/video_everytime.webm",size=(800,370),loop=False,xalign=0.5,yalign=0.1)



# 여기에서부터 게임이 시작합니다.
label start:
    scene bg1
    with fade

    play music "a-small-miracle-132333.mp3"


    $ name = renpy.call_screen("set_name",title=" 이름을 입력해주세요. ", init_name="이름 입력칸")
    $ p = Character( name , color="#28abf1")

    show Natori mtn_01 exp_03 with dissolve
    
    p "대망의 몰입 캠프 날!!!"
    p "두근두근 카이생의 모쏠 탈출기 시작합니다."
    
    stop music

    jump scene2

    return

label scene2:
    scene bg2

    with fade
    
  

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

    
    jump scene2_2

label .google:
    show blog at top
    p "구글은 알겠지?"
    p "구글은 신이야"
    hide blog     
    jump scene2_2

label scene2_2:
    with fade

    show Hitomi m_01 m_02
    with dissolve

    p "그 때 어떤 귀여운 여자가 앞에 다가온다. \n 사람이 이렇게나 귀여울 수 있구나."
    
    p "심장이 미친 듯이 요동친다"
    
    j "안녕~ 너가 태윤이구나! 한 주 동안 잘 부탁해~"
    hide Hitomi with dissolve

    menu: 
        "초반부터 너무 잘해주면 별로겠지?":
            p "너가 직접 코딩해보고 판단해!왜 부탁을  해\n 나는 너가 줏대 있는 인간이었으면 좋겟어."
            jump scene3
        "최대한 친절하게 대하자!":
            p "그..그래 나..도 잘 부탁해~"
            jump scene3
    
            # 말풍선 띄우고, toast로 호감도 하락. 






label scene3:
    with fade
    scene bg_room113_whole

    p "여학생들이 하나둘 도착하기 시작했다. 나는 조용히 관찰했다."
    p "카이스트 여학생이 멋쩍게 머리를 쳐다보며 소리내어 인사했다."
    show Kaistian 
    p "안녕하세요, 제 이름은 지현입니다. 앞으로 한주 동안 잘 부탁드려요."
    p "그녀는 몹시 츤데레 같은 성격을 가진 것처럼 보였다. 다소 냉담하고 거만스러워 보였지만, 가끔씩 보여주는 부끄러움이 그녀를 더욱 매력적으로 보이게 했다."
    hide Kaistian with dissolve
    p "일본에서 온 유학생, 유이가 소개를 시작했다. "
    show Hiyori m01 m02
    with dissolve
    h "콘니치와, 와세다 대학교에서 왔습니다. 한국어가 아직 서툴러서 잘 못하더라도 이해해 주세요." 
    p "그녀의 말투는 약간 어색했지만, 그것이 오히려 그녀의 매력을 더욱 부각시켰다."
    hide Hiyori
    p "이렇게 첫 분반 회의가 시작되었다. 그들과 함께 하는 동안 어떤 일들이 일어날지는 아직 아무도 모른다. 하지만 한 주 동안의 몰입캠프가 우리 모두에게 좋은 추억을 선사하기를 기대한다"

label scene4:   # 첫날, 강의실 안. 
    
    label scene4_1:
        with fade 
        scene bg_113computer
        j "Recycler View가 너무 어려워.. 너는 이거 다 이해했어?"
        menu:
            " (실력이 정말 아쉽다..내 여자친구 상대가 되기로는 부족해라고 생각을 한다.) \n 당연하지…너 컴공 다니면서 여태껏 뭐햇어 너 학점 1점대야?":
                jump .scene4_1_a
            #결과: 일주일동안 토라져서 말안하기( 오늘 저녁 같이 못먹음)
            "내가 천천히 설명 해줄게. 리사이클러 뷰는 어쩌구 저쩌구~":
                jump .scene4_1_b
            
        label .scene4_1_a:
            show Hiyori m10 
            j "오빠! 어떻게 나한테 그렇게 얘기할 수 있어! 정말 너무해!"
            hide Hiyori
            jump scene4_2

        label .scene4_1_b:
            show Hiyori m04
            j "정말고마워! 오빠는 진짜 똑똑한 사람인 것 같아.! \n 오빠랑 팀을 해서 행운인 것 같아!"
            hide Hiyori
            jump scene4_2


    label scene4_2:
        p "연락처 덤프데이터가 필요한데.. 어쩌지..?\n 우리 어플리케이션을 위해 그녀의 연락처를 물어볼까?"
        menu:
            "연락처를 물어본다":
                # 그렇게 첫날이 끝나고 기숙사로 혼자 돌아갔다. 
                jump scene5
            "아..아..니야 아직은 일러. 그녀와 조금 더 친해진 후 연락처를 물어봐야겠어.":
                # 그렇게 첫날이 끝나고 기숙사로 혼자돌아갔다. 
                # 다음날로 이동
                jump scene6
    
    
    
label scene5:   #새벽 2시, 기숙사. 
    with fade 
    scene bg_dorm
    
       
        # #에브리타임을 키고 글을 적는 영상.. 
    p "나랑 만나는 게 행운이라고 했어. 그녀도 나와 같은 마음인 걸까?"
    show video_everytime at top

    #에브리타임에서 희망적인 글 발견.
    p "그녀도 나에게 관심이 있는 것 같아.\n 한 번 연락을 해봐야겠다."
    menu:
        "오늘 정신 없었을 텐데 수고 많았어. 내일 보자.":
            jump .scene5_1_a
        "너를 처음 본 순간 나는 심장이 멎는 줄 알았어… \n 천사가 인간으로 태어났으면 너와 같은 얼굴이었을 거라 확신해 나랑 사귈래?":
            jump .scene5_1_b
        "아냐.. 아직 일러.. (아무것도 보내지 않는다)":
            jump .scene5_1_c

    label .scene5_1_a:
        show kakaotalkVideo1 at top
    label .scene5_1_b:
        show kakaotalkVideo2 at top
    label .scene5_1_c:
        


    


label scene6:
    # 술자리 회식
    scene bg_holala
    p "벌써 주말이잖아. 첫 주가 어떻게 지나갔는지 모르겠네."
    j "뭐야~  여기는 몇반이에요? 3반? 나는 2반 oo 야! 뭐야~ 여기 잘생긴 오빠는 이름이 뭐야?"
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
                "헤에- 오나짱 스고이데스네~ ( 내일 연락이 와서 만나자고 한다.)"
                jump scene7
            "자기 문제는 자기가 알아서 해야지. 그냥 넘긴다.":
                jump scene7


label scene7:
    # 카이마루 
    scene bg_kaimaru

    



