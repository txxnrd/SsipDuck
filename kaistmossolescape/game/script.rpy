
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
image Nakyeong = Live2D("Resources/RACOON01", base=.6, loop=True)

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
image kaist_nightwalk:
    "images/bg_nightwalk.jpg"
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
    zoom 1.3
image bg_117:
    "images/bg_117.jpg"
image bg_zakyo:
    "images/bg_zakyo.jpg"
    zoom 1.4
image soju:
    "soju-straight.png"
    0.5 #this part defines how long to wait before next frame
    "soju-not_straight.png"
    0.5
    repeat



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
    
    "두근두근 [school] 모쏠 탈출기 시작합니다."   

    stop music

    jump scene2

    return

label scene2:
    scene bg2
    with fade

    "저기 멀리에서 짝이 보인다. 여자인듯 하다." # 지현이 작게 넣기
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
    
    p "gpt가 하라는 대로만 해야겠다."

    hide gptvideo with dissolve

    
    jump scene2_2

label .google:
    show blog at top
    p "구글은 알겠지?"

    p "역시 고수는 달라...이 블로그 N회독 해야겟다."

    hide blog with dissolve
    jump scene2_2


label scene2_2:
    with fade
    show Jihyeon m03 m04
    with dissolve

    play music "audio/japanese-corporate-99139.mp3"
    
    "그 때 아까 어렴풋이 보이던 귀여운 여자가 앞에 다가온다. 나의 짝꿍인 듯하다."
    
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
    jump scene6
    
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


    show soju at truecenter

    "사람들의 대화와 웃음이 점차 풍성해져간다."
    "그러던 중 인싸 향기를 내뿜는 한 여성이 내게 다가온다."
    hide soju

    show Nakyeong at top
    n "안녕!나는 파워 E N F P 대장 박나경!"
   
    n " 여기는 몇반이야? 3반? 나는 2반 나경이야!"
    
    n "이 귀요미는 이름이 뭐야?"
    menu:
        "나.. 나 말하는 거야? 나는 [school]에서 온 [name]이야.":
            n  "[school]에도 이런 인재가 있었구나~! 담엔 밥 같이 먹어요ㅎㅎ"
            hide Nakyeong
            jump scene6_1
    
        "저는 [name]입니다만, 초면인데 왜. 반말 하시죠? ":
           
            n " 죄송합니다…제가 무례했네여"
            "갑자기 분위기가 싸해지고, 정적이 흘렀다.."
            hide Nakyeong
            jump scene6_1

    label scene6_1:
        
        "하하, 술게임이나 해볼까요~"    
        "술게임을 시작하며 분위기가 더욱 즐거워지고, 다시 한번 웃음소리가 채워졌다."


        show Hitomi m_06
        "분위기에 휩쓸려 히토미가 술을 연이어 마시는 모습이 보였다."        
        p "히토미, 너무 많이 마시지 않아도 괜찮아."
    
    menu:
        "나서서 그녀를 위해 술을 대신 마신다.":            
            jump scene6_1_a
        
        "자기 일은 스스로 처리하게 둔다. 그냥 그 상황을 지켜본다.":            
            jump scene6_1_b
        

label scene6_1_a:
    hide Hitomi 
    show Hitomi m_05
    h "헤에- 오나짱, 대단하네요~ \n 구해주셔서 고마워요."
    
    h "오나짱 같은 든든한 사람은 처음 만나보는 것 같아요."

    h "새벼크에 소주르을 먹으면 \n 태평소를 가는게 국크룰이라던데 같이 가고 싶어요."
    
    h "조금만 이따가 오나짱과 함께 TPS에 가볼 수 있을까요..?"
    menu:
        
        "국밥 한 그릇 먹고 가면 속도 풀리고 아주 좋지.":
            jump scene7
        "미안, 히토미. 국밥은 혼자 먹어. 오늘은 내가 좀 졸리다.":
            jump scene8


label scene6_1_b:
    hide Hitomi 
    show Hitomi m_05
    h "오나짱 나 술이 좀 취한 거 같아요."
    
    h "술김에 말하는데 오나짱 같은 든든한 사람은 처음 만나보는 것 같아요."

    h "그래서 말인데..\n 새벼크에 소주르을 먹으면 태평소를 가는게 국크룰이라던데 \n 같이 가고 싶어요."
    
    h "조금만 이따가 오나짱과 함께 TPS에 가볼 수 있을까요..?"
    menu:
        
        "국밥 한 그릇 먹고 가면 속도 풀리고 아주 좋지.":
            jump scene7
        "미안, 히토미. 국밥은 혼자 먹어. 오늘은 내가 좀 졸리다.":
            jump scene8



label scene7:
    # 태평소 국밥
    scene bg_taepungso
    hide Hitomi 
    show Hitomi m_07 m_08
    
    "히토미와 함께 국밥집으로 걸어갔다."
    "그녀는 술을 마시고 약간 부어 있는 얼굴이었지만, 그런 그녀도 매력적이었다."
    
    hide Hitomi
    h "국밥 먹은 게 처음이라서 기대되요~"

    "그녀의 신나는 표정을 보고, 나도 미소를 지을 수밖에 없었다."


    hide Hitomi
    show Hitomi m_04
    with dissolve
    
    h "아, 오이시이. \n 한국음식을 오빠랑 먹으면서 \n 한국이랑 오빠에 대해 더 알아가고 싶어요."

    "그녀의 말에 고개를 끄덕이며, \n 우리는 맛있는 국밥을 먹기 시작했다."

    "국밥을 먹다보니, 히토미의 입가에 김치 조각이 묻어 있었다."
    
    show Hitomi m_07
    with dissolve
    
    h "어머, 태평소 국밥 너무 맛있어요."
    
    "입에 묻은 김치를 알아채지도 못한채 \n 그녀는 고스란히 두고 먹는 것을 즐기고 있었다."

menu:
    "김치를 떼어주려는 충동을 억제하며, 그녀에게 알려준다.":
        
        jump scene7_a
    
    "휴지를 꺼내서 그녀의 입가에 묻은 김치를 떼어준다.":
        
        jump scene7_b

label scene7_a:
    p "히토미, 입가에 김치가 묻어 있어."
    
    h "어머! 알려주셔서 고마워요. 민망하네요."

    "그녀는 쑥스럽게 웃으며 김치를 닦아냈다."

label scene7_b:
    "그녀의 입가에 묻은 김치를 볼 수 없어서, 나는 조용히 휴지를 꺼냈다."
    
    p "잠깐만, 히토미."
    
    "그녀의 입가에 묻은 김치를 조심스럽게 떼어냈다."
    
    h "어머! 고마워요, 오니짱."
    
    "그녀는 놀란 표정으로 나를 보며 웃었다."


label scene8:
    show Hitomi m_04
    with dissolve

    scene kaist_nightwalk

    "국밥을 먹은 후 우리는 함께 기숙사로 향했다."
    
    h "오늘 정말 즐거웠어요. 오나짱과 함께 하니까 뭔가 더 신나요."
    
    "그녀의 얼굴에는 술이 올라와서인지, 혹은 기분이 좋아서인지 미소가 넘쳐흘렀다."

    "평소에도 그녀가 예쁘다 생각했지만, 취기가 오른 그녀의 모습은 나를 더욱 설레게 하였다."
    
    "KAIST 캠퍼스의 야경은 언제나 멋졌다. 우리는 걸으며 그 야경을 함께 감상했다."

    
    with dissolve
    
    h "KAIST 캠퍼스 야경은 정말 멋있네요. 이런 곳에서 오나짱이랑 같이 있는 것은 정말 행운아에요."
    
    "그녀의 말에 고개를 끄덕이며, 나도 그런 생각이 들었다."
    
    "그녀를 기숙사 앞까지 데려다주고 나서, 나는 히토미에게 작별 인사를 건넸다."

    p "히토미, 오늘은 이만 잘 가."
   
    h "네, 오나짱. 감사해요. 잘자요!"
    
    "그녀는 기쁜 표정으로 나에게 인사하고 기숙사로 들어간다."

    "지금이 아니면 내 마음을 표현하기 쉽지 않을 것 같다는 생각이 든다."

    menu:
        
        "히토미를 외친다.":
            jump scene8_a
        
        "뒤돌아 갈 길을 간다.":
            jump scene9


label scene8_a:
    show Hitomi m_10
    with dissolve
    h "그녀가 뒤돌아 본다."

    h "오나짱 왜 불렀어요? 할 말 있어요?"

    menu:
            
            "잘 가라고 말 하고 싶었어요.":
               
                jump scene8_a_1
            
            "앞에 차와요.":
                
                jump scene8_a_1

            "히토미. 당신을 더 알아가고 싶어요.":

                jump scene8_a_2



label scene8_a_1:

    h "오나짱 스윗하기까지해. 잘자고 내일 실습실에서 봐요."
    p "그녀와 작별 인사를 하고, 기숙사에 들어와서 피곤해 잠들었다."
    jump scene9

label scene8_a_2:
    "내가 그렇게 말하자 히토미는 조금 놀라보였다."
    show Hitomi m_11
    with dissolve
    h "오나짱, 그 말 진심이에요?"

    menu:    
        "그럼. 더 많이 알고 싶어요.":
            jump scene8_a_2_a
    
        "그냥 말장난이에요.":
            jump scene8_a_2_b       
    
label scene8_a_2_a:
    p "그럼. 더 많이 알고 가까워지고 싶어요."    
    h "그런 오나짱도 꽤나 매력적이네요. 앞으로 재미있을 것 같아요. 잘자요, 오나짱."
    jump scene9

label scene8_a_2_b:
    p "그냥 말장난이에요."    
    h "오나짱, 그런 장난 하지 마세요. 제 심장, 떨려요. 잘자요."    
    "히토미는 서둘러 기숙사로 돌아갔다. 오늘 하루를 생각하며, 나도 조금 더 깊은 생각에 잠겼다."
    jump scene9

    
label scene9:
    # 카이마루 
    p "어제 너무 많이 마셨나?\n 속이 너무 안좋은 걸."    
    p "해장이나 해야겠다"    
    scene bg_kaimaru
     
    p  "리틀 하노이에서 쌀국수를 먹으려고 하는데,"
    p "갑자기 익숙한 얼굴이 보였다."

    show Kaistian 
    p "같은 분반의 카이스트 여학생 시연인 것 같았다."
     
    menu:
        "그녀를 어떻게 대할까?"
        "시연아, 같이 밥 먹을래? 이런데서 뵈니 반갑네.":
            jump scene9_1
        "아니야, 아직 친하지 않은데 그냥 간다. 인사조차 부담스러울 것 같아.":
            jump scene10

    
    label scene9_1: 
        sy "음? 아, 너... [name]이지?"
        
        sy "어제 네가 코딩하던 거, 나도 보고 있었어. 그냥 감탄하고 말았지."
        sy "너의 집중력이나 코드를 다루는 능력, 그것들은 나와는 다른 레벨이야."
        sy "그래서 솔직히, 너한테 그런 걸 인정해주는 게 좀 부끄럽지만, \n 어쨌든 인정해줘야 할 것 같아. 이해할 수 있겠지?"

        p "갑작스럽게 쏟아지는 그녀의 칭찬에, 약간 당황스러웠다."
        p "그녀가 왜 부끄럽게 느껴지는지 잘 모르겠지만 \n 그녀의 칭찬에 어쩔 수 없이 미소를 짓고 말았다."
        p "그녀의 칭찬이 나에게 주는 자부심을 부정할 수 없었다."

        menu: 
            "나도 시연을 칭찬해주었다.":
                jump scene9_2
            "(쑥스러우니까 빨리 넘어가야겠다.) 그래. 고마워.":
                jump scene10
        
        
        
    label scene9_2:
        p "시연, 너도 코딩 잘하더라. 그런 도전적인 문제에 뛰어들어서 해결하는 모습, 정말 대단해."

        sy "정말 그렇게 생각해? 나도 그 문제를 해결하는 데 시간이 좀 걸렸지만,\n 그래도 나름대로 해결 방법을 찾아냈어."
        sy "그래서 그런 칭찬을 듣게 되니, 조금은 기분이 좋네. 나도 좀 자랑스럽다고 할까? 내 능력을 인정해주니까 말이야."
        sy "하지만, 그런 칭찬을 너에게서 들으니 좀 더 기분이 좋아."
        
        sy "아마도 나도 너를 칭찬해주고 싶어서 그런 말을 한 것 같아. 이상하게 나도 너를 칭찬하고 싶어졌거든."
        sy "그런데 이런 말을 하니까 너무 쑥스러워. 그래도 감사해, [name]."
label scene10:
    # 실습실로 걸어가는 길. 
    # 3, 4주차 팀메를 같이 하자고 제안한다. (happy ending, 3~4 주차 .)
    # 담타? 
label scene11:
    # 나경에게 연락이 와서 저녁을 같이 먹기로 했다. 
    # 짝꿍인 지현이는 혼자 밥을 먹도록 냅둔다 vs 거절 한다. 
    p "코딩을 열심히 하고 있는데, 카톡이 왔다."
    p "어제 술자리에서 만난 나경이었다."


    n "안녕, [name]아. 저녁에 시간 있어?"
    n "밥 같이 먹자고 연락했어!"

    p "갑자기 지현이가 걱정이 되었다."
    p "내가 오늘 나경과 저녁을 먹으면, 지현은 혼자 밥을 먹어야 할 텐데..."

    menu:
        "어쩌지.."
        "혹시 내 팀메 지현이도 같이 와도 될까?":
            jump scene11_1
        "미안, 나경아. 이미 지현이와 약속이 있어서 못갈 것 같아. 다음에 보자.":
            jump scene11_2
        "그래, 나경아. 좋아. 저녁에 보자.":
            jump scene11_3

    label scene11_1:
        "나는 나경에게 답했다."
        p "그래, 좋아. 그런데 내 팀메도 같이 오면 어떨까?"
        n "이렇게 답하니 나경이로부터  1시간  이후 답변이 왔다."
        n "아냐, 그럴거면 나는 빠질게."
        p "당황한 나는 다시 카톡을 보내보았지만,  \n 이미 차단 당한 이후였다."
        jump scene14_a
    label scene11_2:
        p "나는 조금 죄책감이 들었다."
        p "미안, 나경아. 이미 지현이와 약속이 있어서 못갈 것 같아. 다음에 보자."
        p "나경은 나의 문자를 본 것듯이 대답했다."
        jump scene14_b

    label scene11_3:
        p "나는 지현이에게 미안한 마음이 들었지만, 나경과의 저녁식사를 수락했다."
        p "그래, 나경아. 좋아. 저녁에 보자."
        n " 나경은 자신이 맛있는 식당을 알아뒀다며 저녁에 만나자고 했다. "
        jump scene12

label scene12
    # 작교
    scene bg_zakyo
    p "나경이가 엄선한 유성 제일가는 술집 '작교'에 도착했다."
    p "분위기도 좋고, 막걸리의 맛도 최고였다."
    
    show Nakyeong
    p "나경은 막걸리 한병을 벌컥벌컥 들이키며 얼굴이 붉어지는 것을 느꼈다."
    p "그리고 그녀는, 그간 자신이 가슴 속에 숨겨온 이야기를 시작했다."

    n "사실, 처음 보았을 때부터 내 이상형이다 싶었어."
    n "내 이상형은 순수한 공대 너드남인데, 너가 딱 그런 느낌이었어."

    p "나는 그 말을 듣고 놀랐다."
    p "나경이가 나를 그런 눈으로 보고 있었다니, 그것을 알기까지 오래 걸렸다."
    p "나는 그녀를 바라보며 답변했다."

    menu:
        "나도 너를 그런 눈으로 봤어, 나경아.":
            jump scene12_1_a
        "그 말, 고마워. 나도 좋아하는 사람이 있어.":
            jump scene12_1_b

    label scene12_1_a:

        p "'나도 너를 그런 눈으로 봤어, 나경아.'"
        "나의 대답에 나경은 눈이 크게 벌어지며 놀라워했다."
        n "그리고 그녀는 미소를 지으며, '정말이야? 그건 너무 좋다.'라고 말했다."
        n "우리, 만나 보지 않을래? " # 해피 엔딩. 
        hide Nakyeong

    label scene12_1_b:
        
        p "그 말, 고마워. 나도 좋아하는 사람이 있어."
        p "나의 대답에 나경은 조금 서운한 듯이 고개를 숙였다."
        p "그리고는, '그래도 나는 네가 좋아. 그런 너를 지켜보는 것만으로도 충분해.'라고 말했다."
        hide Nakyeong
        jump scene13

label scene13:
    # 실습실
    scene bg_room113_whole
    "나경과의 고백을 거절하고 어색한 상태로 실습실에 도착했다."
    "나는 그녀를 거절한 행동에 대해 미안함을 느꼈다. 그녀는 나에게 감정을 표현했지만, 나는 그것을 받아들이지 못했다."
    "실습실에 도착하니 팀메이트인 지현이 혼자 코딩을 하고 있었다."
    p "지현아, 저녁 혼자 먹게 해서 정말 미안하다."
    p "나경과 이야기하면서, 나는 지현을 좋아하고 있었다는 것을 깨달았다."

    show Jihyeon m03 m04
    j "오빠, 밥은 맛있게 먹고 왔어?"

    menu:
        "아니, 자꾸 네 생각이 나서, 빨리 네가 보고 싶어서 먹는 둥 마는 둥 하고 왔어.":
            jump scene13_1_a
        "응 작교 다녀왔는데 맛있더라.":
            jump scene13_1_b

    label scene13_1_a:
        p "아니, 자꾸 네 생각이 나서, 빨리 네가 보고 싶어서 먹는 둥 마는 둥 하고 왔어."
        "나의 대답에 지현이는 놀라 보였다."
        j"그래서 그렇게 빨리 돌아온 거였구나."
        j "나랑도 가주면 안될까?"
        jump scene14

    label scene13_1_b:
        p "응, 작교 다녀왔는데 맛있더라."
        "나의 대답에 지현이는 아무 대답 없이 코딩에 집중하더니,"
        "그 이후로 나는 지현이의 말하는 모습을 다시는 볼 수 없었다"
        jump end3
        
label scene14_a:

label scene14_b:

label scene14_c:

label scene15:
    # 117호 
    scene bg_117    
    "그 주, 시연이가 금주의 픽으로 선정되었다."
    "그녀는 강단에서 자신감 넘치게 발표를 하고 있었다."
    "나는 그녀가 표현하는 강한 열정에 감탄하며 그녀를 보았다."
    "그 순간, 내 마음은 그녀에게로 이끌렸다."

menu:
    "시연에게 말을 건네고, 그녀와 이야기하며 공통 관심사를 찾아보자.":
        jump scene15_1_a
    "시연에게 말을 건네는 것이 너무 두려워, 그녀를 멀리서만 지켜보자.":
        jump scene15_1_b

label scene15_1_a:
    "내가 망설임 없이 시연에게 다가갔다."
    p "시연아, 네 발표 정말 멋있었어. 나도 스타트업과 창업에 관심이 많아."
    "그 말에 시연이는 미소를 지었다."
    p " 우리 같이 3주차 프로젝트를 하면 어떨까?"
    "나의 제안에 시연이는 고민 없이 수락했다."
    "그 순간, 나는 내 마음이 시연에게로 기울어지고 있다는 것을 확실히 느꼈다."
    jump scene16

label scene15_1_b:
    "나는 시연에게 말을 건네는 것이 너무 두려워서, \n 그녀를 멀리서만 지켜보았다."
    "하지만 시연이는 다른 사람과 팀을 이루기 시작했다."
    "나는 그것을 지켜보며, \n  '저 자리가 내 자리가 되어야 했는데..'라고 속으로 생각했다."
    "하지만 나는 담담하게 그 모습을 바라보기만 하고, \n 시연에게 내 마음을 전달하지 못했다."
    jump end4

label scene16:
    

label end1:
    "그렇게 나는 일주일간 그녀와 아무 말도 할 수 없었고, \n 몰입캠프 전체에  인신공격남으로 소문나게 되어 \n 괴로운 한달을 보내야 했다…"
label end2:
    "그렇게 나는 일주일간 그녀와 아무 말도 할 수 없었고, \n 몰입캠프 전체에  급발진남으로 소문나게 되어 \n 괴로운 한달을 보내야 했다…"
label end3:
    "그렇게 나는 굴러들어온 지현이를 걷어찼다. "
label end4: 
    "다른 남자와 잘되어가는 시연의 모습을 지켜보는 것은 \n 마음이 너무 안좋았지만, 내가 할 수 있는 것은 없었다. "
    "그렇게, 나는 모쏠 탈출을 하지 못한 채 게임이 끝났다."
