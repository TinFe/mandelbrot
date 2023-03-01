# return a 2d array to represent the pixels space of the mandelbrot set.
# the desired aspect ratio for displaying the mandelbrot is 3:2. one `size_unit` is 300x200px
def pixel_space(size_unit):
    tot_rows = size_unit * 200
    tot_cols = size_unit * 300
    canvas = []

    row_count = 0
    col_count = 0

    iterations_to_diverge = 0

    while row_count < tot_rows:
        row = []
        while col_count < tot_cols:
            row.append(iterations_to_diverge)
            col_count += 1
        col_count = 0
        row_count += 1
        canvas.append(row)
    return canvas

# iterate on a complex number to test whether it's in the madnelbrot set
def mandelbrot_iterator(complex_num, iterations=100, threshold=100000):
    z = 0
    for i in range(iterations):
        if abs(z) > threshold:

            return i
        z = (z ** 2) + complex_num

    return i

# iterate through pixel space and calculate record how many iterations of mandelbrot calculaion are performed
def mandelbrot_tester(pixel_space):
    mandelbrot_array = pixel_space
    total_rows = len(mandelbrot_array)
    total_cols = len(mandelbrot_array[0])

    # map indexes of 2d array to coordinates on the complex plane
    mandelbrot_x_increment = 3 / total_cols
    mandelbrot_y_increment = 2 / total_rows

    # first complex number to test is in the top right corner of the screen e.g. top left of the complex plane (-3,2)
    x = -2
    y =  1

    for row in range(total_rows):
        for col in range(total_cols):
            mandelbrot_array[row][col] = mandelbrot_iterator(complex(x,y))
            x += mandelbrot_x_increment
        x = -2
        y -= mandelbrot_y_increment

    return mandelbrot_array

# translate number of iterations it takes for a complex coordinate to "blow up" to 8bit grayscale pixel
def mandel_set_to_monochrome_pixel_array(mandelbrot_array):
    monochrome_mandelbrot_array = []
    # number of iterations for complex(-2,1)
    min_iterations = mandelbrot_array[0][0]
    # number of iterations for complex(0,0)
    max_iterations = mandelbrot_array[int(len(mandelbrot_array)/2)][int(len(mandelbrot_array[0])/2)]

    iteration_range = max_iterations - min_iterations

    scale_factor = 4294967295 / iteration_range

    for row in range(len(mandelbrot_array)):
        new_row = []
        for col in range(len(mandelbrot_array[0])):
            print(f'creating index {row}, {col}')
            new_row.append(round(iteration_range * scale_factor) - round((mandelbrot_array[row][col] - min_iterations) * scale_factor))
        monochrome_mandelbrot_array.append(new_row)
    return monochrome_mandelbrot_array




space = pixel_space(5)
mandel = mandelbrot_tester(space)
mandel_monochrome = mandel_set_to_monochrome_pixel_array(mandel)
print(mandel_monochrome)
