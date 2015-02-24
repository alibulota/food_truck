
Feature: Get food
    In order to get food
    As users
    We will be able to look at nearby food trucks

    Senerio: List of food trucks
        Given I am on the home page
        When I click on the Trucks page
        Then I will see a list of trucks

    Senerio: List of food genre trucks
        Given I am on the home page
        When I click on the Search by Cuisine and the American tab
        Then I will see a list of trucks 
    
    Senerio: Direct to Maps Apps
        Given I am on the Truck page
        When I click on an address
        Then I will be taken a maps app