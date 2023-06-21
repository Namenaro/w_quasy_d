from w_quasy import *

def float_to_str(num):
   return "{:.2f}".format(num)

def t_1(w_func):
   print("")
   print('\033[95m' + "===================================================")
   print("                Должно уменьшаться:    " + '\033[0m')
   vals_ = [1, 3, 3, 3]
   index_ = 0
   predicted_val_ = 0.7
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [1, 1, 1, 3]
   index_ = 0
   predicted_val_ = 0.7
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))


def t_2(w_func):
   print("")
   print('\033[95m' +"===================================================")
   print ( "                Должно уменьшаться:    " + '\033[0m')
   vals_ = [1, 3, 3, 3, 3, 3, 3, 3, 3, 3]
   index_ = 0
   predicted_val_ = 0.8
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [1, 3, 3, 3]
   index_ = 0
   predicted_val_ = 0.8
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [1, 3]
   index_ = 0
   predicted_val_ = 0.8
   w = w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))



def t_3(w_func):
   print("")
   print('\033[95m' +"===================================================")
   print ( "                Примерно одинаково    " + '\033[0m')
   vals_ = [1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 0.8
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [1, 3, 3, 3]
   index_ = 0
   predicted_val_ = 0.8
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))


def t_4(w_func):

   print("")
   print('\033[95m' +"===================================================")
   print ("                Должно уменьшаться    " + '\033[0m')
   print("4-й пример")
   vals_ = [1, 7,7,7]
   index_ = 0
   predicted_val_ = 1
   w = w_func(vals_, index_, predicted_val_)

   print("    w = " + float_to_str(w))

   vals_ = [1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 1
   w = w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

def t_5(w_func):
   print("")
   print('\033[95m' +"===================================================")
   print ( "                Должно увеличиваться    " + '\033[0m')
   vals_ = [1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 0.8
   w = w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [1, 1, 1, 1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 0.8
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

def t_6(w_func):
   print("")
   print('\033[95m' + "===================================================")
   print("                6.Должно уменьшаться:    " + '\033[0m')
   vals_ = [1, 3, 3, 3]
   index_ = 0
   predicted_val_ = 0.7
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [1 , 2, 2, 2]
   index_ = 0
   predicted_val_ = 0.7
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

def t_7(w_func):
   print("")
   print('\033[95m' + "===================================================")
   print("                7.Должно уменьшаться:    " + '\033[0m')
   vals_ = [3, 6, 6, 3]
   index_ = 0
   predicted_val_ = 3
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [3, 6, 3, 3]
   index_ = 0
   predicted_val_ = 3
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))



def t_8(w_func):
   print("")
   print('\033[95m' + "===================================================")
   print("                8.Должно уменьшаться:    " + '\033[0m')
   vals_ = [3, 3, 3, 3, 3, 89]
   index_ = 0
   predicted_val_ = 3.1
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [3, 3, 3, 3, 3, 5]
   index_ = 0
   predicted_val_ = 3.1
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

def t_9(w_func):
   print("")
   print('\033[95m' + "===================================================")
   print("                9.ОСОБЫЙ случай - u не информативно! оценивать надо только по val:    " + '\033[0m')
   vals_ = [3, 3, 3, 3]
   index_ = 0
   predicted_val_ = 3
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [2, 2, 2, 2]
   index_ = 0
   predicted_val_ = 3
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))


def t_10(w_func):
   print("")
   print('\033[95m' + "===================================================")
   print("                10.Должно увеличиваться:    " + '\033[0m')
   vals_ = [90, 3]
   index_ = 0
   predicted_val_ = 90
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [90,3, 3]
   index_ = 0
   predicted_val_ = 90
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [90, 3, 3, 3, 3]
   index_ = 0
   predicted_val_ = 90
   w = w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [90, 3, 3, 3, 3, 3,3]
   index_ = 0
   predicted_val_ = 90
   w = w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

if __name__ == '__main__':
   w_func =  w2
   t_1(w_func)
   t_2(w_func)
   t_3(w_func)
   t_4(w_func)
   t_5(w_func)
   t_6(w_func)
   t_7(w_func)
   t_8(w_func)
   t_9(w_func)
   t_10(w_func)

