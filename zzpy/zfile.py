DEFAULT_ROOT_DIR = "./output"


def remove_dir(dir_path):
    """删除文件夹"""
    import os
    import shutil
    if os.path.exists(dir_path):
        try:
            os.removedirs(dir_path)
        except Exception as ex:
            shutil.rmtree(dir_path, ignore_errors=True)


def create_dir(dir_path):
    """创建文件夹"""
    import os
    import shutil
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def init_dir(dir_path):
    """初始化（先删除再创建）文件夹"""
    remove_dir(dir_path)
    create_dir(dir_path)


def get_file_path_from_dir(dir_path):
    """返回文件夹中（第一个）文件的地址"""
    import os
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            return os.path.join(parent, filename)
    return None


def move_file_from_src_dir(dst_file_path, src_dir_path):
    """从src_dir中拿到（唯一）文件，移动到dst_dir，并重命名"""
    import shutil
    src_file_path = get_file_path_from_dir(src_dir_path)
    shutil.move(src_file_path, dst_file_path)


def get_file_line_count(file_path):
    """获取文件行数"""
    count = 0
    for _ in enumerate(open(file_path, 'rb')):
        count += 1
    return count


def get_file_name_list_from_dir(dir_path):
    """获取文件夹下所有文件名"""
    import os
    file_names = []
    for parent_dir, dirs, files in os.walk(dir_path):
        for file_name in files:
            file_names.append(file_name)
    return file_names


def get_file_path_list_from_dir(dir_path):
    """获取文件夹下所有文件路径"""
    import os
    file_pathes = []
    for parent_dir, dirs, files in os.walk(dir_path):
        for file_name in files:
            file_path = os.path.join(parent_dir, file_name)
            file_pathes.append(file_path)
    return file_pathes


def _read_file(file_path, encoding):
    """按编码读取文件"""
    f = None
    text = None
    try:
        f = open(file_path, encoding=encoding)
        text = f.read()
    except:
        pass
    finally:
        if f:
            f.close()
    return text


def read_file(file_path):
    """读取文件"""
    for encoding in ("utf8", "gbk"):
        text = _read_file(file_path, encoding=encoding)
        if text:
            return text
    return None


def write_file(content, file_path):
    with open(file_path, mode="w", encoding="utf8") as fw:
        fw.write(content)


def get_tmp_dir_path(root_dir=None):
    """临时目录"""
    if root_dir is None:
        root_dir = DEFAULT_ROOT_DIR
    import os
    return os.path.join(root_dir, "tmp")


def get_work_dir_path(root_dir=None):
    """工作目录"""
    if root_dir is None:
        root_dir = DEFAULT_ROOT_DIR
    import os
    return os.path.join(root_dir, "work")


def init_dirs(root_dir=None):
    '''初始化所有目录：临时目录、工作目录'''
    if root_dir is None:
        root_dir = DEFAULT_ROOT_DIR
    for dir_path_func in (get_tmp_dir_path, get_work_dir_path):
        dir_path = dir_path_func(root_dir=root_dir)
        init_dir(dir_path)


def read_jsonline(file_path):
    """从jsonline文件按行读取"""
    import jsonlines
    with open(file_path, encoding='utf8') as fr:
        yield from jsonlines.Reader(fr)


def read_jsonline_with_progressbar(file_path, title=None):
    """从jsonline文件按行读取，带进度条"""
    import jsonlines
    from zzpy import pb
    with open(file_path, encoding='utf8') as fr:
        yield from pb(jsonlines.Reader(fr), total=get_file_line_count(file_path), title=title)
