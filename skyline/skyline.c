#include <stdlib.h>
#include <stdio.h>

/* Binary search tree node. */
struct Node {
    int value;
    struct Node *left;
    struct Node *right;
};

struct Node* new_node(int value) {
    struct Node *node = malloc(sizeof(struct Node));  
    node->left = NULL;
    node->right = NULL;
    node->value = value;
    return node;
}

void insert(struct Node **root, int value) {
    /* Find the leaf of the tree where this value should be inserted. */
    struct Node **current = root;
    while (*current != NULL) {
        if (value < (*current)->value) {
            current = &(*current)->left;
        } else {
            current = &(*current)->right;
        }
    }
    *current = new_node(value);
}

struct Node* search(struct Node **root, int value) {
    struct Node **current = root;
    int current_value;
    while (*current != NULL) {
        current_value = (*current)->value;
        if (value == current_value) {
            return *current;
        } else if (value < current_value) {
            current = &(*current)->left;
        } else {
            current = &(*current)->right;
        }
    }
    /* Not found. */
    return NULL;
}

int main(int argc, char **argv) {
    struct Node *root = NULL;

    insert(&root, 4);
    printf("4 == %d\n", root->value);

    insert(&root, 5);
    printf("5 == %d\n", root->right->value);

    insert(&root, 2);
    printf("2 == %d\n", root->left->value);

    insert(&root, 7);
    printf("7 == %d\n", root->right->right->value);

    if (search(&root, 4) == root) {
        printf("4 found\n");
    }
    if (search(&root, 5) == root->right) {
        printf("5 found\n");
    }
    if (search(&root, 2) == root->left) {
        printf("2 found\n");
    }
    if (search(&root, 7) == root->right->right) {
        printf("7 found\n");
    }

    return 0;
}
