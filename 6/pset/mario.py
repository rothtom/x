def main():
    height: int = get_height()
    pyramid = build_pyramid(height)
    for layer in range(len(pyramid)):
        print(pyramid[layer])


def get_height():
    height = 0
    while height <= 0 or height > 8:
        try:
            height= int(input("Height: "))
        except:
            None
    return height

def build_pyramid(height: int):
    pyramid = []
    for i in range(height):
        pyramid.append(build_layer(i + 1, height))
    return pyramid



def build_layer(layer, height):
    empty_spaces = height - layer
    built_layer = " " * empty_spaces + "#" * layer + "  " + "#" * layer
    return built_layer


if __name__ == "__main__":
    main()
