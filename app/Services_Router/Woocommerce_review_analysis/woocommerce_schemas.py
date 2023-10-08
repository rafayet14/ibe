from pydantic import BaseModel,EmailStr,HttpUrl
from datetime import datetime


class Review(BaseModel):
    id: int
    product_id: int
    product_name: str
    product_permalink: HttpUrl
    reviewer: str
    reviewer_email: EmailStr
    review: str
    rating: int
    date_created: datetime


class UserCredentials(BaseModel):
    woocommerce_url : HttpUrl
    consumer_key :str
    consumer_secret :str

