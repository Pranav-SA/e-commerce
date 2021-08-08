# e-commerce

This repository contains sample API for performing checkout action for e-commerce app.

### Folder structure
__core__ contains the function file 'checkout.py' used for calculating total price of the watches in the input list
__data__ contains the watch catalogue as a json file
__test__ contains unit tests for 'checkout.py'
__Dockerfile__ for creating an image and running the app
__app.py__ file containing the URL route for checkout action
__requirements.txt__ file containing list of libraries used
__ecommerce test.postman_collection.json__ Postman collection with sample /checkout API calls for testing

### How to run and test the APIs?
1. Install Docker Desktop
2. Clone this repo 
3. Open a powershell/ terminal window and navigate to the 'e-commerce' directory
4. Run the following command to build the docker image. The name of the image created will be 'ecommercetest'

__docker build . -t ecommercetest__

5. After building the image, run the following command to start the server and use the /checkout api

__docker run -it -p 8080:8080 ecommercetest__

The /checkout api will now be available at http://127.0.0.1:8080/checkout

6. For testing the API, install POSTMAN app and import the ecommerce test.postman_collection.json. This contains sample API calls for testing.
