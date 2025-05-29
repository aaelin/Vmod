screen Vmod_say:
    window background None id "window":

        $ timeofday = persistent.timeofday

        if persistent.font_size == "large":

            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") xpos 38 ypos 924 action ShowMenu("text_history")

            add get_image("gui/dialogue_box/"+timeofday+"/dialogue_box_large.png") xpos 174 ypos 866

            if not config.skipping:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") xpos 1768 ypos 924 action Skip()
            else:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") xpos 1768 ypos 924 action Skip()

            text what id "what" xpos 194 ypos 914 xmaximum 1541 size 33 line_spacing 1 font "mods/Vmod/ShantellSans-Regular.ttf"
            if who:
                text who id "who" xpos 194 ypos 872 size 35 line_spacing 3 font "mods/Vmod/ShantellSans-Regular.ttf"

        elif persistent.font_size == "small":

            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") xpos 38 ypos 949 action ShowMenu("text_history")

            add get_image("gui/dialogue_box/"+timeofday+"/dialogue_box.png") xpos 174 ypos 916
            # imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png") xpos 1508 ypos 933 action HideInterface()
            # imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/save_%s.png") xpos 1567 ypos 933 action ShowMenu('save')
            # imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/menu_%s.png") xpos 1625 ypos 933 action ShowMenu('game_menu_selector')
            # imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/load_%s.png") xpos 1682 ypos 933 action ShowMenu('load')
            
            if not config.skipping:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") xpos 1768 ypos 949 action Skip()
            else:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") xpos 1768 ypos 949 action Skip()

            text what id "what" xpos 194 ypos 964 xmaximum 1541 size 27 line_spacing 2 font "mods/Vmod/ShantellSans-Regular.ttf"
            if who:
                text who id "who" xpos 194 ypos 924 size 28 line_spacing 2 font "mods/Vmod/ShantellSans-Regular.ttf"

    # Убрать get_image и скобки между вокруг пути файла. Далее настраиваете сам путь к файлам (кнопки, фон для диалога).
    # При желании можно убрать $ timeofday = persistent.timeofday, как я и сделал, если Вы не планируете смену диалогового окна в зависимости от времени суток.

    # Далее заменяем экран say на свой экран (спасибо Ане Пернусовой):

init python:
    renpy.display.screen.screens[("say",None)] = renpy.display.screen.screens[("Vmod_say",None)]