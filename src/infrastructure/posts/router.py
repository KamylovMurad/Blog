from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import Response
from src.infrastructure.posts.exceptions import ObjectNotFoundException
from src.infrastructure.posts.repository import PostRepository
from src.infrastructure.posts.schemas import ShortSchemaPost, SchemaPost
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix='/posts',
    tags=['Posts'],
)

templates = Jinja2Templates(directory="src/templates")


@router.post('')
async def create_post(post: ShortSchemaPost) -> SchemaPost:
    new_post = await PostRepository.create(post=post)
    return new_post


@router.put('/{post_id}')
async def update_post(post_id: int, post: ShortSchemaPost) -> SchemaPost:
    try:
        updated_post = await PostRepository.update(post=post, post_id=post_id)
    except ObjectNotFoundException:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post


@router.delete('/{post_id}')
async def delete_post(post_id: int) -> Response:
    try:
        await PostRepository.delete(post_id=post_id)
    except ObjectNotFoundException:
        raise HTTPException(status_code=404, detail="Post not found")
    return Response(status_code=204)


@router.patch('/likes/{post_id}')
async def increase_likes(post_id: int) -> SchemaPost:
    try:
        post = await PostRepository.increase_likes(post_id=post_id)
    except ObjectNotFoundException:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.patch('/dislikes/{post_id}')
async def decrease_likes(post_id: int) -> SchemaPost:
    try:
        post = await PostRepository.decrease_likes(post_id=post_id)
    except ObjectNotFoundException:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.get("/blog")
async def blog(
        request: Request,
):
    posts = await PostRepository.get_posts()
    return templates.TemplateResponse(
        name='blog.html',
        context={
            'request': request,
            'posts': posts
        }
    )

