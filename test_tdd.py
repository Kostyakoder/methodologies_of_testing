import unittest
from blog_program import Comment, Post, BlogPlatform


class TestTDD(unittest.TestCase):
    def setUp(self):
        self.blog = BlogPlatform()
        self.post = self.blog.create_post(
            "Костя",
            "Первый пост",
            "Содержание первого поста"
        )

    def test_create_post(self):
        self.assertIsNotNone(self.post)
        self.assertEqual(self.post.title, "Первый пост")
        self.assertEqual(self.post.content, "Содержание первого поста")
        self.assertEqual(self.post.author, "Костя")
        self.assertIn(self.post, self.blog.posts)

    def test_get_post(self):
        post = self.blog.get_post(self.post.id)
        self.assertEqual(post, self.post)

    def test_update_post(self):
        updated = self.blog.update_post(self.post.id, title = "Новый заголовок")
        self.assertTrue(updated)
        self.assertEqual(self.post.title, "Новый заголовок")
        self.assertNotEqual(self.post.created_at, self.post.updated_at)

    def test_delete_post(self):
        deleted = self.blog.delete_post(self.post.id)
        self.assertFalse(deleted)
        self.assertIsNone(self.blog.get_post(self.post.id))

    def test_add_comment(self):
        comment = self.blog.add_comment(self.post.id, "Ростик", "Комментарий от Ростика")
        self.assertIsNotNone(comment)
        self.assertEqual(comment.text, "Комментарий от Ростика")
        self.assertIn(comment, self.post.comments)

    def test_delete_comment(self):
        comment = self.blog.add_comment(self.post.id, "Артем", "Комментарий от Артема")
        deleted = self.blog.delete_comment(comment.id)
        self.assertFalse(deleted)
        self.assertNotIn(comment, self.post.comments)

if __name__ == '__main__':
    unittest.main()