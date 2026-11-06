from datetime import datetime
from typing import List, Optional


class Comment:
    _id_counter = 1
    def __init__(self, post_id: int, author: str, text: str):
        self.id = Comment._id_counter
        self.post_id = post_id
        self.author = author
        self.text = text
        self.created_at = datetime.now()
        self.updated_at = None
        Comment._id_counter += 1

class Post:
    _id_counter = 1
    def __init__(self, author: str, title: str, content: str):
        self.id = Post._id_counter
        self.author = author
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.comments: List[Comment] = []
        Post._id_counter += 1

class BlogPlatform:
    def __init__(self):
        self.posts: List[Post] = []
        self.comments: List[Comment] = []

    def create_post(self, author: str, title: str, content: str):
        post = Post(author, title, content)
        self.posts.append(post)
        return post

    def get_post(self, post_id: int):
        for post in self.posts:
            if post.id == post_id:
                return post
        return None

    def update_post(self, post_id: int, title: str = None, content: str = None):
        post = self.get_post(post_id)
        if not post:
            return None
        if title is not None:
            post.title = title
        if content is not None:
            post.content = content
        post.updated_at = datetime.now()
        return post

    def delete_post(self, post_id: int):
        post = self.get_post(post_id)
        if not post:
            return "Такого поста нет!"

        self.posts.remove(post)
        self.comments = [comment for comment in self.comments if comment.post_id != post_id]
        return self.posts

    def add_comment(self, post_id: int, author: str, text: str):
        post = self.get_post(post_id)
        if not post:
            return "Такого поста нет!"
        comment = Comment(post_id, author, text)
        post.comments.append(comment)
        self.comments.append(comment)
        return comment

    def get_comments(self, post_id: int):
        return [comment for comment in self.comments if comment.post_id == post_id]

    def delete_comment(self, comment_id: int):
        for comment in self.comments:
            if comment.id == comment_id:
                self.comments.remove(comment)
                post = self.get_post(comment.post_id)
                if post and comment in post.comments:
                    post.comments.remove(comment)
                return post.comments
        return "Такого сообщения нет!"