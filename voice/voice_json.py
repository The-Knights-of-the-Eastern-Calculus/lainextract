import wave
import numpy as np
import json

with open('file_list.txt', 'r') as f:
    filenames = f.readlines()

offsets = np.fromfile('voice_offset_table.bin', dtype=np.uint32)

with open('voice.bin', 'rb') as f:
    voice_data = f.read()

translation_table = {
    'BYA':'ビャ',
    'BYO':'ビョ',
    'BYU':'ビュ',
    'GYA':'ギャ',
    'GYO':'ギョ',
    'GYU':'ギュ',
    'HYA':'ヒャ',
    'HYO':'ヒョ',
    'HYU':'ヒュ',
    'KYA':'キャ',
    'KYO':'キョ',
    'KYU':'キュ',
    'MYA':'ミャ',
    'MYO':'ミョ',
    'MYU':'ミュ',
    'NYA':'ニャ',
    'NYO':'ニョ',
    'NYU':'ニュ',
    'PYA':'ピャ',
    'PYO':'ピョ',
    'PYU':'ピュ',
    'RYA':'リャ',
    'RYO':'リョ',
    'RYU':'リュ',
    'SYA':'シャ',
    'SYO':'ショ',
    'SYU':'シュ',
    'TYA':'チャ',
    'TYO':'チョ',
    'TYU':'チュ',
    'ZYA':'ジャ',
    'ZYO':'ジョ',
    'ZYU':'ジュ',
    'DYA':'ヂャ',
    'DYO':'ヂョ',
    'DYU':'ヂュ',
    'JYA':'ジャ',
    'JYO':'ジョ',
    'JYU':'ジュ',
    'A':'ア',
    'BA':'バ',
    'BE':'ベ',
    'BI':'ビ',
    'BO':'ボ',
    'BU':'ブ',
    'DA':'ダ',
    'DE':'デ',
    'DI':'ヂ',
    'DO':'ド',
    'DU':'ヅ',
    'E':'エ',
    'FA':'ファ',
    'FE':'フェ',
    'FI':'フィ',
    'FO':'フォ',
    'FU':'フゥ',
    'GA':'ガ',
    'GE':'ゲ',
    'GI':'ギ',
    'GO':'ゴ',
    'GU':'グ',
    'HA':'ハ',
    'HE':'ヘ',
    'HI':'ヒ',
    'HO':'ホ',
    'HU':'フ',
    'I':'イ',
    'KA':'カ',
    'KE':'ケ',
    'KI':'キ',
    'KO':'コ',
    'KU':'ク',
    'MA':'マ',
    'ME':'メ',
    'MI':'ミ',
    'MO':'モ',
    'MU':'ム',
    'NA':'ナ',
    'NE':'ネ',
    'NI':'ニ',
    'NN':'ンン',
    'N':'ン',
    'NO':'ノ',
    'NU':'ヌ',
    'O':'オ',
    'PA':'パ',
    'PE':'ペ',
    'PI':'ピ',
    'PO':'ポ',
    'PU':'プ',
    'RA':'ラ',
    'RE':'レ',
    'RI':'リ',
    'RO':'ロ',
    'RU':'ル',
    'SA':'サ',
    'SE':'セ',
    'SI':'シ',
    'SO':'ソ',
    'SU':'ス',
    'TA':'タ',
    'TE':'テ',
    'TI':'チ',
    'TO':'ト',
    'TU':'ツ',
    'U':'ウ',
    'WA':'ワ',
    'YA':'ヤ',
    'YO':'ヨ',
    'YU':'ユ',
    'ZA':'ザ',
    'ZE':'ゼ',
    'ZI':'ジ',
    'ZO':'ゾ',
    'ZU':'ズ',
    '#':'#',
    'CAVE':'CAVE',
    'END':'END'
}

out = []

for i, file in enumerate(filenames):
    offset = offsets[i * 2] * 2048
    size = offsets[i * 2 + 1]
    print(f'{file.strip()}: offset - {offset}, size - {size}')
    translated_name = '_'.join([translation_table[a] for a in file.strip().replace('.WAV', '').split('_')]) + '.WAV'
    out.append({'original_name': file.strip(), 'translated_name': translated_name, 'offset': int(offset), 'size': int(size)})
    print(out[-1])
    # if i not in [9, 10, 11]: # bya, byo, byu are already in wav
    #     with wave.open('extracted/' + file.strip(), 'wb') as wav_file:
    #         wav_file.setparams((1, 2, 22050, 0, 'NONE', 'NONE')) # mono, 16bit, 22050Khz
    #         wav_file.writeframes(voice_data[offset:offset + size])
    # else:
    #     with open('extracted/' + file.strip(), 'wb') as f:
    #         f.write(voice_data[offset:offset + size])

with open('voice.json', 'w') as f:
    json.dump(out, f)
