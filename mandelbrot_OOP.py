class MandelbrotObject:
    iterations = 200
    scale_factor = 4294967295
    min_iterations = 0
    max_iterations = iterations



    def __init__(self, view_size, mandel_center, mandel_zoom_factor):
        self.view_size = view_size
        self.mandel_center_x = mandel_center[0]
        self.mandel_center_y = mandel_center[1]
        # self.complex_plane = (top_left_point, bottom_right_point) = (x,y)
        self.complex_plane_top_left_x = (-2 + self.mandel_center_x) / mandel_zoom_factor
        self.complex_plane_top_left_y = ( 1 + self.mandel_center_y) / mandel_zoom_factor
        self.complex_plane_bottom_right_x = (1 + self.mandel_center_x) / mandel_zoom_factor
        self.complex_plane_bottom_right_y = (-1 + self.mandel_center_y) / mandel_zoom_factor

        self.complex_plane = [self.complex_plane_top_left_x, self.complex_plane_top_left_y,
                              self.complex_plane_bottom_right_x, self.complex_plane_bottom_right_y]
        # determine width and height of view in pixels
        self.view_width = self.view_size * 3
        self.view_height = self.view_size * 2
        # determine amount to increment complex number each iteration: x_increment = (x range) / view_pixels wide
        self.complex_x_increment = abs(self.complex_plane_top_left_x - self.complex_plane_bottom_right_x) / self.view_width
        self.complex_y_increment = abs(self.complex_plane_top_left_y - self.complex_plane_bottom_right_y) / self.view_height
        # create 2d view_array. len(view_array) = total number of rows; len(view_array[0]) = number of columns
        self.view_array = []

        for rows in range(self.view_height):
            new_row = []
            for cols in range(self.view_width):
                c = complex(self.complex_plane[0],self.complex_plane[1])
                num_of_iterations = self.mandelbrot_iterator(c, self.iterations)
                if num_of_iterations > self.max_iterations:
                    self.max_iterations = num_of_iterations
                elif num_of_iterations < self.min_iterations:
                    self.min_iterations = num_of_iterations
                print(f'row {rows}, col {cols} takes {num_of_iterations} before terminating')
                rgb_value = self.iteration_to_rgb(num_of_iterations)
                new_row.append(rgb_value)
                self.complex_plane[0] += self.complex_x_increment
            self.view_array.append(new_row)
            self.complex_plane[1] -= self.complex_y_increment
            self.complex_plane[0] = self.complex_plane_top_left_x

    def mandelbrot_iterator(self, complex_num, iterations=100, threshold=100000):
        z = 0
        for i in range(iterations):
            if abs(z) > threshold:
                return i
            z = (z ** 2) + complex_num
        return i

    iteration_range = max_iterations - min_iterations
    rgb_increment = scale_factor / iteration_range

    def iteration_to_rgb(self, num_of_iterations):
        rgb_value = self.scale_factor - round((num_of_iterations - self.min_iterations) * self.rgb_increment)
        return rgb_value


mandel = MandelbrotObject(100,(-2,0),1)
for row in range(len(mandel.view_array)):
    for col in range(len(mandel.view_array)):
        if mandel.view_array[row][col] > 4294967295:
            print(f"{row},{col},{mandel.view_array[row][col]}")

print(mandel.iteration_range)