# Coding Beginner: Can I really do this class?
The game's main theme is to overcome the assignments of the class.
I tried to put in this game the emotions I felt doing this class.

# How to Play
Player 1 uses 'W', 'A', 'S', and 'D' to move.
Player 2 uses the direction keys to move.

Each player can use 3 skills at maximum. 
At first, each player can use only basic skills which are fired by the 'Ctrl' key for P1, and the '한자' key for P2.

To acquire the second skill, you have to hit the opponent once. Then your character will be upgraded.
This time, the 'Tab' key for P1 and the ',' key for P2.
The second skills are faster and bigger than the basic ones.

To acquire the third skill, the method is the same.
This time, the 'q' key for P1 and the '.' key for P2.
The third skills are much bigger but at the same time slower.

# Rule to Win
Every round each player has 5 lives.
The player who will win 3 times first will be a winner.

# Extra explanations for Coding

(1) manufacture of each skill
첫번째로 각 스킬들이 생성되는 과정으로는, 우선 메인 함수에서 각 스킬의 이미지를 불러와 스케일 조정을 하구요. 각 플레이어 이미지의 rect 정보를 구해놓고, 필요한 빈리스트들을 만들어 놓습니다. 그리고는 키눌림 event 발생시 스킬이미지의 xy좌표를 플레이어의 xy좌표로 지정한다음 해당 스킬의 xy좌표를 담는 빈리스트에 append합니다. 그리고는 후에 draw를 하는 함수안에서 속도를 입히고 충돌을 감지하고 마침내 스킬을 화면에 띄우게 됩니다. 모든 스킬을 같은 과정을 통해 만들었습니다. 

(2) level up effect
두번째 중심 기능으로는 레벨업 효과입니다. 레벨업시에 레벨업이미지와 사운드를 일정 시간동안 화면에 띄우기 위하여 레벨업클래스를 만들어서 life_tick 기능을 부여하였습니다. 또한 콜이젼 체크시에 맞은 플레이어의 목숨 개수에 따라서 잔여 목숨이 4개이면 첫번째 레벨업 효과, 그리고 잔여 목숨이 3개이면 두번째 레벨업 효과가 발생하도록 적용시켰습니다. 

(3) 3 times first, winner 
마지막으로 5판3선승제에 관한 코딩을 설명드리겠습니다. 5라운드가 적용되는 과정을 설명드리자면, 먼저 대기 화면으로 가게하는 함수를 지정한다음, 메인 함수에서 해당 함수를 먼저 실행하고, 그 다음으로 while 무한루프를 돌리면서 두 플레이어 중 한 명이 3승을 하기 전까지는 무한루프를 계속 돌려주는 식으로 5판 3선승제를 적용시켰습니다. 3승을 하였을 시 각 플레이어의 모든 정보를 초기화시키고, break한다음 다시 main함수에 접속하게 하여 대기화면이 띄워지도록 하였습니다.

For playing the game, you can play by downloading the assets folder to the main screen of your computer and opening the Python file in the assets folder.

Thank you!

# Citations
The citations of assets are attached in the assets folder.

# Youtube link
https://youtu.be/Zswbo0_BqHE

![미디어 플레이어 2023-07-12 오전 3_59_39](https://github.com/qlswns0/qlswns0/assets/138393299/d88ff9cb-c992-4adf-b29e-2da51dfc072f)
![미디어 플레이어 2023-07-12 오전 4_03_40](https://github.com/qlswns0/qlswns0/assets/138393299/ed3446a8-3ab0-4ab6-a64b-7451dc35e5a1)
![미디어 플레이어 2023-07-12 오전 4_01_51](https://github.com/qlswns0/qlswns0/assets/138393299/61208ab2-371e-4bc5-afa1-8f6e297eed95)
![미디어 플레이어 2023-07-12 오전 4_02_40](https://github.com/qlswns0/qlswns0/assets/138393299/9268d849-6eba-455c-9136-d0efde67dc2b)
![미디어 플레이어 2023-07-12 오전 4_03_19](https://github.com/qlswns0/qlswns0/assets/138393299/ece5ec54-dd5c-4eec-b1aa-419b05d1ec92)
![미디어 플레이어 2023-07-12 오전 4_02_54](https://github.com/qlswns0/qlswns0/assets/138393299/984f324b-f1ea-4163-ab25-8bf4738f78f5)
![미디어 플레이어 2023-07-12 오전 4_03_21](https://github.com/qlswns0/qlswns0/assets/138393299/07bc982f-cc96-401c-8c38-0ea20093006d)



<!---
qlswns0/qlswns0 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
