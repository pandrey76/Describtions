1. Context rename in files
find . -type f -print0 | xargs -0 sed -i 's|OFB|CBC|g'

2. Files rename
find . -type f -print |sed 's/\(.*\)OFB\(.*\)/mv & \1CBC\2/'| sh
# "Grizzy.and.the.Lemmings.S01E01.Polar.Bear.1080p.NF.WEB-DL.DDP2.0.x264-AJP69.mkv" to view as "001.Polar.Bear.1080p.NF.WEB-DL.DDP2.0.x264-AJP69.mkv"
find . -type f -print | sed 's!.*[Ss]01[Ee]\([[:digit:]][[:digit:]]\)[.]\(.*\)!mv & 0\1.\2!'| sh

3. Directory rename
find . -type d -print |sed 's/\(.*\)OFB\(.*\)/mv & \1CBC\2/'| sh

admin1@ubuntu18:~/acvp/CryptographyVerificationServer$ find . -type f -not -path "./backend/env/*" \( -iname "*.py" ! -iname ".*" \) -print0 | xargs -0 sed -i 's|def construct_test_case_result(self, other|def construct_test_case_result(self, other, stored_vector_set, requested_vector_set|g'


admin1@ubuntu18:~$ find . -type f -not -path "./backend/env/*" \( -iname "*.py" ! -iname ".*" \) -print0 | xargs -0 sed -i 's|return constructing_test_case_result(source_data, other|return constructing_test_case_result(source_data, other, stored_vector_set, requested_vector_set|g'
