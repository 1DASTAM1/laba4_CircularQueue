#include "Circular_Queue.h"

struct Node {
   Node *next;
   int data;
};

struct CircularQueue {
    Node *front;
    Node *rear;
    int Size;
    int MaxSize;
};

CircularQueue* CreateCircularQueue(int size, bool *error) {
    *error = false;
    if (size <= 0) {
        *error = true;
        return nullptr;
    }
    CircularQueue *cq = new CircularQueue;
    cq->front = nullptr;
    cq->rear = nullptr;
    cq->MaxSize = size;
    cq->Size = 0;
    return cq;
}

bool isEmpty(CircularQueue *cq) {
    return (cq->Size == 0);
}

bool isFull(CircularQueue *cq) {
    return (cq->Size == cq->MaxSize);
}

void Enqueue(CircularQueue *cq, int element) {
    Node *newNode = new Node;
    newNode->data = element;
    if (isEmpty(cq)) {
        newNode->next = newNode;
        cq->front = newNode;
        cq->rear = newNode;
        cq->Size = 1;
    } else if(isFull(cq)) {
        if (cq->MaxSize == 1) {
            delete cq->front;
            newNode->next = newNode;
            cq->rear = newNode;
            cq->front = newNode;
        }
        else {
            Node* nextNode = cq->front->next;
            delete cq->front;
            cq->front = nextNode;
            newNode->next = cq->front;
            cq->rear->next = newNode;
            cq->rear = newNode;
        }
    } else {
        newNode->next = cq->front;
        cq->rear->next = newNode;
        cq->rear = newNode;
        cq->Size = cq->Size + 1;
    }
}

int Dequeue(CircularQueue *cq, bool *error) {
    *error = false;
    if (isEmpty(cq)) {
        *error = true;
        return -1;
    }
    else if (cq->Size == 1) {
        int element = cq->front->data;
        delete cq->front;
        cq->front = nullptr;
        cq->rear = nullptr;
        cq->Size = 0;
        return element;
    }
    else {
        Node* nextNode = cq->front->next;
        int element = cq->front->data;
        delete cq->front;
        cq->front = nextNode;
        cq->rear->next = nextNode;
        cq->Size = cq->Size - 1;
        return element;
    }
}

void check(CircularQueue *cq, bool *Empty, int *item) {
    *Empty = false;
    if (isEmpty(cq)) {
        *Empty = true;
    }
    else {
        Node* currentNode = cq->front;
        for (int i = 0; i < cq->Size; i++) {
            item[i] = currentNode->data;
            currentNode = currentNode->next;
        }
    }
}

void DeleteCircularQueue(CircularQueue *cq) {
    if (cq != nullptr) {
        bool error;
        while (cq->Size > 0) {
            Dequeue(cq, &error);
        }
        delete cq;
    }
}

int SizeCircularQueue(CircularQueue *cq) {
    return cq->Size;
}