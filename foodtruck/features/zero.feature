Feature: Gimme a truck
    I would like to demostrate
    How easy it is to find food trucks
    Near me by searching for locations, cuisine, or just seeing the truck listings

    Senerio: Look at trucks
        Given that I am on Home
        When I click on the link The Trucktionary 
        Then I see the list of trucks

    Senerio: Check out the neighborhood
        Given that I am on Home
        When I click on the link Search by Neighborhood
        Then I see the trucks in that neighborhood

    Senerio: Find food genres
        Given that I am on Home
        When I click on the link Search by Cuisine
        Then I will see trucks with that kind of food

    Senerio: See specific food trucks
        Given that I am on The Trucktionary
        When I click on the link The Yeast Whisper
        Then I will see that trucks info
