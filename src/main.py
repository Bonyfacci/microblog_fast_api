import typer
import asyncio

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.database import init_models
from src.routers import users, posts, comments

app = FastAPI()
cli = typer.Typer()


app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)


# app.mount("/static", StaticFiles(directory="src/static/app"), name="static")


@cli.command()
def db_init_models():
    asyncio.run(init_models())
    print("DB Initialized")


# + Alembic

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == '__main__':
    cli()
