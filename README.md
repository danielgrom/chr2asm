# chr2asm
usage: chr2asm [-h] [-n BYTES_PER_LINE] input output

Convert .chr files into .byte directives for ca65.

# positional arguments:
  input                 Input .chr file
  output                Output .asm file

# options:
  -h, --help            show this help message and exit
  -n BYTES_PER_LINE     Number of bytes per line (default: 8)
