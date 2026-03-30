#include <queue>
#include "Circular_Queue.h"

using namespace std;

struct CircularQueue {
    queue<int> Circular_Queue;
    int MaxSize;
};

CircularQueue* CreateCircularQueue(int size, bool *error) {
    *error = false;
    if (size <= 0) {
        *error = true;
        return nullptr;
    }
    CircularQueue *cq = new CircularQueue;
    cq->MaxSize = size;
    return cq;
}

bool isEmpty(CircularQueue *cq) {
    return (cq->Circular_Queue.empty() == true);
}

bool isFull(CircularQueue *cq) {
    return (static_cast<int>(cq->Circular_Queue.size()) == cq->MaxSize);
}

void Enqueue(CircularQueue *cq, int element) {
    if(isFull(cq)) {
        cq->Circular_Queue.pop();
        cq->Circular_Queue.push(element);
    } else {
        cq->Circular_Queue.push(element);
    }
}

int Dequeue(CircularQueue *cq, bool *error) {
    *error = false;
    if (isEmpty(cq)) {
        *error = true;
        return -1;
    }
    int element = cq->Circular_Queue.front();
    cq->Circular_Queue.pop();
    return element;
}

void check(CircularQueue *cq, bool *Empty, int *item) {
    *Empty = false;
    if (isEmpty(cq)) {
        *Empty = true;
    }
    else {
        queue<int> qqq = cq->Circular_Queue;
        for (int i = 0; i < cq->Circular_Queue.size(); i++) {
            item[i] = qqq.front();
            qqq.pop();
        }
    }
}

void DeleteCircularQueue(CircularQueue *cq) {
    if (cq != nullptr) {
        delete cq;
    }
}

int SizeCircularQueue(CircularQueue *cq) {
    return static_cast<int>(cq->Circular_Queue.size());
}