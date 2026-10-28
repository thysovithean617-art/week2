#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include "structures.h"

extern struct MenuItem pizzas[3];
extern struct MenuItem burgers[3];
extern struct MenuItem steaks[3];
extern struct MenuItem hotDrinks[4];
extern struct MenuItem coldDrinks[4];
extern int cart_pizzas[3][3];
extern int cart_burgers[3][3];
extern int cart_steaks[3][3];
extern int cart_hot[4][3];
extern int cart_cold[4][3];

void showMainMenu();         
void showFoodCategories();   
void showPizzaMenu();        
void showBurgerMenu();       
void showSteakMenu();        
void showDrinksMenu();       
void showHotDrinks();        
void showColdDrinks();       
void showYourOrder();        
void showReceipt();          
void handleOrdering(struct MenuItem items[], int cart[][3], int maxItems);
float printCartAndCalculateSubtotal(struct MenuItem items[], int cart[][3], int maxItems);

#endif