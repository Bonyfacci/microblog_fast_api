import typer
import asyncio

from fastapi import FastAPI
# from z_app_fastapi.app.database import init_models
# from z_app_fastapi.app.routers import users

app = FastAPI()
cli = typer.Typer()


app.include_router(users.router)


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
