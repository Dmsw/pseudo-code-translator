from variable_info import BaseVar


class Structure:
    def __init__(self, struct_name):
        self.struct_name = struct_name
        self.variables = list()
        self.name_type = dict()

    def get_name(self):
        return self.struct_name

    def add(self, name, t, val=None):
        _t = BaseVar(name, t, val)
        self.variables.append(_t)
        self.name_type[name] = t

    def get_all_variables(self):
        ret = dict()
        for name, t in self.name_type.items():
            vn = "{}.{}".format(self.struct_name, name)
            ret[vn] = t
        return ret

    def make_definition(self):
        def_feild = ""
        for n, t in self.name_type.items():
            d = "{} {};\n".format(t, n)
            def_feild = def_feild + d
        definition = "typedef struct %s %s;\n" % (self.struct_name, self.struct_name)
        definition = definition + "struct %s {\n%s};\n" % (self.struct_name, def_feild)
        return definition


class StructObject:
    def __init__(self, structure: Structure, object_name):
        self.object_name = object_name
        self.structure = structure

    def get_struct_name(self):
        return self.structure.get_name()

    def get_variables(self):
        return self.get_variables()

    def make_definition(self):
        struct = self.structure
        struct_name = self.get_struct_name()
        object_name = self.object_name
        declare = "{} {};\n".format(struct_name, object_name)
        make_zero = "memset({}, 0, sizeof(struct {}));\n".format(object_name, struct_name)
        init_val = ""
        for v in struct.variables:
            if v.init_val != 0:
                t = "{}.{} = {};\n".format(object_name, v.var_name, v.init_val)
                init_val = init_val + t
        definition = declare + make_zero + init_val
        return definition
