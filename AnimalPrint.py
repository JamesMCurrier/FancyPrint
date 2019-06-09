import random


# Alias python print statement
stdout = print

allsee = []

alien = r''' \            _       _
  \          (_\     /_)
   \           ))   ((
    \        .-"""""""-.  
     \   /^\/  _.   _.  \/^\
      \  \(   /__\ /__\   )/
          \,  \o_/_\o_/  ,/
            \    (_)    /
             `-.'==='.-'
              __) - (__   
             /  `~~~`  \
            /  /     \  \
            \ :       ; /
             \|==(*)==|/
              :       :
               \  |  /
             ___)=|=(___
            {____/ \____}


'''
allsee.append('alien')

alligator = r'''  \
   \
    \
     \
      \        _ ___                /^^\ /^\  /^^\_
    _          _@)@) \            ,,/ '` ~ `'~~ ', `\.
  _/o\_ _ _ _/~`.`...'~\        ./~~..,'`','',.,' '  ~:
 / `,'.~,~.~  .   , . , ~|,   ,/ .,' , ,. .. ,,.   `,  ~\_
( ' _' _ '_` _  '  .    , `\_/ .' ..' '  `  `   `..  `,   \_
 ~V~ V~ V~ V~ ~\ `   ' .  '    , ' .,.,''`.,.''`.,.``. ',   \_
  _/\ /\ /\ /\_/, . ' ,   `_/~\_ .' .,. ,, , _/~\_ `. `. '.,  \_
 < ~ ~ '~`'~'`, .,  .   `_: ::: \_ '      `_/ ::: \_ `.,' . ',  \_
  \ ' `_  '`_    _    ',/ _::_::_ \ _    _/ _::_::_ \   `.,'.,`., \-,-,-,_,_,
   `'~~ `'~~ `'~~ `'~~  \(_)(_)(_)/  `~~' \(_)(_)(_)/ ~'`\_.._,._,'_;_;_;_;_;


'''
allsee.append('alligator')

balloon = r'''    \
     \                 @@@@@@@
      \          @@@@@@@_____@@@@@@@ 
       \     @@@@@________________@@@@@ 
        \  @@@@______________________@@@@ 
          @@____________________________@@ 
        @@________________________________@@ 
       @@_______@@@@@_________@@@@@________@@ 
      @@_______@@@@@@@_______@@@@@@@________@@ 
     @@________@@@@@@@_______@@@@@@@_________@@
     @@_________@@@@@_________@@@@@__________@@
     @@______________________________________@@
     @@______@@@__________________@@@________@@
      @@_______@@@______________@@@_________@@ 
       @@________@@@@________@@@@__________@@ 
        @@_________@@@@@@@@@@@@___________@@ 
          @@____________________________@@ 
            @@@______________________@@@ 
              @@@________________@@@ 
                 @@@@@@______@@@@@@ 
                       @@@@@@ 
                      @@____@@ 
                     @@______@@ 
                      @@@@@@@@ 
                         @@ 
                        @@ 
                      @@@ 
                     @@ 
                     @@ 
                      @@
                      @@
                    @@


'''
allsee.append('balloon')

bird = r'''   \
    \        .-''-.
     \      /      \
      \  .-'`(o)    ;
        '-==.       |
             `._...-;-.
              )--"""   `-.
             /   .        `-.
            /   /      `.    `-.
            |   \    ;   \      `-._________
            |    \    `.`.;          -------`.
             \    `-.   \\\\          `---...|
              `.     `-. ```\.--'._   `---...|
                `-.....7`-.))\     `-._`-.. /
                  `._\ /   `-`         `-.,'
                    / /
                   /=(_
                -./--' `      
              ,^-(_
              ,--' `


'''
allsee.append('bird')

bug = r'''                    _         _
                   /x\       /x\
                  /v\x\     /v\/\
                  \><\x\   /></x/
                   \><\x\ /></x/
           __ __  __\><\x/></x/___
          /##_##\/       \</x/    \__________
         |###|###|  \         \    __________\
          \##|##/ \__\____\____\__/          \\
            |_|   |  |  | |  | |              \|
            \*/   \  |  | |  | /              /
                    /    /
                    

'''
allsee.append('bug')

calf = r'''       \   ,__,
        \  (oo)____
           (__)    )\
              ||--|| *


'''
allsee.append('calf')

cat = r'''    \       /\       /\
     \     /  \"""""/  \
      \   |  \/\"""/\/  |
       \  `, <O>\"/<O> ,`
          ====== Y ======
            \   -^-   /
             \       / \__,
            /  `````       \______,
           |    ```         " " "  \,
           |     `           " "     \
           |            |     "    "  \
           |    _      /            "  |
           | " / \ "  /              " |
           |   | |   |\__ _______\    "|
          / -  | | -  \ /   "   "   " /
          \___/   \___/ \____________/


'''
allsee.append('cat')

cow = r'''      \   ^__^
       \  (oo)\_______
          (__)\       )\/\
              ||----w |
              ||     ||


'''
allsee.append('cow')

devil = r'''     \
      \         ,        ,
       \       /(        )`
        \      \ \___   / |
               /- _  `-/  '
              (/\/ \ \   /\
              / /   | `    \
              O O   ) /    |
              `-^--'`<     '
             (_.)  _  )   /
              `.___/`    /
                `-----' /
   <----.     __ / __   \
   <----|====O)))==) \) /====
   <----'    `--' `.__,' \
                |        |
                 \       /
           ______( (_  / \______
         ,'  ,-----'   |        \
         `--{__________)        \/


'''
allsee.append('devil')

dinosaur = r'''    \                             .       .
     \                           / `.   .' " 
      \                  .---.  <    > <    >  .---.
       \                 |    \  \ - ~ ~ - /  /    |
             _____          ..-~             ~-..-~
            |     |   \~~~\.'                    `./~~~/
           ---------   \__/                        \__/
          .'  O    \     /               /       \  " 
         (_____,    `._.'               |         }  \/~~~/
          `----.          /       }     |        /    \__/
                `-.      |       /      |       /      `. ,~~|
                    ~-.__|      /_ - ~ ^|      /- _      `..-'   
                         |     /        |     /     ~-.     `-. _  _  _
                         |_____|        |_____|         ~ - . _ _ _ _ _>


'''
allsee.append('dinosaur')

dog = r'''   \      __
    \    /  \
     \  / ..|\
       (_\  |_)
       /  \@'
      /     \
  _  /  `   |
 \\/  \  | _\
  \   /_ || \\_
   \____)|_) \_) 


'''
allsee.append('dog')

dragon = r'''       \
        \
         \                   / \  //\
          \    |\___/|      /   \//  \\
               /O  O  \__  /    //  | \ \    
              /     /  \/_/    //   |  \  \  
              @_^_@'/   \/_   //    |   \   \ 
              //_^_/     \/_ //     |    \    \
           ( //) |        \///      |     \     \
         ( / /) _|_ /   )  //       |      \     _\
       ( // /) '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
     (( / / )) ,-{        _      `-.|.-~-.           .~         `.
    (( // / ))  '/\      /                 ~-. _ .-~      .-~^-.  \
    (( /// ))      `.   {            }                   /      \  \
     (( / ))     .----~-.\        \-'                 .~         \  `. \^-.
                ///.----..>        \             _ -~             `.  ^-`  ^-_
                  ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                     /.-~


'''
allsee.append('dragon')

elephant = r'''    \     /\  ___  /\
     \   // \/   \/ \\
        ((    O O    ))
         \\ /     \ //
          \/  | |  \/ 
           |  | |  |  
           |  | |  |  
           |   o   |  
           | |   | |  
           |m|   |m|  


'''
allsee.append('elephant')

fish = r'''  \
   \         ,-.-,-,
    \      _/ / / /       /)
     \   ,'        `.   ,'')
       _/(@) `.      `./ ,')
      (____,`  \:`-.   \ ,')
       (_      /::::}  / `.)
        \    ,' :,-' ,)\ `.)
         `.        ,')  `..)
           \-....-'\      \)  
            `-`-`-`-`


'''
allsee.append('fish')

flamingo = r'''  \                                                    # #
   \                                                   # #
    \    __                                         #  : : #
     \ .^o ~\                                       #  : : #
      | /'~) }      _____                        #. ':': :: #
      |/  / /    ,-~     ~~--.,_              #.  #  : :':: #
         ( (    /  ~-._         ^.             #  ':.: ::': :
          \ "--'--.    "-._       \            ':  ': :: : :':
           "-.________     ~--.,__ ^.           ':.':::.:': :
                     \"~--.,___.-'-. ^.          ':.. ::::.:.:
                      ||    \\      ~-.\       ..::..'::::::::
                      ||     \\        `\    .'  ':. '::::::::
                      ||     //                   '::.::::::::
                      ||    //                  .. :::::::::::
                      ()   //                  '  ':::::::::::
                      ||  //                       .::::::::::
                      || ((                      ' ::::::::::
_.__ __  ___._ __  ___||__`--__._ __  ___ __  _   _'::::::::::
 ~"~   "~     ~  "~   ::  ~~"    ~  ~~   ~  ~~ "~~  ~~--~"---~
                      ::   ::
                      .:    .:


'''
allsee.append('flamingo')

frog = r'''    \     ,-.___.-.
     \ ,-.(|)   (|),-.
       \_*._ ' '_.* _/
        /`-.`--' .-'\
   ,--./    `---'    \,--.
   \   |(  )     (  )|   /
    \  | ||       || |  /
     \ | /|\     /|\ | /
     /  \-._     _,-/  \
    //| \\  `---'  // |\\
   /,-.,-.\       /,-.,-.\
  o   o   o      o   o    o


'''
allsee.append('frog')

giraffe = r'''         \      ___,A.A_  __
          \    \   ,    "_/
           \    ~"|(  o o)
            \     | \    |
                  |  ~\ .|
                  |   |`-'
                  |   |
                  |   |
                  |   |
                  |   |
                  |   |
                 /     \
                !       !
                |   \  /|
                /\   )( (
               /  \  || |\
              !    | || | !
              |    ( )( ) |
             / .    \ ` | |\   
            !   \    |  | ! !
            |   .\_  |  |/  |
             \ /   [\[][]/] |


'''
allsee.append('giraffe')

horse = r'''  \         ,
   \      ,,)\.~,,._
    \    (()`  ``)\))),,_
     \    |     \ ''((\)))),,_          ____
      \   |6`   |   ''((\())) "-.____.-"    `-.-,
       \  |    .'\    ''))))'                  \)))
          |   |   `.     ''                     ((((
          \, _)     \/                          |))))
           `'        |                          (((((
                     \                  |       ))))))
                      `|    |           ,\     /((((((
                       |   / `-.______.<  \   |  )))))
                       |   |  /         `. \  \  ((((
                       |  / \ |           `.\  | (((
                       \  | | |             )| |  ))
                        | | | |            / | |  '
                        | | /_(           /_(/ /
                        /_(/__]           \_/_(
                       /__]                /__]


'''
allsee.append('horse')

kangaroo = r'''                        \                         _  _
                         \                       (\\( \
                          \                       `.\-.)
                              _...._            _,-'   `-.
\                           ,'      `-._.---.,-'       .  \
 \`.                      ,'                               `.
  \ `-...__              /                           .   .:  y
   `._     ``--..__     /                           ,'`---._/
      `-._         ``--'                      |    /_
          `.._                   _            ;   <_ \
              `--.___             `.           `-._ \ \
                     `--<           `.     (\ _/)/ `.\/
                         \            \     `<a \  /_/
                          `.           ;      `._y
                            `--.      /    _../
                                \    /__..'
                                 ;  //
                                <   \\
                                 `.  \\
                                   `. \\_ __
                                     `.`-'  \\
                                       `----'' 


'''
allsee.append('kangaroo')

lion = r'''  /                             ,.
   \                      ,_> `.   ,';
    \                   ,-`'      `'   '`'._
     \              ,,-) ---._   |   .---''`-),.
      \           ,'      `.  \  ;  /   _,'     `,
       \       ,--' ____       \   '  ,'    ___  `-,
        \     _>   /--. `-.              .-'.--\   \__
         \   '-,  (    `.  `.,`~ \~'-. ,' ,'    )    _\
             _<    \     \ ,'  ') )   `. /     /    <,.
          ,-'   _,  \    ,'    ( /      `.    /        `-,
          `-.,-'     `.,'       `         `.,'  `\    ,-'
           ,'       _  /   ,,,      ,,,     \     `-. `-._
          /-,     ,'  ;   ' _ \    / _ `     ; `.     `(`-\
           /-,        ;    (o)      (o)      ;          `'`,
         ,~-'  ,-'    \     '        `      /     \      <_
         /-. ,'        \                   /       \     ,-'
           '`,     ,'   `-/             \-' `.      `-. <
            /_    /      /   (_     _)   \    \          `,
              `-._;  ,' |  .::.`-.-' :..  |       `-.    _\
                _/       \  `:: ,^. :.:' / `.        \,-'
              '`.   ,-'  /`-..-'-.-`-..-'\            `-.
                >_ /     ;  (\/( ' )\/)  ;     `-.    _<
                ,-'      `.  \`-^^^-'/  ,'        \ _<
                 `-,  ,'   `. `"""""' ,'   `-.   <`'
                   ')        `._.,,_.'        \ ,-'
                    '._        '`'`'   \       <
                       >   ,'       ,   `-.   <`'
                        `,/          \      ,-`
                         `,   ,' |   /     /
                          '; /   ;        (
                           _)|   `       (
                           `')         .-'
                             <_   \   /    
                               \   /\(
                                `;/  `


'''
allsee.append('lion')

milk = r'''     \
      \     ____________ 
       \    |__________|
           /           /\
          /           /  \
         /___________/___/|
         |          |     |
         |  ==   == |     |
         |   O   O  | \ \ |
         |     <    |  \ \|
        /|          |   \ \
       / |  \_____/ |   / /
      / /|          |  / /|
     /||\|          | /||\/
         -------------|   
             | |    | | 
            <__/    \__>


'''
allsee.append('milk')

moose = r'''     \
      \   \_\_    _/_/
       \      \__/
              (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||


'''
allsee.append('moose')

penguin = r'''   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/


'''
allsee.append('penguin')

pig = r'''        \
         \
          \
           \    _,--.       ,--._
            \   \  > `-"""-' <  /
             \   `-.         .-'
                   / 'e___e` \
                  (   (o o)   )
                  _\_  `='  _/_
                 / /|`-._.-'|\ \
                / /||_______||\ \
              _/ /_||=======||_\ \_
             / _/==||       ||==\_ \
             `'(   ^^       ^^   )`'
                \               /
                 \______|______/ 
                 |______|______|
                   )__|   |__(
                  /   ]   [   \
                  `--'     `--'


'''
allsee.append('pig')

rhino = r'''      \                        ,-.             __
       \                     ,'   `---.___.---'  `.
        \                  ,'   ,-                 `-._
         \               ,'    /                       \
          \           ,\/     /                        \\
           \      )`._)>)     |                         \\
            \     `>,'    _   \                  /       |\
                    )      \   |   |            |        |\\
           .   ,   /        \  |    `.          |        | ))
           \`. \`-'          )-|      `.        |        /((
            \ `-`   a`     _/ ;\ _     )`-.___.--\      /  `'
             `._         ,'    \`j`.__/        \  `.    \
               / ,    ,'       _)\   /`        _) ( \   /
               \__   /        /nn_) (         /nn__\_) (
                 `--'           /nn__\             /nn__\


'''
allsee.append('rhino')

sheep = r'''     \
      \
          __     
         UooU\.'@@@@@@`.
         \__/(@@@@@@@@@@)
              (@@@@@@@@)
              `YY~~~~YY'
               ||    ||


'''
allsee.append('sheep')

smile = r'''           \ 
            \ 
             \ 
              \           __ooooooooo__
               \      oOOOOOOOOOOOOOOOOOOOOOo
                  oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
               oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
             oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
           oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
          oOOOOOOOOOOO*  *OOOOOOOOOOOOOO*  *OOOOOOOOOOOOo
         oOOOOOOOOOOO      OOOOOOOOOOOO      OOOOOOOOOOOOo
         oOOOOOOOOOOOOo  oOOOOOOOOOOOOOOo  oOOOOOOOOOOOOOo
        oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
        oOOOO     OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO     OOOOo
        oOOOOOO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOo
         *OOOOO  OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  OOOOO*
         *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
          *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
           *OOOOOOo  *OOOOOOOOOOOOOOOOOOOOOOO*  oOOOOOO*
             *OOOOOOOo  *OOOOOOOOOOOOOOOOO*  oOOOOOOO*
               *OOOOOOOOo  *OOOOOOOOOOO*  oOOOOOOOO*
                  *OOOOOOOOo.         .oOOOOOOOO*
                      *OOOOOOOOOOOOOOOOOOOOO*
                           ""ooooooooo""


'''
allsee.append('smile')

snail = r'''  \          /^\    /^\
   \        {  O}  {  O}
    \        \ /    \ /
     \       //     //       _------_
      \     //     //     ./~        ~-_
           / ~----~/     /              \
         /         :   ./       _---_    ~-
        |  \________) :       /~     ~\   |
        |        /    |      |  :~~\  |   |
        |       |     |      |  \___-~    |
        |        \ __/`^\______\.        ./
         \                     ~-______-~\.
         .|                                ~-_
        /_____________________________________~~____


'''
allsee.append('snail')

snake = r'''    \               /^\/^\
     \            _|__|  O|
      \  \/     /~     \_/ \
          \____|__________/  \
                 \_______      \
                         `\     \                 \
                           |     |                  \
                          /      /                    \
                         /     /                       \
                       /      /                         \ \
                      /     /                            \  \
                    /     /             _----_            \   \
                   /     /           _-~      ~-_         |   |
                  (      (        _-~    _--_    ~-_     _/   |
                   \      ~-____-~    _-~    ~-_    ~-_-~    /
                     ~-_           _-~          ~-_       _-~
                        ~--______-~                ~-___-~


'''
allsee.append('snake')

tiger = r"""   \
    \
     \
      \     _ ___.--'''`--''//-,-_--_.
         \`"' ` || \\ \ \\/ / // / ,-\\`,_
        /'`  \ \ || Y  | \|/ / // / - |__ `-,
       /O"\  ` \ `\ |  | ||/ // | \/  \  `-._`-,_.,
      /  _.-. `.-\,___/\ _/|_/_\_\/|_/ |     `-._._)
      `-'``/  /  |  // \__/\__  /  \__/ \
           `-'  /-\/  | -|   \__ \   |-' |
             __/\ / _/ \/ __,-'   ) ,' _|'
            (((__/(((_.' ((___..-'((__,'


"""
allsee.append('tiger')

turkey = r'''     \                                  ,+*^^*+___+++_
      \                           ,*^^^^              )
       \                       _+*                     ^**+_
        \                    +^       _ _++*+_+++_,         )
                 _+^^*+_    (     ,+*^ ^          \+_        )
                {       )  (    ,(    ,_+--+--,      ^)      ^\
               { (@)    } f   ,(  ,+-^ __*_*_  ^^\_   ^\       )
              {:;-/    (_+*-+^^^^^+*+*<_ _++_)_    )    )      /
             ( /  (    (        ,___    ^*+_+* )   <    <      \
              U _/     )    *--<  ) ^\-----++__)   )    )       )
               (      )  _(^)^^))  )  )\^^^^^))^*+/    /       /
             (      /  (_))_^)) )  )  ))^^^^^))^^^)__/     +^^
            (     ,/    (^))^))  )  ) ))^^^^^^^))^^)       _)
             *+__+*       (_))^)  ) ) ))^^^^^^))^^^^^)____*^
             \             \_)^)_)) ))^^^^^^^^^^))^^^^)
              (_             ^\__^^^^^^^^^^^^))^^^^^^^)
                ^\___            ^\__^^^^^^))^^^^^^^^)\\
                     ^^^^^\uuu/^^\uuu/^^^^\^\^\^\^\^\^\^\
                        ___) >____) >___   ^\_\_\_\_\_\_\)
                       ^^^//\\_^^//\\_^       ^(\_\_\_\)
                         ^^^ ^^ ^^^ ^


'''
allsee.append('turkey')

turtle = r'''       \        
        \                                  ___-------___
         \                             _-~~             ~~-_
          \                         _-~                    /~-_
                 /^\__/^\         /~  \                   /    \
               /|  O|| O|        /      \_______________/        \
              | |___||__|      /       /                \          \
              |          \    /      /                    \          \
              |   (_______) /______/                        \_________ \
              |         / /         \                      /            \
               \         \^\\         \                  /               \     /
                 \         ||           \______________/      _-_       //\__//
                   \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
                     ~-----||====/~     |==================|       |/~~~~~
                      (_(__/  ./     /                    \_\      \.
                             (_(___/                         \_____)_)



'''
allsee.append('turtle')

whale = r'''      \        __   __
       \      __ \ / __
        \    /  \ | /  \
                 \|/
            _,.---v---._
   /\__/\  /            \
   \_  _/ /              \
     \ \_|           @ __|
      \                \_
       \     ,__/       /
     ~~~`~~~~~~~~~~~~~~/~~~~

'''
allsee.append('whale')


fortunes = '''A beautiful, smart, and loving person will be coming into your life
A dubious friend may be an enemy in camouflage 
A feather in the hand is better than a bird in the air
A fresh start will put you on your way
A friend asks only for your time not your money
A friend is a present you give yourself
A gambler not only will lose what he has, but also will lose what he doesn’t have
A golden egg of opportunity falls into your lap this month
A good friendship is often more important than a passionate romance
A good time to finish up old tasks
A hunch is creativity trying to tell you something
A lifetime friend shall soon be made
A light heart carries you through all the hard times
A new perspective will come with the new year
A person is never to old to learn
A person of words and not deeds is like a garden full of weeds
A pleasant surprise is waiting for you
A small donation is call for It’s the right thing to do
A smile is your personal welcome mat
A smooth long journey! Great expectations
A soft voice may be awfully persuasive
A truly rich life contains love and art in abundance
Accept something that you cannot change, and you will feel better
Adventure can be real happiness
Advice is like kissing, it costs nothing and is a pleasant thing to do
Advice, when most needed, is least heeded
All the effort you are making will ultimately pay off
All the troubles you have will pass away very quickly
All will go well with your new project
All your hard work will soon pay off
Allow compassion to guide your decisions
An agreeable romance might begin to take on the appearance
An important person will offer you support
An inch of time is an inch of gold
Any decision you have to make tomorrow is a good decision
At the touch of love, everyone becomes a poet
Be careful or you could fall for some tricks today
Beauty in its various forms appeals to you 
Because you demand more from yourself, others respect you deeply
Believe in yourself and others will too
Believe it can be done
Better ask twice than lose yourself once
Carve your name on your heart and not on marble
Change is happening in your life, so go with the flow!
Competence like yours is underrated
Congratulations! You are on your way
Could I get some directions to your heart? 
Courtesy begins in the home
Courtesy is contagious
Curiosity kills boredom Nothing can kill curiosity
Dedicate yourself with a calm mind to the task at hand
Depart not from the path which fate has you assigned
Determination is what you need now
Disbelief destroys the magic
Distance yourself from the vain
Do not be intimidated by the eloquence of others
Do not demand for someone’s soul if you already got his heart
Do not let ambitions overshadow small success
Do not make extra work for yourself
Do not underestimate yourself Human beings have unlimited potentials
Don’t be discouraged, because every wrong attempt discarded is another step forward
Don’t confuse recklessness with confidence 
Don’t just spend time Invest it
Don’t just think, act!
Don’t let friends impose on you, work calmly and silently
Don’t let the past and useless detail choke your existence
Don’t let your limitations overshadow your talents
Don’t worry; prosperity will knock on your door soon
Each day, compel yourself to do something you would rather not do
Education is the ability to meet life’s situations
Embrace this love relationship you have!
Emulate what you admire in your parents 
Emulate what you respect in your friends
Every flower blooms in its own sweet time
Every wise man started out by asking many questions
Everyday in your life is a special occasion
Failure is the chance to do better next time
Failure is the path of lease persistence
Fear and desire – two sides of the same coin
Feeding a cow with roses does not get extra appreciation
For hate is never conquered by hate Hate is conquered by love
For the things we have to learn before we can do them, we learn by doing them
Fortune Not Found: Abort, Retry, Ignore?
From listening comes wisdom and from speaking repentance
From now on your kindness will lead you to success
Get your mind set – confidence will lead you on
Get your mind set…confidence will lead you on
Go take a rest; you deserve it
Good news will be brought to you by mail
Good news will come to you by mail
Good to begin well, better to end well
Happiness begins with facing life with a smile and a wink
Happiness will bring you good luck
Happy life is just in front of you
Hard words break no bones, fine words butter no parsnips
Have a beautiful day
He who expects no gratitude shall never be disappointed 
He who knows he has enough is rich
Help! I’m being held prisoner in a chinese bakery!
How you look depends on where you go
I learn by going where I have to go
If a true sense of value is to be yours it must come through service
If certainty were truth, we would never be wrong
If you continually give, you will continually have
If you look in the right places, you can find some good offerings
If you think you can do a thing or think you can’t do a thing, you’re right
If your desires are not extravagant, they will be granted
If your desires are not to extravagant they will be granted 
Imagination rules the world
In order to take, one must first give
In the end all things will be known
It could be better, but its[sic] good enough
It is better to be an optimist and proven a fool than to be a pessimist and be proven right
It is better to deal with problems before they arise
It is honorable to stand up for what is right, however unpopular it seems
It is worth reviewing some old lessons
It takes courage to admit fault
It’s time to get moving Your spirits will lift accordingly
Keep your face to the sunshine and you will never see shadows
Let the world be filled with tranquility and goodwill
Like the river flow into the sea Something are just meant to be
Listen not to vain words of empty tongue
Listen to everyone Ideas come from everywhere
Living with a commitment to excellence shall take you far
Long life is in store for you
Love is a warm fire to keep the soul warm
Love is like sweet medicine, good to the last drop
Love lights up the world
Love truth, but pardon error 
Man is born to live and not prepared to live
Man’s mind, once stretched by a new idea, never regains it’s original dimensions
Many will travel to hear you speak
Meditation with an old enemy is advised
Miles are covered one step at a time
Nature, time and patience are the three great physicians
Never fear! The end of something marks the start of something new
New ideas could be profitable
New people will bring you new realizations, especially about big issues 
No one can walk backwards into the future
Now is a good time to buy stock
Now is the time to go ahead and pursue that love interest!
Now is the time to try something new
Now is the time to try something new
Others can help you now
Pennies from heaven find their way to your doorstep this year!
People are attracted by your Delicate[sic] features
People find it difficult to resist your persuasive manner
Perhaps you’ve been focusing too much on saving
Physical activity will dramatically improve your outlook today
Pick battles big enough to matter, small enough to win
Place special emphasis on old friendship
Please visit us at wwwwontonfoodcom
Po Says: Pandas like eating bamboo, but I prefer mine dipped in chocolate
Practice makes perfect
Protective measures will prevent costly disasters
Put your mind into planning today Look into the future
Remember to share good fortune as well as bad with your friends
Rest has a peaceful effect on your physical and emotional health
Resting well is as important as working hard
Romance moves you in a new direction
Savor your freedom – it is precious
Say hello to others You will have a happier day
Self-knowledge is a life long process
Share your joys and sorrows with your family
Sift through your past to get a better idea of the present
Sloth makes all things difficult; industry all easy
Small confidences mark the onset of a friendship
Society prepares the crime; the criminal commits it
Someone you care about seeks reconciliation
Soon life will become more interesting
Stand tall Don’t look down upon yourself 
Staying close to home is going to be best for your morale today
Stop searching forever, happiness is just next to you
Success is a journey, not a destination
Success is going from failure to failure without loss of enthusiasm
Swimming is easy Stay floating is hard
Take care and sensitivity you show towards others will return to you
Take the high road
Technology is the art of arranging the world so we do not notice it
The austerity you see around you covers the richness of life like a veil
The best prediction of future is the past
The change you started already have far-reaching effects Be ready
The change you started already have far-reaching effects Be ready
The first man gets the oyster, the second man gets the shell
The harder you work, the luckier you get
The night life is for you
The one that recognizes the illusion does not act as if it is real
The only people who never fail are those who never try
The person who will not stand for something will fall for anything
The philosophy of one century is the common sense of the next
The saints are the sinners who keep on trying
The secret to good friends is no secret to you 
The small courtesies sweeten life, the greater ennoble it
The smart thing to do is to begin trusting your intuitions
The strong person understands how to withstand substantial loss
The sure way to predict the future is to invent it
The truly generous share, even with the undeserving
The value lies not within any particular thing, but in the desire placed on that thing
The weather is wonderful 
There is no mistake so great as that of being always right
There is no wisdom greater than kindness 
There is not greater pleasure than seeing your loved ones prosper
There’s no such thing as an ordinary cat
Things don’t just happen; they happen just
Those who care will make the effort
Time and patience are called for many surprises await you!
Time is precious, but truth is more precious than time
To know oneself, one should assert oneself
To the world you may be one person, but to one person you may be the world
Today is the conserve yourself, as things just won’t budge
Today, your mouth might be moving but no one is listening
Tonight you will be blinded by passion
Use your eloquence where it will do the most good
Welcome change
“Welcome” is a powerful word
Well done is better than well said
What’s hidden in an empty box?
What’s yours in mine, and what’s mine is mine
When more become too much It’s same as being not enough
When your heart is pure, your mind is clear
Wish you happiness
You always bring others happiness
You are a person of another time
You are a talented storyteller 
You are admired by everyone for your talent and ability
You are almost there
You are busy, but you are happy
You are generous to an extreme and always think of the other fellow
You are going to have some new clothes 
You are in good hands this evening
You are modest and courteous
You are never selfish with your advice or your help
You are next in line for promotion in your firm
You are offered the dream of a lifetime Say yes!
You are open-minded and quick to make new friends 
You are solid and dependable
You are soon going to change your present line of work
You are talented in many ways
You are the master of every situation 
You are very expressive and positive in words, act and feeling
You are working hard
You begin to appreciate how important it is to share your personal beliefs
You can keep a secret
You can see a lot just by looking
You can’t steal second base and keep your foot on first
You desire recognition and you will find it
You have a deep appreciation of the arts and music
You have a deep interest in all that is artistic
You have a friendly heart and are well admired 
You have a shrewd knack for spotting insincerity
You have a yearning for perfection 
You have an active mind and a keen imagination
You have an ambitious nature and may make a name for yourself
You have an unusual equipment for success, use it properly
You have exceeded what was expected
You have the power to write your own fortune
You have yearning for perfection
You know where you are going and how to get there
You look pretty
You love challenge
You love chinese food
You make people realize that there exist other beauties in the world
You never hesitate to tackle the most difficult problems 
You seek to shield those you love and like the role of provider 
You should be able to make money and hold on to it
You should be able to undertake and complete anything
You should pay for this check Be generous
You understand how to have fun with others and to enjoy your solitude
You will always be surrounded by true friends
You will always get what you want through your charm and personality
You will always have good luck in your personal affairs
You will be a great success both in the business world and society 
You will be blessed with longevity
You will be pleasantly surprised tonight
You will be sharing great news with all the people you love
You will be successful in your work
You will be traveling and coming into a fortune
You will be unusually successful in business
You will become a great philanthropist in your later years
You will become more and more wealthy
You will enjoy good health
You will enjoy good health; you will be surrounded by luxury
You will find great contentment in the daily, routine activities
You will have a fine capacity for the enjoyment of life
You will have gold pieces by the bushel
You will inherit a large sum of money
You will make change for the better
You will soon be surrounded by good friends and laughter
You will take a chance in something in near future
You will travel far and wide, both pleasure and business
You will travel far and wide,both pleasure and business
Your abilities are unparalleled
Your ability is appreciated
Your ability to juggle many tasks will take you far
Your biggest virtue is your modesty
Your character can be described as natural and unrestrained
Your difficulties will strengthen you
Your dreams are never silly; depend on them to guide you
Your dreams are worth your best efforts to achieve them
Your energy returns and you get things done
Your family is young, gifted and attractive
Your first love has never forgotten you
Your happiness is before you, not behind you! Cherish it
Your hard work will payoff today
Your heart will always make itself known through your words
Your home is the center of great love
Your ideals are well within your reach
Your infinite capacity for patience will be rewarded sooner or later
Your leadership qualities will be tested and proven
Your life will be happy and peaceful
Your life will get more and more exciting
Your love life will be happy and harmonious
Your love of music will be an important part of your life
Your loyalty is a virtue, but not when it’s wedded with blind stubbornness
Your mentality is alert, practical, and analytical
Your mind is creative, original and alert
Your mind is your greatest asset
Your moods signal a period of change
Your quick wits will get you out of a tough situation
Your success will astonish everyone 
Your talents will be recognized and suitably rewarded
Your work interests can capture the highest status or prestige'''

fortunes = fortunes.split('\n')


def hello():
    '''
    Use when friends is being run as the main program (not imported).

    After using funtion, step by step instructions will be shown.
    '''

    # Getting user input
    while True:
        kind = input("Pick a creature, or enter '?' to view all options: ")

        if kind == 'quit':
            return

        elif kind in ['random', '']:
            inlist = random.randint(0, len(allsee) - 1)
            kind = allsee[inlist]
            break

        elif kind not in allsee:
          if kind != '?':
              stdout('\'' + kind + '\'' +
                      ' is not a valid creature\n')

          if kind == '?':
              stdout(str(allsee + ['random', 'quit']) + '\n')

        else:
          break


    mess = input('Message (leave blank for fortune): ')
    if mess == '':
        inlist = int(random.random() * (len(fortunes) - 2))
        mess = fortunes[inlist].strip()

    # picking friend
    print(mess, kind)

    # exit/restart
    hello()


def print(*args, category='all'):

    mess = ''
    for i in args:
        mess += str(i)

    # building message
    finmid = '< ' + mess + ' >' + '\n'
    mtop = ' ' + '__' + '_' * len(mess) + '\n'
    mbot = ' ' + '--' + '-' * len(mess) + '\n'

    message = mtop + finmid + mbot

    choices = allsee

    if category == 'all':
        kind = choices[random.randint(0, len(choices) - 1)]

    elif category == 'basic':
        choices = ['calf', 'cow', 'dog', 'elephant',
                   'moose', 'penguin', 'sheep', 'whale']
        kind = choices[random.randint(0, len(choices) - 1)]

    elif category == 'fancy':
        choices = ['alligator', 'dragon', 'flamingo',
                   'horse', 'lion', 'tiger', 'turkey', 'pig']
        kind = choices[random.randint(0, len(choices) - 1)]

    elif category == 'faves':
        choices = ['devil', 'dinosaur', 'dragon', 'horse',
                   'rhino', 'snail', 'snake', 'turtle', 'alien']
        kind = choices[random.randint(0, len(choices) - 1)]

    elif category in choices:
        kind = category

    else:
        raise ValueError(str(
            category) + ' is not a valid category or creature. Pick "all", "basic", "fancy", "favorites", or "custom", or pick a specific creature.')

    stdout(message + eval(kind))


if __name__ == "__main__":
    hello()
