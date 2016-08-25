#!/usr/bin/env python3

from modules.base_module import BaseSaltModule
import urllib.request
import os
import shutil

class FileModule(BaseSaltModule):


    def func__managed(self,*args,**kwargs):
        module_data = kwargs.get('module_data')
        target_filepath = module_data['section']
        if self.has_source: 
        # 需要把这个文件 copy成section 指定的文件
            if self.source_file is not None:    
                # 已经下载
                shutil.copyfile(self.souce_file,target_filepath)



    def func__directory(self,*args,**kwargs):
        module_data = kwargs.get('module_data')



    def func__user(self,*args,**kwargs):
        pass

    def func__group(self,*args,**kwargs):
        pass

    def func__mode(self,*args,**kwargs):
        pass




    def download_http(self,file_path):
        '''
        拼接下载地址
        '''
        http_server = self.task_obj.main_obj.configs.FILE_SERVER['http']
        url_arg = "file_path=%s" % file_path
        filename = file_path.split('/')[-1]
        url = "http://%s%s?%s" %(http_server,
                                 self.task_obj.main_obj.configs.FILE_SERVER_BASE_PATH,
                                 url_arg)

        f = urllib.request.urlopen(url)
        data = f.read()
        #文件保存路径
        file_save_path = '%s/%s' %(self.task_obj.main_obj.configs.FILE_STORE_PATH,
                                   self.task_obj.task_body['id'])

        if not os.path.isdir(file_save_path):
            #判断文件目录是否存在，否则创建
            os.mkdir(file_save_path)

        with open("%s/%s" %(file_save_path,filename),"wb") as code:
            #写文件
            code.write(data)

        return "%s/%s" %(file_save_path,filename)
        #返回文件保存路径和文件名

    def download_salt(self,file_path):
        print('donlowding from slat:', file_path)


    def func__source(self,*args,**kwargs):
        fileurl = args[0]
        download_type,file_path = fileurl.split(":")
        #下载类型和路径进行切割
        file_download_func = getattr(self,'download_%s' % download_type)
        self.source_file = file_download_func(file_path)
        self.has_source = True

    def func__sources(self,*args,**kwargs):
        for file_source in args[0]:
            self.func__source(file_source)


    def func__recurse(self,*args,**kwargs):
        pass





