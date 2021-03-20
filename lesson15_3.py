class BBox:
    def __init__(self, x0, y0, x1, y1):
        # x0, x1 = (x1, x0) if x1 < x0 else (x0, x1)
        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1

    def __repr__(self):
        return f"(({self._x0}; {self._y0}), ({self._x1}; {self._y1}))"

    def get_area(self):
        return (self._y1 - self._y0) * (self._x1 - self._x0)

    def __add__(self, other):
        x0 = min(self._x0, other._x0)
        y0 = min(self._y0, other._y0)
        x1 = max(self._x1, other._x1)
        y1 = max(self._y1, other._y1)
        return BBox(x0, y0, x1, y1)

    def __eq__(self, other):
        return self._x0 == other._x0 and \
               self._y0 == other._y0 and \
               self._x1 == other._x1 and \
               self._y1 == other._y1

    def __le__(self, other):
        return self._x0 > other._x0


bbox_1 = BBox(2, 2, 3, 4)
bbox_2 = BBox(2, 2, 3, -4)

bbox_3 = bbox_1 + bbox_2  # полиморфизм
print(bbox_3)
print(bbox_1 <= bbox_2)
