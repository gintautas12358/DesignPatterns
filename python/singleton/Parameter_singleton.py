

class ParameterSingleton(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(ParameterSingleton, cls).__new__(cls)

            #initialization here
            cls.port_mappings = {"5000": "8000", "5001": "8001", "5003": "8003"}
            
        return cls._instance