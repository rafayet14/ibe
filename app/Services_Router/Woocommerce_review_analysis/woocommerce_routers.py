from ... import  utils,oauth2,models
from fastapi import Response,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ...database import get_db
from typing import List
import requests
from . import woocommerce_schemas

router = APIRouter(
    prefix= "/Service-Woocommerce",
    tags=['Service-Woocommerce']
)


# WooCommerce API credentials
    # woocommerce_url = "https://woo-noisily-hopeful-philosopher.wpcomstaging.com///wp-json/wc/v3"
    # consumer_key = "ck_2baa6bce46ec0e0a6a5fc1fbe56850e98ab1266c"
    # consumer_secret = "cs_095292f40c9ec30a7da0485775c7cb13eb9424cc"


#define a route to get the store api info and connect to the store
@router.post("/review-analysis")
def get_store_reviews(user_credentials: woocommerce_schemas.UserCredentials,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    
    #if not subscribed to the service raise exception
    service = db.query(models.SubscribedServices)


    
    woocommerce_url = f"{user_credentials.woocommerce_url}///wp-json/wc/v3"
    consumer_key = user_credentials.consumer_key
    consumer_secret = user_credentials.consumer_secret

    



# Define a route to get store reviews
@router.post("/store-reviews",response_model=List[woocommerce_schemas.Review])
async def get_store_reviews(user_credentials: woocommerce_schemas.UserCredentials):
    # Make a GET request to the WooCommerce API to fetch reviews

    woocommerce_url = f"{user_credentials.woocommerce_url}///wp-json/wc/v3"
    consumer_key = user_credentials.consumer_key
    consumer_secret = user_credentials.consumer_secret

    response = requests.get(
        f"{woocommerce_url}/products/reviews",
        auth=(consumer_key, consumer_secret)
    )

    if response.status_code == 200:
        reviews = response.json()
        return reviews
    else:
        return {"error": "Failed to fetch reviews"}


@router.post("/product-reviews/{product_id}", response_model=List[woocommerce_schemas.Review])
async def get_product_reviews(product_id: int,user_credentials: woocommerce_schemas.UserCredentials):
    # Make a GET request to the WooCommerce API to fetch reviews for the specified product

    woocommerce_url = f"{user_credentials.woocommerce_url}///wp-json/wc/v3"
    consumer_key = user_credentials.consumer_key
    consumer_secret = user_credentials.consumer_secret

    response = requests.get(
        f"{woocommerce_url}/products/reviews",
        auth=(consumer_key, consumer_secret)
    )

    if response.status_code == 200:
        reviews = response.json()

        # Filter reviews for the specified product
        reviews = list(filter(lambda review: review["product_id"] == product_id, reviews))

        return reviews
    else:
        return {"error": "Failed to fetch reviews"}
