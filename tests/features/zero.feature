Feature: Gimme a truck
    I would like to demostrate
    How easy it is to find food trucks
    Near me by searching for locations, cuisine, or truck listings  

    Background: I am on the Dine-o-truck website

    Senerio: Look at trucks
        Given I am on the home page
        When I click on the Tdructionary 
        Then I see the list of trucks

    Senerio: Check out the neighborhood
        Given I am on the home page
        When I click on a neighborhood
        Then I see the trucks in that neighborhood

    Senerio: Find food genres
        Given I am on the home page
        When I click on a food genre
        Then I will see trucks with that kind of food

    Senerio: See specific food trucks
        Given I am on the truck page
        When I click on a food truck
        Then I will see that trucks info

    Senerio: Get directions
        Given I am looking at a truck
        When I click on an address
        Then I will be directed to google maps