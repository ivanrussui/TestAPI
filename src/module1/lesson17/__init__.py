# class Configuration:
#
#     def __init__(self, app_name=None, connection_count=None):
#         self.app_name = app_name
#         self.connection_count = connection_count
#
#     def read_config(self, file):
#         f = open(file, 'r')
#         try:
#             f.readline(228)
#             f.readline(228)
#             name_containment = f.readline(228).split('=')
#             self.app_name = name_containment[1].replace('\n', '').replace(' ', '')
#             config_containment = f.readline(228).split('=')
#             self.connection_count = int(config_containment[1].replace(' ', ''))
#         finally:
#             f.close()
#
#
# config = Configuration()
# print(config.__dict__)
# config.read_config("text.txt")
# print(config.__dict__)

