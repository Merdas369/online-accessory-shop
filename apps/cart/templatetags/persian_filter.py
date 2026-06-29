from django import template

register = template.Library()


@register.filter
def persian_number(english_number):
    x = {
        "0": "\u06f0",
        "1": "\u06f1",
        "2": "\u06f2",
        "3": "\u06f3",
        "4": "\u06f4",
        "5": "\u06f5",
        "6": "\u06f6",
        "7": "\u06f7",
        "8": "\u06f8",
        "9": "\u06f9",
    }
    en_num = str(english_number)
    p_num = ""
    for i in en_num:
        p_num += x[i]
    return p_num
