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
    "images/bg_kaimaru.jpeg"
    zoom 1.5
image bg_taepungso:
    "images/bg_taepungso.jpg"
    zoom 1.4
image bg_117:
    "images/bg_117.jpg"
    zoom 1.4

image bg_zakyo:
    "images/bg_zakyo.jpg"
    zoom 1.4

image bg_china_out:
    "images/china_out.jpeg"
    zoom 0.92

image bg_china_in:
    "images/china_in.jpeg"
    zoom 0.92
image bg_smokearea:
    "images/smokearea.jpeg"
    zoom 0.76

image bg_kaistnight:
    "images/bg_kaistnight.jpg"
    zoom 1.4
image bg_dorm2:
    "images/bg_arum.jpg"
    zoom 1.6
image soju:
    "soju-straight.png"
    0.5 #this part defines how long to wait before next frame
    "soju-not_straight.png"
    0.5
    repeat

image gpt_siyeon:
    "images/bg_siyeon_gpt.jpg"
    zoom 1.3    
image mo:
    "images/모.png"
    0.7
image ssol:
    "images/쏠.png"
    0.7
image tal:
    "images/탈.png"
image chul:
    "images/출.png"
image sil:
    "images/실.png"
image pae:
    "images/패.png"
image sa:
    "images/사.png"
image rang:
    "images/랑.png"
image jang:
    "images/쟁.png"
image che:
    "images/취.png"
image heart:
    "images/heart.png"
image mstc_fail:
    "images/fail_to_mstc.jpg"
    zoom 1.5
image ciga:
    "images/ciga.png"
    zoom 0.3


    

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


    show Natori mtn_01 exp_03 with dissolve
    "저기 멀리에서 짝이 보인다. 여자인듯 하다." # 지현이 작게 넣기
    
    play music "spooky&sad.mp3"

    p "아니...짝꿍이 여자야...\n"

    p "여자랑 말을 어떻게 해..미리 말 해주던가 몰캠 놈들..."
    
    p "생각해보니 초등학교 이후로 여자랑 말을 해본 적이 없잖아"
    
    p "온몸이 떨리고 갑자기 집에 가고 싶어졌어."

    stop music
    hide Natori
    
    play music "waitforans.mp3"

menu :

    
    "행동을 결정하시오"
    
    "gpt에게 물어보기":
        jump .gpt    
    "구글링하기":
        jump .google
    

label .gpt:
    stop music
    show gptvideo
    
    p "gpt야 도와줘!!" 
    
    p "gpt가 하라는 대로만 해야겠다."

    hide gptvideo with dissolve

    
    jump scene2_2

label .google:

    stop music
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
    
    "그때 어렴풋이 보이던 귀여운 여자가 앞에 다가온다. 나의 짝꿍인 듯하다."
    
    "사람이 이렇게나 귀여울 수 있구나."
    
    "심장이 미친 듯이 요동친다"    
    
    j "안녕~ 너가 [name]이구나! 한 주 동안 잘 부탁해~"
    
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
    play music  "05. Getting Ready Now!.mp3" 

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

    stop music


label scene4:   # 첫날, 강의실 안. 
    
    label scene4_1:
        with fade 
        scene bg_113computer
        
        show Hiyori m04
        j "Recycler View가 너무 어려워.. 너는 이거 다 이해했어?"

        play music "waitforans.mp3"
        menu:
            
            "당연하지...너 여태껏 컴공 다니면서 뭐햇어 너 학점 1점대야?":
                jump .scene4_1_a
            #결과: 일주일동안 토라져서 말안하기( 오늘 저녁 같이 못먹음)
            "내가 천천히 설명 해줄게. 리사이클러 뷰는 어쩌구 저쩌구~":
                jump .scene4_1_b
            
        label .scene4_1_a:
            stop music
            j "나 사실 학점 1.27이야. 학고 받고 집에서 쫓겨나서 몰입캠프 온거야."
            j "비록 사실이라도 말을 그딴식으로 하는 사람이랑 나는 일주일 동안 같이 못 지낼 거 같아."
            j "넌 탈락이야!"

            play music "spooky&sad.mp3"
            hide Hiyori
            jump end1

        label .scene4_1_b:  
            stop music          
            "개발이 익숙했던 [name]. 1분만에 화면에 연락처 탭을 구현한다."            
            j " 오빠는 정말 똑똑해! \n 세상에 앨런 튜링이랑 오빠만 남는다고 해도 나는 오빠를 택할거야."

            hide Hiyori
            jump scene4_2


    label scene4_2:
        play music "littletension.mp3"
        "리사이클러 뷰를 수정 하던 중 디테일이 부족하다는 생각을 한다."
        
        "'실제 번호를 사용하면 디테일이 살지 않을까'라는 생각을 한다."
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

        stop music
        
        jump scene5

    
label scene5:   #새벽 2시, 기숙사. 
    with fade 
    scene bg_dorm  
        
    p "이 정도면 그린라이트겠지? 사람들한테 물어봐야겠다."

    $ renpy.movie_cutscene("images/video_everytime.webm", delay=None, loops=0, stop_music=True)
    
    p "그녀도 분명 나에게 관심이 있을 거야.얼른 연락을 해야겠다."
    
    play music "15. Bird Songs.mp3"

    menu:
        "오늘 정신 없었을 텐데 고생 많았어ㅎㅎ. 내일 보자.":
            jump scene5_1_a

        "너를 처음 본 순간 나는 심장이 멎는 줄 알았어… \n 천사가 인간으로 태어났으면 너와 같은 얼굴이었을 거라 확신해 나랑 사귈래?":
            jump scene5_1_b

        "아냐.. 아직 일러.. (아무것도 보내지 않는다)":
            
            jump scene6

label scene5_1_a:
    $ renpy.movie_cutscene("images/video_kakaotalk1.webm", delay=None, loops=0, stop_music=True)
    p "그녀와 조금 더 가까워진 기분이 드는 걸 "
    p "내일은 그녀에게 조금 더 적극적으로 다가가봐야지 "
    stop music
    jump scene6
    
label scene5_1_b:
    $ renpy.movie_cutscene("images/video_kakaotalk2.webm", delay=None, loops=0, stop_music=True)
    p "그러자 그녀에게서 연락이 왔다."
    p "설레는 마음으로 카톡창을 열자.."
    stop music
    show Jihyeon m07 m08 m09
    j "너무 당황스러워!\n 다시는 개인적인 일로 연락하지마!"
    jump end2
 
        



label scene6:
    stop music

    # 술자리 회식
    scene bg_holala

    play music "sojudump.mp3"

    p "벌써 주말이잖아. 첫 주가 어떻게 지나갔는지 모르겠네."


    show soju at truecenter

    "사람들의 대화와 웃음이 점차 풍성해져간다."
    "그러던 중 인싸 향기를 내뿜는 한 여성이 내게 다가온다."
    hide soju



    


    show Nakyeong at top

    n "안녕!나는 파워 E N F P 대장 박나경!"
   
    n " 여기는 몇반이야? 3반? 나는 2반 나경이야!"
    
    n "이 귀요미는 이름이 뭐야?"
    
    stop music

    play music "waitforans.mp3"
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

        stop music

        play music "sojudump.mp3"

        "하하, 술게임이나 해볼까요~"
    
        "술게임을 시작하며 분위기가 더욱 즐거워지고, \n다시 한번 웃음소리가 채워졌다."



        show Hitomi m_06
        "분위기에 휩쓸려 히토미가 술을 연이어 마시는 모습이 보였다."        
        p "히토미, 너무 많이 마시지 않아도 괜찮아."
    
    menu:
        "나서서 그녀를 위해 술을 대신 마신다.":            
            jump scene6_1_a
        
        "자기 일은 스스로 처리하게 둔다. 그냥 그 상황을 지켜본다.":            
            jump scene6_1_b
        

label scene6_1_a:
    stop music
    hide Hitomi 
    show Hitomi m_05
    h "헤에- 오나짱, 대단하네요~ \n 구해주셔서 고마워요."
    
    h "오나짱 같은 든든한 사람은 처음 만나보는 것 같아요."

    h "새벼크에 소주르을 먹으면 \n 태평소를 가는게 국크룰이라던데 같이 가고 싶어요."
    
    h "조금만 이따가 오나짱과 함께 TPS에 가볼 수 있을까요..?"
    play music "waitforans.mp3"

    menu:
        
        "국밥 한 그릇 먹고 가면 속도 풀리고 아주 좋지.":
            jump scene7
        "미안, 히토미. 국밥은 혼자 먹어. 오늘은 내가 좀 졸리다.":
            jump scene8


label scene6_1_b:
    
    stop music
    hide Hitomi 
    show Hitomi m_05
    h "오나짱 나 술이 좀 취한 거 같아요."
    
    h "술김에 말하는데 오나짱 같은 든든한 사람은 처음 만나보는 것 같아요."

    h "그래서 말인데..\n 새벼크에 소주르을 먹으면 태평소를 가는게 국크룰이라던데 \n 같이 가고 싶어요."
    
    h "조금만 이따가 오나짱과 함께 TPS에 가볼 수 있을까요..?"
    
    play music "waitforans.mp3"

    menu:
        
        "국밥 한 그릇 먹고 가면 속도 풀리고 아주 좋지.":
            jump scene7
        "미안, 히토미. 국밥은 혼자 먹어. 오늘은 내가 좀 졸리다.":
            jump scene8



label scene7:
    stop music
    # 태평소 국밥
    scene bg_taepungso
    hide Hitomi 
    show Hitomi m_07 m_08

    play music "audio/a-small-miracle-132333.mp3" 
    
    "히토미와 함께 국밥집으로 걸어갔다."
    "그녀는 술을 마시고 약간 부어 있는 얼굴이었지만, 그런 그녀도 매력적이었다."
    
    hide Hitomi

    show Hitomi m_03

    h "국밥 먹은 게 처음이라서 너무 신나요~"

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

    stop music

    play music "waitforans.mp3"

menu:
    "김치를 떼어주려는 충동을 억제하며, 그녀에게 알려준다.":
        
        jump scene7_a
    
    "휴지를 꺼내서 그녀의 입가에 묻은 김치를 떼어준다.":
        
        jump scene7_b

label scene7_a:
    stop music
    p "히토미, 입가에 김치가 묻어 있어."
    
    h "어머! 알려주셔서 고마워요. 민망하네요."

    "그녀는 쑥스럽게 웃으며 김치를 닦아냈다."

label scene7_b:
    stop music
    
    "그녀의 입가에 묻은 김치를 볼 수 없어서, 나는 조용히 휴지를 꺼냈다."
    
    p "잠깐만, 히토미."
    
    "그녀의 입가에 묻은 김치를 조심스럽게 떼어냈다."
    
    h "어머! 고마워요, 오니짱."
    
    "그녀는 놀란 표정으로 나를 보며 웃었다."


label scene8:
    stop music
    play music "happiest_ever.mp3"
    scene bg_kaistnight

    show Hitomi m_02
    with dissolve
    "국밥을 먹은 후 우리는 함께 기숙사로 향했다."
    
    h "오늘 정말 즐거웠어요. 오나짱과 함께 하니까 뭔가 더 신나요."
    
    "그녀의 얼굴에는 술이 올라와서인지, \n혹은 기분이 좋아서인지 미소가 넘쳐흘렀다."

    "평소에도 그녀가 예쁘다 생각했지만, \n취기가 오른 그녀의 모습은 나를 더욱 설레게 하였다."
    
    "KAIST 캠퍼스의 야경은 언제나 멋졌다. \n우리는 걸으며 그 야경을 함께 감상했다."

    

    
    h "KAIST 캠퍼스 야경은 정말 멋있네요. \n이런 곳에서 오나짱이랑 같이 있는 것은 정말 행운아에요."
    
    "그녀의 말에 고개를 끄덕이며, 나도 그런 생각이 들었다."

    scene bg_dorm2

    show Hitomi m_05
    with dissolve
    
    "그녀를 기숙사 앞까지 데려다주고 나서, \n 나는 히토미에게 작별 인사를 건넸다."

    p "히토미, 오늘은 이만 잘 가."
   
    h "네, 오나짱. 감사해요. 잘자요!"
    
    "그녀는 기쁜 표정으로 나에게 인사하고 기숙사로 들어간다."

    "지금이 아니면 내 마음을 표현하기 쉽지 않을 것 같다는 생각이 든다."
    
    stop music

    play music "waitforans.mp3"

    menu:
        
        "히토미를 외친다.":
            jump scene8_a
        
        "뒤돌아 갈 길을 간다.":
            jump scene9

label scene8_a:
    stop music
    show Hitomi m_08
    with dissolve
    h "그녀가 뒤돌아 본다."

    h "오나짱 왜 불렀어요? 할 말 있어요?"
    play music "waitforans.mp3"

    menu:
            
            "잘 가라고 말 하고 싶었어요.":
                jump scene8_a_1
            
            "앞에 차와요.":                
                jump scene8_a_1

            "히토미. 당신을 더 알아가고 싶어요.":
                jump scene8_a_2



label scene8_a_1:
    stop music

    h "오나짱 스윗하기까지해. 잘자고 내일 실습실에서 봐요."
    p "그녀와 작별 인사를 하고, 기숙사에 들어와서 피곤해 잠들었다."
    jump scene9

label scene8_a_2:
    stop music
    "내가 그렇게 말하자 히토미는 조금 놀라보였다."
    show Hitomi m_05
    with dissolve
    h "오나짱, 그 말 진심이에요?"
    
    play music "waitforans.mp3"

    menu:    
        "그럼. 더 많이 알고 싶어요.":
            jump scene8_a_2_a
    
        "그냥 말장난이에요.":
            jump scene8_a_2_b       
    
label scene8_a_2_a:
    stop music
    # play music "littletension.mp3"
    p "그럼. 더 많이 알고 가까워지고 싶어요."    

    h "오나짱. 우리는 구크적도 다르고 \n 현실적인 제약이 너무 많아요."
    
    h "이런 나라도 사랑해 줄 수 있어요?"

    stop music

    menu:
        "험난한 앞길이 우리를 막더라도 나는 너를 사랑할게.":
            jump happyEnding_Hitomi
        "그 정도 확신은 없는 것 같아. 미안해.":
            jump scene9

    jump scene9

label scene8_a_2_b:
    stop music
    play music "littletension.mp3"
    p "그냥 말장난이에요."    
    h "오나짱, 그런 장난 하지 마세요. 제 심장, 떨려요. 잘자요."    
    "히토미는 서둘러 기숙사로 돌아갔다. 오늘 하루를 생각하며, 나도 조금 더 깊은 생각에 잠겼다."
    jump scene9

    
label scene9:
    hide Hitomi
    stop music
    play music "sojudump.mp3"
    show Natori mtn_01 exp_03 with dissolve
    # 카이마루 
       
    scene bg_kaimaru

    "어제 히토미랑 있는게 신나서 너무 많이 마셨나봐"
    
    "속이 너무 안 좋아."    
    
    "카이마루에 해장하러 오길 잘했어." 
     
    "리틀 하노이에서 쌀국수를 먹으려고 하는데,"
    
    "익숙한 얼굴이 보였다."
    hide Natori

    show Kaistian 
    
    "같은 분반의 카이스트 여학생 시연이다."

    stop music
    
    play music "waitforans.mp3"

    menu:
        
        "그녀를 어떻게 대할까?"
        
        "여기에서 보니 반갑다.밥 같이 먹자.":
            jump scene9_1
        
        "아직 친하지도 않은데 그냥 가자. 인사조차 부담스러울 것 같아.":
            jump scene10

    
    label scene9_1: 
        stop music
        sy "음? 아, 너... [name]이지?"

        sy "난 너보면 하고 싶은 말이 있었어."
        
        sy "어제 네가 코딩하던 거, 나 사실 쭉 보고 있었어.\n 그냥 감탄하고 말았지."
        
        sy "너의 집중력이나 코드를 다루는 능력, 그것들은 나와는 다른 레벨이야."
        
        sy "부끄럽긴 하지만, \n 어쨌든 인정해줘야 할 것 같아. 이해할 수 있겠지?"

        "갑작스럽게 쏟아지는 그녀의 칭찬에, 약간 당황스러웠다."
        
        "그녀가 왜 부끄럽게 느끼는지 잘 모르겠지만 \n 그녀의 칭찬에 어쩔 수 없이 미소를 짓고 말았다."

        play music "waitforans.mp3"
        menu: 
            "나도 시연을 칭찬해주어야겠다.":
                jump scene9_2
            "(쑥스러우니까 빨리 넘어가야겠다.) 그래. 고마워.":
                jump scene11
        
        
        
label scene9_2:
    stop music
    
    play music "withsiyeon.mp3"

    p "시연아, 너도 코딩 잘하더라. \n 도전적인 문제에 자신 있게 뛰어들어서 해결하는 모습,\n 정말 대단해."

    sy "정말 그렇게 생각해? 짜식, [name], 너 칭찬 할 줄도 알고 멋있어.\n"
    
    sy "그런 칭찬을 너한테 들으니 기분이 좋다."
    
    sy "난 할 거 있어서 먼저 간다.수고해라."

    "자기 할 말을 내뱉고 갑자기 혼자 가는 그녀."

    "엉뚱한 그녀가 더욱 매력적으로 느껴진다..."

    stop music

    play music "waitforans.mp3"
    menu:
        "서둘러 그녀에게 뛰어가 같이 가자고 한다.":
            jump scene10

        "지현이가 기다리고 있는 실습실로 빠르게 혼자 간다.":
            jump scene11

label scene10:
    stop music
    
    

    sy "나 담배 피러 가는데 너 왜 따라오냐"
    
    "담배를 한 번도 펴본 적 없는 [name]. 괜히 그녀와 함께 있고 싶다."


    play music "waitforans.mp3"
    menu:
        "괜히 같이 피고 싶어...":
            jump scene10_a

        "비흡연자라 담배는 좀 그래.":
            jump scene10_b

label scene10_a:
    stop music
    scene bg_smokearea

    

    play music "smoke.mp3"
    show Kaistian
    show ciga at top 
    
    p "나도 담배 필래. 한 대 줘봐"

    sy "내가 너 담배 처음 물리는거냐."

    p "뭐래ㅋㅋ 나 원래 펴."

    p "불이나 좀 붙여줄래?"

    sy "아니 입에 대야 붙여주지"

    p "아 그래?ㅋㅋ 몰랐네"

    "처음 담배를 펴 본 [name],한 모금의 담배 연기를 크게 삼킨다."
    
    play music "Dangerous.mp3"

    p "켁..켁..나 너무 힘들어.."

    p "몸이 진짜 왜 이러지..."

    "갑자기 발작을 일으키고"

    "니코틴에 약한 [name]은 병원에 실려가고,\n 몰입캠프에 더 이상 참여하지 못한다."

    jump end


label scene10_b:
    stop music
    p "아 담배 피는지는 몰랐네..먼저 갈게"

    jump scene11

    
label scene11:
    stop music
    scene bg_113computer
    play music "summer-walk.mp3"

    "시연이와 대화를 나누고 실습실에 돌아왔다."

    "옆에서 짝꿍 지현이는 열심히 코딩을 하고 있다."
    
    p "코딩을 열심히 하고 있는데, 카톡이 왔다."
    p "어제 술자리에서 만난 나경이었다."


    n "안녕, [name]아. 저녁에 시간 있어?"
    n "밥 같이 먹자고 연락했어!"

    "인상이 좋았던 나경이와 저녁이 먹고 싶었다."
    "허나 지현이가 걱정이 되어 신경이 쓰였다."
    "내가 오늘 나경이랑 저녁을 먹으면, 지현은 혼자 밥을 먹어야 할 텐데..."

    stop music
    play music "waitforans.mp3"

    menu:
        "어쩌지.."
        "혹시 내 팀메 지현이도 같이 와도 될까?":
            jump scene11_1
        "미안, 나경아. 이미 지현이와 약속이 있어서 못갈 것 같아. 다음에 보자.":
            jump scene11_2
        "그래, 나경아. 좋아. 저녁에 보자.":
            jump scene11_3

    label scene11_1:
        stop music
        "나는 나경에게 답했다."
        p "그래, 좋아. 그런데 내 팀메도 같이 오면 어떨까?"
        "이렇게 답하니 나경이로부터  1시간  이후 답변이 왔다."
        n "아니, 나는 빠질게."
        "당황한 나는 다시 카톡을 보내보았지만,  \n 답은 오지 않았다."
        jump scene13_b
    
    label scene11_2:
        stop music
        p "나는 조금 미안함이 들었다."
        
        p "미안, 나경아. 약속이 있어서 안될 것 같아. 다음에 보자."
        
        p "카톡창에 1이 사라졌지만 그녀의 답은 없었다."
        jump scene13_b

    label scene11_3:
        stop music
        p "나는 지현이에게 미안한 마음이 들었지만, 나경이와의 저녁식사를 수락했다."
        p "그래, 나경아. 좋아. 저녁에 보자."
        n " 나경은 자신이 맛있는 식당을 알아뒀다며 저녁에 만나자고 했다. "
        
        "나경이와 단 둘이 밥을 먹는 시간이 벌써 기대 된다."
        
        jump scene12

label scene12:
    # 작교
    scene bg_zakyo
    play music "sojudump.mp3"
    "나경이가 엄선한 유성 제일가는 술집 '작교'에 도착했다."
    
    "한국적인 분위기를 뽐내는 분위기가 좋았고, 막걸리의 맛도 최고였다."
    
    show Nakyeong
    "나경은 막걸리를 연달아 벌컥벌컥 들이키며 얼굴이 붉어져 갔다."

    p "나경아 왜 이렇게 급하게 마셔."

    p "너 무슨 일 있어?"

    n "[name] 너 왜 이렇게 눈치가 없어. \n내가 내 입으로 말을 해야지 알겠어?"
    
    "술에 취한듯한 표정을 한 그녀는,\n 그간 자신이 가슴 속에 숨겨온 이야기를 시작했다."

    n "사실, 처음 보았을 때부터 내 이상형이다 싶었어."
    n "내 이상형은 순수한 공대 너드남인데, \n너가 딱 그런 느낌이었어."
    n "오랜 시간동안 솔로로 지내왔는데, \n너라면 내 삶의 일부를 나눠도 되겠다는 확신이 들었어."

    "나는 그 말을 듣고 놀랐다."

    "까칠하기만 해보이던 나경이의 눈 속에 ,\n 내 모습이 은은하게 사랑과 함께 담겨 있음을 깨달았다."
    
    "나는 그녀를 바라보며 답변했다."

    play music "waitforans.mp3"
    menu:
        "너의 눈에 나만 보이듯, 내 눈에도 너만 보여.":
            jump scene12_1_a
        "그 말, 고마워. 근데 나도 좋아하는 사람이 있어.":
            jump scene12_1_b

    label scene12_1_a:
        stop music
        
        play music "sojudump.mp3"

        p "'너의 눈에 나만 보이듯, 내 눈에도 너만 보여.'"
        "나의 대답에 나경은 눈이 크게 벌어지며 놀라워했다."
        n "그리고 그녀는 미소를 지으며, '정말이야? 그건 너무 좋다.'라고 말했다."
        n "우리, 만나 보지 않을래? " # 해피 엔딩. 

        play music "happyending.mp3"
        #엔딩 추가하기
        hide Nakyeong

        jump end5

    label scene12_1_b:
        stop music
        
        play music "sad.mp3"
        
        p "그 말, 고마워. 근데 나도 좋아하는 사람이 있어."
        
        "나의 대답에 나경은 굉장히 실망한 듯 고개를 숙였다."
        
        n '그래도 나는 네가 좋아.'
        n "지금 당장은 너를 만날 수 없다고 하더라도\n 나는 계속 너를 좋아할거야."
        n "계속 기다릴게. 언제든 마음 바뀌면 알려줘"

        "어쩔 수 없이 그녀를 떠나보냈지만, \n 마음이 아픈 것은 어찌 할 도리가 없었다."

        "기숙사로 돌아가는 길은 무겁기만 하였다. "
        stop music

        hide Nakyeong
        
        jump scene13

label scene13:
    # 실습실
    scene bg_room113_whole
    "나경이의 고백을 거절하고 어색한 상태로 실습실에 도착했다."
    "나는 그녀를 거절한 행동에 대해 미안함을 느꼈다. \n 그녀는 나에게 감정을 표현했지만, \n 나는 그것을 받아들이지 못했다."
    "실습실에 도착하니 팀메이트인 지현이 혼자 코딩을 하고 있었다."
    
    p "지현아, 저녁 혼자 먹게 해서 정말 미안하다."
    j "아니야 덕분에 편하게 먹고 싶은 거 먹고 왔어."
    
    "나경이랑 이야기하면서, 나는 확신이 들었다."
    
    "나는 지현을 좋아하고 있었다는 것..."

    show Jihyeon m03 m04
    j "오빠는 밥 맛있게 먹고 왔어?"

    menu:
        "아니, 네가 보고 싶어서 먹는 둥 마는 둥 하고 왔어.":
            jump scene13_1_a
            
        "응 작교 다녀왔는데 맛있더라.":
            jump scene13_1_b

    label scene13_1_a:
        p "아니, 자꾸 네 생각이 나서, 먹는 둥 마는 둥 하고 왔어."
        "나의 대답에 지현이는 놀라 보였다."
        j "그래서 그렇게 빨리 돌아온 거였구나."
        j "나랑은 술 먹으러 가자"
        play music "waitforans.mp3"
        menu:
            "좋아. 하던거만 하고 가자":
                jump scene14
            "너 놀려고 몰입캠프 왔어?":
                "치이.. 오빠 정말 재미없는 사람이네.. "
                "지현이는 기분이 상했는지 아무 말도 하지 않았다. "
                jump scene16
    label scene13_1_b:
        p "응, 작교 다녀왔는데 맛있더라."
        
        j "그래? 좋다."
        
        "나의 대답에 지현이는 아무 대답 없이 코딩에 집중하였다."
        
        "그 이후로 나는 지현이의 집중하는 뒷모습 만을 보았다."
             
        jump end3

label scene13_b:
    # 실습실
    scene bg_room113_whole
    "나경이의 제안을 거절하고 어색한 상태로 실습실에 도착했다."
    
    "실습실에 도착하니 팀메이트인 지현이 혼자 코딩을 하고 있었다."
    show Jihyeon m03 m04
    
    p "지현아, 잘하고 있었어?"

    j "혼자 하느라고 힘들었지."
    
    "나경이랑 이야기하면서, 나는 확신이 들었다."
    
    "나는 지현을 좋아하고 있었다는 것..."


    j "오빠 오늘은 빨리하고 술 먹는 거 어때?"

    play music "waitforans.mp3"
    menu:
        "좋아. 하던거만 하고 가자":
            jump scene14
        "너 놀려고 몰입캠프 왔어?":
            jump scene16


label scene14:
    stop music
    play music "light_happy.mp3"
    scene bg_china_out
    show Jihyeon m03 m04
    "그렇게 우리는 샤오 차이나에 왔다."

    "그녀와 함께라면 어떤 일이든 일어날 수 있을 것 같다."

    "심장이 요동친다."

    j "오빠 오늘 술 많이 마실까아?"

    p "오늘은 적당히 마시자."

    scene bg_china_in

    "뱉은 말과 달리 밤샘 코딩에 지친 우리는 소주를 미친듯이 들이 부었다."
    show soju at truecenter




    j "오빠랑 둘이서 술 먹으니 너무 좋다."
    
    hide soju

    p "나도 너랑 있으니 너무 좋아."
    
    p "지금뿐만이 아니라 평생 같이 있고 싶어."

    p "나랑 평생 같이 있어줄래?"

    j "이 말만을 기다려왔어 오빠."

    "분위기가 점점 무르익어간다."

    "지금이 타이밍인듯하다."

    "그녀에게 행동을 취한다."

    stop music

    

    play music "waitforans.mp3"
    menu:
        
        "박력 있게 벽치기를 한다.":
            "아뿔싸! 벽이 무너진다."
            jump end4
        "소심하게 손을 잡는다.":
            jump scene15_b





label scene15_b:
    j "오빠...손 잡으니 너무 좋다." 

    j "우리 이렇게 평생 함께하자."

    jump end5

label scene16:
    stop music
    "어김없이 한 주가 지나고 발표날인 목요일이 왔다."
    # 117호 
    scene bg_117    
    show Kaistian
    "그 주, 시연이가 금주의 픽으로 선정되었다."
    "그녀는 강단에서 자신감 넘치게 발표를 하고 있었다."
    "나는 그의 강한 열정에 감탄하며 그녀를 뚫어져라 보았다."
    "그 순간, 내 마음은 그녀에게로 이끌렸다."
    "발표를 마친 그녀가 내 앞자리에 앉는다."
menu:
    "시연에게 말을 건네고, 그녀와 이야기하며 공통 관심사를 찾아보자.":
        jump scene16_1_a
    "시연에게 말을 건네는 것이 너무 두려워, 그녀를 멀리서만 지켜보자.":
        jump scene16_1_b
label scene16_1_a:
    "내가 망설임 없이 시연에게 다가갔다."
    p "시연아, 네 발표 정말 멋있었어. 나도 스타트업과 창업에 관심이 많아."
    "그 말에 시연이는 미소를 지었다."
    p " 우리 같이 3주차 프로젝트를 하면 어떨까?"
    "나의 제안에 시연이는 고민 없이 수락했다."
    "그 순간, 나는 내 마음이 시연에게로 기울어지고 있다는 것을 확실히 느꼈다."
    jump scene17
label scene16_1_b:
    "나는 시연에게 말을 건네는 것이 너무 두려워서, \n 그녀를 멀리서만 지켜보았다."
    "하지만 시연이는 다른 사람과 팀을 이루기 시작했다."
    "나는 그것을 지켜보며, \n  '저 자리가 내 자리가 되어야 했는데..'라고 속으로 생각했다."
    "하지만 나는 담담하게 그 모습을 바라보기만 하고, \n 시연에게 내 마음을 전달하지 못했다."
    jump end7



label scene17:
    # 스터디룸에서 코딩 중
    scene bg_room113_whole
    show Kaistian
    p "시연이와 나는 같이  프로젝트를 진행하게 되었다."
    p "시연이는 프론트엔드를 맡아 플러터로 작업하고 있었고, \n 나는 백엔드를 맡아 Node.js로 작업하고 있었다."
    p "그런데 어느 순간, 시연이는 이유를 모르는 에러에 직면해 고민에 빠져있었다."

    sy "'으아, 너무 어렵다... 공식 문서를 뒤져봐도 도대체 무슨 문제인지 모르겠어.'"

    menu:
        "무슨 문제인데? 나도 플러터 써봤어. 도와줄게!":
            jump scene17_a
        "프론트는 네 업무지. 나도 백엔드 짜느라 바쁜데... 화이팅!":
            jump scene17_b
        "플러터는 나도 안 써봤지만, 그래도 나는 챗지피티 프로 유저니까 도움이 될 수 있을 거야.":
            jump scene17_c

    label scene17_a:
        sy "누구는 플러터 안해봤을 것 같아? 이건 어려운 문제라고."
        sy "나혼자 해결하고 싶어. 아직은 내가 도와달라고 말하지 않았잖아."
        sy "내가 도와달라고 안했는데 나서서 도와주지 않았으면 좋겠어. "
        jump scene18_1
    label scene17_b:
        sy "그렇게 안봤는데 너 정말 싸가지 없다."
        sy "그렇게 쉬우면 니가 해봐. \n 백엔드는 얼마나 잘짜는지 보자. "
        jump end
    label scene17_c:
        sy "어머, 진짜? 너 챗지피티 프로 유저였어?\n 그럼 너랑 같이 프로젝트하는 건 정말 행운이겠다."
        sy "나랑 챗지피티 같이 쓰자. "
        jump scene18_2

label scene18_1:
    p "그날 이후로 시연이와 나는 서로 말 없이 각자의 역할에 집중했다. \n 멋있다고 생각했던 시연이가 자존심이 강하고 틀린 걸  \n 인정하기 싫어하는 사람일 줄은 몰랐다."
    p "우리 둘 다 열심히 했고, 결과물은 그만큼 좋았지만,\n 이제 우리 사이엔 무언가 어색함이 느껴졌다." 
    p "이후로 우리는 프로젝트 외에는 딱히 연락하지 않게 되었다."
    jump end8

label scene18_2:
    "챗지피티를 나눠 쓰게 된 이후로, 시연이와 나는 점점 자주 연락하게 되었다."
    "우리 둘 다 열심히 했고, 결국 금주의 픽에 선정되었다." 
    "3주차에 금주의 픽에 선정되어 기뻤지만,\n 4주차에는 시연이와 함께 팀을 할 수 없어 아쉬웠다. "
    "교실에서 그녀를 마주칠 때마다 심장은 미친 듯이 뛰었다. \n 그런데도 외면하려고 애쓰며, 그저 코딩에만 몰두했다."

    "하지만 챗 지피티를 이용하려고 들어갔을 때, 내 심장은 멎을 듯이 뛰었다. "
    show gpt_siyeon at top
    "그곳에는 '남자에게 고백하는 법', 'intp 이상형' 등의 검색 내역이 남아 있었다. "
    "나와 함께 챗지피티를 쓰는 사람은 시연이밖에 없었다. \n 과연 이게 그녀가 물어본 건지, 그런 생각에 밤새 잠을 이루지 못했다." 
    
    p "몰입캠프가 끝나기 전에 꼭 그녀에게 고백을 해야겠다는 생각을 했다."
    p " 그래서 그냥 잠을 못 이루던 밤, 카톡을 보내기로 결심했다."
    p "그래서 우리 둘은 3분반 1호 커플로 불리게 되었다. \n 몰입캠프 전체에게 똑똑하고 열정 넘치는 커플로 소문이 나, \n 그런 주목받는 내내 시연이와 함께하는 시간이 즐거웠다." 
    jump happyEnding_Siyoen

label end:
    "그렇게 미연시는 막을 내린다.."
    jump end_fail
label end1:
    "그렇게 나는 일주일간 그녀와 아무 말도 할 수 없었고, \n 몰입캠프 전체에  인신공격남으로 소문나게 되어 \n 괴로운 한달을 보내야 했다…"
    jump end_fail
label end2:
    "그렇게 나는 일주일간 그녀와 아무 말도 할 수 없었고, \n 몰입캠프 전체에  급발진남으로 소문나게 되어 \n 괴로운 한달을 보내야 했다…"
    jump end_fail
label end3:
    "그렇게 나는 굴러들어온 지현이를 걷어찼다. "
    jump end_fail

label end4:
    "샤오차이나의 벽은 굉장히 약했다. \n 부상을 입은 지현이와 나는 서둘러 응급실에 실려간다.."
    jump end_fail

label end5:
    "Happy Ending!!"
    jump end_success

label end7: 
    "다른 남자와 잘되어가는 시연의 모습을 지켜보는 것은 \n 마음이 너무 안좋았지만, 내가 할 수 있는 것은 없었다. "
    "그렇게, 나는 모쏠 탈출을 하지 못한 채 게임이 끝났다."
    jump end_fail

label end8: 
    "모쏠탈출은 비록 실패했지만, \n여러 프로젝트를 하며 코딩실력은 한층 성장한 것 같다. "
    jump end_fail

label happyEnding_Siyoen:
    " 나와 시연은 서로의 지적인 욕구를 충족시켜주며, \n몰입캠프 3분반 1호 커플로 소문나게 되었다. "
    jump end_success

label happyEnding_Hitomi:
    " 나와 히토미는 서로의 사랑을 확인하며, \n 몰입캠프 3분반 1호 커플로 소문나게 되었다. "
    jump end_success




label end_fail:
    scene mstc_fail
    show mo with dissolve:
        linear 1.0 xpos 200 ypos 500
    show ssol with dissolve:
        linear 1.0 xpos 400 ypos 500
    show tal with dissolve:
        linear 1.0  xpos 600 ypos 500
    show chul with dissolve:
        linear 1.0 xpos 800 ypos 500
    show sil with dissolve:
        linear 1.0 xpos 1000 ypos 500
    show pae with dissolve:
        linear 1.0 xpos 1200 ypos 500
    $ renpy.pause(15, hard=False)
    jump the_end



label end_success:
    show sa with dissolve:
        linear 1.0 xpos 200 ypos 500
    show rang with dissolve:
        linear 1.0 xpos 500 ypos 500
    show jang with dissolve:
        linear 1.0  xpos 800 ypos 500
    show che with dissolve:
        linear 1.0 xpos 1100 ypos 500
    show heart with dissolve:
        linear 1.0 xpos 1400 ypos 500
    $ renpy.pause(15, hard=False)
    jump the_end


label the_end:
    "The end"



