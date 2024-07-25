import base64
import unittest

import sqlmovies.base


class StructureTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.MODULE = sqlmovies.base
    
    def test_class_exists_basecategoryrepository(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"is not found, but it was marked as required."
        )
        
    def test_class_function_exists_basecategoryrepository_count(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()
        )
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5jb3VudA==').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5jb3VudA==').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}`, "
                f"but it was marked as required."
        )
        
    def test_class_function_signature_match_basecategoryrepository_count(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()
        )
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5jb3VudA==').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5jb3VudA==').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}`, "
                f"but it was marked as required."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5jb3VudA==').decode()
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5jb3VudA==').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"should have 1 argument(s)."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5jb3VudA==').decode()
        )
        self.assertEqual(
            base64.b64decode(b'c2VsZg==').decode(),
            args[0],
            msg=f"The argument #0 of function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5jb3VudA==').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"should be called "
                f"`self`."
        )
        
    def test_class_function_exists_basecategoryrepository_find(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()
        )
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5k').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5k').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}`, "
                f"but it was marked as required."
        )
        
    def test_class_function_signature_match_basecategoryrepository_find(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()
        )
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5k').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5k').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}`, "
                f"but it was marked as required."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5k').decode()
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5k').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"should have 2 argument(s)."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5k').decode()
        )
        self.assertEqual(
            base64.b64decode(b'c2VsZg==').decode(),
            args[0],
            msg=f"The argument #0 of function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5k').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"should be called "
                f"`self`."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5k').decode()
        )
        self.assertEqual(
            base64.b64decode(b'cGs=').decode(),
            args[1],
            msg=f"The argument #1 of function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5k').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"should be called "
                f"`pk`."
        )
        
    def test_class_function_exists_basecategoryrepository_find_all(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()
        )
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2FsbA==').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2FsbA==').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}`, "
                f"but it was marked as required."
        )
        
    def test_class_function_signature_match_basecategoryrepository_find_all(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()
        )
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2FsbA==').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2FsbA==').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}`, "
                f"but it was marked as required."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2FsbA==').decode()
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2FsbA==').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"should have 1 argument(s)."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2FsbA==').decode()
        )
        self.assertEqual(
            base64.b64decode(b'c2VsZg==').decode(),
            args[0],
            msg=f"The argument #0 of function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2FsbA==').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"should be called "
                f"`self`."
        )
        
    def test_class_function_exists_basecategoryrepository_find_by_name(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()
        )
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2J5X25hbWU=').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2J5X25hbWU=').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}`, "
                f"but it was marked as required."
        )
        
    def test_class_function_signature_match_basecategoryrepository_find_by_name(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()
        )
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2J5X25hbWU=').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2J5X25hbWU=').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}`, "
                f"but it was marked as required."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2J5X25hbWU=').decode()
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2J5X25hbWU=').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"should have 2 argument(s)."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2J5X25hbWU=').decode()
        )
        self.assertEqual(
            base64.b64decode(b'c2VsZg==').decode(),
            args[0],
            msg=f"The argument #0 of function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2J5X25hbWU=').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"should be called "
                f"`self`."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2J5X25hbWU=').decode()
        )
        self.assertEqual(
            base64.b64decode(b'bmFtZQ==').decode(),
            args[1],
            msg=f"The argument #1 of function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5maW5kX2J5X25hbWU=').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"should be called "
                f"`name`."
        )
        
    def test_class_function_exists_basecategoryrepository_save(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()
        )
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5zYXZl').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5zYXZl').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}`, "
                f"but it was marked as required."
        )
        
    def test_class_function_signature_match_basecategoryrepository_save(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()
        )
        self.assertIn(
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5zYXZl').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5zYXZl').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}`, "
                f"but it was marked as required."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5zYXZl').decode()
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5zYXZl').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"should have 2 argument(s)."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5zYXZl').decode()
        )
        self.assertEqual(
            base64.b64decode(b'c2VsZg==').decode(),
            args[0],
            msg=f"The argument #0 of function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5zYXZl').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"should be called "
                f"`self`."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode(),
            base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5zYXZl').decode()
        )
        self.assertEqual(
            base64.b64decode(b'Y2F0ZWdvcnk=').decode(),
            args[1],
            msg=f"The argument #1 of function "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeS5zYXZl').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZUNhdGVnb3J5UmVwb3NpdG9yeQ==').decode()}` "
                f"should be called "
                f"`category`."
        )
        
    def test_class_exists_basemoviereport(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode()}` "
                f"is not found, but it was marked as required."
        )
        
    def test_class_function_exists_basemoviereport_get(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode()
        )
        self.assertIn(
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode()}`, "
                f"but it was marked as required."
        )
        
    def test_class_function_signature_match_basemoviereport_get(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode()
        )
        self.assertIn(
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode()}`, "
                f"but it was marked as required."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode(),
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()
        )
        self.assertEqual(
            5,
            len(args),
            msg=f"The function "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode()}` "
                f"should have 5 argument(s)."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode(),
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()
        )
        self.assertEqual(
            base64.b64decode(b'c2VsZg==').decode(),
            args[0],
            msg=f"The argument #0 of function "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode()}` "
                f"should be called "
                f"`self`."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode(),
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()
        )
        self.assertEqual(
            base64.b64decode(b'bGltaXQ=').decode(),
            args[1],
            msg=f"The argument #1 of function "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode()}` "
                f"should be called "
                f"`limit`."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode(),
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()
        )
        self.assertEqual(
            base64.b64decode(b'ZnJvbV95ZWFy').decode(),
            args[2],
            msg=f"The argument #2 of function "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode()}` "
                f"should be called "
                f"`from_year`."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode(),
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()
        )
        self.assertEqual(
            base64.b64decode(b'dG9feWVhcg==').decode(),
            args[3],
            msg=f"The argument #3 of function "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode()}` "
                f"should be called "
                f"`to_year`."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode(),
            base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()
        )
        self.assertEqual(
            base64.b64decode(b'Y2F0ZWdvcmllcw==').decode(),
            args[4],
            msg=f"The argument #4 of function "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0LmdldA==').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'QmFzZU1vdmllUmVwb3J0').decode()}` "
                f"should be called "
                f"`categories`."
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
