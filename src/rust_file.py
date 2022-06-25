# Define a simple way for define or writing code for generating rust code that is abstract
# For example:
"""

print(rust_file.module("test",
    rust_file.struct_def("TestStruct",
        rust_file.struct_field("test_field", "i32"),
        rust_file.struct_field("test_field2", "i32")
    )
))

Should generate:

pub mod test {
    pub struct TestStruct {
        pub test_field: i32,
        pub test_field2: i32,
    }
}

"""
# Note: All code will be generate will be made public in rust.

indent = "\t"


def simple_block(prefix: str, postfix: str, delimiter: str, *args) -> str:
    code = ""
    for index, arg in enumerate(args):
        if isinstance(arg, str):
            code += arg
            if index != len(args) - 1:
                code += delimiter
    # Add a indents to the beginning of each line
    code = code.replace(delimiter, delimiter + indent)
    return f"{prefix}{code}{postfix}"


def module(name: str, *args) -> str:
    return simple_block(f"pub mod {name} {{\n{indent}", "\n}", "\n", *args)


def struct_def(name: str, *args) -> str:
    return simple_block(f"pub struct {name} {{\n{indent}", "\n}", ",\n", *args)


def field(name: str, type: str, public=False) -> str:
    if public:
        return f"pub {name}: {type}"
    else:
        return f"{name}: {type}"


def let_(name: str, type: str, value: str) -> str:
    return f"let {name}: {type} = {value};"


def comment(comment: str) -> str:
    return f"// {comment}"


def if_(condition: str, *args) -> str:
    return simple_block(f"if {condition} {{\n{indent}", "\n}", "\n", *args)


def le(left: str, right: str) -> str:
    return f"{left} <= {right}"


def ge(left: str, right: str) -> str:
    return f"{left} >= {right}"


def eq(left: str, right: str) -> str:
    return f"{left} == {right}"


def ne(left: str, right: str) -> str:
    return f"{left} != {right}"


def gt(left: str, right: str) -> str:
    return f"{left} > {right}"


def lt(left: str, right: str) -> str:
    return f"{left} < {right}"


def and_(left: str, right: str) -> str:
    return f"{left} && {right}"


def or_(left: str, right: str) -> str:
    return f"{left} || {right}"


def not_(condition: str) -> str:
    return f"!{condition}"


def return_(value: str) -> str:
    return f"return {value};"


def function_def(name: str, arguments: [str], return_: str, *args) -> str:
    return simple_block(f"fn {name}({', '.join(arguments)}) -> {return_} {{\n{indent}", "\n}", "\n", *args)


def match(value: str, *args) -> str:
    return simple_block(f"match {value} {{\n{indent}", "\n}", "\n", *args)


def match_arm(value: str, *args) -> str:
    return simple_block(f"{value} => {{\n{indent}", "\n}", "\n", *args)


def match_arm_default(*args) -> str:
    return simple_block(f"_ => {{\n{indent}", "\n}", "\n", *args)


def loop(condition: str, *args) -> str:
    return simple_block(f"loop {{\n{indent}", "\n}", "\n", *args)


def for_(name: str, value: str, *args) -> str:
    return simple_block(f"for {name} in {value} {{\n{indent}", "\n}", "\n", *args)


def while_(condition: str, *args) -> str:
    return simple_block(f"while {condition} {{\n{indent}", "\n}", "\n", *args)


def break_() -> str:
    return "break;"


def continue_() -> str:
    return "continue;"


def operator(function):
    def wrapper(left, right):
        operation = function()
        return f"{left} {operation} {right}"
    return wrapper

@operator
def add() -> str:
    return "+"


@operator
def sub() -> str:
    return "-"


@operator
def mul() -> str:
    return "*"


@operator
def div() -> str:
    return "/"


@operator
def modulo() -> str:
    return "%"


def neg(value: str) -> str:
    return f"-{value}"


@operator
def assign() -> str:
    return "="


def call(name: str, *args) -> str:
    return f"{name}({', '.join(args)})"


def borrow(name: str) -> str:
    return f"&{name}"


def borrow_mut(name: str) -> str:
    return f"&mut {name}"


def custom(code: str) -> str:  # Technically this does nothing but return the code, it just makes it easier to use
    return code


def neq(left: str, right: str) -> str:
    return f"{left} != {right}"


def deref(value: str) -> str:
    return f"*{value}"


def index(value: str, index: str) -> str:
    return f"{value}[{index}]"


def dot(value: str, field: str) -> str:
    return f"{value}.{field}"


def index_namespace(value: str, index: str) -> str:
    return f"{value}::{index}"


def use(name: str) -> str:
    return f"use {name};"
