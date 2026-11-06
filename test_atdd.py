import unittest
from blog_program import BlogPlatform

class TestATDD(unittest.TestCase):
    def setUp(self):
        self.blog = BlogPlatform()

    def test_publish_post(self):
        post = self.blog.create_post('user1', 'Первый пост платформы', 'Привет, мир!')
        self.assertIsNotNone(post)
        self.assertIn(post, self.blog.posts)
        self.assertEqual(post.title, "Первый пост платформы")

    def test_edit_post(self):
        post = self.blog.create_post('user1', 'Первый пост платформы', 'Привет, мир!')
        updated_post = self.blog.update_post(post.id, title = "Обновленный пост")

        self.assertIsNotNone(updated_post)
        self.assertEqual(updated_post.title, "Обновленный пост")
        self.assertIsNotNone(updated_post.updated_at)

    def test_add_comment(self):
        post = self.blog.create_post('user1', 'Первый пост платформы', 'Привет, мир!')
        comment = self.blog.add_comment(post.id, 'user2', 'Автор, молодец!')

        self.assertIsNotNone(comment)
        comments = self.blog.get_comments(post.id)
        self.assertIn(comment, comments)
        self.assertEqual(comments[0].text, 'Автор, молодец!')

if __name__ == '__main__':
    unittest.main()