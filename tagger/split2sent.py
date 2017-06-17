import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input", help="input file path, WNUT input data format")
parser.add_argument("output", help="output file path, each line is a sentence")

args = parser.parse_args()
input_fp = args.input
output_fp = args.output

end_of_sent = False

with open(input_fp) as f, open(output_fp,'w') as outf:
    words = []
    
    for line in f:
        line = line.rstrip()
        if line == "":
            end_of_sent = True
        if end_of_sent:
            if len(words) == 0:
                continue
            else:
                outf.write(' '.join(words) + '\n')
                end_of_sent = False
                words = []
        else:
            word = line.split()[0]
            words.append(word)
            
                
        

