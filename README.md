# FoodGo

FoodGo is the website that has recipe of various tasty dishes<br />
Stack : Backend in Django , Frontend  in BootStrap<br />
The **models** are Desgined in the following way:<br />
**User**        :   Contains common information about any person.<br />
**Recipe**      :   Contains the basic details of the Recipe.<br />
**Ingridents**  :   Contains the ingridents which may be common to different recipe and one recipe can have many Ingridents.<br />

The main **component Division** is as follows:<br />
**accounts**    :   This handles and manage the user accounts.<br />
**Recipe**      :   This app handles the most basic recipe functions like listView, DetailView, CreateView and EditView.<br />
**Ingrident**   :   This app handles the Ingridents which is many to many to field on Recipe.<br />
**Search**      :   This handles the searching feature of the FoodGo Website.<br />

