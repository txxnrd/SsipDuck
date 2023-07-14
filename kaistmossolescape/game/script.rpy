# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.



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
define player_name = "플레이어 이름"

define p = Character("player_name",dynamic = True,color="#000000")



# 여기에서부터 게임이 시작합니다.
label start:
    scene bg1
    
    with fade

    play music "a-small-miracle-132333.mp3"

    $player_name = renpy.input("이름을 입력해주세요.")
    
    
    
    p "대망의 몰입 캠프 날!!!"

    p "두근두근 카이생의 모쏠 탈출기 시작합니다."
    
    jump scene2

    return

label scene2:
    scene bg2

    with fade

    "짝꿍이 여자네...\n"

    "초등학교 이후로 여자랑 말을 해본 적이 없는데..."

    "말은 어떻게 건네야 하지?"
menu :
    "행동을 결정하시오"
    
    "gpt에게 물어보기":
        jump gpt    
    
    "구글링하기":
        jump google
    

label gpt:
    scene gpt with dissolve
    "역시 gpt는 신이야."
    jump next

label google:
    scene blog with dissolve
    "구글은 모르는게 없어."
label next: