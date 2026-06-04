#!/usr/bin/env python3
import sys
import struct
import shutil
import os

def main():
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <input_elf> <output_elf> <patches.txt> <offset>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    patch_path = sys.argv[3]
    offset = int(sys.argv[4], 0)  # Offset can still be hex or decimal

    if not os.path.exists(input_path):
        print(f"Error: input ELF file '{input_path}' not found.")
        sys.exit(1)

    if not os.path.exists(patch_path):
        print(f"Error: patch file '{patch_path}' not found.")
        sys.exit(1)

    # Copy input ELF to output ELF
    shutil.copyfile(input_path, output_path)
    print(f"Copied '{input_path}' → '{output_path}'")

    patches = []
    with open(patch_path, "r") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                addr_str, value_str = line.split()

                # Require hexadecimal address
                if not all(c in "0123456789abcdefABCDEFxX" for c in addr_str):
                    raise ValueError("Address must be hexadecimal")

                addr = int(addr_str, 16)
                value = int(value_str, 16)
                patches.append((addr, value))
            except Exception as e:
                print(f"Skipping malformed line {line_no}: {line} ({e})")
                continue

    if not patches:
        print("No valid patches found — nothing to do.")
        sys.exit(0)

    with open(output_path, "r+b") as f:
        for addr, value in patches:
            file_offset = addr - offset
            if file_offset < 0:
                print(f"Warning: address {addr:#x} < offset {offset:#x}, skipping")
                continue

            f.seek(file_offset)
            data = struct.pack(">I", value)  # Big-endian 4-byte PPC instruction
            f.write(data)
            print(f"Patched offset {file_offset:#x} (addr {addr:#x}) → {value:#010x}")

    print("✅ All patches applied successfully to output file.")

if __name__ == "__main__":
    main()
