# ingenium_hackathon

This project is a backend api implementation for performing anaysis of inventory and trends. Given the necessary data like quantity, replenishing quantity and depletion rate, the backend api will provide the user with the most relevant analytics needed to optimize their inventory.

Currently, the visualizations like efficiency of stock replenishment, sales growth (revenue and profit) and categorical product analysis is being provided. This idea will then be extended to give user recommendations on how to optimize their inventory by transferring certain goods from one inventory to other.


## Setup

1. Installing dependencies

        pip install -r requirements.txt

2. Make and apply migrations
    
        python manage.py makemigrations
        python manage.py migrate

3. Run the Django server
    
        python manage.py runserver

4. The server will be running on http://localhost:8000/




