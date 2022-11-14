class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class tablaValores (metaclass = Singleton):
    ts = [dict()]

    def __init__(self) -> None:
        pass

    def add_id(self, id):
        self.ts[-1][id.name] : id

    def add_context(self):
        self.ts.append(dict())

    def del_context(self):
        self.ts.pop();

    def findKey(self, key):
        for context in self.ts:
            if(key in context):
                return True

        return False

class id:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.initialized = False
        self.used = False
        self.kind = "variable"

    def getType(self):
        return self.type
    def getKind(self):
        return self.kind

class variable(id):
    pass

class funcion(id):
    def __init__(self, name, type, parameters):
        super().__init__(name, type)
        self.parameters = parameters
        self.kind = "function"
    