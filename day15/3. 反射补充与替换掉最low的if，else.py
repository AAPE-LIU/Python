class Cloud(object):
    def upload(self):
        pass
    def download(self):
        pass

    def run(self):
        """
        让用户输入自己要干什么
        up|C:/XXX/XXX.zip  上传文件
        down|XXX.py  下载文件
        :return:
        """
        job = input('请输入您要执行的操作：')
        action = job.split('|')[0]
        # 最low的if，else方法
        if action == 'up':
            print('上传文件')
            self.upload()
        elif action == 'down':
            print('下载文件')
            self.download()
        else:
            print('输入无效，请重新输入')

        # 另外一种方法，创建字典的方法，这种方法挺好的
        dict = {'up':self.upload,'down':self.download}
        dict.get(action)()

        # 最后一种方法就是反射
        motivate = getattr(self,action)  # 但是这种方法要求用户输入的部分操作与函数名必须一致
        motivate()