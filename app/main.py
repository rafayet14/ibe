import sys
sys.stdout.flush()

from fastapi import FastAPI,Response,status,HTTPException,Depends
from . import models,schemas,utils
from .database import engine,SessionLocal,get_db
from .routers import admin,user, auth,services,organization
from .Services_Router.Woocommerce_review_analysis import woocommerce_routers

from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(organization.router)
app.include_router(admin.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(services.router)
app.include_router(woocommerce_routers.router)



