'''
this file is a image operation class
'''
'''
2015/04/14
Fa-Hong zhou
v1.0.0.1 first release
'''


import os
import pickle

'''
exception operation class
'''
class ImageError(Exception):
    pass

class CoordinateError(ImageError):
    pass

class LoadError(ImageError):
    pass

class SaveError(ImageError):
    pass

class ExportError(ImageError):
    pass

class NoFilenameError(ImageError):
    pass

'''
image operation class
'''
class Image():
    def __init__(self, width, height, filename = "", background = "#FFFFFF"):
        self.filename = filename
        self.__background = background
        self.__data = {}
        self.__width = width
        self.__height = height
        self.__colors = (self.__background)

    #private function
    @property
    def background(self):
        return self.__background
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @property
    def colors(self):
        return self.__colors

    '''
    coordinate is like point(x, y)
    get a point's color
    '''
    def __getitem__(slef, coordinate):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or
            not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        return self.__data.get(tuple(coordinate), self.__background)

    '''
    coordinate is like point(x, y)
    set the point's color
    '''
    def __setitem__(slef, coordinate, color):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or
            not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        if color == self.__background:
            self.__data.pop(tuple(coordinate), None)
        else:
            self.__data[tuple(coordinate)] = color
            self.__colors.add(color)

    '''
    coordinate is a point, like (x, y)
    self.__data is a dictdory, Like [(x, y), color]
    delete the point's color
    '''   
    def __delitem__(slef, coordinate):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or
            not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        self.__data.pop(tuple(coordinate), None)

    '''
    use pickle package save the file
    '''
    def save(self, filename = None):
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NotFilenameError()

        fh = None
        try:
            data = [self.width, self.height, self.__background, self.__data]
            fh = open(self.filename, 'wb')
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except(EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()

    '''
    use pickle package load the file
    '''
    def load(self, filename = None):
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NotFilenameError()
        
        fh = None
        try:
            fh = opem(self.filename, "rb")
            data = pickle.load(fh)
            (self.__width, self.__height, self.__background, self.__data) = data
            self.colors = (set(self.__data.values()) | {self.__background})
        except(EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()

    def export(self, filename):
        if filename.lower().endswith(".xpm"):
            self.__export_xmp(filename)
        else:
            raise ExportError("unsupported export format: " + os.path.splitext(filename)[1])

    def export_xmp(self):
        pass
