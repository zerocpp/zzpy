import re
import oss2

__OSS_URL_KEY = "OSS_URL"


class OssConfig:
    def __init__(self, url):
        result = re.search("^(oss://){0,1}([^/]+)/([^?]+)\?(.*)$", url)
        groups = result.groups()
        endpoint = f"https://{groups[1]}"
        assert endpoint
        bucket = groups[2]
        assert bucket
        param = dict([it.split('=')
                      for it in groups[3].split('&')])
        assert param
        access_key_id = param.get("key")
        assert access_key_id
        access_key_secret = param.get("secret")
        assert access_key_secret
        
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.bucket = bucket
        self.endpoint = endpoint


def oss_connect(url=None):
    if not url:
        from .zconfig import get_param
        url = get_param(__OSS_URL_KEY)
    assert url

    return AliOss(url)


class AliOss:
    def __init__(self, url):
        config = OssConfig(url)
        self.bucket = oss2.Bucket(
            oss2.Auth(config.access_key_id, config.access_key_secret), config.endpoint, config.bucket)

    def download(self, key, file_path):
        """下载文件"""
        return self.bucket.get_object_to_file(key, file_path)

    def upload(self, key, file_path, infrequent_access_flag=True):
        """上传文件，infrequent_access_flag低频标识"""
        import oss2
        headers = {
            'x-oss-storage-class': oss2.BUCKET_STORAGE_CLASS_IA} if infrequent_access_flag else None
        return self.bucket.put_object_from_file(key, file_path)

    def delete(self, prefix):
        key_list = [it.key for it in self.bucket.list_objects(
            prefix=prefix).object_list]
        if len(key_list) > 0:
            return self.bucket.batch_delete_objects(key_list=key_list)
        return None

    def exist(self, key):
        """判断文件是否已存在"""
        return self.bucket.object_exists(key)

    def not_exist(self, key):
        """判断文件是否不存在"""
        return not self.exist(key)

    def meta(self, key):
        """获取文件元信息"""
        return self.bucket.get_object_meta(key)
