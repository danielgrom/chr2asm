#!/usr/bin/env python3
# chr2asm.py
# Convert .chr files into .byte directives for ca65

import argparse
import sys

def chr_to_ca65(input_file, output_file, bytes_per_line=8):
    try:
        with open(input_file, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: file '{input_file}' not found.")
        sys.exit(1)

    with open(output_file, "w") as out:
        for i in range(0, len(data), bytes_per_line):
            chunk = data[i:i+bytes_per_line]
            line = ", ".join(f"${b:02X}" for b in chunk)
            out.write(f".byte {line}\n")

    print(f"Conversion finished! Output written to {output_file}")


def main():
    parser = argparse.ArgumentParser(
        prog="chr2asm",
        description="Convert .chr files into .byte directives for ca65."
    )
    parser.add_argument("input", help="Input .chr file")
    parser.add_argument("output", help="Output .asm file")
    parser.add_argument(
        "-n", "--bytes-per-line", type=int, default=8,
        help="Number of bytes per line (default: 8)"
    )

    args = parser.parse_args()

    if args.bytes_per_line <= 0:
        print("Error: --bytes-per-line must be greater than zero.")
        sys.exit(1)

    chr_to_ca65(args.input, args.output, args.bytes_per_line)


if __name__ == "__main__":
    main()
