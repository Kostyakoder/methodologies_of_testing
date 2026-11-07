from behave import given, when, then
from blog_program import BlogPlatform

@given('я на странице создания поста')
def step_impl(context):
    context.blog = BlogPlatform()

@given('пост "{title}" существует')
def step_impl(context, title):
    context.blog = BlogPlatform()
    context.post = context.blog.create_post('author', title, "Содержание")

@when('я ввожу заголовок "{title}" и содержание "{content}"')
def step_impl(context, title, content):
    context.title = title
    context.content = content

@when('нажимаю кнопку "Опубликовать"')
def step_impl(context):
    context.post = context.blog.create_post('author', context.title, context.content)

@then('пост "{title}" появляется в списке постов')
def step_impl(context, title):
    posts = context.blog.posts
    assert any(p.title == title for p in posts), f"Пост '{title}' не найден"

@when('я редактирую заголовок на "{new_title}"')
def step_impl(context, new_title):
    context.new_title = new_title #

@when('сохраняю изменения')
def step_impl(context):
    context.blog.update_post(context.post.id, title=context.new_title)

@then('заголовок поста становится "{expected_title}"')
def step_impl(context, expected_title):
    updated = context.blog.get_post(context.post.id)
    assert updated.title == expected_title, f"Ожидался '{expected_title}', получен '{updated.title}'"

@when('я добавляю комментарий "{text}"')
def step_impl(context, text):
    context.comment = context.blog.add_comment(context.post.id, "user2", text)

@then('комментарий "{text}" отображается под постом')
def step_impl(context, text):
    comments = context.blog.get_comments(context.post.id)
    assert any(c.text == text for c in comments), f"Комментарий '{text}' не найден"