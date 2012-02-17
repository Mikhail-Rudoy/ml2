def make_out_word(out, word):
    mid = len(out) / 2
    return out[:mid] + word + out[mid:]

print make_out_word('<<>>', 'Yay')
print make_out_word('<<>>', 'WooHoo')
print make_out_word('[[]]', 'word')
print make_out_word('abyz', 'YAY')
print make_out_word('HHoo', 'Hello')
