# def reformat_line(line):
#     parts = line.strip().split(":")
    
#     if len(parts) != 4:
#         return None
    
#     username, password, ip, port = parts
#     return f"{ip}:{port}:{username}:{password}"

# def process_file(input_file, output_file):
#     with open(input_file, "r") as infile, open(output_file, "w") as outfile:
#         for line in infile:
#             reformatted = reformat_line(line)
#             if reformatted:
#                 outfile.write(reformatted + "\n")

def reformat_line(line):
    line = line.strip()
    
    # replacing @ with :
    line = line.replace("@", ":")
    
    parts = line.split(":")
    
    if len(parts) != 4:
        return None 
    
    username, password, ip, port = parts
    return f"{ip}:{port}:{username}:{password}"

def process_file(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            reformatted = reformat_line(line)
            if reformatted:
                outfile.write(reformatted + "\n")

if __name__ == "__main__":
    input_path = "./input.txt"
    output_path = "./done/oxylap-resi.txt"
    
    process_file(input_path, output_path)
    print(f"hehe, good luck on the drop Nigerians! Your cleaned up proxy list is in here =======> {output_path}")
