#include <iostream>
// Подключаем и C файл и C++ файл

extern "C"
{
    // Такая запись не всегда нужна, можно и без неё, но могут возникнуть различные проблемы.
    // В частности на MacOS для корректной работы такая запись необходима.
    // Здесь мы указываем, что хидер и соответственно объектный файл, который будет сгенерён
    // он сугубо на языке C и собран C компилятором.
  #include "../sub_project1/include/sub_c.h"
}

#include "../sub_project2/include/sub_cpp.hpp"

int main()
{
  std::cout << "Main !" << std::endl;
  
  c_func_1();
  c_func_2(100);
  
  subCpp sub;
  sub.say_hello();
  
  return 0;
}
