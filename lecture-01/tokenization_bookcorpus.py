import re, tarfile, time, json, gzip, pickle
from collections import Counter

word_re = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")

def build_counts_and_log_jsonl(
    tar_gz_path: str,
    out_prefix: str = "books1",
    suffixes=(".txt",),
    checkpoint_every_files: int = 100,
    encoding: str = "utf-8",
):
    """
    Streams tar.gz once, tokenizes with word_re, updates global Counter,
    and logs (N, |V|, etc.) as JSONL at each checkpoint.
    """
    counter_path = f"{out_prefix}.counter.pkl.gz"   # optional but useful
    log_path = f"{out_prefix}.heaps_log.jsonl"      # JSONL for curve

    counts = Counter()
    total_tokens = 0
    total_files = 0
    skipped_files = 0
    t0 = time.time()

    # overwrite log each run (change to 'a' if you want to append)
    with open(log_path, "w", encoding="utf-8") as logf:
        with tarfile.open(tar_gz_path, mode="r|gz") as tar:
            for m in tar:
                if not m.isfile():
                    continue
                name = m.name
                if suffixes and not name.lower().endswith(tuple(s.lower() for s in suffixes)):
                    continue

                f = tar.extractfile(m)
                if f is None:
                    skipped_files += 1
                    continue

                text = f.read().decode(encoding, errors="replace")
                tokens = [w.lower() for w in word_re.findall(text)]

                counts.update(tokens)
                total_tokens += len(tokens)
                total_files += 1

                if checkpoint_every_files and total_files % checkpoint_every_files == 0:
                    rec = {
                        "tar_path": tar_gz_path,
                        "total_files": total_files,
                        "skipped_files": skipped_files,
                        "total_tokens": total_tokens,   # N
                        "vocab_size": len(counts),      # |V|
                        "elapsed_sec": time.time() - t0,
                    }
                    logf.write(json.dumps(rec) + "\n")
                    logf.flush()

                    # optional: checkpoint counts too (comment out if not needed)
                    with gzip.open(counter_path, "wb") as g:
                        pickle.dump(counts, g, protocol=pickle.HIGHEST_PROTOCOL)

                    print(f"[ckpt] files={total_files:,} N={total_tokens:,} |V|={len(counts):,} time={rec['elapsed_sec']:.1f}s")

        # final record
        rec = {
            "tar_path": tar_gz_path,
            "total_files": total_files,
            "skipped_files": skipped_files,
            "total_tokens": total_tokens,
            "vocab_size": len(counts),
            "elapsed_sec": time.time() - t0,
        }
        logf.write(json.dumps(rec) + "\n")

    # final save of counts (optional)
    with gzip.open(counter_path, "wb") as g:
        pickle.dump(counts, g, protocol=pickle.HIGHEST_PROTOCOL)

    return log_path, counter_path

def main():
    counts, N = build_counts_and_log_jsonl(
    "../.datasets/books1.tar.gz",
    out_prefix="books1_wordcounts",
    suffixes=(".txt",),   # adjust if needed
    checkpoint_every_files=100
    )

if __name__ == '__main__':
    main()
