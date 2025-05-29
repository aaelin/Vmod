init:
    $ mods ["vladstory_prolog"] = u"Этот прекрасный лагерь! 0.78с-test"
    $ vl = Character(u"Влад", color="#54555b", what_color="#E2C778")
    $ li = Character(u"Алина", color="#9604ad", what_color="#E2C778")
    $ isVisible = False
    $ isVisible_tbox = True
    default persistent.failed_4day = False
    default persistent.count_tries = 0
    default persistent.persistent.val_changed = False
    $ message_t = u"Вы вспоминаете совсем другое. Продолжить?"
    
    default persistent.thought_count = 0
    default persistent.achievement_shown = False
    default persistent.achievement_sleep_shown = False
    $ thoughts_imageblank = "mods/Vmod/pic/fon_gui2.png"
    $ thought1 = u""
    $ thought2 = u""
    $ thought3 = u""
    $ thought4 = u""
    $ thought4 = u""


#При нажатии на k — откроется clear_persistent.
# screen clear_persistent:
        # key "k" action SetVariable("isVisible", not isVisible) #Show("clear_persistent")? 
        # if isVisible == True:
            # add "mods/Vmod/pic/fon_gui.png" align(.5, .5)
            # text message_t:
                # xalign 0.5 yalign 0.5
                # size 50 color "#828282"
            # hbox:
                # align (0.45, 0.65)
                # spacing (530)
                # if isVisible_tbox == True:
                    # textbutton "Да":
                        # xysize (200, 50)
                        # size 15 color "#cac4b0"
                        # action [SetVariable("persistent.failed_4day", False), SetVariable("isVisible", not isVisible), SetVariable("message_t", "Доверься себе."),  SetVariable("isVisible_tbox", False),  SetVariable("persistent.val_changed", True)]
                    # textbutton "{s}Нет{/s}":
                        # xysize (200, 50)
                        # action SetVariable("isVisible", not isVisible)

style thought_text_style:  # Создаем новый стиль для текста мыслей
    xanchor 0
    xalign 0.3
    size 38
    color "#980002"
    font "mods/Vmod/Onmark.otf"
    ymaximum 0.8 # Задаем максимальный размер по вертикали (от 0.0 до 1.0)
    yminimum 0.6 # Задаем минимальный размер по вертикали (от 0.0 до 1.0)


screen countplus:
        key "l" action SetVariable("persistent.count_tries", persistent.count_tries + 1)#, Function(ref_count)#Show("clear_persistent")? 
        text str(persistent.count_tries):
            xalign 0.1 yalign 0.1
            size 10 color "#828282"        
        text str(persistent.failed_4day):
            xalign 0.1 yalign 0.15
            size 10 color "#828282"
        text str(persistent.val_changed):
            xalign 0.1 yalign 0.17
            size 10 color "#828282"
        key ";" action [SetVariable("persistent.val_changed", False),SetVariable("persistent.failed_4day", False), SetVariable("persistent.count_tries", 0)]

screen thoughts:
        key "k" action SetVariable("isVisible", not isVisible)
        key "l" action SetVariable("persistent.thought_count", 0), SetVariable("persistent.achievement_shown", False)
        # if isVisible == False:
            # $ check_achievement()
        if isVisible == True:
            $ renpy.sound.play('mods/Vmod/sfx/paper_bag.ogg')
            add thoughts_imageblank align(.5, .5)
            text thought1 style "thought_text_style": # Применяем стиль к тексту
                yalign 0.3
            text thought2 style "thought_text_style":
                yalign 0.4
            text thought3 style "thought_text_style":
                yalign 0.5
            text thought4 style "thought_text_style":
                yalign 0.6

init python:
    def ref_count():
        count_tries_text = "[persistent.count_tries]"

label vladstory_prolog:
    #show screen countplus -  вывести данные строками
    #show screen clear_persistent
    $ message_t = u"Вы вспоминаете совсем другое. Продолжить?"
    if persistent.count_tries == 1:
        "Что-то не то."
        "Такое чувство, будто это было по-другому, совсем иначе.."
        "Но часть меня отчаянно отвергает \"другое\"."
        "Мне нужно просто вспомнить.."
        "Вспомнить.."
        jump failed_onetime  #перекидывает на лейбл с новым выбором
    elif persistent.count_tries == 2:
        "Я не думаю, что всё так и должно было произойти."
        "Кто мне это вверил?"
        "Это же было..{w=1} не по-настоящему, да?"
        "..."
        $ persistent.val_changed = True
        $ persistent.failed_4day = False
        jump failed_onetime  #перекидывает на лейбл с новым выбором
    elif persistent.count_tries > 2:
        "..."
        "Что-то неустанно бьётся в мою голову."
        "Это ложные воспоминания?"
        "Нет.."
        "Я всегда убегал от реальности, которой всегда боялся."
        "Теперь я готов её принять.{w} Я чувствую её буквально кончиками своих пальцев.."
        "Это.."
        jump failed_onetime  #перекидывает на лейбл с новым выбором
    $ new_chapter(0, u"Начало.")
    play music Vmod_music['near_light'] fadein 3
    $ prolog_time()
    show anim prolog_1 with dissolve
    $ renpy.pause(2)
    "Иногда я сомневаюсь в чём-то."
    "В чем-то, что само по себе не имеет почву для сомнения."
    "Думаешь, это плохо?"
    "Возможно.{w=1} Однако, доверяй, но проверяй.."
    $ renpy.pause(1)
    hide anim prolog_1
    show unblink
    show bg semen_room with dspr
    vl "Который час?"
    "Сонными глазами щурюсь в экран своего компьютера, на котором красуется окошка торрента с рекламой казино."
    vl "Десять..{w=1} тридцать."
    vl "Че там писали в вк вчера? встреча выпускников в 11:30?"
    "Приду, конечно же."
    th "Хотя бы ёбла старые увижу, хах."
    $ renpy.pause(2)
    show bg semen_room_window with dissolve
    "За окном бушует и орудует снежная буря."
    th "Еще бы, самый рассвет зимы, 24 декабря на дворе."
    "Ветер воет и завывает, подхватывает снежные хлопья и бросает их в окна."
    "Сегодня снег падает густыми хлопьями, отчего сетка на моем окне устлана природными шедеврами зимы."
    "Я перестал закрывать окна по зимам, только ставлю на проветривание."
    "Почему?{w=1} Жарковато, аж яйца к ляшке прилипают.{w=1} А с полуоткрытым окном хорошо: и спится сладко, и постель прохладная."
    "..."
    "Как бы то ни было, жизнь идет дальше.{w=1} Она никого не щадит.{w=1} Произойдет самое горькое (а оно произойдёт!) — планета продолжит кружиться.{w=1}Так оно и происходит."
    "Человек однажды просыпается одним днем и в один день навсегда засыпает."
    "Так, значит, наша жизнь заключается в том, чтобы оставить на планете след?"
    "Пускай так, я не способен свернуть ось Земли."
    "Отучившись в школе, как и все обычные люди, я поступил в шарагу."
    "Самую обыкновенную."
    vl "Мне просто не хватило немного баллов на более-менее нормальный ВУЗ..."
    "Да и вообще, неудачник я.{w=1} Можно и так сказать.{w=1} У меня даже девушка была - Алина."
    "Помню этот момент.."
    show blink
    $ renpy.pause(3)
    play sound sfx_head_heartbeat loop
    "Серая тугая осень.{w=1} Парк с лавочками, прикрытые чуть сверху хвоей, монумент Ильичу, а следом мемориалы известным писателям.{w=1} Немного сторонюсь, но все же подхожу."

    li "Привет.{w=1} Ну, идем?"
    "Она подалась вперед и обняла меня."
    li "Я сильно скучала.{w=2} Извини, что раньше не могла погулять с тобой.{w=2.0} Ну, дела, учеба.."
    vl "Да я все понимаю.{w=1} Пойдем уже."
    "Она обвила мою правую руку своими обеими."
    th "Это по правде согревающее душу чувство. {w=2.0}Даже если обнимает она не душу, а руку."
    "..."
    odn "Ха-а-а, это та, что на вписке ебали 15 человек?"
    "Я замер. {w}Сердце облилось холодным потом и рваной хваткой ледяные кошачьи когти глубоко оцарапали его, а мозг отказывался работать."
    "Но верить я ему тоже не мог.{w} И почувствовал, что змеиные женские руки у моих рук начали понемногу отлипать."
    th "Невербальный жест ошарашенности, да?"
    "Я точно впал в ступор."
    stop sound
    vl "Так это было не шуткой.."
    hide blink
    show unblink
    $ renpy.pause(3)

    "Не помню, что было дальше."
    "На автопилоте я доковылял домой, лег в кровать и до глубокой ночи дырявил взглядом стену.{w=1} Так прошло пару месяцев.{w=1} Я не отвечал на её звонки.{w=1}  знал, что это правда."
    "Но...{w=2} Я не могу ненавидеть её."
    "Почему?{w} Почему я не в силах ненавидеть того, кто разрушил твою жизнь?"
    "По кускам развалилась и настоящая, и будущая жизнь."
    "Казалось, теперь ничего не связывает меня с реальным миром.{w=1} Лишь естественные нужды выдавали во мне человека."
    "..."
    "Злые, бессильные слёзы впитывались в подушку и вытирались о рукавы."
    "Я ничего не могу с этим поделать.{w=1} Но и отпустить полностью ситуацию не могу.{w=1} Я до сих пор её люблю."
    "Я так чувствую."
    $ renpy.pause(2)
    "Мой взгляд падает на проезжающие машины понизу меня."
    th "Всё когда-нибудь пройдет, всё сростётся.."
    show bg semen_room with dspr
    "За все время моей жизни накопилось куча историй, и вся моя жизнь это, по сути, солянка рассказов — чужих и собственных{w}, — и меня это устраивает."
    play sound sfx_bed_squeak1
    "Моя кровать истошно всхлипнула своими пружинами, стоило мне только встать с нее."
    "Опрокинув в себя пару горячих бутербродов с чаем, я оделся и вышел из дома."
    show door with dspr
    play sound sfx_close_door_campus_1
    "Все как всегда: достаю ключи, закрываю свой бункер на два оборота и съебываюсь восвояси."
    show waytopizdets with dissolve
    play ambience ambience_cold_wind_loop
    play sound sfx_intro_bus_stop_steps loop
    "Снежная мгла бьет по лицу и треплет мой капюшон, как мама когда-то пиздила по затылку."
    "Съежив свою голову, я побрел к остановке."
    "Я наступал и каждый раз мои ботинки окутывала кашица из влажно-грязного снега."
    th "Это мягкая зима.{w=1} Хоть в чём-то мне везёт."
    "Не прошло и пяти минут, как ноги начинали млеть."
    vl "Ёптыть, холодняво сегодня."

    show bg bus_stop with dspr
    
    "И вот, стою на автобусной остановке, чувствуя себя чужаком среди безликой толпы."
    "Все куда-то спешили, а я терпеливо жду своего автобуса."
    "Время тянулось медленно, и я невольно начал разглядывать людей вокруг."
    
    show epilogue_sl with dissolve
    hide bg bus_stop with dspr
    "Их лица казались пустыми и безжизненными, но каждый из них был погружен в свои мысли."
    th "А ведь каждый из них куда-то торопится, у него есть свои цели, стремления.."
    $ renpy.block_rollback()
    "Я посмотрел на часы, потом на циферблат, но цифры предательски расплывались перед глазами."
    "Закрылся в себе, надеясь, что автобус приедет поскорее.."
    "Три минуты, четыре, шесть.."
    "..но время шло, а его все не было."
    show blink
    stop sound fadeout 2
    stop music fadeout 2
    "В голове кружились тревожные мысли."
    th "Что, если автобуса сегодня не будет?"
    th "Что, если на встречу никто не придёт?"
    th "А может быть, мне и правда не стоит появляться там?"
    th "Будет ли кто-нибудь рад меня видеть?{w=1} Миша, Кузя или хотя бы Паша..."
    th "Просто интересно.."
    stop ambience fadeout 2
    "..."
    "Словно призраком, я почувствовал, как меня покидают силы."
    "Мысли стали путаться, а тело стало легким.{w=1} Что-то происходило, но я не понимал, что именно."
    "Моя голова пуста...{w=2} и давно так?"
    "В моей голове наступила тишина и пустота."
    th "Может быть, в ней никогда ничего и не было?"
    "Я завис, застыл в этой паутине нескончаемого ожидания и обьятиях холодного ветра."
    "Вокруг так темно и безмолвно...{w=1} где же я на самом деле?"
    jump day1_vladstory