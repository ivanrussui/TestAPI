# class Task:
#     def __init__(self, id=None, title=None, description=None, done=None):
#         self.id = id
#         self.title = title
#         self.description = description
#         self.done = done
#
#     def __repr__(self):
#         return f"""
#         Task[{self.id}]
#          - title = {self.title}
#          - description = {self.description}
#          - done = {self.done}
#         """
#
#     def to_json(self):
#         json = {}
#         if self.title is not None:
#             json["title"] = self.title
#         if self.description is not None:
#             json["description"] = self.description
#         if self.done is not None:
#             json["done"] = self.done
#         return json
