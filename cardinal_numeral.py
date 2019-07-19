import pygame

dict_of_value = {
    0: 'không',
    1: 'một',
    2: 'hai',
    3: 'ba',
    4: 'bốn',
    5: 'năm',
    6: 'sáu',
    7: 'bảy',
    8: 'tám',
    9: 'chín'
}
dict_of_north = {
    1: '',
    1000: 'nghìn',
    1000000: 'triệu',
    1000000000: 'tỷ'
}
dict_of_south = {
    1: '',
    1000: 'ngàn',
    1000000: 'triệu',
    1000000000: 'tỷ'
}
voice_of_north = {
    'không': './sounds/vie/north/khong.ogg',
    'linh': './sounds/vie/north/linh.ogg',
    'một': './sounds/vie/north/mot1.ogg',
    'mốt': './sounds/vie/north/mot2.ogg',
    'hai': './sounds/vie/north/hai.ogg',
    'ba': './sounds/vie/north/ba.ogg',
    'bốn': './sounds/vie/north/bon.ogg',
    'năm': './sounds/vie/north/nam.ogg',
    'lăm': './sounds/vie/north/lam.ogg',
    'sáu': './sounds/vie/north/sau.ogg',
    'bảy': './sounds/vie/north/bay.ogg',
    'tám': './sounds/vie/north/tam.ogg',
    'chín': './sounds/vie/north/chin.ogg',
    'trăm': './sounds/vie/north/tram.ogg',
    'nghìn': './sounds/vie/north/nghin.ogg',
    'triệu': './sounds/vie/north/trieu.ogg',
    'tỷ': './sounds/vie/north/ty.ogg',
    'mười':'./sounds/vie/north/muoi1.ogg',
    'mươi':'./sounds/vie/north/muoi2.ogg'
}
voice_of_south = {
    'không': './sounds/vie/south/khong.ogg',
    'lẻ': './sounds/vie/south/le.ogg',
    'một': './sounds/vie/south/mot1.ogg',
    'mốt': './sounds/vie/south/mot2.ogg',
    'hai': './sounds/vie/south/hai.ogg',
    'ba': './sounds/vie/south/ba.ogg',
    'bốn': './sounds/vie/south/bon.ogg',
    'năm': './sounds/vie/south/nam.ogg',
    'lăm': './sounds/vie/south/lam.ogg',
    'sáu': './sounds/vie/south/sau.ogg',
    'bảy': './sounds/vie/south/bay.ogg',
    'tám': './sounds/vie/south/tam.ogg',
    'chín': './sounds/vie/south/chin.ogg',
    'trăm': './sounds/vie/south/tram.ogg',
    'ngàn': './sounds/vie/south/ngan.ogg',
    'triệu': './sounds/vie/south/trieu.ogg',
    'tỷ': './sounds/vie/south/ty.ogg',
    'mười': './sounds/vie/south/muoi1.ogg',
    'mươi': './sounds/vie/south/muoi2.ogg'
}

def read_number_from_0_to_99(n):
    """
        input : number from 0 to 99

        output : string res pronnouce the number

    """

    res = []
    if n // 10 == 0:
        res.append(dict_of_value[n % 10])
    else:
        if n // 10 == 1:
            res.append('mười')
            if n % 10 == 5:
                res.append('lăm')
            elif n % 10 == 0:
                res.append('')
            else:
                res.append(dict_of_value[n % 10])
        else:
            res.append(dict_of_value[n // 10])
            res.append('mươi')
            if n % 10 == 5:
                res.append('lăm')
            elif n % 10 == 1:
                res.append('mốt')
            else:
                res.append(dict_of_value[n % 10])
    res = ' '.join(res)
    return res


def read_number_from_0_to_999(n, region):  # region : NORTH or SOUTH

    """
    :param n: number from 0 to 999
    :param region: if value = NORTH => pronounce by North Vietnamese, if value = SOUTH => pronounce by South Vietnamese
    :return: string res pronnouce the number

    """
    res = []
    res.append(dict_of_value[n // 100])
    res.append('trăm')
    temp = (n % 100) // 10
    if temp == 0:
        if n % 10 == 0:
            res.append('')
        elif region == 'NORTH':
            res.append('linh')
            res.append(read_number_from_0_to_99(n % 100))
        elif region == 'SOUTH':
            res.append('lẻ')
            res.append(read_number_from_0_to_99(n % 100))

    else:
        res.append(read_number_from_0_to_99(n % 100))
    res = ' '.join(res)
    return res


def integer_to_vietnamese_numeral(n, region, activate_tts):  # region : NORTH or SOUTH
    """

    :param n: number from 0 to 999,999,999,999
    :param region: if value = NORTH => pronounce by North Vietnamese, if value = SOUTH => pronounce by South Vietnamese
    :param activate_tts: if value = True => voice, if value = False => no voice
    :param activate_tts: if value is not boolean => raise TypeError
    :return: string res pronounce the number and voice

    """
    if isinstance(n, int) is False:
        raise KeyError('Not an integer')
    if n < 0:
        raise ValueError('Not a positive number')
    if not isinstance(activate_tts, bool):
        raise TypeError('Argument "activate_tts" is not a boolean')
    l = [1000000000, 1000000, 1000, 1]
    res = []
    i = 0
    while n // l[i] == 0:
        i += 1
    if n // l[i] >= 100:
        res.append(read_number_from_0_to_999(n // l[i], region))
    else:
        res.append(read_number_from_0_to_99(n // l[i]))
    if region == 'NORTH':
        res.append(dict_of_north[l[i]])
    else:
        res.append(dict_of_south[l[i]])
    n = n % l[i]
    i += 1
    while n != 0:
        if region == 'NORTH':
            if n//l[i]==0:
                i+=1
            else:
                res.append(read_number_from_0_to_999(n // l[i], region))
                res.append(dict_of_north[l[i]])
        if region == 'SOUTH':
            if n//l[i]==0:
                i+=1
            else:
                res.append(read_number_from_0_to_999(n // l[i], region))
                res.append(dict_of_south[l[i]])
        n = n % l[i]
        i += 1
    res = ' '.join(res)
    print(res)
    if activate_tts == True:
        pygame.init()
        l_voice = res.split(' ')
        l_voice.pop(-1)
        if region == 'NORTH':
            for i in l_voice:
                f_voice = voice_of_north[i]
                sound = pygame.mixer.Sound(f_voice)
                channel = sound.play()
                pygame.time.delay(500)
        if region == 'SOUTH':
            for i in l_voice:
                f_voice = voice_of_south[i]
                sound = pygame.mixer.Sound(f_voice)
                channel = sound.play()
                pygame.time.delay(800)
    return res


def integer_to_english_numeral(n):
    """

    :param n: number from 0 to 999,999,999,999
    :return: string res pronnouce the number

    """
    if not isinstance(n, int):
        raise TypeError("Not an integer")
    if n < 0:
        raise ValueError("Not a positive integer")
    else:
        dict_eng = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
             11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
             15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
             19: 'nineteen', 20: 'twenty',
             30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
             70: 'seventy', 80: 'eighty', 90: 'ninety'}
        n_thousand = 1000
        n_million = n_thousand * 1000
        n_billion = n_million * 1000
        n_trillion = n_billion * 1000

        if (n < 20):
            return dict_eng[n]

        if (n < 100):
            if n % 10 == 0:
                return dict_eng[n]
            else:
                return dict_eng[n // 10 * 10] + '-' + dict_eng[n % 10]

        if (n < n_thousand):
            if n % 100 == 0:
                return dict_eng[n // 100] + ' hundred'
            else:
                return dict_eng[n // 100] + ' hundred and ' + integer_to_english_numeral(n % 100)

        if (n < n_million):
            if n % n_thousand == 0:
                return integer_to_english_numeral(n // n_thousand) + ' thousand'
            else:
                return integer_to_english_numeral(n // n_thousand) + ' thousand and ' + integer_to_english_numeral(n % n_thousand)

        if (n < n_billion):
            if (n % n_million) == 0:
                return integer_to_english_numeral(n // n_million) + ' million'
            else:
                return integer_to_english_numeral(n // n_million) + ' million, ' + integer_to_english_numeral(n % n_million)

        if (n < n_trillion):
            if (n % n_billion) == 0:
                return integer_to_english_numeral(n // n_billion) + ' billion'
            else:

                return integer_to_english_numeral(n // n_billion) + ' billion, ' + integer_to_english_numeral(n % n_billion)
        if (n % n_trillion == 0):
            return integer_to_english_numeral(n // n_trillion) + ' trillion'
        else:
            return integer_to_english_numeral(n // n_trillion) + ' trillion, ' + integer_to_english_numeral(n % n_trillion)
dict_eng_voice = {
    'zero': './sounds/eng/zero.ogg',
    'one': './sounds/eng/one.ogg',
    'two': './sounds/eng/two.ogg',
    'three': './sounds/eng/three.ogg',
    'four': './sounds/eng/four.ogg',
    'five': './sounds/eng/five.ogg',
    'six': './sounds/eng/six.ogg',
    'seven': './sounds/eng/seven.ogg',
    'eight': './sounds/eng/eight.ogg',
    'nine': './sounds/eng/nine.ogg',
    'ten': './sounds/eng/ten.ogg',
    'eleven': './sounds/eng/eleven.ogg',
    'twelve': './sounds/eng/twelve.ogg',
    'thirteen': './sounds/eng/thirteen.ogg',
    'fifteen': './sounds/eng/fifteen.ogg',
    'sixteen': './sounds/eng/sixteen.ogg',
    'seventeen': './sounds/eng/seventeen.ogg',
    'eighteen': './sounds/eng/eighteen.ogg',
    'nineteen': './sounds/eng/nineteen.ogg',
    'twenty': './sounds/eng/twenty.ogg',
    'thirty': './sounds/eng/thirty.ogg',
    'fourty': './sounds/eng/fourty.ogg',
    'fifty': './sounds/eng/fifty.ogg',
    'sixty': './sounds/eng/sixty.ogg',
    'seventy': './sounds/eng/seventy.ogg',
    'eighty': './sounds/eng/eighty.ogg',
    'ninety': './sounds/eng/ninety.ogg',
    'hundred': './sounds/eng/hundred.ogg',
    'thousand': './sounds/eng/thousand.ogg',
    'million': './sounds/eng/million.ogg',
    'billion': './sounds/eng/billion.ogg',
    'trillion': './sounds/eng/trillion.ogg',
    'and': './sounds/eng/and.ogg'
}


def voice_of_integer_to_english_numeral(n, activate_tts=False):
    """
    :param n: number from 0 to 999,999,999,999
    :param activate_tts: if value = True => voice, if value = False => no voice
    :param activate_tts: if value is not boolean => raise TypeError
    :return: string res pronounce the number and voice

    """
    res = integer_to_english_numeral(n)
    print(res)
    if not isinstance(activate_tts, bool):
        raise TypeError('Argument "activate_tts" is not a boolean')
    elif activate_tts is True:
        l_voice = res.replace('-', ' ').replace(',', '').split(' ')
        pygame.init()
        for i in l_voice:
            sound = pygame.mixer.Sound(dict_eng_voice[i])
            channel = sound.play()
            clock = pygame.time.Clock().tick(1.234567890)
            channel = sound.stop()
        pygame.quit()
    else:
        return res

# integer_to_vietnamese_numeral(102015, 'NORTH', False)
# integer_to_vietnamese_numeral(102015, 'SOUTH', False)
# integer_to_vietnamese_numeral(102015, 'NORTH', True)
# integer_to_vietnamese_numeral(102015, 'SOUTH', True)
# voice_of_integer_to_english_numeral(102015,False)
# voice_of_integer_to_english_numeral(102015,True)
# integer_to_vietnamese_numeral(-102015, 'NORTH', False)
# integer_to_vietnamese_numeral('102015', 'NORTH', False)
# integer_to_vietnamese_numeral(102015, 'NORTH', 122121)
