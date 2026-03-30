from ctypes import *
from Circular_Queue3 import *
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

lib1 = r"./Circular_Queue1.dll"
lib2 = r"./Circular_Queue2.dll"

v1 = False
v2 = False
v3 = False
cq = None
cppLib = None
sizeQueue = 0
index = None

class Node(Structure):
        pass
Node._fields_ = [("next", POINTER(Node)), ("data", c_int)]

class CircularQueue(Structure):
    _fields_ = [("front", POINTER(Node)), ("rear", POINTER(Node)), ("Size", c_int), ("MaxSize", c_int)]

class libCPP:
    def __init__(self, lib): 
        self.lib = lib
        self.lib = CDLL(lib)
        self.lib.CreateCircularQueue.argtypes = [c_int, POINTER(c_bool)]
        self.lib.CreateCircularQueue.restype = POINTER(CircularQueue)
        self.lib.isEmpty.argtypes = [POINTER(CircularQueue)]
        self.lib.isEmpty.restype = c_bool
        self.lib.isFull.argtypes = [POINTER(CircularQueue)]
        self.lib.isFull.restype = c_bool
        self.lib.Enqueue.argtypes = [POINTER(CircularQueue), c_int]
        self.lib.Enqueue.restype = None
        self.lib.Dequeue.argtypes = [POINTER(CircularQueue), POINTER(c_bool)]
        self.lib.Dequeue.restype = c_int
        self.lib.check.argtypes = [POINTER(CircularQueue), POINTER(c_bool), POINTER(c_int)]
        self.lib.check.restype = None
        self.lib.DeleteCircularQueue.argtypes = [POINTER(CircularQueue)]
        self.lib.DeleteCircularQueue.restype = None
        self.lib.SizeCircularQueue.argtypes = [POINTER(CircularQueue)]
        self.lib.SizeCircularQueue.restype = c_int

def CreateCircularQueue(size:int):
    cq = None
    error = False
    if v3:
        cq, error = CreateCircularQueuePY(size)
    if v1 or v2:
        error = c_bool(False)
        cq = cppLib.lib.CreateCircularQueue(size, byref(error))
    return cq, error

def Enqueue(cq, element:int):
    if v3:
        EnqueuePY(cq, element)
    if v1 or v2:
        cppLib.lib.Enqueue(cq, element)

def isEmpty(cq):
    if v3:
        return is_emptyPY(cq)
    if v1 or v2:
        return cppLib.lib.isEmpty(cq)

def isFull(cq):
    if v3:
        return is_fullPY(cq)
    if v1 or v2:
        return cppLib.lib.isFull(cq)

def Dequeue(cq):
    if v3:
        el, error = DequeuePY(cq)
    if v1 or v2:
        error = c_bool(False)
        el = cppLib.lib.Dequeue(cq, byref(error))
    return el, error

def SizeCircularQueue(cq):
    if v3:
        return SizeCircularQueuePY(cq)
    if v1 or v2:
        return cppLib.lib.SizeCircularQueue(cq)

def checkButton():
    if v3:
        a, empty = checkPY(cq)
    if v1 or v2:
        empty = c_bool(False)
        a = (c_int * SizeCircularQueue(cq))()
        cppLib.lib.check(cq, byref(empty), a)
    if empty:
        output.insert(tk.END, "Очередь пуста.\n")
        output.see(tk.END)
    else:
        output.insert(tk.END, "Элементы очереди: " + str(list(a)) + "\n")
        output.see(tk.END)

def DeleteCircularQueue(cq):
    if v3:
        DeleteCircularQueuePY(cq)
    if v1 or v2:
        cppLib.lib.DeleteCircularQueue(cq)

def min_ind(cq):
    size = SizeCircularQueue(cq)
    min_el, error = Dequeue(cq)
    Enqueue(cq, min_el)
    min_i = 0
    for i in range(1, size):
        el1, error = Dequeue(cq)
        Enqueue(cq, el1)
        if el1 < min_el:
            min_el = el1
            min_i = i
    return min_i

def max_ind(cq):
    size = SizeCircularQueue(cq)
    max_el, error = Dequeue(cq)
    Enqueue(cq, max_el)
    max_i = 0
    for i in range(1, size):
        el1, error = Dequeue(cq)
        Enqueue(cq, el1)
        if el1 > max_el:
            max_el = el1
            max_i = i
    return max_i

def last(cq, ind:int, MaxSize:int):
    size = SizeCircularQueue(cq)
    cq1, error = CreateCircularQueue(MaxSize)
    for i in range(size):
        if i == ind:
            n, error = Dequeue(cq)
        else:
            el, error = Dequeue(cq)
            Enqueue(cq1, el)
    Enqueue(cq1, n)
    DeleteCircularQueue(cq)
    return cq1

def first(cq, ind:int, MaxSize:int):
    size = SizeCircularQueue(cq)
    cq1, error = CreateCircularQueue(MaxSize)
    for i in range(size):
        if i == ind:
            n, error = Dequeue(cq)
        else:
            el, error = Dequeue(cq)
            Enqueue(cq1, el)
    Enqueue(cq1, n)
    for i in range(size - 1):
        el, error = Dequeue(cq1)
        Enqueue(cq1, el)
    DeleteCircularQueue(cq)
    return cq1

def ser(cq, ind:int, MaxSize:int):
    size = SizeCircularQueue(cq)
    cq1, error = CreateCircularQueue(MaxSize)
    cq2, error = CreateCircularQueue(MaxSize)
    for i in range(size):
        if i == ind:
            n, error = Dequeue(cq)
        else:
            el, error = Dequeue(cq)
            Enqueue(cq1, el)
    for i in range(size // 2):
        el, error = Dequeue(cq1)
        Enqueue(cq2, el)
    Enqueue(cq2, n)
    for i in range(size // 2):
        el, error = Dequeue(cq1)
        Enqueue(cq2, el)
    DeleteCircularQueue(cq)
    DeleteCircularQueue(cq1)
    return cq2

def SetLib():
    global v1, v2, v3, cppLib
    lib = lib_choice.get()
    if lib == "C++ динамическая":
        v1 = True
        v2 = False
        v3 = False 
        cppLib = libCPP(lib1)
    elif lib == "C++ STL":
        v1 = False
        v2 = True
        v3 = False
        cppLib = libCPP(lib2)
    elif lib == "Python":
        v1 = False
        v2 = False
        v3 = True
        cppLib = None
    output.insert(tk.END, "Выбрвна: " + lib + "\n")
    output.see(tk.END)
    lib_frame.place_forget()
    len_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

def BackLib():
    global v1, v2, v3
    v1 = False
    v2 = False
    v3 = False
    lib_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    len_frame.place_forget()

def Create():
    global cq, sizeQueue
    try:
        try:
            sizeQueue = int(entry1.get())
        except:
            raise ValueError("Не удалось преобразовать введенное значение в число")
        if sizeQueue < 0:
            raise ValueError("Значение не может быть меньше 0")
        entry1.delete(0, tk.END)
        len_frame.place_forget()
        main_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        cq, error = CreateCircularQueue(sizeQueue)
    except Exception as e:
        output.insert(tk.END, f"Ошибка, неверно указанный размер (Подробнее: {e}).\n")
        output.see(tk.END)
        entry1.delete(0, tk.END)

def EnqueueButton():
    if entry2.get() == "":
        return
    el = int(entry2.get())
    entry2.delete(0, tk.END)
    Enqueue(cq, el)
    output.insert(tk.END, "Добвавлен элемент: " + str(el) + "\n")
    output.see(tk.END)

def DequeueButton():
    el, error = Dequeue(cq)
    if error:
        output.insert(tk.END, "Очередь пуста из неё ничего нельзя удалить.\n")
        output.see(tk.END)
        return
    output.insert(tk.END, "Удалён элемент: " + str(el) + "\n")
    output.see(tk.END)
    
def DeleteCircularQueueButton():
    global sizeQueue
    DeleteCircularQueue(cq)
    main_frame.place_forget()
    len_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    sizeQueue = 0

def SizeButton():
    output.insert(tk.END, "Текущий размер оереди: " + str(SizeCircularQueue(cq)) + "\n")
    output.see(tk.END)

def dopzad():
    if (SizeCircularQueue(cq) <= 0):
        output.insert(tk.END, "Очередь пуста\n")
        output.see(tk.END)
    else:
        main_frame.place_forget()
        dop1_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

def MinButton():
    global index
    index = min_ind(cq)
    dop1_frame.place_forget()
    dop2_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

def MaxButton():
    global index
    index = max_ind(cq)
    dop1_frame.place_forget()
    dop2_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

def firstButton():
    global cq, index
    cq = first(cq, index, sizeQueue)
    index = None
    dop2_frame.place_forget()
    main_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

def serButton():
    global cq, index
    if SizeCircularQueue(cq) % 2 == 1:
        cq = ser(cq, index, sizeQueue)
        index = None
        dop2_frame.place_forget()
        main_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    else:
        output.insert(tk.END, "Колличество элементов чётное, середины нет.\n")
        output.see(tk.END)

def lastButton():
    global cq, index
    cq = last(cq, index, sizeQueue)
    index = None
    dop2_frame.place_forget()
    main_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

root = tk.Tk()
root.geometry("800x600")
root.title("Циклическая очередь")

lib_frame = tk.Frame(root, relief=tk.RAISED, bd=2)
lib_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
tk.Label(lib_frame, text="Выберите библиотеку:" ).pack(side=tk.LEFT, padx=0, pady=50)
tk.Button(lib_frame, text = "Выбрать", command = SetLib).place(relx=0.5, rely=0.8, anchor=tk.CENTER)
lib_choice = tk.StringVar()
lib_combo = ttk.Combobox(lib_frame, textvariable=lib_choice, values=["C++ динамическая", "C++ STL", "Python"], state="readonly", width=20)
lib_combo.pack(side=tk.LEFT, padx=5, pady=5)
lib_combo.current(0)

output = ScrolledText(root, width=90, height=10, font=("Courier New", 9))
output.pack(pady=150, padx=150, fill=tk.BOTH, expand=True)
output.place(x=100, y=420)

len_frame = tk.Frame(root, width=200, height=150, bd=2, relief=tk.RAISED)
entry1 = tk.Entry(len_frame)
entry1.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
tk.Label(len_frame, text="Введите длину:" ).place(relx=0.5, rely=0.1, anchor=tk.CENTER)
tk.Button(len_frame, text = "Выбрать длину", command = Create).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
tk.Button(len_frame, text = "Назад", command = BackLib).place(relx=0.5, rely=0.9, anchor=tk.CENTER)

main_frame = tk.Frame(root, width=400, height=300, bd=2, relief=tk.RAISED)
entry2 = tk.Entry(main_frame)
entry2.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
tk.Button(main_frame, text = "Добавить элемент", command = EnqueueButton).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
tk.Button(main_frame, text = "Удалить элемент", command = DequeueButton).place(relx=0.5, rely=0.4, anchor=tk.CENTER)
tk.Button(main_frame, text = "Размер очереди", command = SizeButton).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
tk.Button(main_frame, text = "Посмотреть элементы очереди", command = checkButton).place(relx=0.5, rely=0.6, anchor=tk.CENTER)
tk.Button(main_frame, text = "Дополнительное задание", command = dopzad).place(relx=0.5, rely=0.7, anchor=tk.CENTER)
tk.Button(main_frame, text = "Удалить очередь", command = DeleteCircularQueueButton).place(relx=0.5, rely=0.9, anchor=tk.CENTER)

dop1_frame = tk.Frame(root, width=150, height=100, bd=2, relief=tk.RAISED)
tk.Button(dop1_frame, text = "Минимальный", command = MinButton).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
tk.Button(dop1_frame, text = "Максимальный", command = MaxButton).place(relx=0.5, rely=0.6, anchor=tk.CENTER)

dop2_frame = tk.Frame(root, width=150, height=150, bd=2, relief=tk.RAISED)
tk.Button(dop2_frame, text = "Начало", command = firstButton).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
tk.Button(dop2_frame, text = "Середина", command = serButton).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
tk.Button(dop2_frame, text = "Конец", command = lastButton).place(relx=0.5, rely=0.7, anchor=tk.CENTER)

root.mainloop()
