# Insert record into table
sqlite3 /home/admin1/acvp/CryptographyVerificationServer/backend/db.sqlite3 "insert into core_cvpserversessionconfig (cvp_run_server_command_prompt, cvp_run_server_ip, cvp_run_server_port, cvp_run_server_with_no_data_generation, cvp_run_server_with_only_data_generation, cvp_run_server_with_corrupt_results) values('EMPTY', 'EMPTY', 'EMPTY', 0, 0, 1);"

# Update entity of record
sqlite3 /home/admin1/acvp/CryptographyVerificationServer/backend/db.sqlite3 "update core_cvpserversessionconfig set cvp_run_server_with_corrupting_results=0 where id=1;"
