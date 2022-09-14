text = "To solve the problem, we will need some definitions. Let (α_1,…,α_k;β_1,…,β_l ) be a configuration, then define"

new_text = text.replace("α", r"\alpha")
new_text = new_text.replace("β", r"\beta")
new_text = new_text.replace("∈", r" \in ")

with open("formatted_text.txt", "w", encoding="utf-8") as fo:
    fo.write(new_text)