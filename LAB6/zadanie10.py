import struct
from pathlib import Path


def text_to_binary(src_txt: Path, dst_bin: Path) -> int:
  """
  Read ints from src_txt (one per line) and write them to dst_bin as 4-byte little-endian ints.
  Returns the number of integers written.
  """
  if not src_txt.exists():
    raise FileNotFoundError(src_txt)
  dst_bin.parent.mkdir(parents=True, exist_ok=True)
  count = 0
  with src_txt.open("r", encoding="utf-8") as fin, dst_bin.open("wb") as fout:
    for line in fin:
      line = line.strip()
      if not line:
        continue
      num = int(line)
      fout.write(struct.pack("<i", num))
      count += 1
  print(f"Wrote {count} integers from {src_txt} to {dst_bin}")
  return count


def main() -> None:
  txt = Path("demo_outputs/zadanie10/numbers.txt")
  binf = Path("demo_outputs/zadanie10/numbers.bin")
  # create example text file
  txt.parent.mkdir(parents=True, exist_ok=True)
  txt.write_text("10\n20\n-5\n100\n", encoding="utf-8")
  text_to_binary(txt, binf)


if __name__ == "__main__":
  main()
