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

Quotes1 = {1: "Мова програмування:computer::computer::computer: <<Чмухтон>>:dash::dash::snake: "
              "навчить молодих нормальній забивочці:muscle::muscle: Сподіваюся, програмісти:pager: "
              "вже скоро зроблять калік з автозабивкою дабл еппл:green_apple::apple: (podviyne yabluko)"
              ":sunglasses::call_me::sunglasses::call_me:",
           2: "Програмісти пустують:call_me_tone1::smiling_imp: "
              "А що, айтішники теж не проти календули з кралями дмухнути) "
              "Ви не думайте, що це задроти:joy::school: Вони таку забивку намішають, що будь-яка краля ошаліє"
              ":dizzy_face::dash::lips: Їм тільки дай приводу) А там вже і «Пітона» свого покажуть, і «СіСі++», "
              "якщо ви розумієте про що я:rofl::thumbsup_tone1::underage: "
              "Калік всіх тішить: і качків, і чотириоких) Головне дмухати з кайфом пацани:point_up_tone1: "
              "І неважливо, якої ти національності:blush: аби не кацап:flag_mu::warning::warning:",
           3: "Оце Ікс-колюмбокс:flushed::scream_cat: Одразу видно що Філ (Spencer) довго готував забивочку "
              ":drooling_face: Обираючи найспіліші:lips: , найсоковитіші:heart_eyes: , найбільш наливні"
              ":green_apple::apple: (podviyni yabluky) На таку X-коробку будь-яка краля:dancer::heart: "
              "примчить та вдихне дим через мундштучеллу:stuck_out_tongue_winking_eye: по самі гланди:drooling_face:"
              ":underage: Поважайте традиції:point_up_tone1: "
              "Не ведіться на хитрощі:triumph: брудних (dirty) сонібоїв "
              ":nauseated_face::face_with_symbols_over_mouth: Пам'ятайте браття,"
              " що наш СПІВВІТЧИЗНИК:flag_mu: Пихфуцій"
              ":man_wearing_turban: казав: Якщо калік покурив - ти у краль:lips: номер один :sun_with_face:"
              ":heart_eyes: Якщо бро плейстейшен:nauseated_face: взяв, то вважай пропав пацан:chicken::blue_heart: "
              "Всім браттям peace:right_facing_fist_tone1::left_facing_fist_tone1: ,"
              " всім кралям kiss:revolving_hearts:",
           4: "Кіберчмухи тут?:sunglasses::mechanical_arm::sunglasses: "
              "Майбутнє майбутнім, але як же в 2077:atom::alembic: "
              "без гарного кумарика?:dizzy_face::dash::thought_balloon: "
              "Ось і поляки:flag_mu: так вважають, тому додали такого красунчика в Найт-Сіті"
              ":last_quarter_moon_with_face::night_with_stars: "
              "Як вже відомо, в голові:brain::exploding_head: "
              "у головного героя сидить:man_in_lotus_position: Кіану Рівз"
              ":scream_cat::star2: , а точніше його персонаж - Джонні Сільверчмух:mechanical_arm::dash::dash: "
              "Він нам і порадить найкращу кіберзабивочку:call_me_tone1::space_invader::dash: "
              "та влаштує колюмбас майбутнього:atom::fire: "
              "Як вугілля нема?:scream_cat::scream_cat::scream_cat: Черговий баг:warning::warning::space_invader: "
              "Недогляділи айтішники:computer::snake::ghost: "
              "Ну нічого, пробачаємо:call_me::sunglasses::call_me::call_me: "
              "Гру чекали - і оновлень дочекаємося:triumph::hourglass::hourglass: "
              "Усім геймерам крутих кумарних імплантів:mechanical_arm::sunglasses::dash: "
              "і неперевершеного чмуху:stuck_out_tongue_winking_eye::stuck_out_tongue_winking_eye: "
              "у віртуальному світі:thumbsup::green_apple::apple::thumbsup:"
              ":thumbsup::metal::metal::call_me:",
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
