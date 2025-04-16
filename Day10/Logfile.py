# Log File Analyzer

errorcount = 0
# with open("server.log", "r") as log, open("errors.log", "w") as error:
#     for line in log:
#         if "ERROR" in line:
#             errorcount += 1
#             error.write(line)

# print(f"Total 'ERROR' lines: {errorcount}")



with open("server.log", "r") as log:
    for line in log:
        if 'ERROR' in line:
            errorcount+=1
            with open("errors.log", "a") as error:
                error.write(line)
print(f"Total 'ERROR' lines: {errorcount}")