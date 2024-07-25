import base64
import unittest

import sqlmovies.category_repository


class StructureTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.MODULE = sqlmovies.category_repository

    def test_class_exists_categoryrepository(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"is not found, but it was marked as required.",
        )

    def test_class_function_exists_categoryrepository___init__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5Ll9faW5pdF9f").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5Ll9faW5pdF9f').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_categoryrepository___init__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5Ll9faW5pdF9f").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5Ll9faW5pdF9f').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5Ll9faW5pdF9f").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5Ll9faW5pdF9f').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5Ll9faW5pdF9f").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5Ll9faW5pdF9f').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5Ll9faW5pdF9f").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"ZGJfcGF0aA==").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5Ll9faW5pdF9f').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should be called "
            f"`db_path`.",
        )

    def test_class_function_exists_categoryrepository_count(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmNvdW50").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmNvdW50').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_categoryrepository_count(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmNvdW50").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmNvdW50').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmNvdW50").decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmNvdW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmNvdW50").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmNvdW50').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should be called "
            f"`self`.",
        )

    def test_class_function_exists_categoryrepository_find(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmQ=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmQ=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_categoryrepository_find(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmQ=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmQ=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmQ=").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmQ=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cGs=").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmQ=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should be called "
            f"`pk`.",
        )

    def test_class_function_exists_categoryrepository_find_all(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYWxs").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYWxs').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_categoryrepository_find_all(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYWxs").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYWxs').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYWxs").decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYWxs').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYWxs").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYWxs').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should be called "
            f"`self`.",
        )

    def test_class_function_exists_categoryrepository_find_by_name(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYnlfbmFtZQ==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYnlfbmFtZQ==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_categoryrepository_find_by_name(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYnlfbmFtZQ==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYnlfbmFtZQ==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYnlfbmFtZQ==").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYnlfbmFtZQ==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYnlfbmFtZQ==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYnlfbmFtZQ==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYnlfbmFtZQ==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"bmFtZQ==").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LmZpbmRfYnlfbmFtZQ==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should be called "
            f"`name`.",
        )

    def test_class_function_exists_categoryrepository_save(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LnNhdmU=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LnNhdmU=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_categoryrepository_save(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode()
        )
        self.assertIn(
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LnNhdmU=").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LnNhdmU=').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LnNhdmU=").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LnNhdmU=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LnNhdmU=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LnNhdmU=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5").decode(),
            base64.b64decode(b"Q2F0ZWdvcnlSZXBvc2l0b3J5LnNhdmU=").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"Y2F0ZWdvcnk=").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5LnNhdmU=').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'Q2F0ZWdvcnlSZXBvc2l0b3J5').decode()}` "
            f"should be called "
            f"`category`.",
        )


# === Internal functions, do not modify ===
import inspect

from types import ModuleType
from typing import List


def _get_function_names(module: ModuleType) -> List[str]:
    names = []
    functions = inspect.getmembers(module, lambda member: inspect.isfunction(member))
    for name, fn in functions:
        if fn.__module__ == module.__name__:
            names.append(name)
    return names


def _get_function_arg_names(module: ModuleType, fn_name: str) -> List[str]:
    arg_names = []
    functions = inspect.getmembers(module, lambda member: inspect.isfunction(member))
    for name, fn in functions:
        if fn.__module__ == module.__name__:
            if fn.__qualname__ == fn_name:
                args_spec = inspect.getfullargspec(fn)
                arg_names = args_spec.args
                if args_spec.varargs is not None:
                    arg_names.extend(args_spec.varargs)
                if args_spec.varkw is not None:
                    arg_names.extend(args_spec.varkw)
                arg_names.extend(args_spec.kwonlyargs)
                break
    return arg_names


def _get_class_names(module: ModuleType) -> List[str]:
    names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for name, cls in classes:
        if cls.__module__ == module.__name__:
            names.append(name)
    return names


def _get_class_function_names(module: ModuleType, cls_name: str) -> List[str]:
    fn_names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for cls_name_, cls in classes:
        if cls.__module__ == module.__name__:
            if cls_name_ == cls_name:
                functions = inspect.getmembers(
                    cls,
                    lambda member: inspect.ismethod(member)
                    or inspect.isfunction(member),
                )
                for fn_name, fn in functions:
                    fn_names.append(fn.__qualname__)
                break
    return fn_names


def _get_class_function_arg_names(
    module: ModuleType, cls_name: str, fn_name: str
) -> List[str]:
    arg_names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for cls_name_, cls in classes:
        if cls.__module__ == module.__name__:
            if cls_name_ == cls_name:
                functions = inspect.getmembers(
                    cls,
                    lambda member: inspect.ismethod(member)
                    or inspect.isfunction(member),
                )
                for fn_name_, fn in functions:
                    if fn.__qualname__ == fn_name:
                        args_spec = inspect.getfullargspec(fn)
                        arg_names = args_spec.args
                        if args_spec.varargs is not None:
                            arg_names.extend(args_spec.varargs)
                        if args_spec.varkw is not None:
                            arg_names.extend(args_spec.varkw)
                        arg_names.extend(args_spec.kwonlyargs)
                        break
                break
    return arg_names
