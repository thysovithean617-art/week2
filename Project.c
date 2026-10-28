#include <stdio.h>
#include <string.h>

// Structure to manage food and drink resources
struct Item {
    char name[30];
    float price;
    int sold; // 0 = Available, 1 = Out of Stock / Sold Out
};

// Global arrays mimicking the data structure from your wireframes
struct Item foods[2] = {
    {"Burger", 5.99, 0},
    {"Pizza", 8.50, 0}
};

struct Item drinks[2] = {
    {"Cola", 1.99, 0},
    {"Water", 1.00, 0}
};

// Global variables to track the current user's order quantities
int ordered_food_qty[2] = {0, 0};
int ordered_drink_qty[2] = {0, 0};

// Declaring the 4 required functions
void displayMainMenu();
void selectFood();
void selectDrinks();
void displayOrderSummary();

int main() {
    printf("--- WELCOME TO THE ORDERING SYSTEM ---\n");
    // Start the system flow from Screen 1
    displayMainMenu();
    return 0;
}

// Function 1: Corresponds to Screen (1) "Menu"
void displayMainMenu() {
    int choice;
    printf("\n=== (1) MAIN MENU ===\n");
    printf("1. Food\n");
    printf("2. Drinks\n");
    printf("Enter your choice (1 or 2): ");
    scanf("%d", &choice);

    if (choice == 1) {
        selectFood(); // Move to Screen (2)_1
    } else if (choice == 2) {
        selectDrinks(); // Skip directly to Screen (2)_2
    } else {
        printf("Invalid choice. Try again.\n");
        displayMainMenu();
    }
}

// Function 2: Corresponds to Screen (2)_1 "Food"
void selectFood() {
    int choice, qty;
    printf("\n=== (2)_1 FOOD MENU ===\n");
    
    // Display items dynamically from the resource pool
    for (int i = 0; i < 2; i++) {
        printf("%d. Name: %s | Price: $%.2f | Status: %s\n", 
               i + 1, foods[i].name, foods[i].price, 
               (foods[i].sold == 1) ? "Sold Out" : "Available");
    }
    
    printf("Select a food item number (or 0 to skip to drinks): ");
    scanf("%d", &choice);
    
    if (choice > 0 && choice <= 2) {
        if (foods[choice - 1].sold == 1) {
            printf("Sorry, this item is sold out!\n");
        } else {
            printf("Enter quantity: ");
            scanf("%d", &qty);
            ordered_food_qty[choice - 1] = qty;
        }
    }
    
    // Arrow pointing from Screen 2_1 to 2_2 in your diagram
    selectDrinks(); 
}

// Function 3: Corresponds to Screen (2)_2 "Drinks"
void selectDrinks() {
    int choice, qty;
    printf("\n=== (2)_2 DRINKS MENU ===\n");
    
    for (int i = 0; i < 2; i++) {
        printf("%d. Name: %s | Price: $%.2f | Status: %s\n", 
               i + 1, drinks[i].name, drinks[i].price, 
               (drinks[i].sold == 1) ? "Sold Out" : "Available");
    }
    
    printf("Select a drink item number (or 0 to proceed to checkout): ");
    scanf("%d", &choice);
    
    if (choice > 0 && choice <= 2) {
        if (drinks[choice - 1].sold == 1) {
            printf("Sorry, this item is sold out!\n");
        } else {
            printf("Enter quantity: ");
            scanf("%d", &qty);
            ordered_drink_qty[choice - 1] = qty;
        }
    }
    
    // Arrow pointing from Screen 2_2 to Screen 3
    displayOrderSummary();
}

// Function 4: Corresponds to Screen (3) "Your Order"
void displayOrderSummary() {
    float total = 0.0;
    int confirmation;
    
    printf("\n=== (3) YOUR ORDER ===\n");
    
    // Print ordered foods if quantity > 0
    for (int i = 0; i < 2; i++) {
        if (ordered_food_qty[i] > 0) {
            printf("Name: %s | Price: $%.2f | QTY: %d\n", 
                   foods[i].name, foods[i].price, ordered_food_qty[i]);
            total += foods[i].price * ordered_food_qty[i];
        }
    }
    
    // Print ordered drinks if quantity > 0
    for (int i = 0; i < 2; i++) {
        if (ordered_drink_qty[i] > 0) {
            printf("Name: %s | Price: $%.2f | QTY: %d\n", 
                   drinks[i].name, drinks[i].price, ordered_drink_qty[i]);
            total += drinks[i].price * ordered_drink_qty[i];
        }
    }
    
    // Total and Confirm blocks at the bottom of Screen 3
    printf("---------------------------\n");
    printf("Total: $%.2f\n", total);
    printf("---------------------------\n");
    printf("1. Confirm Order\n");
    printf("2. Cancel\n");
    printf("Press 1 to Confirm or 2 to Exit: ");
    scanf("%d", &confirmation);
    
    if (confirmation == 1) {
        printf("\nOrder Confirmed! Thank you for your purchase.\n");
    } else {
        printf("\nOrder Cancelled.\n");
    }
}