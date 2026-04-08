Реализация циклической очереди на C++ с использованием динамической памяти(Circular_Queue1.cpp), также реализация используя стандартной библиотекой шаблонов STL(Circular_Queue2.cpp) и реализация на Python(Circular_Queue3.py).
Реализация GUI для взаимодействие с циклическая очередь на Python, с использованием tkinter(main.py).

Комманда в vs code для создания dll в Circular_Queue1.cpp (для MinGW gcc/cpp):
g++.exe -shared -static -static-libgcc -static-libstdc++ -o Circular_Queue1.dll Circular_Queue1.cpp

Комманда в vs code для создания pyd в setup.py:
py setup.py build_ext --inplace
