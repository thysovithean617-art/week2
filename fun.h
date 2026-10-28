#include <stdio.h>
//#include "./handleOrdering.h"

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