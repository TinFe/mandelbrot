class Mandelbrot:
    def __init__(self, zoom_factor, center, iterations, size,):
        self.size = size
        self.iterations = iterations
        # lay out the complex plane based on the zoom_factor and center attributes
        self.offset_x = center[0]
        self.offset_y = center[1]
        self.zoom_factor = zoom_factor
        # store top left and bottom right points of the complex plane as xy coordinates
        self.top_left_coordinate = ((-2 + self.offset_x) / self.zoom_factor, (1 + self.offset_y) / self.zoom_factor)
        self.bottom_right_coordinate = ((1 + self.offset_x) / self.zoom_factor, (-1 + self.offset_y) / self.zoom_factor)
        # lay out a 2d mandelbrot_array to hold pixel coordinates mapped to coordinates on the complex plane
        # aspect ratio of the canvas is always 3:2 because the complex plane starts at
        # xmin,xmax = -2,1, and ymin, ymax = 1,-1 and is never stretched horizontally or vertically
        self.canvas_width = size * 3
        self.canvas_height = size * 2
        self.mandelbrot_array = []
        # prepare to iterate on every point of complex-plane-mapped-canvas
        # as the range of iterations required to test whether a point is in the mandelbrot set will change as we zoom,
        # we need to store variables for min and max iterations required, and update them as we iterate over the canvas
        self.min_iterations = iterations
        self.max_iterations = 1
        # determine amounts to increment complex number by for each iteration
        self.increment_x = abs(self.top_left_coordinate[0] - self.bottom_right_coordinate[0]) / self.canvas_width
        self.increment_y = abs(self.top_left_coordinate[1] - self.bottom_right_coordinate[1]) / self.canvas_height
        # initialize starting complex coordinate for following loop to work with
        self.test_coordinate = [self.top_left_coordinate[0], self.top_left_coordinate[1]]

        # populate self.mandelbrot_array with the number of iterations it takes to break threshold for each coordinate
        for row in range(self.canvas_height):
            new_row = []
            for col in range(self.canvas_width):
                iterate_count = self.iterate(complex(self.test_coordinate[0], self.test_coordinate[1]), iterations)
                # check if iterate_count is the new min or max
                if iterate_count > self.max_iterations:
                    self.max_iterations = iterate_count
                if iterate_count < self.min_iterations:
                    self.min_iterations = iterate_count
                # add tested coordinate to the 2d mandelbrot_array
                new_row.append(iterate_count)
                # move the test coordinate to the new x position
                self.test_coordinate[0] += self.increment_x
            self.mandelbrot_array.append(new_row)
            self.test_coordinate[0] = self.top_left_coordinate[0]
            self.test_coordinate[1] -= self.increment_y

        self.pixel_array = self.iteration_count_to_pixel_value(mandelbrot_array=self.mandelbrot_array,
                        min_iterations=self.min_iterations, max_iterations=self.max_iterations,pixel_value_max=4294967295)

    def iteration_count_to_pixel_value(self, mandelbrot_array, min_iterations, max_iterations, pixel_value_max):
        iteration_range = max_iterations - min_iterations
        pixel_array = mandelbrot_array
        for row in range(len(pixel_array)):
            for col in range(len(pixel_array[0])):
                pixel_array[row][col] = pixel_value_max - round((pixel_array[row][col] - min_iterations) * \
                                             (pixel_value_max / iteration_range))

        return pixel_array
    def iterate(self, complex_num, iterations=100, threshold=100000):
        z = 0
        for i in range(iterations):
            if abs(z) > threshold:
                return i
            z = (z ** 2) + complex_num
        return i



