imp_line_list = input().split("\\")
extension = imp_line_list[len(imp_line_list)-1].split(".")[-1]
filename = imp_line_list[len(imp_line_list)-1][:-len(extension)-1]
print(f'File name: {filename}\nFile extension: {extension}')
