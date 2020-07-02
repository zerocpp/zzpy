import unittest


class ZfileTests(unittest.TestCase):
    def setUp(self):
        import os
        super().setUp()
        self.root_dir = os.path.join("test", "file")
        from zzpy import remove_dir
        remove_dir(self.root_dir)

    def tearDown(self):
        from zzpy import remove_dir
        super().tearDown()
        remove_dir(self.root_dir)

    def test_read_jsonline(self):
        from zzpy import read_jsonline
        from collections.abc import Generator
        import os

        # generator
        file_path = os.path.join("test", "static", "1.jsonl")
        self.assertIsInstance(read_jsonline(file_path), Generator)

        # end file without newline
        data = []
        for i in read_jsonline(file_path):
            data.append(i)
        self.assertListEqual(data, [{"name": "Zero", "age": 31},
                                    {"name": "Flyoung", "age": 17}])

        # generator
        file_path = os.path.join("test", "static", "2.jsonl")
        self.assertIsInstance(read_jsonline(file_path), Generator)

        # end file with newline
        data = []
        for i in read_jsonline(file_path):
            data.append(i)
        self.assertListEqual(data, [{"name": "Zero", "age": 31},
                                    {"name": "Flyoung", "age": 17}])

    def test_create_and_remove_dir(self):
        """测试文件夹的创建和删除"""
        from zzpy import create_dir, remove_dir, init_dir
        from zzpy import get_file_name_list_from_dir
        import os

        # ending without "/"
        a_dir = os.path.join(self.root_dir, "a")
        b_dir = os.path.join(self.root_dir, "a", "b")

        create_dir(b_dir)
        self.assertTrue(os.path.exists(b_dir))

        init_dir(a_dir)
        self.assertTrue(os.path.exists(a_dir))
        self.assertFalse(os.path.exists(b_dir))

    def test_create_and_remove_dir_ending_with_slash(self):
        """测试文件夹名最后带斜线/的创建和删除"""
        from zzpy import create_dir, remove_dir, init_dir
        import os

        # ending with "/"
        a_dir = os.path.join(self.root_dir, "a/")
        b_dir = os.path.join(self.root_dir, "a", "b/")

        create_dir(b_dir)
        self.assertTrue(os.path.exists(b_dir))

        init_dir(a_dir)
        self.assertTrue(os.path.exists(a_dir))
        self.assertFalse(os.path.exists(b_dir))

    def test_init_dirs(self):
        from zzpy import init_dirs
        from zzpy import get_tmp_dir_path
        from zzpy import get_work_dir_path
        from zzpy import remove_dir
        from zzpy import get_file_name_list_from_dir
        import os

        tmp_dir = get_tmp_dir_path(root_dir=self.root_dir)
        work_dir = get_work_dir_path(root_dir=self.root_dir)

        self.assertFalse(os.path.exists(self.root_dir))
        init_dirs(root_dir=self.root_dir)
        self.assertTrue(os.path.exists(self.root_dir))
        self.assertTrue(os.path.exists(tmp_dir))
        self.assertTrue(os.path.exists(work_dir))

    def test_get_file_path_list_from_dir(self):
        from zzpy import get_file_path_list_from_dir
        from zzpy import write_file
        from zzpy import init_dir
        import os

        # init
        a_dir = os.path.join(self.root_dir, "a")
        aa_dir = os.path.join(a_dir, "aa")
        init_dir(aa_dir)
        a10_path = os.path.join(a_dir, "10.txt")
        write_file("10.txt", a10_path)
        aa11_path = os.path.join(aa_dir, "11.txt")
        write_file("11.txt", aa11_path)

        b_dir = os.path.join(self.root_dir, "b")
        bb_dir = os.path.join(b_dir, "bb")
        init_dir(bb_dir)
        bb20_path = os.path.join(bb_dir, "20.txt")
        write_file("20.txt", bb20_path)
        bb21_path = os.path.join(bb_dir, "21.txt")
        write_file("21.txt", bb21_path)

        c_dir = os.path.join(self.root_dir, "c")
        init_dir(c_dir)
        c30_path = os.path.join(c_dir, "30.txt")
        write_file("30.txt", c30_path)

        r_path = os.path.join(self.root_dir, "r.txt")
        write_file("r.txt", r_path)

        # test
        file_path_list = get_file_path_list_from_dir(
            self.root_dir)
        self.assertSetEqual(set(file_path_list), {
                            r_path, a10_path, aa11_path, bb20_path, bb21_path, c30_path})

    def test_get_file_name_list_from_dir(self):
        from zzpy import get_file_name_list_from_dir
        from zzpy import write_file
        from zzpy import init_dir
        import os

        # init
        a_dir = os.path.join(self.root_dir, "a")
        aa_dir = os.path.join(a_dir, "aa")
        init_dir(aa_dir)
        a10_path = os.path.join(a_dir, "10.txt")
        write_file("10.txt", a10_path)
        aa11_path = os.path.join(aa_dir, "11.txt")
        write_file("11.txt", aa11_path)

        b_dir = os.path.join(self.root_dir, "b")
        bb_dir = os.path.join(b_dir, "bb")
        init_dir(bb_dir)
        bb20_path = os.path.join(bb_dir, "20.txt")
        write_file("20.txt", bb20_path)
        bb21_path = os.path.join(bb_dir, "21.txt")
        write_file("21.txt", bb21_path)

        c_dir = os.path.join(self.root_dir, "c")
        init_dir(c_dir)
        c30_path = os.path.join(c_dir, "30.txt")
        write_file("30.txt", c30_path)

        r_path = os.path.join(self.root_dir, "r.txt")
        write_file("r.txt", r_path)

        # test
        file_path_list = get_file_name_list_from_dir(
            self.root_dir)
        self.assertSetEqual(set(file_path_list), {
                            "r.txt", "10.txt", "11.txt", "20.txt", "21.txt", "30.txt"})


def main():
    pass


if __name__ == "__main__":
    main()
