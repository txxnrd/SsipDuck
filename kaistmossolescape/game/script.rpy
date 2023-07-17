

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
image kaist_night:
    "images/kaist_night.jpeg"

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


    image nameofSprite:
        "soju-straight.png"
        0.5 #this part defines how long to wait before next frame
        "soju-not_straight.png"
        0.5
        repeat


    "사람들의 대화와 웃음이 점차 풍성해져간다."

    "그러던 중 인싸 향기를 내뿜는 한 여성이 내게 다가온다."
   
    n "안녕!나는 파워 E N F P 대장 박나경!"
   
    n " 여기는 몇반이야? 3반? 나는 2반 나경이야!"
    
    n "이 귀요미는 이름이 뭐야?"
    menu:
        "나.. 나 말하는 거야? 나는 [school]에서 온 [name]이야.":
        n  "[school]에도 이런 인재가 있었구나 담엔 밥 같이 먹어요"
        
        
        "저는 [name]입니다만, 초면인데 왜. 반말 하시죠? ":
        n " 죄송합니다…제가 무례했네여"
        "갑자기 분위기가 싸해지고, 정적이 흘렀다.."

    label scene6_1:
        
        "하하, 술게임이나 해볼까요~"
    
        "술게임을 시작하며 분위기가 더욱 즐거워지고, 다시 한번 웃음소리가 채워졌다."


        show Hitomi m05
        "분위기에 휩쓸려 히토미가 술을 연이어 마시는 모습이 보였다."
        
        p "히토미, 너무 많이 마시지 않아도 괜찮아."
    
    menu:
        "나서서 그녀를 위해 술을 대신 마신다.":
            
            jump scene6_1_a
        
        "자기 일은 스스로 처리하게 둔다. 그냥 그 상황을 지켜본다.":
            
            jump scene6_1_b

label scene6_1_a:
    h "헤에- 오나짱, 대단하네요~ \n 구해주셔서 고마워요."
    
    h "오나짱 같은 든든한 사람은 처음 만나보는 것 같아요."

    h "새벼크에 소주르을 먹으면 태평소를 가는게 국크룰이라던데 같이 가고 싶어요."
    
    h "조금만 이따가 오나짱과 함께 TPS에 가볼 수 있을까요..?"
    menu:
        
        "국밥 한 그릇 먹고 가면 속도 풀리고 아주 좋지.":
            jump scene7
        "미안, 히토미. 국밥은 혼자 먹어. 오늘은 내가 좀 졸리다.":
            jump scene8


label scene6_1_b:
    h "오나짱 나 술이 좀 취한 거 같아요."
    
    h "술김에 말하는데 오나짱 같은 든든한 사람은 처음 만나보는 것 같아요."

    h "그래서 말인데 새벼크에 소주르을 먹으면 태평소를 가는게 국크룰이라던데 같이 가고 싶어요."
    
    h "조금만 이따가 오나짱과 함께 TPS에 가볼 수 있을까요..?"
    menu:
        
        "국밥 한 그릇 먹고 가면 속도 풀리고 아주 좋지.":
            jump scene7
        "미안, 히토미. 국밥은 혼자 먹어. 오늘은 내가 좀 졸리다.":
            jump scene8



label scene7:
    # 태평소 국밥
    scene bg_taepungso
    
    "히토미와 함께 국밥집으로 걸어갔다."

    "그녀는 술을 마시고 약간 부어 있는 얼굴이었지만, 그런 그녀도 매력적이었다."

    h "국밥 먹은 게 처음이라서 기대되요~"

    "그녀의 신나는 표정을 보고, 나도 미소를 지을 수밖에 없었다."


    show Hitomi m_06
    with dissolve
    
    h "아, 맛있겠다. 한국음식을 오빠랑 먹으면서 한국이랑 오빠에 대해 더 알아가고 싶어요."

    "그녀의 말에 고개를 끄덕이며, 우리는 맛있는 국밥을 먹기 시작했다."


    
    
    "국밥을 먹다보니, 히토미의 입가에 김치 조각이 묻어 있었다."
    
    show Hitomi m_07
    with dissolve
    
    h "어머, 태평소 국밥 너무 맛있어요."
    
    "입에 묻은 김칫가루를 알아채지도 못한채 그녀는 고스란히 두고 먹는 것을 즐기고 있었다."

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
    show Hitomi m_08
    with dissolve

    scene kaist_night

    "국밥을 먹은 후 우리는 함께 기숙사로 향했다."
    
    h "오늘 정말 즐거웠어요. 오나짱과 함께 하니까 뭔가 더 신나요."
    
    "그녀의 얼굴에는 술이 올라와서인지, 혹은 기분이 좋아서인지 미소가 넘쳐흘렀다."

    "평소에도 그녀가 예쁘다 생각했지만, 취기가 오른 그녀의 모습은 나를 더욱 설레게 하였다."
    
    "KAIST 캠퍼스의 야경은 언제나 멋졌다. 우리는 걸으며 그 야경을 함께 감상했다."

    
    show Hitomi m_09
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




label end1:
    "그렇게 나는 일주일간 그녀와 아무 말도 할 수 없었고, \n 몰입캠프 전체에  인신공격남으로 소문나게 되어 \n 괴로운 한달을 보내야 했다..."
label end2:
    "그렇게 나는 일주일간 그녀와 아무 말도 할 수 없었고, \n 몰입캠프 전체에  급발진남으로 소문나게 되어 \n 괴로운 한달을 보내야 했다..."
