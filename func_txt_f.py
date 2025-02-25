nondec = [["канад", "cad", "canad"],
          ["дол", "usd", "dol", "бак", "бач", "buck"],
          ["євр", "евр", "eur"],
          ["шек", "ils", "she"],
          ["біло", "бело", "bilo", "бела", "byn", "bela"],
          ["poun", "brit", "брит", "фун", "ster", "gbp", "стерл"]]
nondec_map = [["CAD", 13], ["USD", 7], ["EUR", 8], ["ILS", 16], ["BYN", 2], ["GBP", 28]]
yesdec = [["руб", "rub"],
          ["йен", "єн", "jp", "jap", "yen", "ien"]]
yesdec_map = [["RUB", 20], ["JPY", 10]]

Quotes1 = {1: "Язык программирования:computer::computer::computer: <<Пыхтон>>:dash::dash::snake:"
              "научит молодых нормальной забибовчке:muscle::muscle:Надеюсь, программисты:pager: "
              "уже скоро сделают калик с автозабивкой дабл эппл:green_apple::apple:(dvoynoye yabloko)"
              ":sunglasses::call_me::sunglasses::call_me:",
           2: "Программисты шалят :call_me_tone1: :smiling_imp:"
              "А че, айтишники тоже непрочь календулу с кралями раздуть) "
              "Вы не думайте, что это задроты:joy: :school: Они такую забивку намешают, что любая краля офигеет"
              ":dizzy_face: :dash: :lips: Им только повод дай) А там уж и «Питона» своего покажут, да «СиСи++», "
              "если вы понимаете о чем я:rofl: :thumbsup_tone1: :underage: "
              "Кальянчик  всех радует: и качков, и очкариков) Главное дуть с кайфом пацаны:point_up_tone1: "
              "И неважно, какой ты национальности:blush:",
           3: "Вот это Икс-колюмбокс :flushed::scream_cat: Сразу видно Фил (Spencer) долго готовил забивку "
              ":drooling_face: Выбирая самые спелые :lips:, самые сочные :heart_eyes:, самые наливные "
              ":green_apple::apple: (dvoynie yabloki)На такую X-коробку любая краля :dancer::heart: "
              "прибежит и вдохнет дым через мундштучеллу :stuck_out_tongue_winking_eye: по самые гланды :drooling_face:"
              ":underage:Чтите традиции :point_up_tone1: Не поддавайтесь на уловки :triumph: грязных (dirty) сонибоев "
              ":nauseated_face::face_with_symbols_over_mouth:Помните братья, что наш РУССКИЙ :flag_mu: Пыхфуций "
              ":man_wearing_turban: говорил:Если калик покурил - ты у краль :lips: номер один :sun_with_face:"
              ":heart_eyes:Если братик плейстейшон :nauseated_face: взял, то считай пропал пацан :chicken::blue_heart:"
              "Всем братьям peace :right_facing_fist_tone1::left_facing_fist_tone1:,"
              " всем кралям kiss :revolving_hearts:",
           4: "Киберпыхи здесь? :sunglasses: :sunglasses: :sunglasses: Будущее будущим, но как в 2077"
              " без хорошего кумарика? :thought_balloon: :thought_balloon: :thought_balloon: "
              "Вот и поляки так думают, поэтому добавили такого красавца в Найт-Сити :night_with_stars: "
              ":night_with_stars: :night_with_stars: Как известно, в голове главного героя сидит Киану Ривз "
              ":star2: :star2: :star2: , а точнее его персонаж - Джонни Сильверпых :dash: :dash: :dash: "
              "Он то нам и посоветует лучшую киберзабивочку и устроит колюмбас будущего :fire: :fire: :fire: "
              "Как угля нет? :scream_cat: :scream_cat: :scream_cat: Очередной баг :warning: :warning: :warning: "
              "Недоглядели игроделы :ghost: :ghost: :ghost: Ну ничего, прощаем :call_me: :call_me: :call_me: "
              "Игру ждали - и обновлений дождемся :hourglass: :hourglass: :hourglass:  "
              "Всем геймерам крутых кумарочных имплантов и качественного пыха в виртуальном мире :thumbsup: :thumbsup: "
              ":thumbsup: :metal: :metal: :call_me:",
           }


def msg_end_temp_1(number):
    msg_ending = "ь"
    exep1 = ("1", "2", "3", "4")
    exep2 = ("11", "12", "13", "14")
    if str(number).endswith(exep2):
        msg_ending = "ь"
    elif str(number).endswith(exep1):
        msg_ending = "ня"
    return msg_ending


def msg_end_temp_2(number):
    msg_ending = ""
    exep1 = ("2", "3", "4")
    exep2 = ("11", "12", "13", "14")
    exep3 = "1"
    if str(number).endswith(exep2):
        msg_ending = ""
    elif str(number).endswith(exep1):
        msg_ending = "и"
    elif str(number).endswith(exep3):
        msg_ending = "у"
    return msg_ending
