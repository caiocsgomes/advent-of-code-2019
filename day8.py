image = ''
with open("day8-input.txt", "r") as f:
    image = f.read().split()

image_string = image[0]
wide = 25
tall = 6
layer_size = wide * tall
ptr = 0
min_occ = layer_size + 1

for i in range(0, len(image_string), layer_size):
    count = image_string[i: i + layer_size].count('0')
    if count < min_occ:
        min_occ = count
        ptr = i
image_layer = image_string[ptr: ptr + layer_size]
print("Part1: ", image_layer.count('1') * image_layer.count('2'))

# 0 BLACK
# 1 WHITE
# 2 TRANSPARENT

# https://stackoverflow.com/questions/12699827/python-block-character-will-not-print
# https://en.wikipedia.org/wiki/Code_page_437

image_layers = [image_string[i:i + layer_size] for i in range(0, len(image_string), layer_size)]
image = []
white_color = bytes((219,)).decode('cp437')
for i_layer in range(layer_size):
    for layer in image_layers:
        color = layer[i_layer]
        if color in {'0', '1'}:
            if color == '1':
                image.append(white_color)
            else:
                image.append(' ')
            break
    if len(image) == layer_size:
        break

image_decoded = [''.join(image[i:i + wide]) for i in range(0, len(image_string), wide)]

print("Part2 :")
for i in range(tall):
    print(image_decoded[i])
