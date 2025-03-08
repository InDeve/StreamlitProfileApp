chunk_size = 25 * 1024 * 1024  # 25mb
with open("ml_models\\toxicity.keras", "rb") as f:
    part = 0
    while chunk := f.read(chunk_size):
        with open(f"model_part_{part}", "wb") as p:
            p.write(chunk)
        part += 1