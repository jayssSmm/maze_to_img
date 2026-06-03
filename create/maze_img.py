from PIL import Image, ImageDraw

def maze_matrix(filename):

    with open(filename) as f:
        contents = f.read()

    contents = contents.splitlines()

    height = len(contents)
    breadth = max(len(i) for i in contents)

    maze = []
    for i in range(breadth):
        row = []
        for j in range(height):
            if (contents[i][j] == '#'):
                row.append(True)
            else:
                row.append(False)
        maze.append(row)

    return maze, breadth, height

def maze_png(maze:list, breadth:int, height:int):
    
    img = Image.new("RGB", (breadth * 100, height * 100))

    wall = Image.new("RGB", (100, 100), '#282828')
    visited = Image.new("RGB", (100, 100), '#467846')
    square_size = 100

    for i in range(breadth):
        for j in range(height):
            square = wall if maze[i][j] else visited
            draw = ImageDraw.Draw(square)

            draw.rectangle(
                [(0, 0), (99, 99)],
                outline="white",
                width=1
            )

            x1 = j * square_size
            y1 = i * square_size
            '''
            x2 = x1 + square_size
            y2 = y1 + square_size
            '''
            img.paste(square, (x1, y1))

    return img

if __name__=='__main__':
    
    filename = "maze.txt"
    maze_png(*maze_matrix(filename)).show()