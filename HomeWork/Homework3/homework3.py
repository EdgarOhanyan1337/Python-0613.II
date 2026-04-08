import sys; sys.stdout.reconfigure(encoding='utf-8')



s1 = 'abc'
s2 = 'xyz'
new_s1 = s2[:2] + s1[2:]
new_s2 = s1[:2] + s2[2:]
print(f"1. Արդյունք: '{new_s1} {new_s2}'")

print()


s_welcome = "Welcome"
res_ing = s_welcome[:3] + "ing"
print(f"2. {s_welcome} -> {res_ing}")

print()


s_abcd = "abcd"
if len(s_abcd) > 1:
    res_swap = s_abcd[-1] + s_abcd[1:-1] + s_abcd[0]
else:
    res_swap = s_abcd
print(f"3. {s_abcd} -> {res_swap}")

print()


s_len = "Python Programming"
print(f"4. '{s_len}' տողի երկարությունը՝ {len(s_len)}")

print()

s_restart = "restart"
# Используем индекс -2 для замены конкретной буквы 'r' на '$'
res_dollar = s_restart[:-2] + "$" + s_restart[-1]
print(f"5. {s_restart} -> {res_dollar}")

print()


sentence = "Python is an amazing programming language"
words = sentence.split()
longest_word = max(words, key=len)
print(f"6. Ամենաերկար բառը՝ '{longest_word}', երկարությունը՝ {len(longest_word)}")

print()


sentence_task7 = "Hello world from Python script"
word_count = len(sentence_task7.split())
print(f"7. Բառերի քանակը՝ {word_count}")
