#include <stdio.h>
#include <string.h>
#include "functions.h"

struct MenuItem pizzas[3] = {
    {"Seafood Pizza", 6.00, 9.00, 12.00},
    {"Pork Pizza", 5.00, 8.00, 10.00},
    {"Beef Pizza", 7.00, 10.00, 12.00}
};
struct MenuItem burgers[3] = {
    {"Chicken Burger", 2.50, 3.70, 5.00},
    {"Pork Burger", 2.50, 3.70, 5.00},
    {"Beef Burger", 2.80, 4.00, 6.00}
};
struct MenuItem steaks[3] = {
    {"Chicken Steak", 7.00, 7.00, 7.00}, 
    {"Pork Steak", 9.00, 9.00, 9.00},
    {"Beef Steak", 10.00, 10.00, 10.00}
};
struct MenuItem hotDrinks[4] = {
    {"Espresso", 2.70, 3.45, 3.95},
    {"Americano", 2.20, 3.00, 3.65},
    {"Hot Chocolate", 2.50, 3.35, 3.85},
    {"Caffe Latte", 2.40, 3.35, 3.85}
};
struct MenuItem coldDrinks[4] = {
    {"Ice Caffe Latte", 2.65, 3.65, 4.00},
    {"Ice Americano", 2.40, 3.35, 3.75},
    {"Ice Mocha", 2.75, 3.75, 4.25},
    {"Ice Chocolate", 2.75, 3.65, 4.00}
};

int cart_pizzas[3][3] = {0};
int cart_burgers[3][3] = {0};
int cart_steaks[3][3] = {0};
int cart_hot[4][3] = {0};
int cart_cold[4][3] = {0};

void handleOrdering(struct MenuItem items[], int cart[][3], int maxItems) {
    int itemChoice, sizeChoice, qty;
    printf("\nSelect item number (or 0 to go back to category menu): ");
    scanf("%d", &itemChoice);
    
    if (itemChoice > 0 && itemChoice <= maxItems) {
        printf("Select Size (1 = S, 2 = M, 3 = L): ");
        scanf("%d", &sizeChoice);
        
        if (sizeChoice >= 1 && sizeChoice <= 3) {
            printf("Enter Quantity: ");
            scanf("%d", &qty);
            if (qty > 0) {
                cart[itemChoice - 1][sizeChoice - 1] += qty;
                printf("Successfully added to cart!\n");
            }
        } else {
            printf("Invalid Size.\n");
        }
    }
}
float printCartAndCalculateSubtotal(struct MenuItem items[], int cart[][3], int maxItems) {
    float subtotal = 0.0;
    char sizeLabels[3] = {'S', 'M', 'L'};
    
    for (int i = 0; i < maxItems; i++) {
        for (int s = 0; s < 3; s++) {
            if (cart[i][s] > 0) {
                float price = (s == 0) ? items[i].priceS : (s == 1) ? items[i].priceM : items[i].priceL;
                float cost = price * cart[i][s];
                subtotal += cost;
                printf("%-18s (%c)  |  $%-6.2f  |  QTY: %d\n", items[i].name, sizeLabels[s], price, cart[i][s]);
            }
        }
    }
    return subtotal;
}
void showMainMenu() {
    int choice;
    printf("\n=============================\n");
    printf("         (1) MENU            \n");
    printf("=============================\n");
    printf("1. Food\n2. Drinks\n3. Go directly to Checkout\n");
    printf("-----------------------------\n");
    printf("Enter choice (1-3): ");
    scanf("%d", &choice);
    
    if (choice == 1) showFoodCategories();
    else if (choice == 2) showDrinksMenu();
    else if (choice == 3) showYourOrder();
    else { printf("Invalid choice!\n"); showMainMenu(); }
}
void showFoodCategories() {
    int choice;
    printf("\n=============================\n");
    printf("         (2) FOOD            \n");
    printf("=============================\n");
    printf("1. Pizza\n2. Burger\n3. Steak\n4. Proceed to Drinks Menu\n5. Back to Main Menu\n");
    printf("-----------------------------\n");
    printf("Enter choice (1-5): ");
    scanf("%d", &choice);
    
    if (choice == 1) showPizzaMenu();
    else if (choice == 2) showBurgerMenu();
    else if (choice == 3) showSteakMenu();
    else if (choice == 4) showDrinksMenu();
    else showMainMenu();
}
void showPizzaMenu() {
    printf("\n=========================================\n");
    printf("            (2.1) PIZZA                  \n");
    printf("=========================================\n");
    for (int i = 0; i < 3; i++) {
        printf("%d. %-15s | S:$%.2f | M:$%.2f | L:$%.2f\n", 
               i + 1, pizzas[i].name, pizzas[i].priceS, pizzas[i].priceM, pizzas[i].priceL);
    }
    handleOrdering(pizzas, cart_pizzas, 3);
    showFoodCategories(); 
}
void showBurgerMenu() {
    printf("\n=========================================\n");
    printf("            (2.2) BURGER                 \n");
    printf("=========================================\n");
    for (int i = 0; i < 3; i++) {
        printf("%d. %-15s | S:$%.2f | M:$%.2f | L:$%.2f\n", 
               i + 1, burgers[i].name, burgers[i].priceS, burgers[i].priceM, burgers[i].priceL);
    }
    handleOrdering(burgers, cart_burgers, 3);
    showFoodCategories(); 
}
void showSteakMenu() {
    printf("\n=========================================\n");
    printf("            (2.3) STEAK                  \n");
    printf("=========================================\n");
    for (int i = 0; i < 3; i++) {
        printf("%d. %-15s | Flat Price: $%.2f\n", i + 1, steaks[i].name, steaks[i].priceS);
    }
    handleOrdering(steaks, cart_steaks, 3);
    showFoodCategories(); 
}
void showDrinksMenu() {
    int choice;
    printf("\n=============================\n");
    printf("         (3) DRINKS          \n");
    printf("=============================\n");
    printf("1. Hot\n2. Cold\n3. Back to Food Menu\n4. Move to Checkout\n");
    printf("-----------------------------\n");
    printf("Enter choice (1-4): ");
    scanf("%d", &choice);
    
    if (choice == 1) showHotDrinks();
    else if (choice == 2) showColdDrinks();
    else if (choice == 3) showFoodCategories();
    else showYourOrder();
}
void showHotDrinks() {
    printf("\n=========================================\n");
    printf("          (3.1) HOT DRINKS               \n");
    printf("=========================================\n");
    for (int i = 0; i < 4; i++) {
        printf("%d. %-12s | S:%.2f | M:%.2f | L:%.2f\n", 
               i + 1, hotDrinks[i].name, hotDrinks[i].priceS, hotDrinks[i].priceM, hotDrinks[i].priceL);
    }
    handleOrdering(hotDrinks, cart_hot, 4);
    showDrinksMenu(); 
}
void showColdDrinks() {
    printf("\n=========================================\n");
    printf("          (3.2) COLD DRINKS              \n");
    printf("=========================================\n");
    for (int i = 0; i < 4; i++) {
        printf("%d. %-15s | S:%.2f | M:%.2f | L:%.2f\n", 
               i + 1, coldDrinks[i].name, coldDrinks[i].priceS, coldDrinks[i].priceM, coldDrinks[i].priceL);
    }
    handleOrdering(coldDrinks, cart_cold, 4);
    showDrinksMenu(); 
}
void showYourOrder() {
    float grandTotal = 0.0;
    int confirmationChoice;
    
    printf("\n=========================================\n");
    printf("          (4) YOUR ORDER                 \n");
    printf("=========================================\n");
    
    grandTotal += printCartAndCalculateSubtotal(pizzas, cart_pizzas, 3);
    grandTotal += printCartAndCalculateSubtotal(burgers, cart_burgers, 3);
    grandTotal += printCartAndCalculateSubtotal(steaks, cart_steaks, 3);
    grandTotal += printCartAndCalculateSubtotal(hotDrinks, cart_hot, 4);
    grandTotal += printCartAndCalculateSubtotal(coldDrinks, cart_cold, 4);
    
    printf("-----------------------------------------\n");
    printf("TOTAL:                               $%.2f\n", grandTotal);
    printf("-----------------------------------------\n");
    printf("1. Confirm Order\n2. Go Back to Main Menu to Edit Order\n3. Cancel and Exit\n");
    printf("Enter selection: ");
    scanf("%d", &confirmationChoice);
    
    if (confirmationChoice == 1) showReceipt();
    else if (confirmationChoice == 2) showMainMenu();
    else printf("\nOrder cancelled successfully.\n");
}
void showReceipt() {
    float finalTotal = 0.0;
    printf("\n=========================================\n");
    printf("            (5) RECEIPT                  \n");
    printf("=========================================\n");
    printf("%-20s   %-8s   %-4s\n", "Name", "Price", "QTY");
    printf("-----------------------------------------\n");
    
    finalTotal += printCartAndCalculateSubtotal(pizzas, cart_pizzas, 3);
    finalTotal += printCartAndCalculateSubtotal(burgers, cart_burgers, 3);
    finalTotal += printCartAndCalculateSubtotal(steaks, cart_steaks, 3);
    finalTotal += printCartAndCalculateSubtotal(hotDrinks, cart_hot, 4);
    finalTotal += printCartAndCalculateSubtotal(coldDrinks, cart_cold, 4);
    
    printf("-----------------------------------------\n");
    printf("TOTAL AMOUNT PAID:                   $%.2f\n", finalTotal);
    printf("=========================================\n");
    printf("   Thank you! Have a great meal.         \n");
}