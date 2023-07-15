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
image Hiyori = Live2D("Resources/Hiyori", base=.6, loop=True)
image Natori = Live2D("Resources/natori_pro_t06", base=.6, loop=True)
define j = Character("지현")


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
image gptvideo =Movie(play="images/gptvideo.webm",size=(1120,620),loop=False,xalign=0.5,yalign=0.1)

define config.gl2 = True
image Hiyori = Live2D("Resources/Hiyori", base=.6, loop=True)
image Natori = Live2D("Resources/natori_pro_t06", base=.6, loop=True) 
define j = Character("지현",color="#e38634")

# 여기에서부터 게임이 시작합니다.
label start:
    scene bg1
    
    with fade

    play music "a-small-miracle-132333.mp3"

    $ name = renpy.call_screen("set_name",title=" 이름을 입력해주세요. ", init_name="이름 입력칸")

    $ school = renpy.call_screen("set_name",title=" 학교를 입력해주세요. ", init_name="학교 입력칸")
    
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

    hide blog with dissolve
    
    jump scene2_2

label scene2_2:
    with fade

    show Hiyori m03 m04
    with dissolve
    "그 때 어떤 귀여운 여자가 앞에 다가온다. 나의 짝꿍이다."
    "사람이 이렇게나 귀여울 수 있구나."
    
    "심장이 미친 듯이 요동친다"
    
    j "안녕~ 너가 태윤이구나! 한 주 동안 잘 부탁해~"
    
    menu: 
        "초반부터 너무 잘해주면 별로겠지?":
            p "너가 직접 코딩해보고 판단해!왜 부탁을 해\n 나는 너가 줏대 있는 인간이었으면 좋겟어."
            jump scene2_3_1    
        "최대한 친절하게 대하자!":
            p "그..그래 나..도 잘 부탁해~"
            jump scene2_3_2
            # 말풍선 띄우고, toast로 호감도 하락. 
label scene2_3_1:
    with fade

    show Hiyori m03 m04
    with dissolve

    j "미친놈인가...쟤랑은 말 섞으면 안되겠다."
    
    jump scene3

label scene2_3_2:
    with fade

    show Hiyori m03 m04
    with dissolve

    j "그래ㅋㅋ 나는 이화여대에서 왔는데 너는 어디서 왔어?"

    p "나는 [school]에서 왔어. 이번주 잘해보자"

    show Hiyori m03 m04
    with dissolve

    

    "여자랑 대화 하는 거 할만하네 후훗. 역시 나야"


    
    jump scene3




label scene3:
    with fade

    j "여학생들이 하나둘 도착하기 시작했다. 나는 조용히 관찰했다."
    
    j "카이스트 여학생이 멋쩍게 머리를 쳐다보며 소리내어 인사했다."
    
    j "안녕하세요, 제 이름은 지현입니다. 앞으로 한주 동안 잘 부탁드려요."
    
    j "그녀는 몹시 츤데레 같은 성격을 가진 것처럼 보였다."
    j "다소 냉담하고 거만스러워 보였지만, 가끔씩 보여주는 부끄러움이 그녀를 더욱 매력적으로 보이게 했다."

    



    

