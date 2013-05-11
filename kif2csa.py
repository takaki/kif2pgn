#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import re

header="""V2.2
$START_TIME:2013/01/01
N+AAAA
N-BBBB
P1-KY-KE-GI-KI-OU-KI-GI-KE-KY
P2 * -HI *  *  *  *  * -KA * 
P3-FU-FU-FU-FU-FU-FU-FU-FU-FU
P4 *  *  *  *  *  *  *  *  * 
P5 *  *  *  *  *  *  *  *  * 
P6 *  *  *  *  *  *  *  *  * 
P7+FU+FU+FU+FU+FU+FU+FU+FU+FU
P8 * +KA *  *  *  *  * +HI * 
P9+KY+KE+GI+KI+OU+KI+GI+KE+KY
+"""

zensuji = list('１２３４５６７８９')
kansuji = list('一二三四五六七八九')

zen_map = dict(zip(zensuji, range(1,10)))
kan_map = dict(zip(kansuji, range(1,10)))

piece   = '歩香桂銀金角飛玉と馬龍'
piece_map   = dict(zip(list('歩香桂銀金角飛玉と馬龍'),
    ['FU','KY','KE','GI','KI','KA','HI','OU','TO','UM','RY']))
piece_n_map = dict(zip(list('香桂銀'), ['NY', 'NK', 'NG']))
promotion_map = dict(zip(['FU', 'KY', 'KE', 'GI', 'KA', 'HI'],
                     ['TO', 'NY', 'NK', 'NG', 'UM', 'RY']))

line_re = re.compile('( *\d+) +([^ ]+)')

move_list = []
f = open(sys.argv[1])
for i in f:
    res = line_re.match(i)
    if res:
        num = int(res.groups()[0])
        s = res.groups()[1]
        if s[0] in zensuji:
            next_position = "%d%s" % (zen_map[s[0]], kan_map[s[1]])
        elif s[0] == '同':
            pass
        elif s[0] == '反' or s[0] == '切' or s[0] == '投':
            break
        else:
            raise RuntimeError("Unknown Move", s[0])
        if s[2] in piece:
            piace_name = piece_map[s[2]]
            rest = s[3:]
        elif s[2] == '成':
            piace_name = piece_n_map[s[3]]
            rest = s[4:]
        else:
            raise RuntimeError("Unknown Piece", s[2])
        promote = ''
        if rest[0] == '成':
            piace_name = promotion_map[piace_name]
            prev_position = rest[2] + rest[3]
        elif rest[0] == '打':
            prev_position = '00'
        elif rest[0] == '(':
            prev_position = rest[1] + rest[2]
        else:
            raise RuntimeError("Unknown ???", rest[0])
        move_list.append("%s%s%s" % (prev_position, next_position,
                                       piace_name))
print(header)
for i,j in enumerate(move_list):
    if i % 2 == 0:
        print('+' + j)
    else:
        print('-' + j)
        
