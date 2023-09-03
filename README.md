# Husam Obidat Repo that I clone it
`https://github.com/HusamObe/test-VV`

# All Step
`pip install -r requirements.txt`

```
Get all post: "https://new-backend-alpha.vercel.app/api/v1/posts/"
Put post: "https://new-backend-alpha.vercel.app/api/v1/posts/[id for post]"
Delete post: "https://new-backend-alpha.vercel.app/api/v1/posts/[id for post]"
Post create post: "https://new-backend-alpha.vercel.app/api/v1/posts/"
{
    "title": "test4",
    "description": "testing",
    "funding_goal": "5000.00",
    "allowed_donors": 6,
    "creator": 1,
    "category": 2
}
Get post depend on category: "https://new-backend-alpha.vercel.app/api/v1/posts/categories/[id of category]/"
Get post depend on user: "https://new-backend-alpha.vercel.app/api/v1/posts/user/[id of user]/"

Get comments for specefic post :"https://new-backend-alpha.vercel.app/api/v1/comments/[id for post]/"
Post create comment: "https://new-backend-alpha.vercel.app/api/v1/comments/"
{
    "body": "very nice 2",
    "project": 1,
    "user": 1
}
Put comment: "https://new-backend-alpha.vercel.app/api/v1/comments/detail/[id for comment]/"
Delete comment: "https://new-backend-alpha.vercel.app/api/v1/comments/detail/[id for comment]/""

Get reply comment depend on comment: "https://new-backend-alpha.vercel.app/api/v1/comments/child-comments/[id of parnt comment]/"
Post reply comment depend on comment: "https://new-backend-alpha.vercel.app/api/v1/comments/child-comments/[id of parnt comment]/"
Put replay: "https://new-backend-alpha.vercel.app/api/v1/comments/child-detail/[id for child comment]/"
Delete reply: "https://new-backend-alpha.vercel.app/api/v1/comments/child-detail/[id for child comment]"

Post create user: "https://new-backend-alpha.vercel.app/api/v1/accounts/"
{
    "username": "nermeen",
    "password": "12345678As$%",
    "profile_picture": null,
    "bio": "husam",
    "email": "husamobe1991@gmail.com"
}
Get user info: "https://new-backend-alpha.vercel.app/api/v1/accounts/[id for user]/"
Put user: "https://new-backend-alpha.vercel.app/api/v1/accounts/[id for user]/"
Delete user: "https://new-backend-alpha.vercel.app/api/v1/accounts/[id for user]/"


For the Donations

Post http://127.0.0.1:8000/api/v1/posts/project id/donate/
{
  "user": 1,
  "amount":10500.500
}

```
