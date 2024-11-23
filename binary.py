import struct


def convert_to_binary(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "wb") as outfile:
            for line in infile:
                line = line.strip()
                if not line:
                    continue

                command = line[0]
                data = line[1:].strip()

                if command == "i":  # Inteiro de 32 bits
                    try:
                        value = int(data)
                        outfile.write(struct.pack("i", value))
                    except ValueError:
                        print(f"Invalid integer value in line: {line}")

                elif command == "f":  # Float de 32 bits
                    try:
                        value = float(data)
                        outfile.write(struct.pack("f", value))
                    except ValueError:
                        print(f"Invalid float value in line: {line}")

                elif command == "c":  # Caráter (byte)
                    try:
                        value = int(data)
                        if 0 <= value <= 255:
                            outfile.write(struct.pack("B", value))
                        else:
                            print(f"Invalid byte value in line: {line}")
                    except ValueError:
                        print(f"Invalid byte value in line: {line}")

                elif command == "s":  # String
                    value = data.replace("\\n", "\n").replace("\\r", "\r")
                    outfile.write(value.encode("utf-8"))

                elif command == "z":  # Zeros
                    try:
                        value = int(data)
                        if value >= 0:
                            outfile.write(b"\x00" * value)
                        else:
                            print(f"Invalid zero padding value in line: {line}")
                    except ValueError:
                        print(f"Invalid zero padding value in line: {line}")

                else:
                    print(f"Unrecognized command in line: {line}")
        
        print(f"File successfully converted to binary: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except IOError as e:
        print(f"Error reading or writing files: {e}")


def main():
    input_file = input("Enter the input file name (.txt): ").strip()
    if not input_file.endswith(".txt"):
        print("Invalid input file format. Please provide a '.txt' file.")
        return

    output_file = input_file.replace(".txt", ".dat")
    convert_to_binary(input_file, output_file)


if __name__ == "__main__":
    main()

