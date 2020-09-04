class VarInfo():
    def __init__(self,
                 name,
                 line_statement,
                 line_no,
                 is_defined=False,
                 hint_type=None,
                 init_method='normal',
                 definition=None,
                 init_val=None,
                 var_type=None):
        self.var_name = name
        self.set_is_defined(is_defined)
        self.set_init_method(init_method)
        self.set_hint_type(hint_type)
        self.set_line_number(line_no)
        self.set_line_statement(line_statement)
        self.set_init_val(init_val)
        self.set_definition(definition)
        self.set_var_type(var_type)

    def set_is_defined(self, is_defined):
        self.is_defined = is_defined

    def set_var_type(self, var_type):
        self.var_type = var_type

    def set_init_val(self, init_val):
        self.init_val = init_val

    def set_line_number(self, lineno):
        self.line_no = lineno

    def set_hint_type(self, hint_type):
        self.hint_type = hint_type

    def set_line_statement(self, statement):
        self.line_statement = statement

    def set_init_method(self, init_method):
        self.init_method = init_method

    def set_definition(self, definition):
        if self.init_method == "normal":
            self.definition = definition
        else:
            if self.init_val == 0:
                self.definition = definition
            else:
                self.definition = str(definition)  + "\nmemset({}, {}, sizeof({}));".format(self.var_name, self.init_val, self.var_name)

    def make_definition(self):
        if self.init_method == 'normal':
            if self.init_val is not None:
                self.set_definition("{} {} = {};".format(self.var_type, self.var_name, self.init_val))
            else:
                self.set_definition("{} {};".format(self.var_type, self.var_name))
        elif self.init_method == 'array':
            self.set_definition("{} {}[MAXLENGTH] = {{0}};".format(self.var_type, self.var_name))
