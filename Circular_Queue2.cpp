#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <queue>
#include <vector>

using namespace std;

namespace py = pybind11;

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
    }
    cq->Circular_Queue.push(element);
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

vector<int> check(CircularQueue *cq, bool *Empty) {
    vector<int> res;
    *Empty = false;
    if (isEmpty(cq)) {
        *Empty = true;
    }
    else {
        queue<int> qqq = cq->Circular_Queue;
        for (int i = 0; i < cq->Circular_Queue.size(); i++) {
            res.push_back(qqq.front());
            qqq.pop();
        }
    }
    return res;
}

void DeleteCircularQueue(CircularQueue *cq) {
    if (cq != nullptr) {
        delete cq;
    }
}

int SizeCircularQueue(CircularQueue *cq) {
    return static_cast<int>(cq->Circular_Queue.size());
}

pair<CircularQueue*, bool> Qcreate(int size) {
    bool error;
    CircularQueue* cq = CreateCircularQueue(size, &error);
    return {cq, error};
}

pair<int, bool> Qdequeue(CircularQueue* cq) {
    bool error;
    int val = Dequeue(cq, &error);
    return {val, error};
}

pair<vector<int>, bool> Qcheck(CircularQueue* cq) {
    bool empty;
    vector<int> qqq = check(cq, &empty);
    return {qqq, empty};
}

PYBIND11_MODULE(Circular_Queue2, m) {
    py::class_<CircularQueue>(m, "CircularQueue")
        .def("CreateCircularQueue", &Qcreate)
        .def("isEmpty", &isEmpty)
        .def("isFull", &isFull)
        .def("Enqueue", &Enqueue)
        .def("Dequeue", &Qdequeue)
        .def("check", &Qcheck)
        .def("SizeCircularQueue", &SizeCircularQueue)
        .def("DeleteCircularQueue", &DeleteCircularQueue);
}
