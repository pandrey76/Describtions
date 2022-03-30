find_package(OpenSSL)

if(OPENSSL_FOUND)
  message("TEST OpenSSL2 found!")
else()
  set(all_found_result "not found")
  message("TEST OpenSSL2 not found!")
endif()

if(OPENSSL_LIBRARIES)
  message("TEST OpenSSL2 lib found!")
else()
  set(all_found_result "not found")
  message("TEST OpenSSL2 lib not found!")
endif()

# Флаг REQUIRED говорит о том, что если MFC не найден, то прекратить дальнейшую генерацию, т.е. эта библиотек нужна для
# работы, но почему то это в данном примере не работает, поэтому используется кастыль с глобальной
# переменной "all_found_result".
find_package(MFC REQUIRED)
if(MFC_FOUND)
  message("MFC_FOUND found!")
else()
  set(all_found_result "not found")
  message("MFC_FOUND not found!")
endif()

