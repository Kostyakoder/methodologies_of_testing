import unittest
from blog_program import BlogPlatform, Post, Comment


class TestBlogSDD(unittest.TestCase):
    def setUp(self):
        Post._id_counter = 1
        Comment._id_counter = 1
        self.blog = BlogPlatform()

    def test_create_post_example(self):
        post = self.blog.create_post("Иван", "Новости", "Сегодня вышел релиз")

        self.assertIsNotNone(post)
        self.assertEqual(post.author, "Иван")
        self.assertEqual(post.title, "Новости")
        self.assertEqual(post.content, "Сегодня вышел релиз")
        self.assertEqual(post.id, 1)

    def test_add_comment_success_example(self):
        post = self.blog.create_post("Автор", "Пост", "Текст")
        comment = self.blog.add_comment(post.id, "Анна", "Спасибо!")

        self.assertIsNotNone(comment)
        self.assertEqual(comment.text, "Спасибо!")
        self.assertEqual(comment.post_id, post.id)

    def test_add_comment_nonexistent_post_example(self):
        result = self.blog.add_comment(999, "Анна", "Текст")

        self.assertEqual(result, "Такого поста нет!")


if __name__ == '__main__':
    unittest.main()