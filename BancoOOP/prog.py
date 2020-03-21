class Meta(type):

    def __new__(mcs, name, bases, namespace):
        print(namespace)
        if 'attr_classe' in namespace:
        return type.__new__(mcs,name, bases, namespace)

class A(metaclass=Meta):

    attr_classe = "estou em A"

class B(A):

    attr_classe = "estou em B"
