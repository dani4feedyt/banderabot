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
