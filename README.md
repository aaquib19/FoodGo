# FoodGo

FoodGo is the website that has recipe of various tasty dishes
Stack : Backend in Django , Frontend  in BootStrap
The **models** are Desgined in the following way:
**User**        :   Contains common information about any person.
**Recipe**      :   Contains the basic details of the Recipe
**Ingridents**  :   Contains the ingridents which may be common to different recipe and one recipe can have many Ingridents

The main **component Division** is as follows:
**accounts**    :   This handles and manage the user accounts
**Recipe**      :   This app handles the most basic recipe functions like listView, DetailView, CreateView and EditView
**Ingrident**   :   This app handles the Ingridents which is many to many to field on Recipe
**Search**      :   This handles the searching feature of the FoodGo Website


