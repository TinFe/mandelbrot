import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc
from mandelbrot import Mandelbrot


test = Mandelbrot(zoom_factor=1,center=(0,0),iterations=100,size=200)


# create a MainWindow class
class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        main_widget = qtw.QWidget()
        main_widget.setLayout(qtw.QVBoxLayout())
        self.setCentralWidget(main_widget)

        width = test.canvas_width
        height = test.canvas_height
        image = qtg.QImage(width, height, qtg.QImage.Format.Format_RGB32)

        for row in range(len(test.pixel_array)):
            for col in range(len(test.pixel_array[0])):
                print(f'view loop running row, col = {row,col}')
                pos = qtc.QPoint(col, row)
                image.setPixel(pos, test.pixel_array[row][col])

        filename = 'mandelbrot.png'
        image.save(filename)

        pixmap = qtg.QPixmap.fromImage(image)
        pixmap_item = qtw.QGraphicsPixmapItem(pixmap)

        scene = qtw.QGraphicsScene()
        scene.addItem(pixmap_item)

        view = qtw.QGraphicsView()
        view.setScene(scene)

        main_widget.layout().addWidget(view)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
