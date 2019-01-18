class t1(type):
    def __new__(meta, name, bases, class_dict):
        if bases!= (object, ):
            if class_dict['sides'] < 3:
                raise ValueError('need 3 more')
        return type.__new__(meta, name, bases, class_dict)


class polygon(object, metaclass=t1):
    sides = None

    @classmethod
    def get_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(polygon):
    sides = 1



