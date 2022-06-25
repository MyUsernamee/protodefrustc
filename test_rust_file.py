import unittest

from src import rust_file


class RustTestCase(unittest.TestCase):
    def test_module(self):

        self.assertEqual("pub mod test {\n\t\n}", rust_file.module("test"))

    def test_struct_def(self):

        self.assertEqual("pub struct TestStruct {\n\tpub test_field: i32,\n\tpub test_field2: i32\n}", rust_file.struct_def("TestStruct",
            rust_file.field("test_field", "i32", True),
            rust_file.field("test_field2", "i32", True)
        ))

    def test_field(self):

        self.assertEqual("pub test_field: i32", rust_file.field("test_field", "i32", True))
        self.assertEqual("test_field: i32", rust_file.field("test_field", "i32"))

    def test_let(self):

        self.assertEqual("let test_field: i32 = 1;", rust_file.let_("test_field", "i32", "1"))

    def test_comment(self):

        self.assertEqual("// This is a comment", rust_file.comment("This is a comment"))

    def test_if(self):

        self.assertEqual("if test_field == 1 {\n\treturn 1;\n}", rust_file.if_("test_field == 1",
            rust_file.return_("1")
        ))

    def test_return(self):

        self.assertEqual("return 1;", rust_file.return_("1"))

    def test_call(self):

        self.assertEqual("fibbonacci(1)", rust_file.call("fibbonacci", "1"))

    def test_add(self):

        self.assertEqual("1 + 1", rust_file.add("1", "1"))

    def test_sub(self):

        self.assertEqual("1 - 1", rust_file.sub("1", "1"))

    def test_eq(self):

        self.assertEqual("1 == 1", rust_file.eq("1", "1"))

    def test_neq(self):

        self.assertEqual("1 != 1", rust_file.neq("1", "1"))

    def test_gt(self):

        self.assertEqual("1 > 1", rust_file.gt("1", "1"))

    def test_lt(self):

        self.assertEqual("1 < 1", rust_file.lt("1", "1"))

    def test_ge(self):

        self.assertEqual("1 >= 1", rust_file.ge("1", "1"))

    def test_le(self):

        self.assertEqual("1 <= 1", rust_file.le("1", "1"))

    def test_and(self):

        self.assertEqual("1 && 1", rust_file.and_("1", "1"))

    def test_or(self):

        self.assertEqual("1 || 1", rust_file.or_("1", "1"))

    def test_not(self):

        self.assertEqual("!1", rust_file.not_("1"))

    def test_while(self):

        self.assertEqual("while test_field == 1 {\n\treturn 1;\n}", rust_file.while_("test_field == 1",
            rust_file.return_("1")
        ))

    def test_for(self):

        self.assertEqual("for i in 0..10 {\n\treturn 1;\n}", rust_file.for_("i", "0..10",
                                                                            rust_file.return_("1")))

    def test_fibbonacci(self):
        code = rust_file.function_def("fibbonacci",
        [rust_file.field("iteration", "usize")],
        "u32",
            rust_file.if_(rust_file.eq("iteration", "1"),
                          rust_file.return_("1")),
            rust_file.return_(
                rust_file.add(rust_file.call("fibbonacci", rust_file.sub("iteration", "1")),
                              rust_file.call("fibbonacci", rust_file.sub("iteration", "2")))
            )
        )

        self.assertEqual(code, "fn fibbonacci(iteration: usize) -> u32 {\n\tif iteration == 1 {\n\t\treturn 1;\n\t}\n\treturn fibbonacci(iteration - 1) + fibbonacci(iteration - 2);\n}")

    def test_dot(self):
        code = rust_file.dot("test_field", "test_field2")

        self.assertEqual(code, "test_field.test_field2")

    def test_index(self):

        code = rust_file.index("test_field", "test_field2")

        self.assertEqual(code, "test_field[test_field2]")

    def test_assign(self):

        code = rust_file.assign("test_field", "test_field2")

        self.assertEqual(code, "test_field = test_field2")

    def test_deref(self):

        code = rust_file.deref("test_field")

        self.assertEqual(code, "*test_field")

    def test_index_namespace(self):

        code = rust_file.index_namespace("test_field", "test_field2")

        self.assertEqual(code, "test_field::test_field2")

    def test_use(self):

        code = rust_file.use("test_field")

        self.assertEqual(code, "use test_field;")

if __name__ == '__main__':
    unittest.main()
