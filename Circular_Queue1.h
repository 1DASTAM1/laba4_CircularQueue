#pragma once

extern "C" {
    typedef struct CircularQueue CircularQueue;
    __declspec(dllexport) CircularQueue* CreateCircularQueue(int size, bool *error);
    __declspec(dllexport) bool isEmpty(CircularQueue *cq);
    __declspec(dllexport) bool isFull(CircularQueue *cq);
    __declspec(dllexport) void Enqueue(CircularQueue *cq, int element);
    __declspec(dllexport) int Dequeue(CircularQueue *cq, bool *error);
    __declspec(dllexport) void check(CircularQueue *cq, bool *Empty, int *item);
    __declspec(dllexport) void DeleteCircularQueue(CircularQueue *cq);
    __declspec(dllexport) int SizeCircularQueue(CircularQueue *cq);
}
