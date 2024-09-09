#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Node{
    struct Node* left;
    struct Node* right;
    int data;
}Node;
Node* newNode(int data){
    Node* node=(Node*)malloc(sizeof(Node));
    node->left=node->right=NULL;
    node->data=data;
    return node;
}

typedef struct Queue {
    Node** nodes;  // Array of pointers to nodes
    int front, rear, size;
    unsigned capacity;
} Queue;

// Function to create a queue of given capacity
Queue* createQueue(unsigned capacity) {
    Queue* queue = (Queue*)malloc(sizeof(Queue));
    queue->capacity = capacity;
    queue->front = queue->size = 0;
    queue->rear = capacity - 1; 
    queue->nodes = (Node**)malloc(queue->capacity * sizeof(Node*));
    return queue;
}

int isFull(Queue* queue) {
    return (queue->size == queue->capacity);
}

int isEmpty(Queue* queue) {
    return (queue->size == 0);
}

void enqueue(Queue* queue, Node* item) {
    if (isFull(queue))
        return;
    queue->rear = (queue->rear + 1) % queue->capacity;
    queue->nodes[queue->rear] = item;
    queue->size = queue->size + 1;
}

Node* dequeue(Queue* queue) {
    if (isEmpty(queue))
        return NULL;
    Node* item = queue->nodes[queue->front];
    queue->front = (queue->front + 1) % queue->capacity;
    queue->size = queue->size - 1;
    return item;
}

void levelOrder(Node* root) {
    if (root == NULL)
        return;
    
    Queue* queue = createQueue(100);  
    enqueue(queue, root);
    
    while (!isEmpty(queue)) {
        Node* current = dequeue(queue);
        printf("%d ", current->data);
        
        if (current->left != NULL)
            enqueue(queue, current->left);
        
        if (current->right != NULL)
            enqueue(queue, current->right);
    }
    
    free(queue->nodes);
    free(queue);
}


Node* insert(Node* root,int data){
    if(root==NULL)
        return newNode(data);
    else{
        Node* cur;
        if(data<=root->data){
            cur=insert(root->left,data);
            root->left=cur;                
        }
        else{
            cur=insert(root->right,data);
            root->right=cur;
        }
        
    }
    return root;
}
int main(){
    Node* root=NULL;
    int T,data;
    scanf("%d",&T);
    while(T-->0){
        scanf("%d",&data);
        root=insert(root,data);
    }
    levelOrder(root);
    return 0;
    
}
