import pefile
import os
import glob

def scan_folder_for_linker_versions():
    exe_files = glob.glob("*.exe")

    if not exe_files:
        print("No *.exe found in this directory.")
        return

    print(f"{'File':<25} | {'Major':<6} | {'Minor (Hex)':<12}")
    print("-" * 48)

    for exe_path in exe_files:
        try:
            pe = pefile.PE(exe_path, fast_load=True)
            major = pe.OPTIONAL_HEADER.MajorLinkerVersion
            minor = pe.OPTIONAL_HEADER.MinorLinkerVersion

            print(f"{exe_path[:25]:<25} | {major:<6} | {minor:<3} (0x{minor:02X})")

        except Exception as e:
            print(f"{exe_path[:25]:<25} | Error while reading")

if __name__ == "__main__":
    scan_folder_for_linker_versions()
